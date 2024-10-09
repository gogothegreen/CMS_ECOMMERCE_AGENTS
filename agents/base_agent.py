import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def query_llm(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content

    def process_task(self, task):
        raise NotImplementedError("Subclasses must implement this method")
