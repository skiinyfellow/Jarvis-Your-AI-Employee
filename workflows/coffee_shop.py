from core.hermes.workflow import Workflow
import logging

logger = logging.getLogger(__name__)


def check_inventory(context: dict) -> dict:
    """Check coffee shop inventory.
    
    Args:
        context: Request context
        
    Returns:
        Inventory check result
    """
    logger.info("Executing inventory check")
    return {
        "action": "inventory_check",
        "request": context,
        "status": "checking"
    }


def get_inventory_status(context: dict) -> dict:
    """Get current inventory status.
    
    Args:
        context: Request context
        
    Returns:
        Inventory status
    """
    logger.info("Getting inventory status")
    return {
        "action": "inventory_status",
        "items": {
            "coffee_beans": 50,
            "milk": 30,
            "cups": 200
        },
        "status": "ok"
    }


# Define coffee shop workflows
coffee_inventory_workflow = Workflow("coffee_inventory")
coffee_inventory_workflow.add_step(check_inventory)
coffee_inventory_workflow.add_step(get_inventory_status)


def get_all_workflows() -> dict:
    """Get all available workflows.
    
    Returns:
        Dictionary of workflow definitions
    """
    return {
        "coffee_inventory": coffee_inventory_workflow,
    }
