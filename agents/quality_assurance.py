from .base_agent import BaseAgent

class QualityAssuranceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Quality Assurance")

    def process_task(self, task):
        prompt = f"As a QA specialist, review this task for a CMS with e-commerce features: {task}"
        return self.query_llm(prompt)

    def review_code(self, code):
        prompt = f"Review this Node.js code for best practices, security, and potential issues:\n\n{code}"
        return self.query_llm(prompt)

    def generate_tests(self, code):
        prompt = f"Generate unit tests for this Node.js code:\n\n{code}"
        return self.query_llm(prompt)
