"""
Jarvis Telegram Bot Interface

Receives user messages via Telegram and converts them to tasks.
"""

import logging
from telegram.handlers import handle_message
from core.hermes.task import Task

logger = logging.getLogger(__name__)


def process_message(message: str) -> Task:
    """Process incoming Telegram message.
    
    Args:
        message: User message text
        
    Returns:
        Task object for workflow execution
    """
    try:
        task = handle_message(message)
        logger.info(f"Message processed into task: {task.id}")
        return task
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        raise


if __name__ == "__main__":
    # Test message processing
    test_message = "check inventory"
    task = process_message(test_message)
    print(f"Task ID: {task.id}")
    print(f"Command: {task.command}")
    print(f"Status: {task.status}")
