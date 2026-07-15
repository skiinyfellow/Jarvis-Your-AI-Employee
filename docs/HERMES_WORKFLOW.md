# Hermes Workflow Engine

## Overview

Hermes is the execution layer of Jarvis that transforms user requests into actionable workflows.

## Architecture

```
User Message
    ↓
Telegram Intake
    ↓
Task Creation
    ↓
Hermes Router
    ↓
Workflow Selection
    ↓
Workflow Executor
    ↓
Business Module
    ↓
Result
```

## Components

### Task
Represents a unit of work with:
- Unique ID (UUID)
- Command text
- User origin
- Status tracking
- Timestamp

### Router
Maps commands to handlers:
- Pattern matching
- Route registration
- Dynamic handler lookup

### Workflow
Multi-step execution pipeline:
- Sequential step execution
- Context passing
- Error handling

### Executor
Executes workflows with:
- Error handling
- Logging
- Result collection

### Event Bus
Publish-subscribe messaging:
- Event subscriptions
- Callback execution
- Error isolation

### Task Queue
FIFO task management:
- Task queueing
- Sequential processing
- Status tracking

## Usage Example

```python
from core.hermes.task import Task
from core.hermes.router import HermesRouter
from workflows.coffee_shop import coffee_inventory_workflow
from core.hermes.executor import WorkflowExecutor

# Create a task from user input
task = Task(command="check inventory", user="telegram")

# Route to appropriate workflow
router = HermesRouter()
router.register("inventory", lambda: coffee_inventory_workflow)

# Execute
executor = WorkflowExecutor()
result = executor.execute(coffee_inventory_workflow, {"request": task.command})
```

## Future Integrations

- Email intake
- Calendar integration
- CRM system
- Inventory system
- Accounting system
- Voice commands
- SMS messages
- Slack integration
