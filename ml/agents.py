from inference import query_model


class BaseAgent:
    def __init__(self, model=None, openai_api_key=None):
        self.model = model
        self.openai_api_key = openai_api_key

    def inference(self, prompt, temp=0.7):
        return query_model(
            model_str=self.model,
            prompt=prompt,
            temp=temp,
            openai_api_key=self.openai_api_key,
            system_prompt=self.system_prompt()
        )


class SubTopicAgent(BaseAgent):
    def system_prompt(self):
        return (
            "Generate 5-7 specific research sub-topics for a literature review. "
            "Format: Numbered list of concise phrases (3-5 words).\n"
            "Example:\n"
            "1. Neural radiance fields in 3D reconstruction\n"
            "2. Diffusion models for medical imaging"
        )


class PostdocAgent(BaseAgent):
    def system_prompt(self):
        return (
            "You are a senior researcher conducting systematic literature reviews. "
            "Your tasks:\n"
            "1. Generate final report using stored paper information.\n"
            "2. Compare methodologies and results\n"
            "3. Identify research gaps\n"
            "4. Generate academic-quality reports\n\n"
            "Focus on:\n"
            "- Critical analysis of experimental designs\n"
            "- Relationships between studies\n"
            "- Practical/theoretical implications\n"
            "- Clear identification of contradictions\n"
            "- Formal academic writing style"
        )
