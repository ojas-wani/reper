import streamlit as st
import os
import json
import base64
import shutil
from literature_review import perform_literature_review
import generate_report
import novel_ideas
import torch

# Set page config must be the first Streamlit command
st.set_page_config(page_title="Research Literature Review", layout="wide")

torch.classes.__path__ = []

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: translateY(-1px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .stNumberInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .stCheckbox>div>div>div {
        border-radius: 5px;
    }
    .paper-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .section-header {
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


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


def clear_database_folder(db_folder="database"):
    """Clear all files in the database folder."""
    if os.path.exists(db_folder):
        for file_name in os.listdir(db_folder):
            file_path = os.path.join(db_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                st.error(f"Error deleting {file_name}: {e}")


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

    # Main content container
    with st.container():
        st.markdown("""
            <div class='section-header'>
                <h3>Research Parameters</h3>
                <p style='color: #7f8c8d;'>Configure your literature review settings below</p>
            </div>
        """, unsafe_allow_html=True)

        # Two rows of input fields with better spacing
        col1, col2, col3 = st.columns(3)
        with col1:
            research_topic = st.text_input(
                "Research Topic",
                placeholder="Enter your research topic or question",
                help="This is the main topic you want to research. Be specific for better results."
            )
            
            # Add sub-topic input section
            st.markdown("### Sub-topics")
            st.markdown("Enter your research sub-topics below. You can add multiple sub-topics.")
            
            # Initialize session state for sub-topics if not present
            if "subtopics" not in st.session_state:
                st.session_state.subtopics = []
            if "ai_subtopics" not in st.session_state:
                st.session_state.ai_subtopics = []
            if "original_ai_subtopics" not in st.session_state:
                st.session_state.original_ai_subtopics = []
            
            # Show AI-generated topics first
            if st.session_state.original_ai_subtopics:
                st.markdown("### AI-Generated Research Topics (6-7 topics)")
                st.markdown("These are the core research topics generated by AI:")
                for i, subtopic in enumerate(st.session_state.original_ai_subtopics, 1):
                    st.markdown(f"**{i}.** {subtopic}")
                st.markdown("---")
            
            # Text area for entering additional sub-topics
            st.markdown("### Your Additional Sub-topics")
            st.markdown("Add your own sub-topics below (one per line):")
            subtopics_input = st.text_area(
                "Enter additional sub-topics",
                value="\n".join(st.session_state.subtopics),
                height=100,
                help="Enter each sub-topic on a new line. These will be combined with the AI-generated topics above."
            )
            
            # Update session state with new sub-topics
            if subtopics_input:
                st.session_state.subtopics = [st.strip() for st in subtopics_input.split("\n") if st.strip()]
            
            # Button to generate new AI sub-topics
            if st.button("Generate New AI Topics"):
                from agents import SubTopicAgent
                agent = SubTopicAgent()
                generated_subtopics = agent.inference(research_topic)
                # Parse the generated sub-topics (remove numbers and dots)
                parsed_subtopics = [st.split(". ", 1)[1] if ". " in st else st 
                                  for st in generated_subtopics.split("\n") 
                                  if st.strip()]
                # Store AI-generated sub-topics separately
                st.session_state.ai_subtopics = parsed_subtopics
                # Store original AI-generated topics
                st.session_state.original_ai_subtopics = parsed_subtopics.copy()
                st.rerun()
            
            # Display all current sub-topics
            if st.session_state.subtopics or st.session_state.ai_subtopics:
                st.markdown("### All Research Topics")
                
                # Show user-entered sub-topics
                if st.session_state.subtopics:
                    st.markdown("**Your Additional Topics:**")
                    for i, subtopic in enumerate(st.session_state.subtopics, 1):
                        st.markdown(f"{i}. {subtopic}")
                
                # Show AI-generated sub-topics
                if st.session_state.ai_subtopics and st.session_state.ai_subtopics != st.session_state.original_ai_subtopics:
                    st.markdown("**New AI-Generated Topics:**")
                    for i, subtopic in enumerate(st.session_state.ai_subtopics, 1):
                        st.markdown(f"{i}. {subtopic}")
                
                # Button to clear all sub-topics
                if st.button("Clear All Topics"):
                    st.session_state.subtopics = []
                    st.session_state.ai_subtopics = []
                    st.session_state.original_ai_subtopics = []
                    st.rerun()
            
        with col2:
            open_ai_key = st.text_input(
                "OpenAI API Key (Optional)",
                type="password",
                placeholder="Your OpenAI API Key",
                help="Enter your OpenAI API key for enhanced analysis capabilities."
            )
        with col3:
            base_url = st.text_input(
                "Base URL (Optional)",
                value="",
                placeholder="Base URL for API",
                help="Custom API endpoint if you're using a different OpenAI-compatible service."
            )

        # Second row of inputs with better spacing
        st.markdown("<br>", unsafe_allow_html=True)
        col4, col5, col6, col7, col8 = st.columns(5)
        with col4:
            max_value = st.number_input(
                "Max Papers",
                max_value=100,
                value=20,
                step=1,
                help="Maximum number of papers to collect for your research topic."
            )
        with col5:
            start_year = st.number_input(
                "Start Year",
                min_value=1900,
                max_value=2025,
                value=2020,
                step=1,
                help="Starting year for paper collection."
            )
        with col6:
            end_year = st.number_input(
                "End Year",
                min_value=1900,
                max_value=2025,
                value=2025,
                step=1,
                help="Ending year for paper collection."
            )
        with col7:
            generate_report_flag = st.checkbox(
                "Generate Report",
                value=True,
                help="Generate a comprehensive literature review report."
            )
        with col8:
            generate_novel_approach_flag = st.checkbox(
                "Novel Approach",
                value=True,
                help="Generate novel research approaches and ideas."
            )

        # Centered Get Results button with better styling
        st.markdown("<br>", unsafe_allow_html=True)
        button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
        with button_col2:
            disabled_button = (research_topic.strip() == "")
            if st.button("Start Literature Review", disabled=disabled_button):
                # Clear existing files in database folder
                clear_database_folder()
                
                
                with st.spinner("🔍 Performing literature review..."):
                    # Clean optional inputs
                    open_ai_key = open_ai_key.strip() or None
                    base_url = base_url.strip() or None

                    # Combine user sub-topics with original AI-generated topics
                    all_subtopics = list(set(st.session_state.subtopics + st.session_state.original_ai_subtopics))

                    # Run the literature review step with adjusted max_value
                    literature_data = perform_literature_review(
                        research_topic,
                        start_year,
                        end_year,
                        max_count=max_value,
                        open_ai_key=open_ai_key,
                        base_url=base_url,
                        user_subtopics=all_subtopics
                    )
                if literature_data is None:
                    st.error(
                        "Literature review failed. Please check the logs for errors.")
                    return
                
                st.success("Literature review completed!")

                # Store checkbox states in session state
                st.session_state["generate_report_flag"] = generate_report_flag
                st.session_state["generate_novel_approach_flag"] = generate_novel_approach_flag

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

    # Results section with improved styling
    if st.session_state.get("results_generated", False):
        st.markdown("---")
        
        # Only show download section if either report or novel approach was generated
        if st.session_state["generate_report_flag"] or st.session_state["generate_novel_approach_flag"]:
            st.markdown("""
                <div class='section-header'>
                    <h3>Generated Results</h3>
                    <p style='color: #7f8c8d;'>Download your literature review documents below</p>
                </div>
            """, unsafe_allow_html=True)

            if st.session_state["result_files"]:
                for file_name, file_content in st.session_state["result_files"].items():
                    # Only show report files if report was generated
                    if "report" in file_name.lower() and not st.session_state["generate_report_flag"]:
                        continue
                    # Only show novel approach files if novel approach was generated
                    if "novel" in file_name.lower() and not st.session_state["generate_novel_approach_flag"]:
                        continue
                        
                    mime = "application/json" if file_name.endswith(".json") else "text/markdown" if file_name.endswith(".md") else "text/plain"
                    st.download_button(
                        label=f"📥 Download {file_name}",
                        data=file_content,
                        file_name=file_name,
                        mime=mime
                    )

        # Papers Information section with card-based layout
        st.markdown("""
            <div class='section-header'>
                <h3>Research Papers</h3>
                <p style='color: #7f8c8d;'>Detailed information about collected papers</p>
            </div>
        """, unsafe_allow_html=True)

        data_file = os.path.join("database", "literature_data.json")
        if os.path.exists(data_file):
            try:
                with open(data_file, "r", encoding="utf-8", errors="replace") as f:
                    data = json.load(f)
                # Debug information
                # st.write("Debug - Data loaded successfully")
                # st.write("Debug - Data structure:", data.keys())
                
                if "sub_topics" in data:
                    # Debug information
                    # st.write("Debug - Number of subtopics:", len(data["sub_topics"]))
                    
                    # Calculate number of subtopics to show
                    num_subtopics = len(data["sub_topics"])
                    subtopics = list(data["sub_topics"].items())[:num_subtopics]
                    
                    # Only show papers up to max_value
                    total_papers = 0
                    for sub_topic, papers in subtopics:
                        if total_papers >= max_value:
                            break
                        st.markdown(f"### {sub_topic}")
                        # Debug information
                        # st.write(f"Debug - Papers in {sub_topic}:", len(papers))
                        
                        for paper in papers:
                            if total_papers >= max_value:
                                break
                            # Debug information
                            # st.write("Debug - Paper data:", paper)
                            
                            st.markdown(f"""
                                <div class='paper-card'>
                                    <h4 style='color: #2c3e50; margin-bottom: 10px;'>{paper.get('title', 'N/A')}</h4>
                                    <p style='color: #34495e;'><strong>Summary:</strong> {paper.get('summary', 'N/A')}</p>
                                    <p style='color: #7f8c8d;'><strong>Published:</strong> {paper.get('published', 'N/A')}</p>
                                    <a href='{paper.get('link', '#')}' target='_blank' style='color: #4CAF50; text-decoration: none;'>🔗 View Paper</a>
                                </div>
                            """, unsafe_allow_html=True)
                            total_papers += 1
                else:
                    st.warning("No papers info found in literature_data.json.")
            except Exception as e:
                st.error(f"Error reading literature_data.json: {e}")
                st.write("Debug - Full error:", str(e))
        else:
            st.error("literature_data.json not found.")
    else:
        st.markdown("""
            <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; border-left: 4px solid #3498db;'>
                <p style='color: #7f8c8d;'>Enter your research topic and parameters above to start the literature review process.</p>
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
