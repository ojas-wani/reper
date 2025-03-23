from tools import ArxivSearch
from agents import SubTopicAgent, PostdocAgent
import os
import re


def extract_prompt(text, word):
    code_block_pattern = rf"```{word}(.*?)```"
    code_blocks = re.findall(code_block_pattern, text, re.DOTALL)
    return "\n".join(code_blocks).strip()


def extract_sub_topics(text):
    # Extracts numbered list items (1., 2., etc.)
    pattern = r'\d+\.\s+(.*)'
    matches = re.findall(pattern, text)
    return matches


def get_sub_topics(sub_topic_agent, research_topic):
    # Initial step to get sub-topics
    initial_response = sub_topic_agent.inference(
        research_topic=research_topic,
        temp=0.8
    )
    print("Initial Agent Response:", initial_response, "\n~~~~~~~~~~~")

    # Extract sub-topics
    sub_topics = extract_sub_topics(initial_response)

    print("Potential Sub-topics:\n")
    for i, sub_topic in enumerate(sub_topics, 1):
        print(f"{i}. {sub_topic.strip()}")

    return sub_topics


def get_papers_by_sub_topic(sub_topic_agent, sub_topics):
    arxiv_engine = ArxivSearch()
    papers_collected = []

    for sub_topic in sub_topics:
        papers = arxiv_engine.find_papers_by_str(sub_topic.strip(), N=3)
        if papers:
            papers_collected.extend(papers.split("\n\n"))
            print(
                f"Found {len(papers.split('\n\n'))} papers for sub-topic: {sub_topic}")

    return papers_collected


def perform_literature_review(research_topic, num_papers):
    sub_topic_agent = SubTopicAgent(model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B", notes=[],
                                    openai_api_key=os.getenv("OPENAI_API_KEY"))
    postdoc_agent = PostdocAgent(model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B", notes=[],
                                 openai_api_key=os.getenv("OPENAI_API_KEY"))

    print(f"Starting literature review for: {research_topic}")

    # Get sub-topics
    sub_topics = get_sub_topics(sub_topic_agent, research_topic)

    # Get papers by sub-topics
    papers_collected = get_papers_by_sub_topic(sub_topic_agent, sub_topics)

    # Use PostdocAgent to select top 10 papers closely aligned with the main topic
    selected_papers = postdoc_agent.process_papers(
        papers_collected, research_topic)

    # Display results
    print("\nLiterature Review Completed. Selected Papers:")
    for i, paper in enumerate(selected_papers, 1):
        print(f"\nPaper #{i}:")
        print(paper)


if __name__ == "__main__":
    research_topic = "machine learning in Health care"
    perform_literature_review(research_topic, num_papers=5)


"""
def literature_review(self):

    arx_eng = ArxivSearch()
    max_tries = self.max_steps * 5 # lit review often requires extra steps
    # get initial response from PhD agent
    resp = self.phd.inference(self.research_topic, "literature review", step=0, temp=0.8)
    if self.verbose: print(resp, "\n~~~~~~~~~~~")
    # iterate until max num tries to complete task is exhausted
    for _i in range(max_tries):
        feedback = str()

        # grab summary of papers from arxiv
        if "```SUMMARY" in resp:
            query = extract_prompt(resp, "SUMMARY")
            papers = arx_eng.find_papers_by_str(query, N=self.arxiv_num_summaries)
            feedback = f"You requested arXiv papers related to the query {query}, here was the response\n{papers}"

        # grab full text from arxiv ID
        elif "```FULL_TEXT" in resp:
            query = extract_prompt(resp, "FULL_TEXT")
            # expiration timer so that paper does not remain in context too long
            arxiv_paper = f"```EXPIRATION {self.arxiv_paper_exp_time}\n" + arx_eng.retrieve_full_paper_text(query) + "```"
            feedback = arxiv_paper

        # if add paper, extract and add to lit review, provide feedback
        elif "```ADD_PAPER" in resp:
            query = extract_prompt(resp, "ADD_PAPER")
            feedback, text = self.phd.add_review(query, arx_eng)
            if len(self.reference_papers) < self.num_ref_papers:
                self.reference_papers.append(text)

        # completion condition
        if len(self.phd.lit_review) >= self.num_papers_lit_review:
            # generate formal review
            lit_review_sum = self.phd.format_review()
            # if human in loop -> check if human is happy with the produced review
            if self.human_in_loop_flag["literature review"]:
                retry = self.human_in_loop("literature review", lit_review_sum)
                # if not happy, repeat the process with human feedback
                if retry:
                    self.phd.lit_review = []
                    return retry
            # otherwise, return lit review and move on to next stage
            if self.verbose: print(self.phd.lit_review_sum)
            # set agent
            self.set_agent_attr("lit_review_sum", lit_review_sum)
            # reset agent state
            self.reset_agents()
            self.statistics_per_phase["literature review"]["steps"] = _i
            return False
        resp = self.phd.inference(self.research_topic, "literature review", feedback=feedback, step=_i + 1, temp=0.8)
        if self.verbose: print(resp, "\n~~~~~~~~~~~")
    raise Exception("Max tries during phase: Literature Review")
"""
