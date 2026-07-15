import logging


class ConversationMemory:
    """In-memory conversation history."""
    
    def __init__(self):
        self.messages = []
        self.logger = logging.getLogger(__name__)
    
    def add_user(self, message: str) -> bool:
        """Add user message to conversation.
        
        Args:
            message: User message
            
        Returns:
            True if added successfully
        """
        if not message or not isinstance(message, str):
            self.logger.warning("Invalid user message")
            return False
        
        self.messages.append({
            "role": "user",
            "content": message.strip()
        })
        return True
    
    def add_ai(self, message: str) -> bool:
        """Add AI response to conversation.
        
        Args:
            message: AI response
            
        Returns:
            True if added successfully
        """
        if not message or not isinstance(message, str):
            self.logger.warning("Invalid AI message")
            return False
        
        self.messages.append({
            "role": "assistant",
            "content": message.strip()
        })
        return True
    
    def history(self) -> list:
        """Get full conversation history.
        
        Returns:
            List of messages
        """
        return self.messages.copy()
    
    def clear(self) -> bool:
        """Clear conversation history.
        
        Returns:
            True if cleared successfully
        """
        self.messages = []
        return True
