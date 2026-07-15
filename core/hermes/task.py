from datetime import datetime
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


class Task:
    """Represents a unit of work in Jarvis."""
    
    def __init__(
        self,
        command: str,
        user: str = "system"
    ):
        """Initialize a task.
        
        Args:
            command: The command/action to execute
            user: User who initiated the task
        """
        self.id = str(uuid4())
        self.command = command
        self.user = user
        self.created = datetime.utcnow()
        self.status = "pending"
        self.result = None
        logger.debug(f"Task created: {self.id} - {command}")
    
    def complete(self, result=None):
        """Mark task as completed.
        
        Args:
            result: Optional result data
        """
        self.status = "completed"
        self.result = result
        logger.info(f"Task completed: {self.id}")
    
    def fail(self, error: str = None):
        """Mark task as failed.
        
        Args:
            error: Optional error message
        """
        self.status = "failed"
        self.result = error
        logger.error(f"Task failed: {self.id} - {error}")
    
    def to_dict(self) -> dict:
        """Convert task to dictionary.
        
        Returns:
            Task data as dict
        """
        return {
            "id": self.id,
            "command": self.command,
            "user": self.user,
            "created": self.created.isoformat(),
            "status": self.status,
            "result": self.result
        }