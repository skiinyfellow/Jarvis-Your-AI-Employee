import logging
from typing import Callable, List, Any

logger = logging.getLogger(__name__)


class Workflow:
    """Represents a multi-step workflow."""
    
    def __init__(self, name: str):
        """Initialize workflow.
        
        Args:
            name: Workflow name
        """
        self.name = name
        self.steps: List[Callable] = []
        logger.debug(f"Workflow created: {name}")
    
    def add_step(
        self,
        function: Callable
    ) -> None:
        """Add execution step to workflow.
        
        Args:
            function: Step function that accepts context
        """
        if not callable(function):
            logger.error("Step must be callable")
            raise ValueError("Step must be callable")
        
        self.steps.append(function)
        logger.debug(f"Step added to {self.name}")
    
    def execute(
        self,
        context: Any
    ) -> Any:
        """Execute all workflow steps.
        
        Args:
            context: Initial context data
            
        Returns:
            Final result after all steps
        """
        result = context
        step_count = 0
        
        try:
            for step in self.steps:
                step_count += 1
                logger.debug(f"Executing step {step_count} of {len(self.steps)}")
                result = step(result)
            
            logger.info(f"Workflow {self.name} completed successfully")
            return result
        
        except Exception as e:
            logger.error(f"Workflow {self.name} failed at step {step_count}: {e}")
            raise
    
    def clear_steps(self) -> None:
        """Clear all workflow steps."""
        self.steps = []
        logger.debug(f"Steps cleared for {self.name}")