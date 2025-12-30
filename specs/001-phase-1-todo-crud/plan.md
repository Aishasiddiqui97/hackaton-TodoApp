# Implementation Plan: Phase I - Todo CRUD Console App

**Branch**: `001-phase-1-todo-crud` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-phase-1-todo-crud/spec.md`

## Summary

Build an in-memory Python console application for managing a todo list with five core operations: Add Task, View Tasks, Update Task Description, Delete Task, and Mark Task Complete/Incomplete. The application will use a menu-driven interface, store all data in memory (lost on exit), support a single user, and require no external dependencies beyond Python 3.11+ standard library.

**Technical Approach**: Simple procedural design with clear separation between data management (task storage and operations) and user interface (menu display and input handling). Use Python dictionary for O(1) task lookups by ID, maintain a counter for sequential ID generation, and implement input validation at the CLI layer before passing to data operations.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory (Python dictionary)
**Testing**: Manual testing initially (automated tests optional for Phase I)
**Target Platform**: Cross-platform console/terminal (Windows, macOS, Linux)
**Project Type**: Single project (simple console application)
**Performance Goals**: < 1 second response time for all operations, < 50MB memory for up to 1000 tasks
**Constraints**: No persistence, no external libraries, no networking, < 1 second startup time
**Scale/Scope**: Single-user session, up to a few hundred tasks typical, in-memory only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Spec-Driven Development
- Specification approved and complete (specs/001-phase-1-todo-crud/spec.md)
- This plan derived strictly from approved spec
- No new features introduced beyond spec requirements

### ✅ No Feature Invention
- Plan implements only specified features: Add, View, Update, Delete, Mark Complete/Incomplete
- No additional convenience features added
- No abstractions beyond what's needed for Phase I

### ✅ Phase Boundary Enforcement
- **VERIFIED**: No persistence mechanisms (no files, no databases)
- **VERIFIED**: No multi-user concepts or authentication
- **VERIFIED**: No web/API frameworks or networking
- **VERIFIED**: No future-phase features (priorities, due dates, tags, search, filtering)
- **VERIFIED**: No architectural hooks for future phases
- Plan focuses solely on Phase I in-memory console application

### ✅ Technology Standards Compliance
- **Language**: Python 3.11+ ✓
- **Dependencies**: Standard library only ✓
- **No external services**: Confirmed ✓

### ✅ Clean Architecture Principles
- **Separation of Concerns**: Data layer (task storage/operations) separate from presentation layer (CLI/menu)
- **Single Responsibility**: Each function handles one specific operation
- **No premature abstraction**: Simple procedural design appropriate for Phase I scope

### ⚠️ Stateless Services
- **N/A for Phase I**: Single-threaded console application, not a service architecture
- Note: This principle becomes relevant in Phase II+ (multi-user, web services)

**Gate Status**: ✅ PASSED - All applicable constitutional requirements met

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-1-todo-crud/
├── spec.md              # Feature specification (completed)
├── plan.md              # This file (implementation plan)
├── research.md          # Phase 0 research output (see below)
├── data-model.md        # Phase 1 data model (see below)
├── quickstart.md        # Phase 1 user guide (see below)
└── contracts/           # Phase 1 contracts (N/A for console app)
```

### Source Code (repository root)

```text
src/
├── todo_app.py          # Main entry point and menu loop
├── task_manager.py      # Task storage and CRUD operations
└── ui.py                # CLI display and input handling utilities

tests/                   # (Optional for Phase I)
├── test_task_manager.py # Unit tests for task operations
└── test_integration.py  # Integration tests for user journeys
```

**Structure Decision**: Single project structure selected. This is a simple console application with minimal complexity. All source code will reside in `src/` directory with three modules:

1. **todo_app.py**: Entry point, main loop, menu coordination
2. **task_manager.py**: Task data structure, ID generation, CRUD operations
3. **ui.py**: Display formatting, input prompts, error messages

No need for complex layering or multiple projects. Tests are optional for Phase I but structure allows adding them later if needed.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

*No violations - all constitutional requirements satisfied.*

---

## Phase 0: Research & Technical Decisions

