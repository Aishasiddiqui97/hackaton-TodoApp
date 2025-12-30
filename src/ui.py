"""
User Interface Module

This module handles all user interaction including menu display, input prompts,
input validation, and output formatting for the console-based todo application.

Responsibilities:
- Display menu and task lists in formatted tables
- Prompt users for input (menu choices, task descriptions, task IDs)
- Validate user input (non-empty strings, valid integers, valid ranges)
- Display success and error messages with clear formatting
"""


def display_menu() -> None:
    """Display the main menu with all available options."""
    print("\n===== Todo List Application =====\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print()


def display_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in a formatted table.

    Args:
        tasks: List of task dictionaries with id, description, and completed fields
    """
    if not tasks:
        print("\nTask list is empty. Add some tasks to get started!\n")
        return

    print("\nID  | Description                      | Status")
    print("----|----------------------------------|------------")

    for task in tasks:
        task_id = task["id"]
        description = task["description"]
        status = "Complete" if task["completed"] else "Incomplete"

        # Truncate description if longer than 34 characters
        if len(description) > 34:
            description = description[:31] + "..."

        print(f"{task_id:<4}| {description:<34}| {status}")

    print()


def get_menu_choice() -> int:
    """
    Prompt for and validate menu choice.

    Returns:
        Valid menu choice as integer (1-7)
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                display_error("Invalid choice. Please select 1-7.")
        except ValueError:
            display_error("Please enter a valid number.")


def get_task_description() -> str:
    """
    Prompt for and validate task description.

    Returns:
        Non-empty task description string
    """
    while True:
        description = input("Enter task description: ").strip()
        if description:
            return description
        else:
            display_error("Description cannot be empty.")


def get_task_id() -> int:
    """
    Prompt for and validate task ID.

    Returns:
        Task ID as integer
    """
    while True:
        try:
            task_id = int(input("Enter task ID: "))
            return task_id
        except ValueError:
            display_error("Please enter a valid task ID (number).")


def display_error(message: str) -> None:
    """
    Display an error message.

    Args:
        message: The error message to display
    """
    print(f"ERROR: {message}")


def display_success(message: str) -> None:
    """
    Display a success message.

    Args:
        message: The success message to display
    """
    print(f"✓ {message}")
