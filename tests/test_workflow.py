from core.hermes.workflow import Workflow
from core.hermes.executor import WorkflowExecutor
import logging

logger = logging.getLogger(__name__)


def test_workflow_creation():
    """Test workflow creation."""
    workflow = Workflow("test")
    assert workflow.name == "test"
    assert len(workflow.steps) == 0


def test_workflow_execution():
    """Test workflow execution."""
    workflow = Workflow("test")
    workflow.add_step(lambda x: x + " done")
    result = workflow.execute("task")
    assert result == "task done"


def test_workflow_multiple_steps():
    """Test workflow with multiple steps."""
    workflow = Workflow("multi_step")
    workflow.add_step(lambda x: x.upper())
    workflow.add_step(lambda x: x + "!") 
    result = workflow.execute("hello")
    assert result == "HELLO!"


def test_workflow_executor():
    """Test workflow executor."""
    workflow = Workflow("executor_test")
    workflow.add_step(lambda x: {**x, "processed": True})
    
    executor = WorkflowExecutor()
    result = executor.execute(workflow, {"data": "test"})
    
    assert result["data"] == "test"
    assert result["processed"] is True