### Research Topics

Since this is a simple console application with Python standard library only, minimal research is required. Key decisions documented below:

### Decision 1: Data Structure for Task Storage

**Decision**: Use Python dictionary with integer keys for task storage
**Rationale**:
- O(1) lookup by task ID (required for update, delete, mark operations)
- Maintains insertion order in Python 3.7+ (helpful for display)
- Simple to implement and understand
- No need for complex data structures given Phase I scope

**Alternatives Considered**:
- List of task objects: O(n) lookup, would need linear search for ID
- Named tuples or dataclasses: Overkill for three simple fields
- SQLite in-memory: Violates "no database" constraint

**Implementation Detail**: `tasks: dict[int, dict[str, Any]]` where inner dict has keys: `id`, `description`, `completed`

### Decision 2: ID Generation Strategy

**Decision**: Use simple integer counter, starting from 1, increment on each add
**Rationale**:
- Sequential IDs are user-friendly (1, 2, 3...)
- Simple to implement with single integer variable
- No collision risk in single-threaded application
- Meets FR-002 requirement for unique sequential IDs

**Alternatives Considered**:
- UUID: Overkill, not user-friendly for console display
- Auto-increment from max ID: More complex, unnecessary for Phase I

**Implementation Detail**: `next_id = 1`, increment after each successful add, never reuse IDs even after deletion

### Decision 3: Input Validation Strategy

**Decision**: Validate at CLI layer before calling task_manager functions
**Rationale**:
- Single point of validation for user input
- Task manager functions can assume valid input
- Clear separation: UI handles user errors, task manager handles data operations
- Easier to provide user-friendly error messages at CLI layer

**Validation Rules**:
- Task ID: Must be integer, must exist in tasks dictionary
- Description: Must not be empty or whitespace-only
- Menu choice: Must be valid option number

### Decision 4: Error Handling Approach

**Decision**: Return success/error tuples from task_manager functions, display errors in CLI layer
**Rationale**:
- No exceptions for expected user errors (invalid ID, empty description)
- Exceptions only for unexpected programming errors
- Caller (UI layer) decides how to present errors to user
- Simple and explicit error handling

**Return Pattern**: `(success: bool, message: str)` or `(success: bool, data: Any, message: str)`

### Decision 5: Display Formatting

**Decision**: Use simple tabular format with fixed-width columns for task display
**Rationale**:
- Meets NFR-U003 (readable format with clear column alignment)
- Easy to implement with Python string formatting
- Works in any terminal width (reasonable defaults)
- Clear visual separation between ID, description, and status

**Format Example**:
```
ID  | Description                | Status
----|----------------------------|------------
1   | Buy groceries              | Incomplete
2   | Finish project report      | Complete
```

---

## Phase 1: Design & Contracts

### Data Model

See [data-model.md](./data-model.md) for complete data model specification.

**Summary**:
- **Task Entity**: Three fields (id: int, description: str, completed: bool)
- **Storage**: Dictionary mapping task ID (int) to task dictionary
- **ID Generation**: Simple counter, starts at 1, increments on add
- **Validation Rules**: Description non-empty/non-whitespace, ID must exist for operations

### Module Design

#### Module 1: task_manager.py (Data Layer)

**Responsibilities**:
- Maintain tasks dictionary and next_id counter
- Implement CRUD operations: add, get_all, update, delete, mark_complete, mark_incomplete
- Return operation results with success/failure indicators

**Public Functions**:
```python
def add_task(description: str) -> tuple[bool, int, str]:
    """Add new task, return (success, task_id, message)"""

def get_all_tasks() -> list[dict]:
    """Return list of all tasks as dictionaries"""

def update_task(task_id: int, new_description: str) -> tuple[bool, str]:
    """Update task description, return (success, message)"""

def delete_task(task_id: int) -> tuple[bool, str]:
    """Delete task, return (success, message)"""

def mark_complete(task_id: int) -> tuple[bool, str]:
    """Mark task as complete, return (success, message)"""

def mark_incomplete(task_id: int) -> tuple[bool, str]:
    """Mark task as incomplete, return (success, message)"""

def task_exists(task_id: int) -> bool:
    """Check if task ID exists"""
```

