import logging
from typing import Any
from core.hermes.workflow import Workflow

logger = logging.getLogger(__name__)


class WorkflowExecutor:
    """Executes workflows with error handling."""
    
    def execute(
        self,
        workflow: Workflow,
        data: Any
    ) -> Any:
        """Execute a workflow.
        
        Args:
            workflow: Workflow to execute
            data: Input data for workflow
            
        Returns:
            Workflow execution result
            
        Raises:
            ValueError: If workflow or data is invalid
            RuntimeError: If execution fails
        """
        if not workflow:
            raise ValueError("Workflow cannot be None")
        
        try:
            logger.info(f"Executing workflow: {workflow.name}")
            result = workflow.execute(data)
            logger.info(f"Workflow {workflow.name} succeeded")
            return result
        
        except Exception as e:
            logger.error(f"Workflow execution failed: {e}")
            raise RuntimeError(f"Workflow execution failed: {e}")