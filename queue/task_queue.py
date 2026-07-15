from collections import deque
import logging
from typing import Optional
from core.hermes.task import Task

logger = logging.getLogger(__name__)


class TaskQueue:
    """FIFO task queue for workflow execution."""
    
    def __init__(self):
        self.queue: deque = deque()
        self._processed_count = 0
    
    def add(self, task: Task) -> None:
        """Add task to queue.
        
        Args:
            task: Task to add
        """
        if not task or not isinstance(task, Task):
            logger.warning("Invalid task")
            raise ValueError("Must be a Task object")
        
        self.queue.append(task)
        logger.debug(f"Task added to queue: {task.id}")
    
    def next(self) -> Optional[Task]:
        """Get next task from queue.
        
        Returns:
            Next Task or None if queue empty
        """
        if self.queue:
            task = self.queue.popleft()
            self._processed_count += 1
            logger.debug(f"Task dequeued: {task.id}")
            return task
        return None
    
    def size(self) -> int:
        """Get queue size.
        
        Returns:
            Number of tasks in queue
        """
        return len(self.queue)
    
    def is_empty(self) -> bool:
        """Check if queue is empty.
        
        Returns:
            True if empty, False otherwise
        """
        return len(self.queue) == 0
    
    def clear(self) -> None:
        """Clear all tasks from queue."""
        self.queue.clear()
        logger.debug("Queue cleared")
    
    def processed_count(self) -> int:
        """Get total tasks processed.
        
        Returns:
            Count of processed tasks
        """
        return self._processed_count
