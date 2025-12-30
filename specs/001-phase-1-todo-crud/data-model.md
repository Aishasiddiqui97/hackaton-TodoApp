# Data Model: Phase I - Todo CRUD Console App

**Feature**: 001-phase-1-todo-crud
**Date**: 2025-12-31
**Purpose**: Define data structures, entities, and storage mechanisms for Phase I

## Overview

Phase I uses a simple in-memory data model with one entity (Task) stored in a Python dictionary. No persistence, no databases, no complex relationships.

## Entities

### Task Entity

Represents a single todo item with three fields.

**Fields**:

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `id` | int | Yes | Auto-assigned | Unique, sequential, ≥ 1 | Unique identifier for the task |
| `description` | str | Yes | None | Non-empty, non-whitespace | What the task is about |
| `completed` | bool | Yes | False | True or False | Whether the task is completed |

**Field Details**:

- **id**:
  - Type: Integer
  - Generated automatically by system on task creation
  - Starts at 1, increments sequentially (1, 2, 3, 4...)
  - Never reused, even after task deletion
  - Immutable (never changes once assigned)

- **description**:
  - Type: String
  - User-provided text describing the task
  - Must not be empty or contain only whitespace
  - No maximum length enforced (reasonable length ~500 characters assumed)
  - Mutable (can be updated via Update Task operation)

- **completed**:
  - Type: Boolean
  - True = task is complete
  - False = task is incomplete (default)
  - Mutable (toggled via Mark Complete/Incomplete operations)

**Example Task Objects**:

```python
# Task 1: Incomplete
{
    "id": 1,
    "description": "Buy groceries",
    "completed": False
}

# Task 2: Complete
{
    "id": 2,
    "description": "Finish project report",
    "completed": True
}

# Task 3: Incomplete
{
    "id": 3,
    "description": "Call dentist for appointment",
    "completed": False
}
```

## Storage Structure

### Primary Storage

**Type**: Python dictionary
**Structure**: `dict[int, dict[str, Any]]`
**Key**: Task ID (int)
**Value**: Task object (dict with id, description, completed)

**Example**:

```python
tasks = {
    1: {"id": 1, "description": "Buy groceries", "completed": False},
    2: {"id": 2, "description": "Finish project report", "completed": True},
    3: {"id": 3, "description": "Call dentist", "completed": False}
}
```

**Rationale**:
- O(1) lookup, update, and delete operations by task ID
- Maintains insertion order (Python 3.7+) for consistent display
- Simple and idiomatic Python pattern
- No external dependencies required

### ID Generation

**Type**: Integer counter
**Initial Value**: 1
**Increment**: +1 after each successful task creation
**Persistence**: None (resets to 1 on application restart)

**Example**:

```python
next_id = 1  # Initial state

# After adding first task:
next_id = 2  # Ready for next task

# After adding second task:
next_id = 3  # Ready for next task

# After deleting task 2:
next_id = 3  # Still 3 (IDs never reused)
```

**Important**: ID counter only increments, never decrements. Deleted task IDs are never reused.

## Data Operations

### Create (Add Task)

**Operation**: Add new task to tasks dictionary

**Input**:
- description (str, non-empty)

**Process**:
1. Validate description (non-empty, non-whitespace)
2. Assign current `next_id` as task ID
3. Create task object: `{"id": next_id, "description": description, "completed": False}`
4. Insert into tasks dictionary: `tasks[next_id] = task`
5. Increment `next_id` by 1
6. Return success with assigned task ID

**Output**: `(success: bool, task_id: int, message: str)`

**Example**:
```python
# Before:
tasks = {}
next_id = 1

# Add "Buy milk":
tasks[1] = {"id": 1, "description": "Buy milk", "completed": False}
next_id = 2

# Result:
tasks = {1: {"id": 1, "description": "Buy milk", "completed": False}}
next_id = 2
```

### Read (View All Tasks)

**Operation**: Retrieve all tasks from dictionary