**Data Structure**:
```python
tasks: dict[int, dict[str, Any]] = {}
next_id: int = 1
```

**Error Handling**: Functions return tuple with success boolean and message. No exceptions for user errors.

#### Module 2: ui.py (Presentation Layer)

**Responsibilities**:
- Display menu and task list
- Prompt user for input
- Validate user input (non-empty, integer, valid menu choice)
- Format task display for readability
- Display error and success messages

**Public Functions**:
```python
def display_menu() -> None:
    """Display main menu options"""

def display_tasks(tasks: list[dict]) -> None:
    """Display all tasks in formatted table"""

def get_menu_choice() -> int:
    """Prompt for menu choice, validate, return integer"""

def get_task_description() -> str:
    """Prompt for task description, validate non-empty, return string"""

def get_task_id() -> int:
    """Prompt for task ID, validate integer, return int"""

def display_error(message: str) -> None:
    """Display error message in red or highlighted"""

def display_success(message: str) -> None:
    """Display success message in green or highlighted"""
```

**Input Validation**:
- Description: Strip whitespace, check not empty
- Task ID: Parse as integer, handle ValueError
- Menu choice: Parse as integer, check in valid range (1-7)

#### Module 3: todo_app.py (Application Layer)

**Responsibilities**:
- Application entry point (if __name__ == "__main__")
- Main loop: display menu → get choice → execute operation → repeat
- Coordinate between UI and task_manager modules
- Handle exit condition

**Main Loop Structure**:
```python
def main():
    while True:
        ui.display_menu()
        choice = ui.get_menu_choice()

        if choice == 1:  # Add Task
            handle_add_task()
        elif choice == 2:  # View Tasks
            handle_view_tasks()
        elif choice == 3:  # Update Task
            handle_update_task()
        elif choice == 4:  # Delete Task
            handle_delete_task()
        elif choice == 5:  # Mark Complete
            handle_mark_complete()
        elif choice == 6:  # Mark Incomplete
            handle_mark_incomplete()
        elif choice == 7:  # Exit
            print("Goodbye!")
            break
```

**Operation Handlers**: Each handler function coordinates UI prompts and task_manager calls, displays results

### Control Flow

**Application Lifecycle**:
1. Start application (`python src/todo_app.py`)
2. Enter main loop
3. Display menu (7 options)
4. Get user menu choice
5. Execute corresponding operation
6. Display result (success/error message)
7. Return to step 3 (unless Exit chosen)
8. Exit application (all data lost)

**Add Task Flow**:
1. Display menu → user selects "1. Add Task"
2. Prompt for task description
3. Validate description (non-empty, non-whitespace)
4. Call task_manager.add_task(description)
5. Display success message with assigned task ID
6. Return to main menu

**View Tasks Flow**:
1. Display menu → user selects "2. View Tasks"
2. Call task_manager.get_all_tasks()
3. If empty, display "Task list is empty"
4. If not empty, format and display tasks in table
5. Return to main menu

**Update Task Flow**:
1. Display menu → user selects "3. Update Task"
2. Prompt for task ID
3. Validate ID is integer
4. Prompt for new description
5. Validate description (non-empty, non-whitespace)
6. Call task_manager.update_task(task_id, new_description)
7. Display success or error message ("Task ID not found")
8. Return to main menu

**Delete Task Flow**:
1. Display menu → user selects "4. Delete Task"
2. Prompt for task ID
3. Validate ID is integer
4. Call task_manager.delete_task(task_id)
5. Display success or error message ("Task ID not found")
6. Return to main menu

**Mark Complete Flow**:
1. Display menu → user selects "5. Mark Complete"
2. Prompt for task ID
3. Validate ID is integer
4. Call task_manager.mark_complete(task_id)
5. Display success or error message ("Task ID not found")
6. Return to main menu

**Mark Incomplete Flow**:
1. Display menu → user selects "6. Mark Incomplete"
2. Prompt for task ID
3. Validate ID is integer
4. Call task_manager.mark_incomplete(task_id)
5. Display success or error message ("Task ID not found")
6. Return to main menu

