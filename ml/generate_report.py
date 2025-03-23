# generate_report.py

import os
import json
from datetime import datetime
from agents import PostdocAgent


def generate_literature_report():
    # -----------------------
    # 0) Load data from JSON
    # -----------------------
    try:
        with open("../database/literature_data.json") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load data: {e}")
        return

    # Instantiate the PostdocAgent
    postdoc_agent = PostdocAgent(
        # model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
        model="gemini-2.0-flash",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Prepare base structure for the final report
    report_content = {
        "title": f"Systematic Literature Review: {data['metadata']['research_topic']}",
        "sections": {
            "abstract": "",
            "subtopics_list": "",
            "analysis_subtopics": "",            # (1) Sub-topics
            "analysis_methodologies": "",        # (2) Key methodologies
            "analysis_findings": "",             # (3) Major findings
            "analysis_limitations": "",          # (4) Limitations
            # (5) Relationships to other studies
            "analysis_relationships": "",
            "analysis_future_prospects": "",     # (6) Future prospects
            # (7) Potential research directions
            "analysis_research_directions": "",
            "references": set()
        }
    }

    # -----------------------
    # 1) Generate Abstract
    # -----------------------
    try:
        report_content["sections"]["abstract"] = postdoc_agent.inference(
            f"Generate an abstract for a single, cohesive literature review on: {data['metadata']['research_topic']}.\n"
            "Avoid dividing the abstract by sub-topics, just provide a general overview.\n"
            "Write in a formal academic style."
        )
    except Exception as e:
        print(f"Abstract generation failed: {e}")

    # -----------------------
    # 2) Sub-topics as a Numbered List
    # -----------------------
    # Extract sub-topic names from the JSON keys
    subtopic_names = list(data["sub_topics"].keys())
    if not subtopic_names:
        subtopic_list_str = "No sub-topics found."
    else:
        subtopic_list_str = "\n".join(
            [f"{i}. {st}" for i, st in enumerate(subtopic_names, start=1)]
        )
    report_content["sections"]["subtopics_list"] = subtopic_list_str

    # -----------------------
    # 3) Gather All Papers
    # -----------------------
    all_papers = []
    for _, papers in data["sub_topics"].items():
        all_papers.extend(papers)

    # Convert the list of papers to a nicely formatted JSON string
    papers_json_str = json.dumps(all_papers, indent=2)

    # -----------------------
    # 4) Generate Literature Analysis (Seven Headings)
    # -----------------------
    # We'll do multiple calls to the PostdocAgent, one per heading, so that the text is coherent for each section.

    # (1) Sub-topics (incorporate them organically, do NOT create separate sections)
    # Even though we show a numbered sub-topic list above, this section is for the textual discussion.
    try:
        prompt_subtopics = (
            f"You are a senior researcher discussing sub-topics as they appear in the following papers:\n\n"
            f"{papers_json_str}\n\n"
            "Discuss how these sub-topics arise collectively across the studies in an integrated manner.\n"
            "Do NOT create separate headings for each sub-topic. Instead, weave them into a unified narrative.\n"
            "Write in a formal academic style."
        )
        report_content["sections"]["analysis_subtopics"] = postdoc_agent.inference(
            prompt_subtopics)
    except Exception as e:
        print(f"Sub-topics analysis generation failed: {e}")

    # (2) Key methodologies
    try:
        prompt_methodologies = (
            "Analyze the key methodologies used across all of these papers:\n\n"
            f"{papers_json_str}\n\n"
            "Discuss them in a unified manner (no separate sub-topic headings). "
            "Focus on experimental setups, data handling, analysis techniques, etc., in formal academic style."
        )
        report_content["sections"]["analysis_methodologies"] = postdoc_agent.inference(
            prompt_methodologies)
    except Exception as e:
        print(f"Key methodologies generation failed: {e}")

    # (3) Major findings
    try:
        prompt_findings = (
            "Analyze the major findings from the following papers:\n\n"
            f"{papers_json_str}\n\n"
            "Synthesize the findings into one cohesive discussion. "
            "Highlight common themes or unique results. Write in formal academic style."
        )
        report_content["sections"]["analysis_findings"] = postdoc_agent.inference(
            prompt_findings)
    except Exception as e:
        print(f"Major findings generation failed: {e}")

    # (4) Limitations
    try:
        prompt_limitations = (
            "Discuss the limitations identified across the following papers:\n\n"
            f"{papers_json_str}\n\n"
            "Unify them into a single discussion, referencing typical constraints, possible biases, and other weaknesses. "
            "Write in a formal academic style."
        )
        report_content["sections"]["analysis_limitations"] = postdoc_agent.inference(
            prompt_limitations)
    except Exception as e:
        print(f"Limitations generation failed: {e}")

    # (5) Relationships to other studies
    try:
        prompt_relationships = (
            "Discuss how these papers relate to each other and to broader research in the field:\n\n"
            f"{papers_json_str}\n\n"
            "Highlight interconnections, differences, or complementary findings. Formal academic style."
        )
        report_content["sections"]["analysis_relationships"] = postdoc_agent.inference(
            prompt_relationships)
    except Exception as e:
        print(f"Relationships generation failed: {e}")

    # (6) Future prospects
    try:
        prompt_future = (
            "Based on the combined insights from these papers:\n\n"
            f"{papers_json_str}\n\n"
            "Discuss future prospects for this field of research. "
            "What are upcoming developments, broader impacts, or next steps? Formal academic style."
        )
        report_content["sections"]["analysis_future_prospects"] = postdoc_agent.inference(
            prompt_future)
    except Exception as e:
        print(f"Future prospects generation failed: {e}")

    # (7) Potential research directions
    try:
        prompt_research_dirs = (
            "Based on the insights from these papers:\n\n"
            f"{papers_json_str}\n\n"
            "Propose potential research directions for future investigations. "
            "Stay cohesive and formal in style."
        )
        report_content["sections"]["analysis_research_directions"] = postdoc_agent.inference(
            prompt_research_dirs)
    except Exception as e:
        print(f"Potential research directions generation failed: {e}")

    # -----------------------
    # 5) Generate References
    # -----------------------
    try:
        for papers in data["sub_topics"].values():
            for paper in papers:
                # Example: "- Paper Title (2022). https://arxiv.org/abs/1234.5678"
                ref = f"- {paper['title']} ({paper['published']}). {paper['link']}"
                report_content["sections"]["references"].add(ref)
    except Exception as e:
        print(f"Reference generation failed: {e}")

    # -----------------------
    # 6) Build Final Markdown
    # -----------------------
    md_content = (
        f"# {report_content['title']}\n"
        f"*Generated on {datetime.now().strftime('%Y-%m-%d')}*\n\n"

        "## Abstract\n"
        f"{report_content['sections']['abstract']}\n\n"

        "## Sub-topics (Numbered List)\n"
        f"{report_content['sections']['subtopics_list']}\n\n"

        "## Literature Analysis\n"
        "### 1. Sub-topics\n"
        f"{report_content['sections']['analysis_subtopics']}\n\n"

        "### 2. Key methodologies\n"
        f"{report_content['sections']['analysis_methodologies']}\n\n"

        "### 3. Major findings\n"
        f"{report_content['sections']['analysis_findings']}\n\n"

        "### 4. Limitations\n"
        f"{report_content['sections']['analysis_limitations']}\n\n"

        "### 5. Relationships to other studies\n"
        f"{report_content['sections']['analysis_relationships']}\n\n"

        "### 6. Future prospects\n"
        f"{report_content['sections']['analysis_future_prospects']}\n\n"

        "### 7. Potential research directions\n"
        f"{report_content['sections']['analysis_research_directions']}\n\n"

        "## References\n"
    )

    # Sort references so the order is consistent
    sorted_references = sorted(report_content["sections"]["references"])
    md_content += "\n".join(sorted_references)

    # -----------------------
    # 7) Save to File
    # -----------------------
    try:
        with open("../database/literature_review_report.md", "w") as f:
            f.write(md_content)
        print("\n=== Single integrated report with all seven sections generated successfully ===")
    except Exception as e:
        print(f"Failed to save final report: {e}")


if __name__ == "__main__":
    generate_literature_report()
