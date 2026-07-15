import requests
import os


class OllamaClient:
    def __init__(self):
        self.host = os.getenv(
            "OLLAMA_HOST",
            "http://localhost:11434"
        )
        self.model = os.getenv(
            "OLLAMA_MODEL",
            "mistral"
        )

    def generate(self, prompt):
        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get(
            "response",
            ""
        )