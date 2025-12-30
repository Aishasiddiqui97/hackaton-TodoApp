# Quickstart Guide: Phase I Todo Application

**Feature**: Phase I - Todo CRUD Console App
**Date**: 2025-12-31
**For**: End users and developers

## What is This?

A simple command-line todo list application for tracking tasks. Add tasks, view your list, update descriptions, delete tasks, and mark tasks as complete or incomplete. All data is stored in memory and lost when you exit.

## Requirements

- Python 3.11 or higher installed on your system
- A terminal or command prompt

**Check your Python version**:
```bash
python --version
```

If you see `Python 3.11.x` or higher, you're good to go!

## Installation

No installation required! The application uses only Python standard library.

**Optional**: Clone or download the project repository to your local machine.

## Running the Application

1. **Open a terminal/command prompt**

2. **Navigate to the project directory**:
   ```bash
   cd path/to/hacharton-2
   ```

3. **Run the application**:
   ```bash
   python src/todo_app.py
   ```

4. **You should see the main menu**:
   ```
   ===== Todo List Application =====

   1. Add Task
   2. View Tasks
   3. Update Task
   4. Delete Task
   5. Mark Task Complete
   6. Mark Task Incomplete
   7. Exit

   Enter your choice (1-7):
   ```

## Basic Usage

### Adding a Task

1. Select **1** (Add Task) from the menu
2. Enter a description for your task
3. Press Enter
4. You'll see: `Task added successfully with ID: 1`

**Example**:
```
Enter your choice (1-7): 1
Enter task description: Buy groceries
Task added successfully with ID: 1
```

### Viewing All Tasks

1. Select **2** (View Tasks) from the menu
2. All your tasks will be displayed in a table

**Example**:
```
Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Complete
3   | Call dentist                     | Incomplete
```

**If you have no tasks yet**:
```
Task list is empty. Add some tasks to get started!
```

### Updating a Task

1. Select **3** (Update Task) from the menu
2. Enter the ID of the task you want to update
3. Enter the new description
4. Press Enter

**Example**:
```
Enter your choice (1-7): 3
Enter task ID: 1
Enter new description: Buy groceries and milk
Task updated successfully!
```

### Deleting a Task

1. Select **4** (Delete Task) from the menu
2. Enter the ID of the task you want to delete
3. Confirm by pressing Enter

**Example**:
```
Enter your choice (1-7): 4
Enter task ID: 2
Task deleted successfully!
```

### Marking a Task as Complete

1. Select **5** (Mark Task Complete) from the menu
2. Enter the ID of the task you completed
3. Press Enter

**Example**:
```
Enter your choice (1-7): 5
Enter task ID: 1
Task marked as complete!
```

### Marking a Task as Incomplete

1. Select **6** (Mark Task Incomplete) from the menu
2. Enter the ID of the task you want to mark as incomplete
3. Press Enter

**Example**:
```
Enter your choice (1-7): 6
Enter task ID: 1
Task marked as incomplete!
```

### Exiting the Application

1. Select **7** (Exit) from the menu
2. The application will close
3. **All your tasks will be lost** (Phase I has no persistence)

**Example**:
```
Enter your choice (1-7): 7
Goodbye!
```

## Common Questions

### Q: Where are my tasks saved?

**A**: They're not! Phase I stores tasks in memory only. When you exit the application, all tasks are lost. This is intentional for Phase I.

**Future phases** will add file or database persistence.

### Q: What happens if I enter an invalid task ID?

**A**: You'll see an error message like:
```
ERROR: Task ID 99 not found.
```

The application will return to the main menu, and you can try again.

### Q: Can I have two tasks with the same description?

**A**: Yes! Task IDs are unique, but descriptions can be anything you want, including duplicates.

### Q: What if I enter a blank task description?

**A**: You'll see an error message like:
```
ERROR: Description cannot be empty.
```

You'll be prompted to enter a valid description.

### Q: Can I undo an operation?

**A**: No, there's no undo feature in Phase I. Be careful when deleting tasks!

### Q: How many tasks can I add?

**A**: Technically thousands, but the application is designed for up to a few hundred tasks in a single session. Performance will remain excellent for typical use.

### Q: Can I search or filter tasks?

**A**: Not in Phase I. You can view all tasks, but there's no search, filter, or sort functionality yet.

**Future phases** will add these features.

### Q: Can I add priorities or due dates?

**A**: Not in Phase I. Tasks have only three attributes: ID, description, and completion status.

**Future phases** will add priorities, due dates, tags, and more.

## Tips for Best Use

1. **Keep descriptions concise**: Descriptions can be long, but shorter ones display better in the table
2. **Use task IDs**: Always refer to tasks by their ID number, not by description
3. **View tasks regularly**: Use option 2 to see your current task list and their IDs
4. **Mark tasks complete**: Use option 5 to mark finished tasks—it's satisfying and helps track progress!
5. **Exit cleanly**: Always use option 7 to exit (don't close the terminal abruptly)

## Troubleshooting

### "Python not found" or "python: command not found"

**Solution**: Python is not installed or not in your PATH. Install Python 3.11+ from [python.org](https://www.python.org/downloads/).

On some systems, try `python3` instead of `python`:
```bash
python3 src/todo_app.py
```

### "No module named 'task_manager'" or similar

**Solution**: Make sure you're running the command from the project root directory (where `src/` folder is located), not from inside the `src/` folder.

### Application crashes or freezes

**Solution**: Press Ctrl+C to exit, then restart. If the problem persists, report it as a bug.

### Invalid input causes errors

**Solution**: The application validates most input, but if you encounter unexpected behavior:
- Ensure you're entering numbers (not text) for task IDs and menu choices
- Ensure you're entering text (not blank) for task descriptions

## Example Session

Here's a complete example session from start to finish:

```
$ python src/todo_app.py

===== Todo List Application =====

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

Enter your choice (1-7): 1
Enter task description: Buy groceries
Task added successfully with ID: 1

Enter your choice (1-7): 1
Enter task description: Finish project report
Task added successfully with ID: 2

Enter your choice (1-7): 1
Enter task description: Call dentist
Task added successfully with ID: 3

Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Incomplete
3   | Call dentist                     | Incomplete

Enter your choice (1-7): 5
Enter task ID: 2
Task marked as complete!

Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Complete
3   | Call dentist                     | Incomplete

Enter your choice (1-7): 4
Enter task ID: 3
Task deleted successfully!

Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Complete

Enter your choice (1-7): 7
Goodbye!
```

## Next Steps

Once you're comfortable with Phase I:

- **Phase II** will add file/database persistence (tasks saved between sessions)
- **Phase III** will add advanced features (priorities, due dates, tags, search)
- **Phase IV** will add web interface and real-time collaboration
- **Phase V** will add distributed architecture for scaling

But for now, enjoy the simplicity of Phase I! 🎯

## Feedback and Issues

If you encounter bugs or have suggestions:
1. Note the exact steps to reproduce the issue
2. Note what you expected to happen vs. what actually happened
3. Report to your development team or project maintainer

## Summary

- **Run**: `python src/todo_app.py`
- **Add tasks**: Option 1
- **View tasks**: Option 2
- **Update/Delete/Mark**: Options 3-6
- **Exit**: Option 7
- **Remember**: All data is lost on exit (Phase I has no persistence)

Happy task tracking! ✅
