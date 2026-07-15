import logging

logger = logging.getLogger(__name__)


class VectorMemory:
    """Simple in-memory vector search for semantic similarity."""
    
    def __init__(self):
        self.documents = []
    
    def add(self, text: str) -> bool:
        """Add document to vector memory.
        
        Args:
            text: Document text
            
        Returns:
            True if added successfully
        """
        if not text or not isinstance(text, str):
            logger.warning("Invalid text for vector memory")
            return False
        
        self.documents.append(text.strip())
        return True
    
    def search(self, query: str, limit: int = 5) -> list:
        """Search documents for query (simple keyword matching).
        
        Args:
            query: Search query
            limit: Maximum results to return
            
        Returns:
            List of matching documents
        """
        if not query or not isinstance(query, str):
            return []
        
        query_lower = query.lower()
        matches = []
        
        for doc in self.documents:
            if query_lower in doc.lower():
                matches.append(doc)
        
        return matches[:limit]
    
    def clear(self) -> bool:
        """Clear all documents.
        
        Returns:
            True if cleared successfully
        """
        self.documents = []
        return True