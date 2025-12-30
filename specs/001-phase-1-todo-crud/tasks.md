# Tasks: Phase I - Todo CRUD Console App

**Input**: Design documents from `/specs/001-phase-1-todo-crud/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓

**Tests**: Tests are OPTIONAL for Phase I per spec. Tasks below do not include automated tests.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow plan.md structure (plan.md:76-87)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure per plan.md:416-428

- [X] **T001** Create project directory structure: `src/` folder at repository root
  - **Precondition**: Repository root exists
  - **Expected Output**: `src/` directory created
  - **Artifacts**: `src/` directory
  - **Reference**: plan.md:76-87 (Project Structure)

- [X] **T002** Create Python module files with docstrings
  - **Precondition**: T001 complete (`src/` exists)
  - **Expected Output**: Three empty .py files with module docstrings
  - **Artifacts**: `src/task_manager.py`, `src/ui.py`, `src/todo_app.py`
  - **Reference**: plan.md:79-83, plan.md:200-309 (Module Design)
  - **Content**: Each file should have module-level docstring describing its purpose

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data layer that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Data Layer Foundation (task_manager.py)

- [X] **T003** Implement task storage data structures in src/task_manager.py
  - **Precondition**: T002 complete (task_manager.py exists)
  - **Expected Output**: Module-level variables for storage and ID counter
  - **Artifacts**: Module variables in src/task_manager.py
  - **Reference**: data-model.md:45-60 (Storage Structure), plan.md:231-235
  - **Content**:
    ```python
    # Module-level storage
    tasks: dict[int, dict[str, Any]] = {}
    next_id: int = 1
    ```

- [X] **T004** [P] Implement task_exists() function in src/task_manager.py
  - **Precondition**: T003 complete (storage variables exist)
  - **Expected Output**: Function that checks if task ID exists in tasks dict
  - **Artifacts**: task_exists() function in src/task_manager.py
  - **Reference**: plan.md:227-228, data-model.md:208-222 (Validation Rules)
  - **Signature**: `def task_exists(task_id: int) -> bool:`
  - **Logic**: Return `task_id in tasks`

- [X] **T005** [P] Implement get_all_tasks() function in src/task_manager.py
  - **Precondition**: T003 complete (storage variables exist)
  - **Expected Output**: Function that returns list of all tasks
  - **Artifacts**: get_all_tasks() function in src/task_manager.py
  - **Reference**: plan.md:212-213, data-model.md:97-107 (Read Operation)
  - **Signature**: `def get_all_tasks() -> list[dict]:`
  - **Logic**: Return `list(tasks.values())`

**Checkpoint**: Foundation ready - data storage and basic query functions complete

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add tasks with descriptions, system assigns unique IDs
**Independent Test**: Launch app, select Add Task, enter description, verify task added with ID
**Reference**: spec.md:10-23 (User Story 1)

### Implementation for User Story 1

- [X] **T006** [US1] Implement add_task() function in src/task_manager.py
  - **Precondition**: T003, T004 complete (storage and task_exists ready)
  - **Expected Output**: Function that creates new task with auto-assigned ID
  - **Artifacts**: add_task() function in src/task_manager.py
  - **Reference**: plan.md:209-210, data-model.md:64-95 (Create Operation), spec.md FR-001, FR-002, FR-003
  - **Signature**: `def add_task(description: str) -> tuple[bool, int, str]:`
  - **Logic**:
    1. Assign current `next_id` to new task
    2. Create task dict: `{"id": next_id, "description": description, "completed": False}`
    3. Insert into tasks: `tasks[next_id] = task_dict`
    4. Increment `next_id` by 1
    5. Return `(True, task_id, "Task added successfully")`

- [X] **T007** [US1] Implement get_task_description() function in src/ui.py
  - **Precondition**: T002 complete (ui.py exists)
  - **Expected Output**: Function that prompts for and validates task description
  - **Artifacts**: get_task_description() function in src/ui.py
  - **Reference**: plan.md:259-260, plan.md:272-275 (Input Validation), spec.md FR-009
  - **Signature**: `def get_task_description() -> str:`
  - **Logic**:
    1. Prompt: "Enter task description: "
    2. Get input, strip whitespace
    3. If empty, display error and re-prompt
    4. Return validated description

- [X] **T008** [US1] Implement display_success() function in src/ui.py
  - **Precondition**: T002 complete (ui.py exists)
  - **Expected Output**: Function that displays success messages
  - **Artifacts**: display_success() function in src/ui.py
  - **Reference**: plan.md:268-269, spec.md NFR-U004
  - **Signature**: `def display_success(message: str) -> None:`
  - **Logic**: Print message (optionally with green color or highlighting)

- [X] **T009** [US1] Implement display_error() function in src/ui.py
  - **Precondition**: T002 complete (ui.py exists)
  - **Expected Output**: Function that displays error messages
  - **Artifacts**: display_error() function in src/ui.py
  - **Reference**: plan.md:265-267, spec.md NFR-U002, plan.md:385-388 (Error Message Format)
  - **Signature**: `def display_error(message: str) -> None:`
  - **Logic**: Print "ERROR: {message}" (optionally with red color or highlighting)

- [X] **T010** [US1] Implement handle_add_task() in src/todo_app.py
  - **Precondition**: T006, T007, T008, T009 complete
  - **Expected Output**: Handler function that orchestrates Add Task operation
  - **Artifacts**: handle_add_task() function in src/todo_app.py
  - **Reference**: plan.md:309, plan.md:323-329 (Add Task Flow), spec.md:18-22 (Acceptance Scenarios)
  - **Logic**:
    1. Call ui.get_task_description()
    2. Call task_manager.add_task(description)
    3. Call ui.display_success(f"Task added successfully with ID: {task_id}")

**Checkpoint**: User Story 1 complete - users can add tasks and receive confirmation with assigned ID

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can see all tasks in readable format with ID, description, and status
**Independent Test**: Add several tasks, select View Tasks, verify all display correctly
**Reference**: spec.md:26-39 (User Story 2)

### Implementation for User Story 2

- [X] **T011** [US2] Implement display_tasks() function in src/ui.py
  - **Precondition**: T005 complete (get_all_tasks exists)
  - **Expected Output**: Function that formats and displays task list as table
  - **Artifacts**: display_tasks() function in src/ui.py
  - **Reference**: plan.md:253-254, plan.md:176-182 (Display Format), spec.md FR-004, NFR-U003
  - **Signature**: `def display_tasks(tasks: list[dict]) -> None:`
  - **Logic**:
    1. If empty list, print "Task list is empty"
    2. Else, print header: "ID  | Description                      | Status"
    3. Print separator: "----|----------------------------------|------------"
    4. For each task, print formatted row: f"{id:<4}| {desc:<34}| {'Complete' if completed else 'Incomplete'}"

- [X] **T012** [US2] Implement handle_view_tasks() in src/todo_app.py
  - **Precondition**: T011 complete (display_tasks exists), T005 complete (get_all_tasks exists)
  - **Expected Output**: Handler function that orchestrates View Tasks operation
  - **Artifacts**: handle_view_tasks() function in src/todo_app.py
  - **Reference**: plan.md:331-335 (View Tasks Flow), spec.md:34-38 (Acceptance Scenarios)
  - **Logic**:
    1. Call task_manager.get_all_tasks()
    2. Call ui.display_tasks(tasks)

**Checkpoint**: User Story 2 complete - users can view all tasks in formatted table

---

## Phase 5: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Users can mark tasks as complete or incomplete to track progress
**Independent Test**: Add task, mark complete, verify status changes, mark incomplete, verify toggle
**Reference**: spec.md:74-88 (User Story 5)

### Implementation for User Story 5

- [X] **T013** [P] [US5] Implement mark_complete() function in src/task_manager.py
  - **Precondition**: T003, T004 complete (storage and task_exists ready)
  - **Expected Output**: Function that sets task completed status to True
  - **Artifacts**: mark_complete() function in src/task_manager.py
  - **Reference**: plan.md:221-223, data-model.md:131-147 (Mark Complete Operation), spec.md FR-007
  - **Signature**: `def mark_complete(task_id: int) -> tuple[bool, str]:`
  - **Logic**:
    1. If not task_exists(task_id), return `(False, f"Task ID {task_id} not found")`
    2. Set `tasks[task_id]["completed"] = True`
    3. Return `(True, "Task marked as complete")`

- [X] **T014** [P] [US5] Implement mark_incomplete() function in src/task_manager.py
  - **Precondition**: T003, T004 complete (storage and task_exists ready)
  - **Expected Output**: Function that sets task completed status to False
  - **Artifacts**: mark_incomplete() function in src/task_manager.py
  - **Reference**: plan.md:224-226, data-model.md:149-165 (Mark Incomplete Operation), spec.md FR-008
  - **Signature**: `def mark_incomplete(task_id: int) -> tuple[bool, str]:`
  - **Logic**:
    1. If not task_exists(task_id), return `(False, f"Task ID {task_id} not found")`
    2. Set `tasks[task_id]["completed"] = False`
    3. Return `(True, "Task marked as incomplete")`

- [X] **T015** [US5] Implement get_task_id() function in src/ui.py
  - **Precondition**: T002 complete (ui.py exists), T009 complete (display_error exists)
  - **Expected Output**: Function that prompts for and validates task ID as integer
  - **Artifacts**: get_task_id() function in src/ui.py
  - **Reference**: plan.md:262-264, plan.md:274-275 (Input Validation), spec.md FR-010
  - **Signature**: `def get_task_id() -> int:`
  - **Logic**:
    1. Prompt: "Enter task ID: "
    2. Try to parse as int
    3. If ValueError, display "Please enter a valid task ID (number)" and re-prompt
    4. Return validated integer ID

- [X] **T016** [US5] Implement handle_mark_complete() in src/todo_app.py
  - **Precondition**: T013, T015, T008, T009 complete
  - **Expected Output**: Handler function that orchestrates Mark Complete operation
  - **Artifacts**: handle_mark_complete() function in src/todo_app.py
  - **Reference**: plan.md:357-362 (Mark Complete Flow), spec.md:83-87 (Acceptance Scenarios)
  - **Logic**:
    1. Call ui.get_task_id()
    2. Call task_manager.mark_complete(task_id)
    3. If success, call ui.display_success(message)
    4. Else, call ui.display_error(message)

- [X] **T017** [US5] Implement handle_mark_incomplete() in src/todo_app.py
  - **Precondition**: T014, T015, T008, T009 complete
  - **Expected Output**: Handler function that orchestrates Mark Incomplete operation
  - **Artifacts**: handle_mark_incomplete() function in src/todo_app.py
  - **Reference**: plan.md:364-370 (Mark Incomplete Flow), spec.md:83-87 (Acceptance Scenarios)
  - **Logic**:
    1. Call ui.get_task_id()
    2. Call task_manager.mark_incomplete(task_id)
    3. If success, call ui.display_success(message)
    4. Else, call ui.display_error(message)

**Checkpoint**: User Story 5 complete - users can toggle task completion status

---

## Phase 6: User Story 3 - Update Task Description (Priority: P2)

**Goal**: Users can correct or refine task descriptions
**Independent Test**: Add task, select Update, change description, verify update while ID/status unchanged
**Reference**: spec.md:42-55 (User Story 3)

### Implementation for User Story 3

- [X] **T018** [US3] Implement update_task() function in src/task_manager.py
  - **Precondition**: T003, T004 complete (storage and task_exists ready)
  - **Expected Output**: Function that updates task description
  - **Artifacts**: update_task() function in src/task_manager.py
  - **Reference**: plan.md:215-217, data-model.md:109-129 (Update Operation), spec.md FR-005
  - **Signature**: `def update_task(task_id: int, new_description: str) -> tuple[bool, str]:`
  - **Logic**:
    1. If not task_exists(task_id), return `(False, f"Task ID {task_id} not found")`
    2. Update `tasks[task_id]["description"] = new_description`
    3. Return `(True, "Task updated successfully")`

- [X] **T019** [US3] Implement handle_update_task() in src/todo_app.py
  - **Precondition**: T018, T015, T007, T008, T009 complete
  - **Expected Output**: Handler function that orchestrates Update Task operation
  - **Artifacts**: handle_update_task() function in src/todo_app.py
  - **Reference**: plan.md:337-346 (Update Task Flow), spec.md:50-54 (Acceptance Scenarios)
  - **Logic**:
    1. Call ui.get_task_id()
    2. Call ui.get_task_description()
    3. Call task_manager.update_task(task_id, new_description)
    4. If success, call ui.display_success(message)
    5. Else, call ui.display_error(message)

**Checkpoint**: User Story 3 complete - users can update task descriptions

---

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks that are no longer relevant
**Independent Test**: Add tasks, select Delete, provide ID, verify task removed from list
**Reference**: spec.md:58-71 (User Story 4)

### Implementation for User Story 4

- [X] **T020** [US4] Implement delete_task() function in src/task_manager.py
  - **Precondition**: T003, T004 complete (storage and task_exists ready)
  - **Expected Output**: Function that removes task from storage
  - **Artifacts**: delete_task() function in src/task_manager.py
  - **Reference**: plan.md:218-220, data-model.md:111-129 (Delete Operation), spec.md FR-006
  - **Signature**: `def delete_task(task_id: int) -> tuple[bool, str]:`
  - **Logic**:
    1. If not task_exists(task_id), return `(False, f"Task ID {task_id} not found")`
    2. Delete from dict: `del tasks[task_id]`
    3. Return `(True, "Task deleted successfully")`
  - **Note**: ID counter not affected, IDs never reused (data-model.md:122)

- [X] **T021** [US4] Implement handle_delete_task() in src/todo_app.py
  - **Precondition**: T020, T015, T008, T009 complete
  - **Expected Output**: Handler function that orchestrates Delete Task operation
  - **Artifacts**: handle_delete_task() function in src/todo_app.py
  - **Reference**: plan.md:348-353 (Delete Task Flow), spec.md:66-70 (Acceptance Scenarios)
  - **Logic**:
    1. Call ui.get_task_id()
    2. Call task_manager.delete_task(task_id)
    3. If success, call ui.display_success(message)
    4. Else, call ui.display_error(message)

**Checkpoint**: User Story 4 complete - users can delete tasks

---

## Phase 8: Application Lifecycle (Main Loop & Menu)

**Purpose**: Tie everything together with menu loop and application entry point

### Main Menu Implementation

- [X] **T022** Implement display_menu() function in src/ui.py
  - **Precondition**: T002 complete (ui.py exists)
  - **Expected Output**: Function that displays main menu with 7 options
  - **Artifacts**: display_menu() function in src/ui.py
  - **Reference**: plan.md:250-251, spec.md FR-012, NFR-U001
  - **Signature**: `def display_menu() -> None:`
  - **Content**:
    ```
    ===== Todo List Application =====

    1. Add Task
    2. View Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task Complete
    6. Mark Task Incomplete
    7. Exit
    ```

- [X] **T023** Implement get_menu_choice() function in src/ui.py
  - **Precondition**: T022, T009 complete (display_menu and display_error exist)
  - **Expected Output**: Function that prompts for and validates menu choice
  - **Artifacts**: get_menu_choice() function in src/ui.py
  - **Reference**: plan.md:256-258, plan.md:275 (Menu Validation), spec.md FR-011
  - **Signature**: `def get_menu_choice() -> int:`
  - **Logic**:
    1. Prompt: "Enter your choice (1-7): "
    2. Try to parse as int
    3. If ValueError or not in range 1-7, display "Invalid choice. Please select 1-7" and re-prompt
    4. Return validated choice

- [X] **T024** Implement main() function in src/todo_app.py
  - **Precondition**: T010, T012, T016, T017, T019, T021, T022, T023 complete (all handlers and menu ready)
  - **Expected Output**: Main application loop coordinating all operations
  - **Artifacts**: main() function in src/todo_app.py
  - **Reference**: plan.md:285-307 (Main Loop Structure), plan.md:313-321 (Application Lifecycle), spec.md FR-013
  - **Logic**:
    1. While True loop
    2. Call ui.display_menu()
    3. Call ui.get_menu_choice()
    4. Route to appropriate handler (1-6) or break if 7 (Exit)
    5. On Exit, print "Goodbye!"

- [X] **T025** Add module entry point in src/todo_app.py
  - **Precondition**: T024 complete (main function exists)
  - **Expected Output**: Python entry point that calls main()
  - **Artifacts**: Entry point code in src/todo_app.py
  - **Reference**: plan.md:280-281, plan.md:471-476 (Running Instructions)
  - **Content**:
    ```python
    if __name__ == "__main__":
        main()
    ```

**Checkpoint**: Application complete - full menu loop with all 7 operations functional

---

## Phase 9: Integration Validation

**Purpose**: Verify all user stories work together and meet specification

- [X] **T026** Manual integration test - Complete user journey
  - **Precondition**: T001-T025 complete (application fully implemented)
  - **Expected Output**: All operations work end-to-end without errors
  - **Test Steps**:
    1. Run `python src/todo_app.py`
    2. Add 3 tasks (verify IDs 1, 2, 3 assigned)
    3. View tasks (verify all 3 appear with "Incomplete" status)
    4. Mark task 2 complete (verify success message)
    5. View tasks (verify task 2 shows "Complete")
    6. Update task 1 description (verify success message)
    7. View tasks (verify task 1 description changed, ID and status unchanged)
    8. Delete task 3 (verify success message)
    9. View tasks (verify only tasks 1 and 2 remain)
    10. Mark task 2 incomplete (verify success message)
    11. View tasks (verify task 2 shows "Incomplete")
    12. Exit (verify "Goodbye!" message)
  - **Reference**: spec.md:130-137 (Success Criteria), quickstart.md:110-186 (Example Session)

- [X] **T027** Manual validation - Error handling
  - **Precondition**: T026 complete (basic operations validated)
  - **Expected Output**: All error cases handled gracefully per spec
  - **Test Steps**:
    1. Run application
    2. Try to add task with empty description (verify error, re-prompt)
    3. Try to view tasks when list is empty (verify "empty list" message)
    4. Add task, then try to update with non-existent ID (verify "not found" error)
    5. Try to delete non-existent ID (verify "not found" error)
    6. Try to mark complete/incomplete with non-existent ID (verify "not found" error)
    7. Try invalid menu choice (verify error, re-prompt)
    8. Try non-integer input for task ID (verify error, re-prompt)
    9. Try non-integer input for menu choice (verify error, re-prompt)
  - **Reference**: spec.md:91-96 (Edge Cases), spec.md FR-009, FR-010, FR-011, NFR-R001, NFR-R002

- [X] **T028** Performance validation
  - **Precondition**: T026 complete (application functional)
  - **Expected Output**: All performance requirements met
  - **Test Steps**:
    1. Measure startup time (verify < 1 second per NFR-P001)
    2. Add 100 tasks sequentially (verify no errors per SC-005)
    3. Measure View operation time with 100 tasks (verify < 1 second per NFR-P002)
    4. Measure Update/Delete/Mark operations (verify < 1 second per NFR-P002)
  - **Reference**: spec.md:200-203 (Performance NFRs), spec.md SC-005, SC-006

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - create project structure first
- **Foundational (Phase 2)**: Depends on Setup - creates data layer blocking all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational completion
  - Phase 3 (US1 - Add): Can start after Foundational
  - Phase 4 (US2 - View): Can start after Foundational, uses US1 to test
  - Phase 5 (US5 - Mark): Can start after Foundational, uses US1 to test
  - Phase 6 (US3 - Update): Can start after Foundational, uses US1 to test
  - Phase 7 (US4 - Delete): Can start after Foundational, uses US1 to test
- **Main Loop (Phase 8)**: Depends on all user story handlers (T010, T012, T016, T017, T019, T021)
- **Validation (Phase 9)**: Depends on complete application (T001-T025)

### Task-Level Dependencies

**Critical Path** (must be sequential):
1. T001 → T002 → T003 (Setup → Module files → Storage)
2. T003 → T006 (Storage → Add task function)
3. T006, T007, T008, T009 → T010 (Components → Add handler)
4. All handlers → T024 (Handlers → Main loop)
5. T024 → T025 → T026 (Main → Entry point → Integration test)

**Parallel Opportunities**:
- **After T003 complete**: T004, T005 can run in parallel (both read from storage, no writes)
- **After T002 complete**: T007, T008, T009 can run in parallel (all in ui.py, no interdependencies)
- **After T003, T004 complete**: T013, T014 can run in parallel (both status operations, similar logic)
- **User story handlers**: T010 (US1), T012 (US2), T016/T017 (US5), T019 (US3), T021 (US4) can be developed in parallel once their dependencies are met

### Parallel Execution Strategy

**Wave 1** (After T003):
- Launch T004, T005 in parallel

**Wave 2** (After T002):
- Launch T007, T008, T009 in parallel

**Wave 3** (After T003, T004):
- Launch T013, T014 in parallel

**Wave 4** (After dependencies met):
- T010 (needs T006, T007, T008, T009)
- T012 (needs T005, T011)
- T016, T017 (need T013/T014, T015, T008, T009)
- T019 (needs T018, T015, T007, T008, T009)
- T021 (needs T020, T015, T008, T009)

---

## Implementation Strategy

### MVP First (Minimum Viable Product)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T005)
3. Complete Phase 3: User Story 1 - Add (T006-T010)
4. Complete Phase 4: User Story 2 - View (T011-T012)
5. Add minimal menu (T022-T025 with only Add/View/Exit)
6. **STOP and VALIDATE**: Test adding and viewing tasks
7. This is your MVP - working todo list!

### Incremental Delivery

After MVP validation:
8. Add Phase 5: Mark Complete/Incomplete (T013-T017)
9. Update menu to include Mark options
10. Test independently
11. Add Phase 6: Update (T018-T019)
12. Update menu to include Update option
13. Test independently
14. Add Phase 7: Delete (T020-T021)
15. Update menu to include Delete option
16. Complete Phase 9: Full validation (T026-T028)

### Sequential (Safest) Strategy

Follow task order T001 → T002 → ... → T028 sequentially. Each task builds on previous. Good for learning or when unsure about parallel execution.

---

## Notes

- **File References**: All src/ paths are relative to repository root
- **Spec Compliance**: Every task references specific spec.md requirement (FR-xxx, NFR-xxx, SC-xxx)
- **Plan Alignment**: Every task references plan.md section with implementation details
- **Data Model**: Tasks T003-T020 implement operations from data-model.md
- **No Tests**: Per spec, automated tests are optional for Phase I (manual testing in T026-T028)
- **Phase Boundaries**: No tasks introduce persistence, multi-user, or future-phase features per constitution
- **Atomic Tasks**: Each task produces one deliverable artifact or function
- **Testability**: Each task has clear preconditions and expected outputs for validation

---

## Summary Statistics

- **Total Tasks**: 28
- **Phases**: 9 (Setup → Foundational → 5 User Stories → Main Loop → Validation)
- **Files Created**: 3 (task_manager.py, ui.py, todo_app.py)
- **Functions Implemented**: 16 total
  - task_manager.py: 7 functions (add, get_all, update, delete, mark_complete, mark_incomplete, task_exists)
  - ui.py: 7 functions (display_menu, display_tasks, get_menu_choice, get_task_description, get_task_id, display_error, display_success)
  - todo_app.py: 7 functions (main + 6 handlers)
- **User Stories**: 5 (Add, View, Update, Delete, Mark Complete/Incomplete)
- **Estimated LOC**: ~400-500 lines total (simple, readable code)

**Ready for implementation**: Execute tasks in order T001→T028 or follow parallel strategy for faster completion.
