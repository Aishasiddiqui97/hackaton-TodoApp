# Research: Phase I - Todo CRUD Console App

**Feature**: 001-phase-1-todo-crud
**Date**: 2025-12-31
**Purpose**: Document technical research and decision-making for Phase I implementation

## Overview

Phase I is a simple in-memory Python console application with minimal complexity. This document captures research findings and rationale for key technical decisions.

## Research Questions

### Q1: What data structure should be used for task storage?

**Context**: Application needs to store tasks with O(1) lookup by ID for update, delete, and mark operations.

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Python dict with int keys | O(1) lookup, maintains insertion order (Py3.7+), simple | None for this use case | ✅ **SELECTED** |
| List of dicts/objects | Simple iteration, preserves order | O(n) lookup requires linear search | ❌ Rejected (performance) |
| Named tuples | Immutable, lightweight | Still need list/dict container, O(n) search | ❌ Rejected (no benefit) |
| Dataclasses | Type hints, cleaner code | Overkill for 3 fields, still need container | ❌ Rejected (complexity) |
| SQLite in-memory | SQL queries, relational | Violates "no database" constraint | ❌ Rejected (constraint violation) |

**Selected**: **Python dictionary** `dict[int, dict[str, Any]]`

**Rationale**:
- Provides O(1) lookup by task ID (critical for update/delete/mark operations)
- Maintains insertion order in Python 3.7+ (helpful for consistent display)
- Simple and idiomatic Python
- No external dependencies
- Supports all required operations efficiently

**Implementation**:
```python
tasks: dict[int, dict[str, Any]] = {}
# Example: {1: {"id": 1, "description": "Buy milk", "completed": False}}
```

---

### Q2: How should unique task IDs be generated?

**Context**: Spec requires unique sequential integer IDs starting from 1 (FR-002).

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Simple counter (1, 2, 3...) | User-friendly, simple, meets spec | IDs not reused after deletion | ✅ **SELECTED** |
| UUID/GUID | Globally unique, no collisions | Not user-friendly, overkill | ❌ Rejected (usability) |
| Auto-increment from max ID | Reuses IDs after deletion | More complex, can confuse users | ❌ Rejected (complexity) |
| Timestamp-based | Unique, sortable | Not sequential, not user-friendly | ❌ Rejected (spec violation) |

**Selected**: **Simple integer counter**

**Rationale**:
- Meets FR-002 requirement: "unique sequential integer ID"
- User-friendly for console display (1, 2, 3... easy to remember and type)
- Simple to implement: single integer variable, increment on add
- No collision risk in single-threaded single-user application
- IDs never reused even after deletion (simpler logic, avoids confusion)

**Implementation**:
```python
next_id: int = 1
# On add: assign current next_id, then increment
# Never decrement or reuse, even after deletion
```

---

### Q3: Where should input validation occur?

**Context**: Need to validate user input (non-empty descriptions, valid IDs, menu choices) before operations.

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| At UI layer (before calling task_manager) | Single point of validation, task_manager stays simple | UI layer has more responsibility | ✅ **SELECTED** |
| At task_manager layer | Data layer ensures own integrity | Duplicates validation logic, tight coupling | ❌ Rejected |
| At both layers | Defense in depth | Unnecessary complexity for Phase I | ❌ Rejected |

**Selected**: **Validate at UI layer**

**Rationale**:
- Single point of validation (DRY principle)
- Clear separation of concerns: UI handles user errors, task_manager handles data
- task_manager functions can assume valid input (simpler logic)
- Easier to provide user-friendly error messages at UI layer
- UI layer controls retry loops for invalid input

**Validation Points**:
- **Task description**: Strip whitespace, check not empty, reprompt if invalid
- **Task ID**: Parse as integer (handle ValueError), check range if needed, reprompt if invalid
- **Menu choice**: Parse as integer, check in range 1-7, reprompt if invalid

---

### Q4: How should errors be handled and communicated?

**Context**: Need to handle expected user errors (invalid ID, empty description) and unexpected system errors.

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Return tuples (success, message) | Explicit, no exceptions for expected errors | More return values to handle | ✅ **SELECTED** |
| Raise exceptions for all errors | Pythonic, single error path | Exceptions for expected user input overkill | ❌ Rejected |
| Return None on error | Simple | Loses error context, ambiguous | ❌ Rejected |
| Status codes | Language-agnostic pattern | Less Pythonic, requires lookup | ❌ Rejected |

**Selected**: **Return tuples with success boolean and message**

**Rationale**:
- Explicit error handling (no hidden exceptions)
- Caller (UI layer) decides how to present errors to user
- No exceptions for expected user errors (invalid ID, empty description)
- Exceptions only for unexpected programming errors (memory, bugs)
- Simple and clear pattern

**Pattern**:
```python
# For operations returning data:
def add_task(description: str) -> tuple[bool, int, str]:
    # Returns: (success, task_id, message)

# For operations not returning data:
def delete_task(task_id: int) -> tuple[bool, str]:
    # Returns: (success, message)
```

---

