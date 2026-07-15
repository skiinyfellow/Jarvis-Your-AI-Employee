from core.llm.ollama_client import OllamaClient
from core.memory.memory_store import MemoryStore


class JarvisAgent:
    def __init__(self):
        self.llm = OllamaClient()
        self.memory = MemoryStore()

    def ask(self, question):
        memories = self.memory.get_all()
        context = "\n".join(memories)
        prompt = f"""
You are Jarvis, an AI employee.
Memory:
{context}
User:
{question}
"""
        answer = self.llm.generate(prompt)
        self.memory.save(question)
        self.memory.save(answer)
        return answer