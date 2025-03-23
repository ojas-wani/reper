# streamlit_app.py

import streamlit as st
import os
import json
import base64
from literature_review import perform_literature_review
import generate_report
import novel_ideas
import torch

torch.classes.__path__ = []

def load_result_files(db_folder="database"):
    result_files = {}
    if os.path.exists(db_folder):
        for file_name in os.listdir(db_folder):
            file_path = os.path.join(db_folder, file_name)
            try:
                # Use errors="replace" to handle decoding issues.
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    result_files[file_name] = f.read()
            except Exception as e:
                st.error(f"Error reading {file_name}: {e}")
    return result_files


def main():
    st.set_page_config(page_title="Research Literature Review", layout="wide")

    # Initialize session state for result files and results_generated flag if not already present.
    if "result_files" not in st.session_state:
        st.session_state["result_files"] = {}
    if "results_generated" not in st.session_state:
        st.session_state["results_generated"] = False

    # Top: Display Logo using SVG
    logo_svg = '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 80">
      <!-- Background shape -->
      <rect x="10" y="10" width="220" height="60" rx="12" fill="#1e1e1e" />
      
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
      <text x="120" y="62" font-family="Arial, sans-serif" font-size="10" fill="#9c9c9c" text-anchor="middle">Literature Review Made Simple</text>
    </svg>
    '''
    
    # Function to encode the SVG to a data URL for inline display
    def svg_to_data_url(svg):
        b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
        return f'data:image/svg+xml;base64,{b64}'
    
    # Display logo centered
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{svg_to_data_url(logo_svg)}" width="240px"></div>',
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'></h1>",
                unsafe_allow_html=True)
    st.markdown("---")

    # Two rows of input fields
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        research_topic = st.text_input(
            "Research Topic", "Drop your Research Idea Here")
    with col2:
        open_ai_key = st.text_input(
            "OpenAI API Key (Optional)", type="password")
    with col3:
        base_url = st.text_input("Base URL (Optional)", value="")

    col4, col5, col6, col7, col8 = st.columns(5)
    with col4:
        max_value = st.number_input(
            "Max Papers to Collect", min_value=1, max_value=100, value=20, step=1)
    with col5:
        start_year = st.number_input(
            "Start Year", min_value=1900, max_value=2100, value=2020, step=1)
    with col6:
        end_year = st.number_input(
            "End Year", min_value=1900, max_value=2100, value=2025, step=1)
    with col7:
        generate_report_flag = st.checkbox("Generate Report", value=True)
    with col8:
        generate_novel_approach_flag = st.checkbox(
            "Generate Novel Approach", value=True)

    # Centered Get Results button
    st.markdown("<br>", unsafe_allow_html=True)
    button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
    with button_col2:
        if st.button("Get Results"):
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
                st.error(
                    "Literature review failed. Please check the logs for errors.")
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
                        for paper in papers:
                            st.markdown(
                                f"**Title:** {paper.get('title', 'N/A')}")
                            st.markdown(
                                f"**Published:** {paper.get('published', 'N/A')}")
                            st.markdown(
                                f"**Link:** {paper.get('link', 'N/A')}")
                            st.markdown("---")
                else:
                    st.warning("No papers info found in literature_data.json.")
            except Exception as e:
                st.error(f"Error reading literature_data.json: {e}")
        else:
            st.error("literature_data.json not found.")

        st.markdown("## Download Files")
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
            st.info(
                "No result files available. Please run the workflow to generate files.")
    else:
        st.info("Results will be displayed here once the workflow is complete.")


if __name__ == "__main__":
    main()