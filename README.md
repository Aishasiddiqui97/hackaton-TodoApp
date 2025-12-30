# Evolution of Todo - Phase I

A simple command-line todo list application for managing tasks in memory.

## Phase I Features

- ✅ Add tasks with automatic ID assignment
- ✅ View all tasks in a formatted table
- ✅ Update task descriptions
- ✅ Delete tasks
- ✅ Mark tasks as complete or incomplete
- ✅ Input validation and error handling
- ✅ Menu-driven interface

## Requirements

- Python 3.11 or higher

## Installation

No installation required. The application uses only Python standard library.

## Usage

Run the application from the repository root:

```bash
python src/todo_app.py
```

### Menu Options

1. **Add Task** - Create a new task with a description
2. **View Tasks** - Display all tasks in a table format
3. **Update Task** - Change the description of an existing task
4. **Delete Task** - Remove a task from the list
5. **Mark Task Complete** - Mark a task as finished
6. **Mark Task Incomplete** - Mark a task as unfinished
7. **Exit** - Close the application

### Example Session

```
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
✓ Task added successfully with ID: 1

Enter your choice (1-7): 1
Enter task description: Finish project report
✓ Task added successfully with ID: 2

Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Incomplete

Enter your choice (1-7): 5
Enter task ID: 2
✓ Task marked as complete

Enter your choice (1-7): 2

ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Complete

Enter your choice (1-7): 7

Goodbye!
```

## Important Notes

- **In-Memory Storage**: All tasks are stored in memory only. When you exit the application, all data is lost.
- **No Persistence**: This is Phase I - no file or database storage is implemented yet.
- **Single User**: Designed for single-user, single-session use.

## Phase I Constraints

Per the project constitution and specification:

- ✅ Python 3.11+ with standard library only
- ✅ In-memory data structures (Python dictionary)
- ✅ Console-based interface only
- ✅ No databases
- ✅ No file storage
- ✅ No web frameworks
- ✅ No external dependencies
- ✅ No authentication
- ✅ No future-phase features

## File Structure

```
src/
├── task_manager.py  # Data layer (CRUD operations, storage)
├── ui.py            # Presentation layer (display, input, validation)
└── todo_app.py      # Application layer (main loop, handlers)
```

## Testing

The application has been validated against all Phase I acceptance criteria:

- ✅ All 5 user stories functional (Add, View, Update, Delete, Mark)
- ✅ Input validation works (empty descriptions, invalid IDs, invalid menu choices)
- ✅ Error messages are clear and actionable
- ✅ Task list displays correctly (formatted table with ID, description, status)
- ✅ Sequential ID assignment (1, 2, 3...)
- ✅ Application starts and exits cleanly

## Future Phases

Phase I is complete. Future phases will add:

- **Phase II**: Multi-user support with authentication and persistence
- **Phase III**: Advanced features (priorities, due dates, tags, search)
- **Phase IV**: Real-time collaboration and synchronization
- **Phase V**: Distributed architecture with event-driven scaling

## Documentation

For detailed documentation, see:

- `specs/001-phase-1-todo-crud/spec.md` - Feature specification
- `specs/001-phase-1-todo-crud/plan.md` - Implementation plan
- `specs/001-phase-1-todo-crud/tasks.md` - Task breakdown
- `specs/001-phase-1-todo-crud/quickstart.md` - User guide

## License

This is an educational project for demonstrating Spec-Driven Development principles.
