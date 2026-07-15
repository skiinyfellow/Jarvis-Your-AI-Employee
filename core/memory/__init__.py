"""
Memory - Persistent Context System

Manages long-term and short-term memory for Jarvis,
including context persistence and historical tracking.

TODO:
- Implement memory storage
- Add context management
- Create memory retrieval
- Setup memory optimization
"""

__version__ = "0.1.0"

from .storage import MemoryStore  # TODO: Create storage.py

__all__ = ["MemoryStore"]
