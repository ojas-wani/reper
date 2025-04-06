import json
from agents import NovelApproachAgent


def propose_novel_approach_and_save(open_ai_key=None, base_url=None):
    """
    1. Load literature data from JSON.
    2. Call the NovelApproachAgent to propose a new research direction.
    3. Save the resulting approach as Markdown.
    """
    try:
        with open("database/literature_data.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load literature data: {e}")
        return

    prompt = (
        "Below is the literature review data.\n\n"
        f"Research Topic: {data['metadata']['research_topic']}\n"
        f"Sub-topics found: {list(data['sub_topics'].keys())}\n\n"
        "Based on these findings, please propose a novel research approach that:\n"
        "- Addresses existing gaps or limitations\n"
        "- Builds on current methodologies\n"
        "- Introduces an innovative angle or extension of the studies\n"
        "Provide a concise but thorough academic rationale.\n"
    )

    novel_agent = NovelApproachAgent(
        model="gemini-2.0-flash",
        openai_api_key=open_ai_key,
        base_url=base_url
    )

    novel_approach = novel_agent.inference(prompt=prompt)

    md_content = (
        f"# Novel Research Approach\n\n"
        f"**Topic**: {data['metadata']['research_topic']}\n\n"
        f"**Proposed Approach**:\n\n"
        f"{novel_approach}\n"
    )

    output_file = "database/novel_approach.md"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Novel approach saved successfully to '{output_file}'!")
    except Exception as e:
        print(f"Failed to save novel approach: {e}")


if __name__ == "__main__":
    propose_novel_approach_and_save()
