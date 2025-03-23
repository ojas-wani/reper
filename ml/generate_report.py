import os
import json
from datetime import datetime
from agents import PostdocAgent


def generate_literature_report():
    try:
        with open("../database/literature_data.json") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load data: {e}")
        return

    postdoc_agent = PostdocAgent(
        # model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
        model="gemini-2.0-flash",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    report_content = {
        "title": f"Systematic Literature Review: {data['metadata']['research_topic']}",
        "sections": {
            "abstract": "",
            "themes": {},
            "references": set()
        }
    }

    # Abstract
    try:
        report_content["sections"]["abstract"] = postdoc_agent.inference(
            f"Generate abstract for literature review on: {data['metadata']['research_topic']}\n"
            f"Sub-topics: {list(data['sub_topics'].keys())}\n"
            "Include methodology, key findings, and implications."
        )
    except Exception as e:
        print(f"Abstract generation failed: {e}")

    # Thematic Analysis
    for theme, papers in data["sub_topics"].items():
        try:
            analysis = postdoc_agent.inference(
                f"Analyze theme: {theme}\n"
                f"Papers: {json.dumps(papers)}\n"
                "Provide critical analysis covering:\n"
                "- Key methodologies\n- Major findings\n- Limitations\n- Relationships to other studies"
            )
            report_content["sections"]["themes"][theme] = analysis
        except Exception as e:
            print(f"Theme analysis failed for {theme}: {e}")

    # References
    try:
        for papers in data["sub_topics"].values():
            for paper in papers:
                ref = f"- {paper['title']} ({paper['published']}). {paper['link']}"
                report_content["sections"]["references"].add(ref)
    except Exception as e:
        print(f"Reference generation failed: {e}")

    # Generate Markdown
    md_content = f"""# {report_content['title']}
*Generated on {datetime.now().strftime('%Y-%m-%d')}*

## Abstract
{report_content['sections']['abstract']}

## Thematic Analysis
"""

    for theme, analysis in report_content['sections']['themes'].items():
        md_content += f"\n### {theme}\n{analysis}"

    md_content += "\n\n## References\n" + \
        "\n".join(sorted(report_content['sections']['references']))

    try:
        with open("../database/literature_review_report.md", "w") as f:
            f.write(md_content)
        print("\n=== Report generated successfully ===")
    except Exception as e:
        print(f"Failed to save report: {e}")


if __name__ == "__main__":
    generate_literature_report()
