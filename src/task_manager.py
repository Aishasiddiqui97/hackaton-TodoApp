"""
Task Manager Module

This module handles all task data management operations including storage,
CRUD operations (Create, Read, Update, Delete), and status management.

Tasks are stored in-memory using a Python dictionary with integer keys (task IDs)
and dictionary values containing task data (id, description, completed status).

Data persists only during the application runtime and is lost on exit.
"""

from typing import Any

# Module-level storage (T003)
tasks: dict[int, dict[str, Any]] = {}
next_id: int = 1


def task_exists(task_id: int) -> bool:
    """
    Check if a task with the given ID exists in storage.

    Args:
        task_id: The ID of the task to check

    Returns:
        True if task exists, False otherwise
    """
    return task_id in tasks


def get_all_tasks() -> list[dict]:
    """
    Retrieve all tasks from storage.

    Returns:
        List of task dictionaries. Empty list if no tasks exist.
    """
    return list(tasks.values())


def add_task(description: str) -> tuple[bool, int, str]:
    """
    Add a new task with the given description.

    Assigns a unique sequential ID and initializes the task as incomplete.

    Args:
        description: The task description (must be non-empty)

    Returns:
        Tuple of (success, task_id, message)
        - success: True if task was added
        - task_id: The assigned task ID
        - message: Success message
    """
    global next_id

    task_id = next_id
    tasks[task_id] = {
        "id": task_id,
        "description": description,
        "completed": False
    }
    next_id += 1

    return (True, task_id, "Task added successfully")


def update_task(task_id: int, new_description: str) -> tuple[bool, str]:
    """
    Update the description of an existing task.

    Args:
        task_id: The ID of the task to update
        new_description: The new description

    Returns:
        Tuple of (success, message)
        - success: True if task was updated, False if not found
        - message: Success or error message
    """
    if not task_exists(task_id):
        return (False, f"Task ID {task_id} not found")

    tasks[task_id]["description"] = new_description
    return (True, "Task updated successfully")


def delete_task(task_id: int) -> tuple[bool, str]:
    """
    Delete a task from storage.

    Args:
        task_id: The ID of the task to delete

    Returns:
        Tuple of (success, message)
        - success: True if task was deleted, False if not found
        - message: Success or error message
    """
    if not task_exists(task_id):
        return (False, f"Task ID {task_id} not found")

    del tasks[task_id]
    return (True, "Task deleted successfully")


def mark_complete(task_id: int) -> tuple[bool, str]:
    """
    Mark a task as complete.

    Args:
        task_id: The ID of the task to mark as complete

    Returns:
        Tuple of (success, message)
        - success: True if task was marked complete, False if not found
        - message: Success or error message
    """
    if not task_exists(task_id):
        return (False, f"Task ID {task_id} not found")

    tasks[task_id]["completed"] = True
    return (True, "Task marked as complete")


def mark_incomplete(task_id: int) -> tuple[bool, str]:
    """
    Mark a task as incomplete.

    Args:
        task_id: The ID of the task to mark as incomplete

    Returns:
        Tuple of (success, message)
        - success: True if task was marked incomplete, False if not found
        - message: Success or error message
    """
    if not task_exists(task_id):
        return (False, f"Task ID {task_id} not found")

    tasks[task_id]["completed"] = False
    return (True, "Task marked as incomplete")
