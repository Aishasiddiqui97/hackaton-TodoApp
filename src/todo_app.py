"""
Todo Application Module

This is the main application module that coordinates between the UI and task manager.
It implements the main menu loop and handles routing user choices to appropriate
operation handlers.

The application provides 7 menu options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

All data is stored in memory and lost when the application exits.
"""

import task_manager
import ui


def handle_add_task() -> None:
    """Handle the Add Task operation (User Story 1)."""
    description = ui.get_task_description()
    success, task_id, message = task_manager.add_task(description)
    ui.display_success(f"Task added successfully with ID: {task_id}")


def handle_view_tasks() -> None:
    """Handle the View Tasks operation (User Story 2)."""
    tasks = task_manager.get_all_tasks()
    ui.display_tasks(tasks)


def handle_update_task() -> None:
    """Handle the Update Task operation (User Story 3)."""
    task_id = ui.get_task_id()
    new_description = ui.get_task_description()
    success, message = task_manager.update_task(task_id, new_description)

    if success:
        ui.display_success(message)
    else:
        ui.display_error(message)


def handle_delete_task() -> None:
    """Handle the Delete Task operation (User Story 4)."""
    task_id = ui.get_task_id()
    success, message = task_manager.delete_task(task_id)

    if success:
        ui.display_success(message)
    else:
        ui.display_error(message)


def handle_mark_complete() -> None:
    """Handle the Mark Task Complete operation (User Story 5)."""
    task_id = ui.get_task_id()
    success, message = task_manager.mark_complete(task_id)

    if success:
        ui.display_success(message)
    else:
        ui.display_error(message)


def handle_mark_incomplete() -> None:
    """Handle the Mark Task Incomplete operation (User Story 5)."""
    task_id = ui.get_task_id()
    success, message = task_manager.mark_incomplete(task_id)

    if success:
        ui.display_success(message)
    else:
        ui.display_error(message)


def main() -> None:
    """Main application loop."""
    while True:
        ui.display_menu()
        choice = ui.get_menu_choice()

        if choice == 1:
            handle_add_task()
        elif choice == 2:
            handle_view_tasks()
        elif choice == 3:
            handle_update_task()
        elif choice == 4:
            handle_delete_task()
        elif choice == 5:
            handle_mark_complete()
        elif choice == 6:
            handle_mark_incomplete()
        elif choice == 7:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
