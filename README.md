# Research Literature Review Assistant

An AI-powered tool for automated literature review and research analysis.

## Features

- Automated literature review generation
- Novel research approach suggestions
- Interactive web interface
- Customizable search parameters
- Comprehensive report generation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Repo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_base_url_here  # Optional
```

## Usage

1. Start the Streamlit app:
```bash
cd ml
streamlit run streamlit_app.py
```

2. Open your browser and navigate to the provided URL (usually http://localhost:8501)

3. Enter your research topic and parameters in the web interface

4. Click "Get Results" to start the analysis

## Project Structure

```
Repo/
├── ml/
│   ├── static/
│   │   └── styles.css
│   ├── agents.py
│   ├── generate_report.py
│   ├── inference.py
│   ├── literature_review.py
│   ├── main.py
│   ├── novel_ideas.py
│   ├── requirements.txt
│   ├── streamlit_app.py
│   └── tools.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for paper retrieval

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your chosen license]

## Contact

[Your contact information] 