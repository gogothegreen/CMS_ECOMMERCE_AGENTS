from .base_agent import BaseAgent

class ProjectManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Project Manager")

    def process_task(self, task):
        prompt = f"As a project manager for a CMS with e-commerce features, analyze this task and provide a high-level plan: {task}"
        return self.query_llm(prompt)

    def break_down_tasks(self, project_description):
        prompt = f"Break down this project into specific tasks for a CMS with e-commerce features: {project_description}"
        return self.query_llm(prompt)
