# main.py
import os
import logging
from literature_review import perform_literature_review
import generate_report
import novel_ideas

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main(
    research_topic: str,
    max_value: int,
    open_ai_key: str,
    base_url: str = None,
    start_year: int = None,
    end_year: int = None,
    generate_report_flag: bool = True,
    generate_novel_approach_flag: bool = True
):
    """
    Main function to perform literature review workflow.
    
    Args:
        research_topic (str): The research topic to analyze
        max_value (int): Maximum number of papers to collect
        open_ai_key (str): OpenAI API key
        base_url (str, optional): Custom OpenAI API base URL
        start_year (int, optional): Start year for paper search
        end_year (int, optional): End year for paper search
        generate_report_flag (bool): Whether to generate literature report
        generate_novel_approach_flag (bool): Whether to generate novel approach
    """
    try:
        logger.info("Starting literature review...")
        literature_data = perform_literature_review(
            research_topic,
            start_year,
            end_year,
            max_count=max_value,
            open_ai_key=open_ai_key,
            base_url=base_url
        )
        
        if not literature_data:
            logger.error("Literature review failed. Exiting workflow.")
            return

        if generate_report_flag:
            logger.info("Generating literature report...")
            generate_report.generate_literature_report(
                open_ai_key=open_ai_key,
                base_url=base_url
            )

        if generate_novel_approach_flag:
            logger.info("Proposing novel research approach...")
            novel_ideas.propose_novel_approach_and_save(
                open_ai_key=open_ai_key,
                base_url=base_url
            )

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage (commented out)
    """
    main(
        research_topic="LLM for high quality code generation",
        max_value=20,
        open_ai_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        start_year=2020,
        end_year=2025
    )
    """
