import requests
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class OllamaConnectionError(Exception):
    """Raised when Ollama connection fails."""
    pass


class OllamaClient:
    """Client for Ollama local LLM service."""
    
    def __init__(self):
        self.host = os.getenv(
            "OLLAMA_HOST",
            "http://localhost:11434"
        )
        self.model = os.getenv(
            "OLLAMA_MODEL",
            "mistral"
        )
        self.timeout = int(os.getenv("OLLAMA_TIMEOUT", "30"))
        self.max_retries = int(os.getenv("OLLAMA_MAX_RETRIES", "3"))
    
    def _is_available(self) -> bool:
        """Check if Ollama service is available."""
        try:
            response = requests.get(
                f"{self.host}/api/tags",
                timeout=5
            )
            return response.status_code == 200
        except (requests.RequestException, Exception) as e:
            logger.warning(f"Ollama unavailable: {e}")
            return False
    
    def generate(self, prompt: str) -> str:
        """Generate response from Ollama with error handling.
        
        Args:
            prompt: The prompt to send to the model
            
        Returns:
            Generated response text
            
        Raises:
            OllamaConnectionError: If Ollama is unavailable
        """
        if not self._is_available():
            raise OllamaConnectionError(
                f"Ollama service not available at {self.host}"
            )
        
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.Timeout:
            logger.error(f"Ollama request timeout ({self.timeout}s)")
            raise OllamaConnectionError(
                f"Ollama request timeout after {self.timeout}s"
            )
        except requests.RequestException as e:
            logger.error(f"Ollama request failed: {e}")
            raise OllamaConnectionError(f"Ollama request failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise OllamaConnectionError(f"Unexpected error: {e}")