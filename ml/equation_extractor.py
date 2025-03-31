import re
import json
import os
import io
import requests
from typing import List, Dict, Optional
import pymupdf as fitz  # PyMuPDF
import numpy as np
from PIL import Image
# import pytesseract
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
from urllib.parse import urlparse
import tempfile

def download_paper(url: str) -> Optional[str]:
    """Download paper from URL and save as temporary PDF."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, stream=True, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Create papers directory if it doesn't exist
        papers_dir = os.path.join("database", "papers")
        os.makedirs(papers_dir, exist_ok=True)
        
        # Generate a unique filename based on URL hash
        filename = f"paper_{hash(url)}.pdf"
        temp_file = os.path.join(papers_dir, filename)
        
        with open(temp_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        if not os.path.exists(temp_file) or os.path.getsize(temp_file) == 0:
            print(f"Failed to save PDF to {temp_file}")
            return None
            
        print(f"Successfully downloaded PDF to {temp_file}")
        return temp_file
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading paper from {url}: {str(e)}")
        return None
    except IOError as e:
        print(f"Error saving PDF to {temp_file}: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

class EquationExtractor:
    def __init__(self):
        # Initialize TrOCR model for equation recognition
        self.processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
        self.model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
        self.model.eval()  # Set to evaluation mode
        if torch.cuda.is_available():
            self.model = self.model.to('cuda')
        
    def extract_equations_from_pdf(self, pdf_path: str) -> List[Dict]:
        """Extract equations from a PDF file."""
        equations = []
        try:
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                page = doc[page_num]
                # Extract text and images
                text = page.get_text()
                image_list = page.get_images()
                
                # Process text for inline equations
                inline_eqs = self._extract_inline_equations(text)
                equations.extend(inline_eqs)
                
                # Process images for displayed equations
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Convert to PIL Image
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    # Use TrOCR to recognize equations in images
                    with torch.no_grad():  # Disable gradient computation
                        pixel_values = self.processor(image, return_tensors="pt").pixel_values
                        if torch.cuda.is_available():
                            pixel_values = pixel_values.to('cuda')
                        generated_ids = self.model.generate(pixel_values)
                        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
                    
                    # Check if the recognized text is an equation
                    if self._is_equation(generated_text):
                        equations.append({
                            "type": "displayed",
                            "equation": generated_text,
                            "page": page_num + 1,
                            "position": "image"
                        })
            
            doc.close()
        except Exception as e:
            print(f"Error processing PDF {pdf_path}: {str(e)}")
        
        return equations
    
    def _extract_inline_equations(self, text: str) -> List[Dict]:
        """Extract inline equations from text."""
        equations = []
        # Common equation patterns
        patterns = [
            r'\$[^$]+\$',  # LaTeX inline math
            r'\\\([^)]+\\\)',  # LaTeX inline math
            r'\\\[[^\]]+\\\]',  # LaTeX display math
            r'\\begin{equation}[^}]+\\end{equation}',  # LaTeX equation environment
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                equation = match.group(0)
                if self._is_equation(equation):
                    equations.append({
                        "type": "inline",
                        "equation": equation,
                        "position": "text"
                    })
        
        return equations
    
    def _is_equation(self, text: str) -> bool:
        """Check if text contains mathematical content."""
        # Common mathematical symbols and patterns
        math_symbols = ['=', '+', '-', '*', '/', '^', '\\', '∫', '∑', '∏', '√', '±', '×', '÷']
        math_patterns = [
            r'\\[a-zA-Z]+',  # LaTeX commands
            r'[0-9]+',  # Numbers
            r'[a-zA-Z]+',  # Variables
        ]
        
        # Check for mathematical symbols
        has_symbols = any(symbol in text for symbol in math_symbols)
        
        # Check for mathematical patterns
        has_patterns = any(re.search(pattern, text) for pattern in math_patterns)
        
        return has_symbols or has_patterns
    
    def convert_to_markdown(self, equation: str) -> str:
        """Convert equation to markdown format."""
        # Remove LaTeX delimiters if present
        equation = equation.strip('$')
        equation = equation.strip('\\(').strip('\\)')
        equation = equation.strip('\\[').strip('\\]')
        
        # Convert to markdown
        if equation.startswith('\\begin{equation}'):
            equation = equation.replace('\\begin{equation}', '')
            equation = equation.replace('\\end{equation}', '')
        
        return f"$${equation}$$"

def extract_equations_from_papers(papers_data: Dict) -> Dict:
    """Extract equations from all papers in the literature data."""
    extractor = EquationExtractor()
    equations_by_paper = {}
    
    for sub_topic, papers in papers_data.get("sub_topics", {}).items():
        equations_by_paper[sub_topic] = []
        for paper in papers:
            paper_equations = []
            
            # Download and process paper from URL
            if "link" in paper:
                pdf_path = download_paper(paper["link"])
                if pdf_path:
                    equations = extractor.extract_equations_from_pdf(pdf_path)
                    paper_equations.extend(equations)
                    # Don't delete the file anymore as we want to keep it
            
            if paper_equations:
                equations_by_paper[sub_topic].append({
                    "title": paper.get("title", "Unknown"),
                    "equations": paper_equations
                })
    
    return equations_by_paper

def save_equations_to_file(equations_data: Dict, output_file: str = "database/equations.json"):
    """Save extracted equations to a JSON file."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(equations_data, f, indent=2, ensure_ascii=False) 