### Error Handling Strategy

**User Input Errors** (Expected):
- Invalid menu choice → Display "Invalid choice. Please select 1-7." → Re-prompt
- Non-integer task ID → Display "Please enter a valid task ID (number)." → Re-prompt
- Empty description → Display "Description cannot be empty." → Re-prompt
- Non-existent task ID → Display "Task ID {id} not found." → Return to menu

**System Errors** (Unexpected):
- Let Python exceptions bubble up (e.g., memory errors)
- Application will crash and exit (acceptable for Phase I)
- No error recovery needed for unexpected errors in Phase I

**Error Message Format**:
- Clear and specific (e.g., "Task ID 5 not found" not "Error")
- Actionable (tell user what to do next)
- Consistent formatting (e.g., "ERROR: {message}")

### Contracts

**N/A for Phase I Console Application**

Phase I is a standalone console application with no network APIs, no external integrations, and no inter-service communication. Therefore, no formal API contracts or interface definitions are required.

**Internal Module Contracts** are documented in function signatures above (Module Design section). These are internal implementation details, not external contracts.

---

## Phase 2: Architecture Decisions (ADRs)

No architecturally significant decisions requiring formal ADRs were identified during planning. All technical choices are straightforward implementations of spec requirements with standard Python patterns.

**Reasoning**: Phase I is intentionally simple with well-established solutions:
- In-memory dictionary storage (standard Python)
- Procedural console menu (standard pattern)
- Sequential integer IDs (universal approach)
- Tuple return values for error handling (idiomatic Python)

If architecturally significant decisions arise during implementation, they should be documented via `/sp.adr` command.

---

## Implementation Notes

### Module Creation Order

1. **task_manager.py** (data layer first)
   - Can be developed and tested independently
   - No dependencies on other modules

2. **ui.py** (presentation layer second)
   - Depends on task_manager data structure (dict format)
   - Can be tested with mock task data

3. **todo_app.py** (application layer last)
   - Depends on both task_manager and ui modules
   - Integrates everything together

### Testing Strategy (Optional for Phase I)

If tests are added (not required by spec):
- **Unit tests**: Test task_manager functions with various inputs
- **Integration tests**: Test full user journeys (add → view → update → delete)
- **Manual testing**: Primary validation method for Phase I

### Performance Considerations

- Dictionary lookups: O(1) for all operations by ID
- get_all_tasks: O(n) where n = number of tasks (acceptable for Phase I scale)
- No performance bottlenecks expected for < 1000 tasks
- Memory: ~1KB per task × 1000 tasks = ~1MB (well under 50MB constraint)

### Future Phase Considerations (DO NOT IMPLEMENT)

This section documents what will NOT be implemented in Phase I but may appear in future phases:

**Phase II (Multi-user, Persistence)**:
- File or database persistence
- User authentication
- Multi-user task separation

**Phase III (Advanced Features)**:
- Task priorities, due dates, tags
- Search and filtering
- Task categories

**Phase IV-V (Distributed)**:
- Web interface
- Real-time synchronization
- Event-driven architecture

**IMPORTANT**: None of these future features should influence Phase I design. No hooks, no abstractions, no preparation for future phases per Constitution Principle III (Phase Boundary Enforcement).

---

## Quickstart Guide

See [quickstart.md](./quickstart.md) for user-facing guide on running and using the Phase I Todo application.

**Summary for Developers**:
1. Ensure Python 3.11+ installed
2. Navigate to repository root
3. Run: `python src/todo_app.py`
4. Follow on-screen menu prompts
5. Exit: Choose option 7 from menu

---

## Next Steps

**This plan is now complete.** Next command: `/sp.tasks` to generate implementation tasks from this plan and the specification.

**Artifacts Created by This Plan**:
- ✅ plan.md (this file)
- ⏭️ research.md (to be created below)
- ⏭️ data-model.md (to be created below)
- ⏭️ quickstart.md (to be created below)

**Tasks Command**: After `/sp.tasks`, expect tasks organized by user story (P1 first: Add, View, Mark; then P2: Update, Delete) with clear dependencies and parallel opportunities.
