# literature_review.py

import os
import re
import json
from datetime import datetime
from tools import ArxivSearch
from agents import SubTopicAgent


def extract_sub_topics(text):
    """
    Extract sub-topics from the user/generative model response.
    We expect lines in the format:
      1. SubTopicOne
      2. SubTopicTwo
      ...
    """
    try:
        return [
            m.group(1).strip()
            for m in re.finditer(r'\d+\.\s+(.*?)(?:\n|$)', text)
            if len(m.group(1).strip()) > 3
        ]
    except Exception as e:
        print(f"Error extracting sub-topics: {e}")
        return []


def extract_paper_metadata(paper):
    """
    Convert a raw paper info string into a dict with title, arxiv_id, published, summary, link.
    """
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


def perform_literature_review(research_topic, start_year, end_year, max_count=50, open_ai_key=None, base_url=None, user_subtopics=None):
    """
    Perform a literature review:
      1. Use provided sub-topics or generate new ones if none provided
      2. Determine how many papers per sub-topic, so total does not exceed max_count.
      3. For each sub-topic, fetch papers (filtered by date) and collect up to that limit.
      4. Save results to literature_data.json.
    """
    print(f"\n=== Starting Literature Review: {research_topic} ===")
    print(
        f"Date Range: {start_year}-{end_year}, Max total papers: {max_count}\n")

    # Base structure for the final JSON
    report = {
        "metadata": {
            "research_topic": research_topic,
            "generated_at": datetime.now().isoformat(),
            "source": "arXiv"
        },
        "sub_topics": {}
    }

    # 1) Get Sub-Topics (either from user or generate new ones)
    try:
        if user_subtopics:
            print("Using user-provided sub-topics...")
            sub_topics = user_subtopics
            print(f"Using {len(sub_topics)} sub-topics: {len([s for s in sub_topics if s in user_subtopics])} user-provided and {len([s for s in sub_topics if s not in user_subtopics])} AI-generated")
            print(f"User-provided sub-topics: {[s for s in sub_topics if s in user_subtopics]}")
            print(f"AI-generated sub-topics: {[s for s in sub_topics if s not in user_subtopics]}")
        else:
            print("Generating sub-topics...")
            sub_agent = SubTopicAgent(
                model="gemini-2.0-flash",
                openai_api_key=open_ai_key,
                base_url=base_url
            )
            sub_topic_response = sub_agent.inference(research_topic)
            sub_topics = extract_sub_topics(sub_topic_response)
            
        if not sub_topics:
            print("No sub-topics identified; exiting.")
            return None

        print(f"Identified sub-topics:\n  " + "\n  ".join(sub_topics))
    except Exception as e:
        print(f"Failed to get sub-topics: {e}")
        return None

    # 2) Decide how many papers per sub-topic
    sub_topic_count = len(sub_topics)
    papers_per_subtopic = max_count // sub_topic_count  # integer division
    if papers_per_subtopic < 1:
        papers_per_subtopic = 1

    print(
        f"\nWe have {sub_topic_count} sub-topics. Each sub-topic will collect up to {papers_per_subtopic} papers.\n")

    arxiv_engine = ArxivSearch()

    # 3) For each sub-topic, fetch papers
    for st in sub_topics:
        print(f"\nSearching for papers on: {st}")
        try:
            # Combine research topic with sub-topic for more focused search
            combined_query = f"{research_topic} {st}"
            print(f"  Searching with query: {combined_query}")
            raw_papers = arxiv_engine.find_papers_by_str(
                query=combined_query,
                start_year=start_year,
                end_year=end_year,
                N=50  # Increased from 100 to ensure we get enough papers per sub-topic
            )
            papers = raw_papers.split("\n\n")
            papers = [p for p in papers if p.strip()]
            print(f"  Found {len(papers)} raw papers for '{st}'")

            # Extract metadata from each paper
            paper_metadata = []
            for paper in papers:
                metadata = extract_paper_metadata(paper)
                if metadata:
                    paper_metadata.append(metadata)

            # Limit to papers_per_subtopic
            paper_metadata = paper_metadata[:papers_per_subtopic]
            report["sub_topics"][st] = paper_metadata

            print(f"  Found {len(paper_metadata)} papers for '{st}'")
        except Exception as e:
            print(f"  Error searching for '{st}': {e}")
            report["sub_topics"][st] = []

    # 4) Save final JSON
    try:
        os.makedirs("database", exist_ok=True)
        with open("database/literature_data.json", "w") as f:
            json.dump(report, f, indent=2)
        print("\n=== Data collection completed successfully ===")
    except Exception as e:
        print(f"\nFailed to save results: {e}")

    return report


if __name__ == "__main__":
    # Example usage:
    research_idea = "LLM for high quality code generation"
    start_year = 2020
    end_year = 2025
    max_count = 20
    perform_literature_review(research_idea, start_year, end_year, max_count)
