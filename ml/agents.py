# agents.py

from inference import query_model


class BaseAgent:
    def __init__(self, model=None, openai_api_key=None, base_url=None):
        self.model = model
        self.openai_api_key = openai_api_key
        self.base_url = base_url

    def inference(self, prompt, temp=0.7):
        return query_model(
            model_str=self.model,
            prompt=prompt,
            temp=temp,
            openai_api_key=self.openai_api_key,
            base_url=self.base_url,
            system_prompt=self.system_prompt()
        )


class SubTopicAgent(BaseAgent):
    def system_prompt(self):
        return (
            "Generate exactly 6-7 specific research sub-topics for a literature review. "
            "Format: Numbered list of concise phrases (3-5 words).\n"
            "Example:\n"
            "1. Neural radiance fields in 3D reconstruction\n"
            "2. Diffusion models for medical imaging"
        )

    def get_user_subtopics(self):
        """Get sub-topics from user input."""
        print("\nEnter your sub-topics (one per line). Type 'done' when finished:")
        user_subtopics = []
        while True:
            subtopic = input("> ").strip()
            if subtopic.lower() == 'done':
                break
            if subtopic:  # Only add non-empty sub-topics
                user_subtopics.append(subtopic)
        return user_subtopics

    def review_and_refine_subtopics(self, generated_subtopics, user_subtopics):
        """Show all sub-topics and allow user to refine them."""
        all_subtopics = generated_subtopics + user_subtopics
        
        while True:
            print("\nCurrent sub-topics:")
            for i, subtopic in enumerate(all_subtopics, 1):
                print(f"{i}. {subtopic}")
            
            print("\nOptions:")
            print("1. Add more sub-topics")
            print("2. Remove a sub-topic")
            print("3. Edit a sub-topic")
            print("4. Continue with current sub-topics")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                new_subtopics = self.get_user_subtopics()
                all_subtopics.extend(new_subtopics)
            elif choice == '2':
                try:
                    index = int(input("Enter the number of the sub-topic to remove: ")) - 1
                    if 0 <= index < len(all_subtopics):
                        removed = all_subtopics.pop(index)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid index")
                except ValueError:
                    print("Please enter a valid number")
            elif choice == '3':
                try:
                    index = int(input("Enter the number of the sub-topic to edit: ")) - 1
                    if 0 <= index < len(all_subtopics):
                        new_text = input("Enter new text: ").strip()
                        if new_text:
                            all_subtopics[index] = new_text
                    else:
                        print("Invalid index")
                except ValueError:
                    print("Please enter a valid number")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        
        return all_subtopics

    def get_final_subtopics(self, prompt):
        """Get both generated and user sub-topics, then refine them."""
        # Get AI-generated sub-topics
        generated_response = self.inference(prompt)
        generated_subtopics = [line.strip() for line in generated_response.split('\n') 
                             if line.strip() and line[0].isdigit()]
        
        # Get user sub-topics
        user_subtopics = self.get_user_subtopics()
        
        # Review and refine all sub-topics
        final_subtopics = self.review_and_refine_subtopics(generated_subtopics, user_subtopics)
        
        return final_subtopics


class PostdocAgent(BaseAgent):
    def system_prompt(self):
        return (
            "You are a senior researcher with extensive experience in conducting "
            "systematic literature reviews. You excel at writing a SINGLE, cohesive "
            "academic report without dividing the text by sub-topic headings.\n\n"
            "You must:\n"
            "1. Provide a holistic, unified analysis of the provided sub-topics and papers.\n"
            "2. Critically assess methodologies, major findings, limitations, and relationships.\n"
            "3. Discuss potential research directions and future prospects.\n"
            "4. Maintain a formal academic writing style.\n\n"
            "Key instructions:\n"
            "- DO NOT produce multiple separate sections named after each sub-topic.\n"
            "- Instead, weave the sub-topics organically into a single integrated narrative.\n"
            "- Provide well-structured paragraphs that present a cohesive discussion.\n"
            "- When referring to sub-topics, label them in-line (e.g., '[Theme X]: ...'), but do not isolate them into standalone headings.\n"
            "- Summaries must focus on the overarching research question, bridging the sub-topics.\n"
            "- Identify future directions or gaps that emerge from the synergy of these studies.\n\n"
            "Remember:\n"
            "- The user provides the sub-topics and relevant papers.\n"
            "- Your primary task is to consolidate them into ONE unified analysis.\n"
            "- Keep the tone formal, precise, and academically rigorous.\n"
        )


class NovelApproachAgent(BaseAgent):
    def system_prompt(self):
        return (
            "You are an 'innovation consultant' for academic research. You specialize in:\n"
            "1. Identifying knowledge gaps.\n"
            "2. Proposing novel or creative research designs.\n"
            "3. Suggesting how to leverage or extend existing studies in new ways.\n\n"
            "When given the user's existing literature review and context, your task is:\n"
            "- Synthesize a new research direction or experimental approach.\n"
            "- Explain how it builds on existing findings.\n"
            "- Highlight its potential significance or impact.\n"
            "- Maintain a formal, yet forward-thinking, academic style.\n\n"
            "Key Instructions:\n"
            "- Assume the user already has a thorough literature review.\n"
            "- Do NOT simply repeat known findings—focus on creative, fresh directions.\n"
            "- If relevant, propose relevant data, methods, or partnerships not yet considered.\n"
            "- Always justify why your novel approach is worth investigating, pointing to the relevant gaps in the literature.\n"
        )
