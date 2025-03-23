# novel_approach_pdf.py

import os
import json
from agents import NovelApproachAgent

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from textwrap import wrap


def propose_novel_approach_and_save_pdf():
    """
    1. Load literature data from JSON.
    2. Use NovelApproachAgent to propose a new research direction.
    3. Store the result in a PDF file using ReportLab.
    """
    try:
        # Load your final literature data
        with open("../database/literature_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load literature data: {e}")
        return

    # Build the prompt, referencing the existing review info
    prompt = (
        "Below is the literature review data.\n\n"
        f"Research Topic: {data['metadata']['research_topic']}\n"
        f"Sub-topics found: {list(data['sub_topics'].keys())}\n\n"
        "Based on these findings, please propose a new, innovative research approach that:\n"
        "- Addresses existing gaps or limitations\n"
        "- Builds on current methodologies\n"
        "- Introduces an innovative angle or extension of the studies\n"
        "Provide a concise but thorough academic rationale.\n"
    )

    # Instantiate the agent
    novel_agent = NovelApproachAgent(
        model="gemini-2.0-flash",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Get the novel approach from the agent
    novel_approach = novel_agent.inference(prompt=prompt)

    # Set up PDF output
    pdf_filename = "../database/novel_approach.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=LETTER)
    c.setTitle("Novel Research Approach")

    # Define some layout parameters
    width, height = LETTER  # 612 x 792 in points
    margin = 1 * inch
    text_width = width - 2 * margin
    y_position = height - margin

    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "Novel Research Approach")
    y_position -= 0.5 * inch

    # Topic
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position,
                 f"Topic: {data['metadata']['research_topic']}")
    y_position -= 0.5 * inch

    # Approach heading
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Proposed Approach:")
    y_position -= 0.3 * inch

    # Switch to normal font for the text body
    c.setFont("Helvetica", 11)

    # Wrap the approach text so it fits within the margins
    # 70 chars is ~ for page width
    wrapped_text = wrap(novel_approach, width=70)

    for line in wrapped_text:
        # If we reach near the bottom, create a new page
        if y_position <= margin:
            c.showPage()
            c.setFont("Helvetica", 11)
            y_position = height - margin

        c.drawString(margin, y_position, line)
        y_position -= 14  # move down 14 points (about one line of text)

    # Finalize and save PDF
    c.showPage()
    c.save()
    print(f"Novel approach saved successfully to '{pdf_filename}'!")
    print("Done.")


if __name__ == "__main__":
    propose_novel_approach_and_save_pdf()
