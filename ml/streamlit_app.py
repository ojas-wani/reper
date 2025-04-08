import streamlit as st
import os
import json
import base64
from literature_review import perform_literature_review
import generate_report
import novel_ideas
import torch

# Disable dynamic imports and set Streamlit configuration
st.set_page_config(
    page_title="Research Literature Review",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# This is a research literature review app'
    }
)

# Disable dynamic imports
st.markdown("""
    <script>
        // Disable dynamic imports
        window.import = function() {
            console.warn('Dynamic imports are disabled');
            return Promise.reject(new Error('Dynamic imports are disabled'));
        };
    </script>
""", unsafe_allow_html=True)

# Load custom CSS using absolute path
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(os.path.dirname(current_dir), "static")
css_path = os.path.join(static_dir, "styles.css")

# Add error handling for static files
try:
    if os.path.exists(css_path):
        with open(css_path, encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("CSS file not found. Some styling may be missing.")
except Exception as e:
    st.warning(f"Error loading CSS: {str(e)}")

# Initialize torch
torch.classes.__path__ = []

def load_result_files(db_folder="database"):
    result_files = {}
    if os.path.exists(db_folder):
        for file_name in os.listdir(db_folder):
            file_path = os.path.join(db_folder, file_name)
            try:
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    result_files[file_name] = f.read()
            except Exception as e:
                st.error(f"Error reading {file_name}: {e}")
    return result_files

def main():
    # Initialize session state for result files and results_generated flag if not already present.
    if "result_files" not in st.session_state:
        st.session_state["result_files"] = {}
    if "results_generated" not in st.session_state:
        st.session_state["results_generated"] = False
    if "generate_report_flag" not in st.session_state:
        st.session_state["generate_report_flag"] = True
    if "generate_novel_approach_flag" not in st.session_state:
        st.session_state["generate_novel_approach_flag"] = True

    # Top: Display Logo using SVG
    logo_svg = '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 80">
      <!-- Background shape -->
      <rect x="10" y="10" width="220" height="60" rx="12" fill="#2c3e50" />
      
      <!-- Accent border -->
      <rect x="10" y="10" width="220" height="60" rx="12" fill="none" stroke="#4CAF50" stroke-width="2" />
      
      <!-- Main text "REPER" -->
      <text x="120" y="48" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="#ffffff" text-anchor="middle">REPER</text>
      
      <!-- Document icon to the left -->
      <path d="M40,30 L40,50 L55,50 L55,40 L45,40 L45,30 Z" fill="#4CAF50" />
      <path d="M45,30 L45,40 L55,40 Z" fill="#4CAF50" />
      
      <!-- Search magnifying glass to the right -->
      <circle cx="180" cy="38" r="8" fill="none" stroke="#4CAF50" stroke-width="2.5" />
      <line x1="185" y1="45" x2="192" y2="52" stroke="#4CAF50" stroke-width="2.5" stroke-linecap="round" />
      
      <!-- Tagline -->
      <text x="120" y="62" font-family="Arial, sans-serif" font-size="10" fill="#bdc3c7" text-anchor="middle">Literature Review Made Simple</text>
    </svg>
    '''

    # Function to encode the SVG to a data URL for inline display
    def svg_to_data_url(svg):
        b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
        return f'data:image/svg+xml;base64,{b64}'

    # Display logo centered with padding
    st.markdown(
        f'<div style="display: flex; justify-content: center; padding: 20px 0;"><img src="{svg_to_data_url(logo_svg)}" width="240px"></div>',
        unsafe_allow_html=True
    )

    # Welcome message
    st.markdown("""
        <div style='text-align: center; color: #2c3e50; margin-bottom: 30px;'>
            <h2>Welcome to REPER</h2>
            <p style='color: #7f8c8d;'>Your AI-powered research literature review assistant</p>
        </div>
    """, unsafe_allow_html=True)

    # Move input fields to the sidebar
    with st.sidebar:
        st.markdown("""
            <div class='section-header'>
                <h3>Research Parameters</h3>
                <p style='color: #7f8c8d;'>Configure your literature review settings below</p>
            </div>
        """, unsafe_allow_html=True)

        research_topic = st.text_input(
            "Research Topic",
            placeholder="Enter your research topic or question",
            help="This is the main topic you want to research. Be specific for better results."
        )
        # open_ai_key = st.text_input(
        #     "OpenAI API Key (Optional)",
        #     type="password",
        #     placeholder="Your OpenAI API Key",
        #     help="Enter your OpenAI API key for enhanced analysis capabilities."
        # )
        # base_url = st.text_input(
        #     "Base URL (Optional)",
        #     value="",
        #     placeholder="Base URL for API",
        #     help="Custom API endpoint if you're using a different OpenAI-compatible service."
        # )

        max_value = st.number_input(
            "Max Papers",
            min_value=6,
            max_value=100,
            value=18,
            step=1,
            help="Maximum number of papers to collect for your research topic."
        )
        start_year = st.number_input(
            "Start Year",
            min_value=1900,
            max_value=2025,
            value=2005,
            step=1,
            help="Starting year for paper collection."
        )
        end_year = st.number_input(
            "End Year",
            min_value=1900,
            max_value=2025,
            value=2025,
            step=1,
            help="Ending year for paper collection."
        )
        generate_report_flag = st.checkbox(
            "Generate Report",
            value=True,
            help="Generate a comprehensive literature review report."
        )
        generate_novel_approach_flag = st.checkbox(
            "Novel Approach",
            value=True,
            help="Generate novel research approaches and ideas."
        )

        # Centered Get Results button
        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.button("Get Results", use_container_width=True)

    # Main content container
    with st.container():
        if submit:
            # Clean optional inputs
            open_ai_key = open_ai_key.strip() or None
            base_url = base_url.strip() or None

            # Run the literature review step
            with st.spinner("Performing literature review..."):
                literature_data = perform_literature_review(
                    research_topic,
                    start_year,
                    end_year,
                    max_count=max_value,
                    open_ai_key=open_ai_key,
                    base_url=base_url
                )
            if literature_data is None:
                st.error("Literature review failed. Please check the logs for errors.")
                return
            st.success("Literature review completed!")

                # Conditionally generate the literature report
            if generate_report_flag:
                with st.spinner("Generating literature report..."):
                    generate_report.generate_literature_report(
                        open_ai_key=open_ai_key,
                        base_url=base_url
                    )
                st.success("Literature report generated!")
            else:
                st.info("Skipped literature report generation.")

            # Conditionally generate the novel research approach
            if generate_novel_approach_flag:
                with st.spinner("Generating novel research approach..."):
                    novel_ideas.propose_novel_approach_and_save(
                        open_ai_key=open_ai_key,
                        base_url=base_url
                    )
                st.success("Novel research approach generated!")
            else:
                st.info("Skipped novel research approach generation.")

            # Load generated files into session state for persistent download links.
            st.session_state["result_files"] = load_result_files()
            # Set flag to show results
            st.session_state["results_generated"] = True

        # Only show results if they have been generated
        if st.session_state.get("results_generated", False):
            st.markdown("---")
            st.markdown("## Generated Files")
            if st.session_state["result_files"]:
                for file_name, file_content in st.session_state["result_files"].items():
                    # Determine MIME type based on file extension
                    if file_name.endswith(".json"):
                        mime = "application/json"
                    elif file_name.endswith(".md"):
                        mime = "text/markdown"
                    else:
                        mime = "text/plain"
                    st.download_button(
                        label=f"Download {file_name}",
                        data=file_content,
                        file_name=file_name,
                        mime=mime
                    )
            else:
                st.info("No result files available. Please run the workflow to generate files.")

            st.markdown("## Papers Information")

            # Read and display papers info from literature_data.json
            data_file = os.path.join("database", "literature_data.json")
            if os.path.exists(data_file):
                try:
                    with open(data_file, "r", encoding="utf-8", errors="replace") as f:
                        data = json.load(f)
                    if "sub_topics" in data:
                        for sub_topic, papers in data["sub_topics"].items():
                            st.markdown(f"### {sub_topic}")
                            total_papers = 0  # Initialize the counter
                            for paper in papers:
                                if total_papers >= max_value:
                                    break
                                
                                st.markdown(f"""
                                    <div class='paper-card'>
                                        <h4 style='color: #2c3e50; margin-bottom: 10px;'>{paper.get('title', 'N/A')}</h4>
                                        <p style='color: #34495e;'><strong>Summary:</strong> {paper.get('summary', 'N/A')}</p>
                                        <p style='color: #7f8c8d;'><strong>Published:</strong> {paper.get('published', 'N/A')}</p>
                                        <a href='{paper.get('link', '#')}' target='_blank' style='color: #4CAF50; text-decoration: none;'>🔗 View Paper</a>
                                    </div>
                                """, unsafe_allow_html=True)
                                total_papers += 1
                except Exception as e:
                    st.error(f"Error reading literature_data.json: {e}")
            else:
                st.warning("No papers info found in literature_data.json.")
        else:
            st.info("Results will be displayed here once the workflow is complete.")

if __name__ == "__main__":
    main()
