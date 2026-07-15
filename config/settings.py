import os
from dotenv import load_dotenv

load_dotenv()

# AI Configuration
OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "mistral"
)

OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "30"))
OLLAMA_MAX_RETRIES = int(os.getenv("OLLAMA_MAX_RETRIES", "3"))

# Memory Configuration
MEMORY_DATABASE = os.getenv(
    "MEMORY_DATABASE",
    "jarvis_memory.db"
)

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