**Input**: None

**Process**:
1. Get all values from tasks dictionary
2. Convert to list
3. Return list (empty list if no tasks)

**Output**: `list[dict]`

**Example**:
```python
# tasks = {1: {...}, 2: {...}, 3: {...}}
# Returns: [{"id": 1, ...}, {"id": 2, ...}, {"id": 3, ...}]
```

### Update (Update Task Description)

**Operation**: Update description of existing task

**Input**:
- task_id (int)
- new_description (str, non-empty)

**Process**:
1. Check if task_id exists in tasks dictionary
2. If not exists, return error
3. If exists, validate new_description (non-empty, non-whitespace)
4. Update description: `tasks[task_id]["description"] = new_description`
5. Keep id and completed unchanged
6. Return success

**Output**: `(success: bool, message: str)`

**Example**:
```python
# Before:
tasks[1] = {"id": 1, "description": "Buy milk", "completed": False}

# Update description to "Buy groceries":
tasks[1]["description"] = "Buy groceries"

# After:
tasks[1] = {"id": 1, "description": "Buy groceries", "completed": False}
# id and completed unchanged
```

### Delete (Delete Task)

**Operation**: Remove task from dictionary

**Input**:
- task_id (int)

**Process**:
1. Check if task_id exists in tasks dictionary
2. If not exists, return error
3. If exists, delete from dictionary: `del tasks[task_id]`
4. Return success

**Output**: `(success: bool, message: str)`

**Note**: Deleted task IDs are never reused. `next_id` counter is not affected by deletions.

**Example**:
```python
# Before:
tasks = {1: {...}, 2: {...}, 3: {...}}

# Delete task 2:
del tasks[2]

# After:
tasks = {1: {...}, 3: {...}}
# Task 2 is gone, next_id still increments normally
```

### Mark Complete

**Operation**: Set task completed status to True

**Input**:
- task_id (int)

**Process**:
1. Check if task_id exists in tasks dictionary
2. If not exists, return error
3. If exists, set completed to True: `tasks[task_id]["completed"] = True`
4. Return success

**Output**: `(success: bool, message: str)`

**Example**:
```python
# Before:
tasks[1] = {"id": 1, "description": "Buy milk", "completed": False}

# Mark complete:
tasks[1]["completed"] = True

# After:
tasks[1] = {"id": 1, "description": "Buy milk", "completed": True}
```

### Mark Incomplete

**Operation**: Set task completed status to False

**Input**:
- task_id (int)

**Process**:
1. Check if task_id exists in tasks dictionary
2. If not exists, return error
3. If exists, set completed to False: `tasks[task_id]["completed"] = False`
4. Return success

**Output**: `(success: bool, message: str)`

**Example**:
```python
# Before:
tasks[1] = {"id": 1, "description": "Buy milk", "completed": True}

# Mark incomplete:
tasks[1]["completed"] = False

# After:
tasks[1] = {"id": 1, "description": "Buy milk", "completed": False}
```

## Validation Rules

### Task Description

**Rule**: Must not be empty or contain only whitespace

**Validation**:
```python
def is_valid_description(desc: str) -> bool:
    return desc and desc.strip()
```

**Valid Examples**:
- "Buy groceries"
- "  Call dentist  " (will be stripped to "Call dentist")
- "A" (single character is fine)

**Invalid Examples**:
- "" (empty string)
- "   " (whitespace only)
- None (not a string)

### Task ID

**Rule**: Must exist in tasks dictionary

**Validation**:
```python
def is_valid_task_id(task_id: int) -> bool:
    return task_id in tasks
```

**Valid Examples**:
- 1 (if task 1 exists)
- 5 (if task 5 exists)

