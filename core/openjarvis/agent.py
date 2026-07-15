from core.llm.ollama_client import OllamaClient, OllamaConnectionError
from core.memory.memory_store import MemoryStore
import logging

logger = logging.getLogger(__name__)


class JarvisAgent:
    """Main Jarvis AI agent combining LLM and memory."""
    
    def __init__(self):
        """Initialize Jarvis agent.
        
        Raises:
            RuntimeError: If components fail to initialize
        """
        try:
            self.llm = OllamaClient()
            self.memory = MemoryStore()
            logger.info("JarvisAgent initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize JarvisAgent: {e}")
            raise RuntimeError(f"Failed to initialize JarvisAgent: {e}")
    
    def ask(self, question: str) -> str:
        """Ask Jarvis a question.
        
        Args:
            question: User question
            
        Returns:
            AI generated response
            
        Raises:
            ValueError: If question is invalid
            OllamaConnectionError: If LLM is unavailable
        """
        if not question or not isinstance(question, str):
            raise ValueError("Question must be a non-empty string")
        
        try:
            # Get recent memory context
            memories = self.memory.get_all()[:5]  # Last 5 memories
            context = "\n".join(memories) if memories else "(No prior context)"
            
            # Build prompt
            prompt = f"""
You are Jarvis, an AI employee assistant. You are helpful, professional, and focused on business operations.

Recent context:
{context}

User question:
{question}

Provide a concise, professional response.
"""
            
            # Generate response
            answer = self.llm.generate(prompt)
            
            # Store in memory
            self.memory.save(f"Q: {question}")
            self.memory.save(f"A: {answer}")
            
            logger.debug(f"Agent processed question: {question[:50]}...")
            return answer
        
        except OllamaConnectionError as e:
            logger.error(f"LLM connection error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error in agent ask: {e}")
            raise
