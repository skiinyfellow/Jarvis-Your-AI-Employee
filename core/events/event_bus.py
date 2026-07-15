import logging
from typing import Callable, Dict, List, Any

logger = logging.getLogger(__name__)


class EventBus:
    """Simple event bus for pub/sub pattern."""
    
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
    
    def subscribe(
        self,
        event: str,
        callback: Callable
    ) -> None:
        """Subscribe to event.
        
        Args:
            event: Event name
            callback: Callback function
        """
        if not event or not callback:
            logger.warning("Invalid event or callback")
            return
        
        if not callable(callback):
            logger.error("Callback must be callable")
            raise ValueError("Callback must be callable")
        
        self.listeners.setdefault(
            event,
            []
        ).append(callback)
        logger.debug(f"Subscribed to event: {event}")
    
    def publish(
        self,
        event: str,
        data: Any = None
    ) -> int:
        """Publish event to all subscribers.
        
        Args:
            event: Event name
            data: Event data
            
        Returns:
            Number of listeners triggered
        """
        listeners = self.listeners.get(event, [])
        count = 0
        
        for callback in listeners:
            try:
                callback(data)
                count += 1
            except Exception as e:
                logger.error(f"Error in event callback: {e}")
        
        logger.debug(f"Event published: {event} ({count} listeners)")
        return count
    
    def unsubscribe(
        self,
        event: str,
        callback: Callable
    ) -> bool:
        """Unsubscribe from event.
        
        Args:
            event: Event name
            callback: Callback to remove
            
        Returns:
            True if removed, False otherwise
        """
        if event not in self.listeners:
            return False
        
        try:
            self.listeners[event].remove(callback)
            logger.debug(f"Unsubscribed from event: {event}")
            return True
        except ValueError:
            return False