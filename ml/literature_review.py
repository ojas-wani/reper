import os
import re
import json
import time
from datetime import datetime
from tools import ArxivSearch
from agents import SubTopicAgent


def extract_sub_topics(text):
    try:
        return [m.group(1).strip() for m in re.finditer(r'\d+\.\s+(.*?)(?:\n|$)', text) if len(m.group(1).strip()) > 3]
    except Exception as e:
        print(f"Error extracting sub-topics: {e}")
        return []


def extract_paper_metadata(paper):
    try:
        return {
            "title": re.search(r"Title: (.*)", paper).group(1),
            "arxiv_id": re.search(r"ID: (.*)", paper).group(1),
            "published": re.search(r"Published: (.*)", paper).group(1),
            "summary": re.search(r"Summary: (.*?)(?:\n[A-Z]+: |$)", paper, re.DOTALL).group(1).strip(),
            "link": re.search(r"Link: (.*)", paper).group(1)
        }
    except Exception as e:
        print(f"Failed to parse paper: {e}")
        return None


def perform_literature_review(research_topic):
    print(f"\n=== Starting Literature Review: {research_topic} ===\n")

    report = {
        "metadata": {
            "research_topic": research_topic,
            "generated_at": datetime.now().isoformat(),
            "source": "arXiv"
        },
        "sub_topics": {}
    }

    try:
        print("Generating sub-topics...")
        sub_agent = SubTopicAgent(model="gemini-2.0-flash",
                                  openai_api_key=os.getenv("OPENAI_API_KEY"))
        sub_topics = extract_sub_topics(sub_agent.inference(research_topic))
        print(f"Identified sub-topics: {', '.join(sub_topics)}\n")
    except Exception as e:
        print(f"Failed to generate sub-topics: {e}")
        return None

    arxiv_engine = ArxivSearch()

    for st_idx, st in enumerate(sub_topics, 1):
        print(f"\nProcessing sub-topic {st_idx}/{len(sub_topics)}: {st}")
        report["sub_topics"][st] = []

        try:
            raw_papers = arxiv_engine.find_papers_by_str(
                st, N=3)  # Top 3 papers only
            papers = raw_papers.split("\n\n")
            print(f"  Found {len(papers)} papers")
        except Exception as e:
            print(f"  Paper search failed: {e}")
            continue

        for p_idx, paper in enumerate(papers, 1):
            paper_data = extract_paper_metadata(paper)
            if paper_data:
                report["sub_topics"][st].append(paper_data)
                print(f"    Added paper {p_idx}: {paper_data['title']}.")

    try:
        # Ensure the database folder exists
        os.makedirs("../database", exist_ok=True)
        with open("../database/literature_data.json", "w") as f:
            json.dump(report, f, indent=2)
        print("\n=== Data collection completed successfully ===")
    except Exception as e:
        print(f"\nFailed to save results: {e}")

    return report


if __name__ == "__main__":
    research_idea = "Tools for the literature review. Similar to automated systematic review."
    perform_literature_review(research_idea)
