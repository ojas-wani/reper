from inference import query_model

class BaseAgent:
    def __init__(self, model=None, notes=None, openai_api_key=None):
        self.model = model
        self.openai_api_key = openai_api_key
        self.notes = notes or []

    def inference(self, research_topic, temp=None):
        return query_model(
            model_str=self.model,
            prompt=self._user_prompt(research_topic),
            temp=temp,
            openai_api_key=self.openai_api_key,
            system_prompt=self._system_prompt()
        )

    def _system_prompt(self):
        return ("Your goal is to perform a literature review for the presented task and add papers to the literature review.\n")

    def _user_prompt(self, research_topic):
        return f"Research topic: {research_topic}\n"


class SubTopicAgent(BaseAgent):
    def _system_prompt(self):
        return (
            "You are a PhD student from a top university conducting a literature review. "
            "First, generate a numbered list of specific research sub-topics related to the main research topic. "
            "Each sub-topic should be a concise keyword or phrase. "
            "After listing sub-topics, use the SUMMARY command to search arXiv for papers on each sub-topic. "
            "Example response:\n"
            "1. Sub-topic 1\n" "```SUMMARY\nSub-topic 1\n```"
            "2. Sub-topic 2\n" "```SUMMARY\nSub-topic 2\n```"   
        )


class PostdocAgent(BaseAgent):
    def _system_prompt(self, papers=None):
        prompt = (
            "You are a postdoc researcher doing literature review for a research project proposal. "
            "Your task is to read papers gathered by your phd student and add them to the official review if they are relevant. "
            "Here is the papers gathered by your phd student:\n"
            "Use the ADD_PAPER command to add papers after reading them."
            "Read the paper summaries for each paper from the phd student and analyze them to see if they are relevant to the research project proposal.\n"
            "If you feel that you have to analyze the full text of a paper, you can use the FULL_TEXT command to get the full text of a paper."
            
            "If you believe a paper is relevant to the research project proposal, you can add it to the official review after reading using the following command: ```ADD_PAPER\narXiv_paper_title\narXiv_paper_ID\nArXiv_paper_link\nPAPER_SUMMARY\n```\nwhere arXiv_paper_ID is the ID of the arXiv paper, PAPER_SUMMARY is a brief summary of the paper, and ADD_PAPER is just the word ADD_PAPER. You can only add one paper at a time. \n"
            "Make sure to use ADD_PAPER when you see a relevant paper. DO NOT use SUMMARY too many times."
            "You can only use a single command per inference turn. Do not use more than one command per inference. If you use multiple commands, then only one of them will be executed, not both.\n"
            "Make sure to extensively discuss the experimental results in your summary.\n"
            "When performing a command, make sure to include the three ticks (```) at the top and bottom ```COMMAND\ntext\n``` where COMMAND is the specific command you want to run (e.g. ADD_PAPER, PAPER_TITLE, PAPER_LINK, SUMMARY). Do not use the word COMMAND make sure to use the actual command, e.g. your command should look exactly like this: ```ADD_PAPER\ntext\n``` (where the command could be from ADD_PAPER, PAPER_TITLE, PAPER_LINK, SUMMARY)\n"
            "Example response:\n"
            "```ADD_PAPER\narXiv_paper_title\narXiv_paper_ID\nArXiv_paper_link\nPAPER_SUMMARY\n```"
        )
        if papers:
            prompt += "\nHere are the papers gathered by your PhD student:\n"
            for paper in papers:
                prompt += f"- {paper}\n"
        return prompt

    def process_papers(self, papers, research_topic):
        selected_papers = []
        for paper in papers:
            response = self.inference(
                research_topic=research_topic,
                temp=0.8
            )
            if "```ADD_PAPER" in response:
                selected_papers.append(paper)
                if len(selected_papers) >= 10:
                    break
        return selected_papers

"""

command_instructions =
(
    "To collect paper summaries, use the following command: ```SUMMARY\nSEARCH QUERY\n```\n where SEARCH QUERY is a string that will be used to find papers with semantically similar content and SUMMARY is just the word SUMMARY. Make sure your search queries are very short.\n"
    "To get the full paper text for an arXiv paper, use the following command: ```FULL_TEXT\narXiv paper ID\n```\n where arXiv paper ID is the ID of the arXiv paper (which can be found by using the SUMMARY command), and FULL_TEXT is just the word FULL_TEXT. Make sure to read the full text using the FULL_TEXT command before adding it to your list of relevant papers.\n"
    "If you believe a paper is relevant to the research project proposal, you can add it to the official review after reading using the following command: ```ADD_PAPER\narXiv_paper_ID\nPAPER_SUMMARY\n```\nwhere arXiv_paper_ID is the ID of the arXiv paper, PAPER_SUMMARY is a brief summary of the paper, and ADD_PAPER is just the word ADD_PAPER. You can only add one paper at a time. \n"
    "Make sure to use ADD_PAPER when you see a relevant paper. DO NOT use SUMMARY too many times."
    "You can only use a single command per inference turn. Do not use more than one command per inference. If you use multiple commands, then only one of them will be executed, not both.\n"
    "Make sure to extensively discuss the experimental results in your summary.\n"
    "When performing a command, make sure to include the three ticks (```) at the top and bottom ```COMMAND\ntext\n``` where COMMAND is the specific command you want to run (e.g. ADD_PAPER, FULL_TEXT, SUMMARY). Do not use the word COMMAND make sure to use the actual command, e.g. your command should look exactly like this: ```ADD_PAPER\ntext\n``` (where the command could be from ADD_PAPER, FULL_TEXT, SUMMARY)\n")


phase_str = (
    "Your goal is to perform a literature review for the presented task and add papers to the literature review.\n"
    "You have access to arXiv and can perform two search operations: (1) finding many different paper summaries from a search query and (2) getting a single full paper text for an arXiv paper.\n"
)
"""
