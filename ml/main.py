# main.py
import os
from literature_review import perform_literature_review
import generate_report
import novel_ideas


def main():
    # These variables should be provided by the frontend.
    # For demonstration, example values are used here:
    # Replace with frontend input
    research_topic = "LLM for high quality code generation"
    max_value = 20  # Maximum number of papers to collect
    open_ai_key = os.getenv("OPENAI_API_KEY")  # Or passed from frontend
    base_url = os.getenv("OPENAI_BASE_URL") if os.getenv(
        "OPENAI_BASE_URL") else None  # Optional
    start_year = 2020  # Replace with frontend input
    end_year = 2025    # Replace with frontend input

    # Boolean flags to control workflow steps (set via frontend)
    generate_report_flag = True
    generate_novel_approach_flag = True

    print("Starting literature review...")
    literature_data = perform_literature_review(
        research_topic,
        start_year,
        end_year,
        max_count=max_value,
        open_ai_key=open_ai_key,
        base_url=base_url
    )
    if not literature_data:
        print("Literature review failed. Exiting workflow.")
        return

    if generate_report_flag:
        print("Generating literature report...")
        generate_report.generate_literature_report(
            open_ai_key=open_ai_key,
            base_url=base_url
        )
    else:
        print("Skipping literature report generation.")

    if generate_novel_approach_flag:
        print("Proposing novel research approach...")
        novel_ideas.propose_novel_approach_and_save(
            open_ai_key=open_ai_key,
            base_url=base_url
        )
    else:
        print("Skipping novel research approach generation.")


if __name__ == "__main__":
    main()
