from core.hermes.task import Task
import logging

logger = logging.getLogger(__name__)


def handle_message(message: str) -> Task:
    """Convert Telegram message to Task.
    
    Args:
        message: Raw message text
        
    Returns:
        Task object
    """
    if not message or not isinstance(message, str):
        logger.warning("Invalid message")
        raise ValueError("Message must be non-empty string")
    
    logger.debug(f"Handling message: {message[:50]}...")
    task = Task(
        command=message.strip(),
        user="telegram"
    )
    return task
