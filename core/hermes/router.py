import logging
from typing import Callable, Optional, Dict

logger = logging.getLogger(__name__)


class HermesRouter:
    """Routes commands to appropriate handlers."""
    
    def __init__(self):
        self.routes: Dict[str, Callable] = {}
    
    def register(
        self,
        name: str,
        function: Callable
    ) -> None:
        """Register a command handler.
        
        Args:
            name: Command name or pattern
            function: Handler function
        """
        self.routes[name] = function
        logger.info(f"Registered route: {name}")
    
    def route(
        self,
        command: str
    ) -> Optional[Callable]:
        """Route command to handler.
        
        Args:
            command: User command
            
        Returns:
            Handler function if found, None otherwise
        """
        if not command or not isinstance(command, str):
            logger.warning("Invalid command for routing")
            return None
        
        command_lower = command.lower()
        
        # Try exact match first
        if command_lower in self.routes:
            logger.debug(f"Exact route match: {command_lower}")
            return self.routes[command_lower]
        
        # Try keyword match
        for key in self.routes:
            if key in command_lower:
                logger.debug(f"Keyword route match: {key}")
                return self.routes[key]
        
        logger.warning(f"No route found for: {command}")
        return None
    
    def list_routes(self) -> list:
        """List all registered routes.
        
        Returns:
            List of route names
        """
        return list(self.routes.keys())