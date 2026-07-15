import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "mistral"
)

MEMORY_DATABASE = os.getenv(
    "MEMORY_DATABASE",
    "jarvis_memory.db"
)