### Q5: How should tasks be displayed to the user?

**Context**: Spec requires readable format with clear column alignment (NFR-U003).

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Fixed-width table with separators | Clear, professional, readable | May truncate long descriptions | ✅ **SELECTED** |
| Simple list (one task per line) | Compact, handles long descriptions | Less readable, no alignment | ❌ Rejected |
| Pretty-printed JSON | Structured, parseable | Not user-friendly for humans | ❌ Rejected |
| Rich formatting (colors, boxes) | Visually appealing | Requires external library, overkill | ❌ Rejected |

**Selected**: **Fixed-width table with column separators**

**Rationale**:
- Meets NFR-U003 requirement for clear column alignment
- Professional appearance
- Easy to implement with Python string formatting
- Works in any terminal
- Clear visual separation between ID, description, and status

**Format**:
```
ID  | Description                      | Status
----|----------------------------------|------------
1   | Buy groceries                    | Incomplete
2   | Finish project report            | Complete
3   | Call dentist for appointment     | Incomplete
```

**Handling Long Descriptions**: Truncate to ~40 characters with "..." if needed for display, but store full description.

---

## Technology Choices

### Language & Runtime

**Selected**: Python 3.11+

**Rationale**:
- Mandated by constitution (Technology Standards)
- Widely available, cross-platform
- Simple syntax ideal for console applications
- Rich standard library eliminates need for external dependencies
- Type hints available (Python 3.11+ has improved type system)

### Dependencies

**Selected**: Python standard library only (no external packages)

**Rationale**:
- Meets spec constraint TC-007
- Keeps application simple and self-contained
- No dependency management needed
- Fast startup (< 1 second requirement)
- No compatibility issues

**Standard Library Modules Used**:
- None specifically required (basic Python features sufficient)
- Optional: `typing` for type hints (development aid)

### Testing Approach

**Selected**: Manual testing (automated tests optional)

**Rationale**:
- Spec does not require automated tests
- Phase I scope is small (5 operations, 3 modules)
- Manual testing sufficient for validation
- If automated tests added later: use `pytest` (most popular, simple)

---

## Architecture Decisions

### Module Structure

**Selected**: Three-module design (task_manager, ui, todo_app)

**Rationale**:
- Clear separation of concerns
- Data layer (task_manager) independent of UI
- Presentation layer (ui) handles all user interaction
- Application layer (todo_app) coordinates between them
- Each module has single responsibility
- Simple enough for Phase I, no over-engineering

### Control Flow

**Selected**: Single-threaded synchronous menu loop

**Rationale**:
- Meets spec constraint OC-004 (synchronous blocking input)
- Simple and appropriate for console application
- No concurrency needed for single-user Phase I
- Easy to understand and maintain

**Pattern**:
```python
while True:
    display_menu()
    choice = get_input()
    execute_operation(choice)
    if choice == exit:
        break
```

---

## Performance Considerations

### Operation Complexity

| Operation | Complexity | Rationale |
|-----------|------------|-----------|
| Add task | O(1) | Dictionary insert |
| View all tasks | O(n) | Iterate all tasks |
| Update task | O(1) | Dictionary lookup + update |
| Delete task | O(1) | Dictionary delete |
| Mark complete/incomplete | O(1) | Dictionary lookup + update |

**Analysis**: All operations are O(1) or O(n), well within performance requirements for up to 1000 tasks.

### Memory Usage

**Estimate**: ~1KB per task (description + overhead) × 1000 tasks = ~1MB

**Analysis**: Well under 50MB constraint (NFR-P003), no memory concerns for Phase I.

### Startup Time

**Estimate**: < 0.1 seconds (Python interpreter start + import std library)

**Analysis**: Well under 1 second constraint (NFR-P001).

---

## Security Considerations

**Scope**: Minimal security concerns for Phase I

**Analysis**:
- Single-user, no authentication required
- No network communication, no external attacks
- No persistence, no data at rest to protect
- No sensitive data handling (just task descriptions)
- Input validation prevents crashes from malformed input

**Recommendations**: None for Phase I. Security becomes relevant in Phase II+ (multi-user, persistence, network).

---

## Future Phases (DO NOT IMPLEMENT)

This section documents what will NOT appear in Phase I but may be researched for future phases:

**Phase II**: Persistence (file formats: JSON, SQLite, database choices)
**Phase III**: Search algorithms, filtering strategies, date handling
**Phase IV**: Web frameworks, REST API design, authentication patterns
**Phase V**: Message queues, event sourcing, distributed systems

**CRITICAL**: Do not implement or prepare for these in Phase I per Constitution Principle III.

---

## Summary

All research complete. Key decisions:
- ✅ Python dictionary for task storage (O(1) lookups)
- ✅ Simple integer counter for ID generation
- ✅ Input validation at UI layer
- ✅ Return tuples for error handling
- ✅ Fixed-width table for task display
- ✅ Three-module architecture (task_manager, ui, todo_app)
- ✅ Manual testing approach

No unresolved questions. Ready to proceed to data model and implementation.
