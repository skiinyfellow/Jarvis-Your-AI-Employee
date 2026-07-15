"""
Hermes - Workflow Manager

Manages task automation, workflow orchestration, and
process execution across the Jarvis platform.

TODO:
- Implement workflow engine
- Add task scheduling
- Create workflow templates
- Setup execution pipeline
"""

__version__ = "0.1.0"

from .workflows import WorkflowManager  # TODO: Create workflows.py

__all__ = ["WorkflowManager"]
