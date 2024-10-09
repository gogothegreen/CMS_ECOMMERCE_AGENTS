from .base_agent import BaseAgent

class FullStackDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__("Full-Stack Developer")

    def process_task(self, task):
        prompt = f"As a full-stack developer using Node.js, implement this task for a CMS with e-commerce features: {task}"
        return self.query_llm(prompt)

    def generate_code(self, task):
        prompt = f"Generate Node.js code for this task in a CMS with e-commerce features: {task}"
        return self.query_llm(prompt)

    def refactor_code(self, code):
        prompt = f"Refactor and improve this Node.js code:\n\n{code}"
        return self.query_llm(prompt)