**Invalid Examples**:
- 99 (if task 99 doesn't exist)
- 0 (IDs start at 1)
- -1 (IDs are positive)

## State Transitions

### Task Lifecycle

```
┌─────────────┐
│   Created   │
│ completed:  │
│   False     │
└──────┬──────┘
       │
       │ (created with completed=False)
       │
       ▼
┌─────────────┐  Mark Complete   ┌─────────────┐
│ Incomplete  │ ───────────────>  │  Complete   │
│ completed:  │                   │ completed:  │
│   False     │ <─────────────── │   True      │
└──────┬──────┘  Mark Incomplete └──────┬──────┘
       │                                │
       │ Delete                         │ Delete
       │                                │
       ▼                                ▼
   ┌─────────┐                      ┌─────────┐
   │ Deleted │                      │ Deleted │
   └─────────┘                      └─────────┘
```

**Transitions**:
1. **Create** → Incomplete (completed=False by default)
2. **Mark Complete** → Incomplete → Complete (completed=False → True)
3. **Mark Incomplete** → Complete → Incomplete (completed=True → False)
4. **Delete** → Any state → Deleted (removed from storage)
5. **Update** → Any state → Same state (only description changes, not status)

## Constraints

### Phase I Specific

- **No Persistence**: All data lost when application exits
- **In-Memory Only**: No files, no databases
- **No Relationships**: Tasks are independent, no subtasks or dependencies
- **No Metadata**: No creation time, modification time, or history
- **No Ordering**: Display order is insertion order (dict preserves order in Py3.7+)
- **No Indexing**: Only lookup by primary key (task ID)
- **No Transactions**: All operations are immediate and atomic

### Future Phases (DO NOT IMPLEMENT)

- **Phase II**: Add persistence (file or database)
- **Phase III**: Add metadata (timestamps, priorities, tags, due dates)
- **Phase IV**: Add relationships (subtasks, dependencies)
- **Phase V**: Add event sourcing (task history, audit trail)

**CRITICAL**: Do not add these features in Phase I per Constitution Principle III.

## Data Integrity

### Uniqueness

- **Task IDs**: Guaranteed unique by sequential counter
- **No Duplicates**: Dictionary keys enforce uniqueness

### Consistency

- **ID Immutability**: Task ID never changes after creation
- **Status Integrity**: completed is always boolean (never null/undefined)
- **Description Integrity**: Empty descriptions never reach storage layer (validated at UI)

### Concurrency

**N/A for Phase I**: Single-threaded, single-user, synchronous operations

## Example Data Scenarios

### Scenario 1: Empty State (Application Start)

```python
tasks = {}
next_id = 1
```

### Scenario 2: Three Tasks (Mixed Status)

```python
tasks = {
    1: {"id": 1, "description": "Buy groceries", "completed": False},
    2: {"id": 2, "description": "Finish report", "completed": True},
    3: {"id": 3, "description": "Call dentist", "completed": False}
}
next_id = 4
```

### Scenario 3: After Deleting Task 2

```python
tasks = {
    1: {"id": 1, "description": "Buy groceries", "completed": False},
    3: {"id": 3, "description": "Call dentist", "completed": False}
}
next_id = 4  # Still 4, not 3 (IDs never reused)
```

### Scenario 4: 100 Tasks (Performance Test)

```python
tasks = {
    1: {"id": 1, "description": "Task 1", "completed": False},
    2: {"id": 2, "description": "Task 2", "completed": True},
    ...
    100: {"id": 100, "description": "Task 100", "completed": False}
}
next_id = 101

# Performance: All operations still O(1) or O(n)
# Memory: ~100KB (well within 50MB constraint)
```

## Summary

**Entity**: Task (id, description, completed)
**Storage**: Python dictionary (task_id → task_dict)
**ID Generation**: Simple integer counter (starts at 1, increments, never reuses)
**Operations**: Add, View All, Update, Delete, Mark Complete, Mark Incomplete
**Validation**: Non-empty descriptions, existing IDs
**Constraints**: In-memory only, no persistence, no relationships, no metadata

**Ready for implementation**: Data model is complete and aligned with specification requirements.
