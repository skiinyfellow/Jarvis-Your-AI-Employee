import sqlite3
from datetime import datetime
import os
import logging

logger = logging.getLogger(__name__)


class MemoryStore:
    """SQLite-backed memory storage for Jarvis."""
    
    def __init__(self, path: str = None):
        """Initialize memory store.
        
        Args:
            path: Path to SQLite database. Defaults to MEMORY_DATABASE env var
                  or 'jarvis_memory.db'
        """
        if path is None:
            path = os.getenv("MEMORY_DATABASE", "jarvis_memory.db")
        
        self.path = path
        try:
            self.connection = sqlite3.connect(path)
            self.create_table()
            logger.info(f"Memory store initialized at {path}")
        except sqlite3.Error as e:
            logger.error(f"Failed to initialize memory store: {e}")
            raise
    
    def create_table(self):
        """Create memories table if it doesn't exist."""
        try:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Failed to create table: {e}")
            raise
    
    def save(self, content: str) -> bool:
        """Save content to memory.
        
        Args:
            content: Text to save
            
        Returns:
            True if saved successfully
        """
        if not content or not isinstance(content, str):
            logger.warning("Invalid content for memory save")
            return False
        
        try:
            self.connection.execute(
                """
                INSERT INTO memories
                (content, created_at)
                VALUES (?, ?)
                """,
                (
                    content.strip(),
                    datetime.utcnow().isoformat()
                )
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Failed to save memory: {e}")
            return False
    
    def get_all(self) -> list:
        """Retrieve all memories.
        
        Returns:
            List of memory content strings
        """
        try:
            result = self.connection.execute(
                "SELECT content FROM memories ORDER BY created_at DESC"
            )
            return [
                row[0]
                for row in result.fetchall()
            ]
        except sqlite3.Error as e:
            logger.error(f"Failed to retrieve memories: {e}")
            return []
    
    def clear(self) -> bool:
        """Clear all memories.
        
        Returns:
            True if cleared successfully
        """
        try:
            self.connection.execute("DELETE FROM memories")
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Failed to clear memories: {e}")
            return False
    
    def close(self):
        """Close database connection."""
        try:
            if self.connection:
                self.connection.close()
        except sqlite3.Error as e:
            logger.error(f"Error closing connection: {e}")