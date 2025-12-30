<!--
Sync Impact Report:
Version Change: 0.0.0 → 1.0.0
Modified Principles:
  - All principles newly created for Evolution of Todo project
Added Sections:
  - Core Principles (6 principles)
  - Phase Governance
  - Technology Standards
  - Quality & Architecture Standards
  - Development Workflow
  - Agent Behavior Contract
Removed Sections: None (initial constitution)
Templates Status:
  ✅ plan-template.md: Reviewed - aligns with constitution checks
  ✅ spec-template.md: Reviewed - aligns with requirements and user stories
  ✅ tasks-template.md: Reviewed - aligns with phase organization and testing
Follow-up TODOs: None
-->

# Evolution of Todo Project Constitution

## Core Principles

### I. Spec-Driven Development (MANDATORY)

**Rule**: No agent may write production code without approved specifications and tasks.

**Workflow**: All development MUST follow this sequence:
1. **Constitution** → Establishes project-wide governance and principles
2. **Specification** → Defines what to build (user stories, requirements, success criteria)
3. **Plan** → Defines how to build (architecture, technical approach, design artifacts)
4. **Tasks** → Defines implementation steps (concrete, testable, dependency-ordered)
5. **Implementation** → Execute tasks with verification at each step

**Enforcement**:
- Agents MUST NOT implement features not documented in approved specs
- Agents MUST NOT deviate from approved specifications without updating the spec first
- All refinements MUST occur at the specification or plan level, never directly in code
- Code reviews MUST verify traceability to approved specs and tasks

**Rationale**: Spec-Driven Development ensures every line of code has a documented purpose, approved design, and clear acceptance criteria. This prevents scope creep, enables parallel work, and maintains architectural integrity across all five phases of the Evolution of Todo project.

### II. No Feature Invention

**Rule**: Agents MUST implement only what is explicitly specified. Creativity is expressed through architectural design in the planning phase, not through unsolicited features in code.

**Prohibited Actions**:
- Adding "nice to have" features beyond the specification
- Implementing convenience methods not required by tasks
- Creating abstractions not called for in the plan
- Adding configuration options not specified in requirements

**Permitted Actions**:
- Implementing exactly what the spec requires
- Proposing additions to the spec for user approval
- Raising clarifying questions when requirements are ambiguous

**Rationale**: Feature invention creates unreviewed complexity, untested code paths, and architectural drift. All features must be justified at the spec level where they can be evaluated for necessity, cost, and alignment with project goals.

### III. Phase Boundary Enforcement

**Rule**: Each phase (I through V) is strictly scoped by its specification. Features from future phases MUST NOT leak into earlier phases.

**Phase Integrity Requirements**:
- Phase I implementation MUST contain only Phase I features as specified
- Dependencies on future-phase components are FORBIDDEN
- Architectural hooks or abstractions for future phases are PROHIBITED unless explicitly specified
- Phase boundaries are defined by approved specifications, not by agent judgment

**Evolution Pathway**:
- Architecture MAY evolve across phases ONLY through updated specifications and plans
- When moving from Phase N to Phase N+1, new specs and plans MUST be created
- Refactoring from earlier phases requires specification updates, not direct code changes

**Rationale**: Phase discipline prevents architectural gold-plating, maintains focus on current deliverables, and ensures each phase delivers working, tested software. It also allows project stakeholders to pause, reassess, or pivot between phases based on real feedback.

### IV. Agent Autonomy within Guardrails

**Rule**: Agents operate autonomously to execute approved tasks but MUST respect constitutional constraints.

**Agent Authority**:
- Agents HAVE authority to: choose implementation details within task scope, refactor within task boundaries, select algorithms and data structures that meet specifications
- Agents DO NOT have authority to: skip or reorder tasks without approval, implement features outside current phase scope, modify approved specs or plans

**Human-in-the-Loop Triggers**:
- Ambiguous requirements → Ask 2-3 targeted clarifying questions
- Unforeseen dependencies → Surface and request prioritization
- Architectural uncertainty → Present options with tradeoffs and await decision
- Completion checkpoints → Summarize work and confirm next steps

**Rationale**: Balanced autonomy enables agent productivity while maintaining human control over scope, priorities, and architectural decisions. Agents are tools for execution, not for product management or architectural visioning.

### V. No Manual Coding by Humans

**Rule**: All production code MUST be written by agents following approved specifications. Human developers contribute through specification, review, and approval, not through direct code authorship.

**Human Roles**:
- Write and approve specifications
- Review agent-generated code for correctness and spec compliance
- Approve or reject pull requests
- Update specifications when requirements change
- Provide clarifications when agents request them

**Agent Roles**:
- Generate all production code from specs and tasks
- Write tests as specified
- Refactor within task scope
- Document implementation decisions
- Request clarifications when needed

**Exception**: Humans MAY write code in emergency hotfix situations, but such code MUST be retrospectively spec'd and replaced by agent-generated code in the next sprint.

**Rationale**: Agent-authored code ensures consistency with specifications, eliminates ad-hoc implementation drift, and creates a traceable audit trail from requirements to implementation. Human creativity is channeled into specification and architecture, not ad-hoc coding.

### VI. Test-Driven Development (When Specified)

**Rule**: When tests are specified in requirements, they MUST be written before implementation and MUST fail before code is written to pass them.

**TDD Workflow (when tests required)**:
1. Write test based on task specification
2. Verify test fails (red)
3. Implement minimum code to pass test (green)
4. Refactor within task scope if needed
5. Verify test still passes

**Test Requirements**:
- Contract tests for all public APIs
- Integration tests for user journeys
- Unit tests when explicitly specified in tasks
- Tests MUST be independently runnable

**Test Optionality**: Not all features require tests. Test requirements are defined in specifications and tasks. When tests are not specified, agents MUST NOT add them proactively.

**Rationale**: TDD (when appropriate) ensures code correctness, provides executable specifications, and prevents regressions. However, not all code needs tests—specifications define testing requirements based on risk, criticality, and project phase.

## Phase Governance

### Phase Structure

The Evolution of Todo project is organized into five sequential phases:
- **Phase I**: Core Todo CRUD operations (single-user, local or simple cloud persistence)
- **Phase II**: Multi-user support with authentication and authorization
- **Phase III**: Advanced features (tags, search, filtering, due dates, priorities)
- **Phase IV**: Real-time collaboration and synchronization
- **Phase V**: Distributed architecture with event-driven scaling

### Phase Transition Rules

**Moving from Phase N to Phase N+1 requires**:
1. All Phase N specifications implemented and verified
2. Phase N+1 specification written and approved
3. Phase N+1 implementation plan created
4. Phase N+1 tasks generated and reviewed
5. Explicit approval to proceed to Phase N+1

**Forbidden**: Skipping phases, parallel phase work (unless explicitly scoped), implementing Phase N+1 features "in advance" during Phase N.

### Specification Updates Within a Phase

**Minor updates** (clarifications, edge case handling, small scope additions) require:
- Updated spec document with change summary
- Updated plan if architectural impact exists
- Updated tasks reflecting new work
- Agent proceeds after approval

**Major updates** (significant scope changes, architectural pivots) require:
- Re-approval of updated specification
- Regeneration of plan and tasks
- Review of implementation work already completed

## Technology Standards

### Backend Technology Stack

**Language**: Python 3.11+
**Web Framework**: FastAPI (ASGI-based, async support)
**ORM**: SQLModel (Pydantic + SQLAlchemy integration)
**Database**: Neon DB (PostgreSQL-compatible, serverless)
**AI/Agents**: OpenAI Agents SDK (for future AI-enhanced features)
**Observability**: MCP (Model Context Protocol) for agent tooling and integrations

**Constraints**:
- All backend services MUST be written in Python
- Async/await patterns MUST be used for I/O-bound operations
- Type hints MUST be used for all function signatures (Pydantic models encouraged)
- No synchronous blocking calls in async endpoints

### Frontend Technology Stack (Phase II onwards)

**Framework**: Next.js (React-based, App Router preferred)
**Language**: TypeScript (strict mode enabled)
**Styling**: TailwindCSS or CSS Modules (specified per phase)
**State Management**: React Context or Zustand (specified per phase)

**Constraints**:
- All frontend code MUST be written in TypeScript
- Server components preferred over client components where applicable
- API calls MUST use typed clients

### Infrastructure & Orchestration (Phase IV-V)

**Containerization**: Docker
**Orchestration**: Kubernetes (for multi-service deployments)
**Messaging**: Kafka (event streaming in Phase V)
**Service Mesh**: Dapr (distributed application runtime, Phase V)

**Constraints**:
- Services MUST be containerized via Docker
- Container images MUST be production-ready (no debug tools, minimal layers)
- Kubernetes manifests MUST include resource limits and health checks

### Dependency Management

**Python**: Use `pyproject.toml` (Poetry or pip-tools)
**Node.js**: Use `package.json` with lockfile (`package-lock.json` or `pnpm-lock.yaml`)
**Versioning**: Pin major versions, allow minor/patch updates unless breaking changes observed

## Quality & Architecture Standards

### Clean Architecture Principles

**Layered Structure**:
1. **Domain Layer**: Business entities and rules (no dependencies on frameworks)
2. **Application Layer**: Use cases, services, orchestration (depends on domain)
3. **Infrastructure Layer**: Database, external APIs, frameworks (depends on application)
4. **Presentation Layer**: Controllers, API routes, CLI commands (depends on application)

**Dependency Rule**: Dependencies MUST point inward (presentation → application → domain). No inner layer may depend on an outer layer.

**Rationale**: Clean architecture ensures business logic is independent of frameworks, databases, and UI, enabling testability, maintainability, and technology swaps.

### Stateless Services (Where Required)

**Rule**: Services handling HTTP requests MUST be stateless. All state MUST reside in databases or external state stores.

**Stateless Requirements**:
- No in-memory session storage (use JWT or database-backed sessions)
- No process-local caches shared across requests (use Redis or similar)
- Horizontal scaling MUST NOT break functionality

**Exceptions**: Background workers, scheduled jobs, or single-instance services MAY maintain local state if explicitly specified.

**Rationale**: Stateless services enable horizontal scaling, fault tolerance, and cloud-native deployment patterns required for Phases IV-V.

### Separation of Concerns

**Module Responsibilities**: Each module, class, or function MUST have a single, well-defined responsibility.

**Prohibited**:
- God objects or classes with multiple unrelated responsibilities
- Business logic in controllers or presentation layer
- Data access logic in domain entities

**Encouraged**:
- Single Responsibility Principle (SRP) at all levels
- Dependency injection for testability
- Interface-based abstractions for external dependencies

### Cloud-Native Readiness

**12-Factor Principles**: Applications MUST adhere to relevant 12-factor app principles:
- Configuration via environment variables
- Stateless processes
- Logs as event streams (stdout/stderr)
- Graceful shutdown on SIGTERM
- Port binding for service exposure

**Observability**: All services MUST emit structured logs and expose health check endpoints (`/health`, `/ready`).

## Development Workflow

### Standard Development Sequence

1. **Specification** (`/sp.specify`)
   - User provides feature description
   - Agent generates or updates `specs/<feature>/spec.md`
   - User reviews and approves specification

2. **Planning** (`/sp.plan`)
   - Agent generates implementation plan in `specs/<feature>/plan.md`
   - Includes architecture, design artifacts, complexity analysis
   - User reviews and approves plan

3. **Task Generation** (`/sp.tasks`)
   - Agent generates task list in `specs/<feature>/tasks.md`
   - Tasks are concrete, testable, dependency-ordered
   - User reviews and approves tasks

4. **Implementation** (`/sp.implement`)
   - Agent executes tasks in dependency order
   - Marks tasks complete as implementation progresses
   - Commits code with references to task IDs

5. **Commit & PR** (`/sp.git.commit_pr`)
   - Agent commits changes with descriptive message
   - Creates pull request with summary linking to spec
   - User reviews and approves or requests changes

### Prompt History Records (PHR)

**Rule**: After every user input that results in significant work, agents MUST create a Prompt History Record in `history/prompts/`.

**PHR Routing**:
- Constitution-related prompts → `history/prompts/constitution/`
- Feature-specific prompts (spec, plan, tasks, implementation) → `history/prompts/<feature-name>/`
- General prompts → `history/prompts/general/`

**PHR Contents**:
- Full user prompt (verbatim, not truncated)
- Agent response summary
- Files created or modified
- Tests run or created
- Outcome and evaluation

**Rationale**: PHRs create an audit trail of all agent interactions, enabling retrospective analysis, debugging, and continuous improvement of agent prompts.

### Architecture Decision Records (ADR)

**Rule**: Agents MUST suggest creating an ADR when they detect an architecturally significant decision during planning or task generation.

**Significance Test** (all must be true):
- **Impact**: Long-term consequences (framework choice, data model, API design, security model, platform choice)
- **Alternatives**: Multiple viable options were considered
- **Scope**: Cross-cutting, influences overall system design

**Suggestion Format**:
```
📋 Architectural decision detected: [brief description]
   Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
```

**User Action**: User MUST explicitly run `/sp.adr` command; agents MUST NOT auto-create ADRs.

**ADR Location**: `history/adr/<id>-<slug>.md`

**Rationale**: ADRs capture the "why" behind key architectural choices, preventing future confusion, enabling informed refactoring, and preserving institutional knowledge.

### Commit & PR Standards

**Commit Messages**:
- Use conventional commit format: `<type>(<scope>): <description>`
- Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`
- Reference task IDs in commit body

**Pull Requests**:
- Title: Brief description of feature or fix
- Body: Link to specification, list of completed tasks, test plan
- All PRs MUST pass CI checks before merge
- PRs MUST be reviewed by human before merge

## Agent Behavior Contract

### What Agents MUST Do

1. **Follow specifications exactly**: Implement only what is specified, no more, no less
2. **Ask for clarification**: When requirements are ambiguous, ask targeted questions
3. **Create PHRs**: Document every significant user interaction
4. **Suggest ADRs**: Identify architecturally significant decisions and suggest documentation
5. **Respect phase boundaries**: Never implement features from future phases
6. **Execute in order**: Follow the Constitution → Spec → Plan → Tasks → Implement workflow
7. **Validate continuously**: Check work against specs and tasks at each step

### What Agents MUST NOT Do

1. **Invent features**: No unsolicited additions beyond the specification
2. **Skip steps**: No jumping directly to code without specs and tasks
3. **Manual refactoring**: No refactoring outside task scope
4. **Cross-phase contamination**: No future-phase features in current phase
5. **Auto-create ADRs**: Always wait for user consent before creating ADRs
6. **Ignore failures**: Never proceed if tests fail or tasks cannot be completed
7. **Modify specs directly**: Propose changes, do not make them unilaterally

### Human as Tool Strategy

Agents MUST invoke human input when:
- Requirements are unclear or ambiguous
- Multiple valid architectural approaches exist with significant tradeoffs
- Unforeseen dependencies block progress
- Major milestones are reached (phase completion, all tasks done)

Humans are the ultimate decision-makers for scope, priorities, and architecture. Agents are execution engines, not product managers.

## Governance

### Constitutional Authority

This constitution is the **supreme governing document** for all agents operating on the Evolution of Todo project. No specification, plan, or task may contradict the principles defined herein.

### Amendment Process

**Who Can Propose**: Any team member (human or agent) may propose an amendment.

**Amendment Requirements**:
1. Proposed change documented with rationale
2. Impact analysis on existing specs, plans, and code
3. Team review and approval
4. Version bump according to semantic versioning:
   - **MAJOR**: Backward-incompatible governance changes, principle removals or redefinitions
   - **MINOR**: New principles added, materially expanded guidance
   - **PATCH**: Clarifications, wording improvements, typo fixes
5. Update of dependent templates and documentation
6. Migration plan for in-flight work affected by amendment

**Approval Authority**: Project lead or designated constitutional reviewer.

### Compliance Review

**Frequency**: Constitution compliance MUST be verified at every PR review.

**Reviewers MUST Check**:
- Code traceable to approved specs and tasks
- No feature invention
- Phase boundaries respected
- Technology standards followed
- PHRs created for significant interactions
- ADRs created for architectural decisions

**Violations**: Non-compliant PRs MUST be rejected with explanation. Repeated violations require specification or constitutional clarification.

### Conflict Resolution

**Precedence Order** (highest to lowest):
1. This constitution
2. Approved specifications
3. Approved implementation plans
4. Generated tasks
5. Agent judgment

When conflicts arise, the higher-precedence document governs. Conflicts within the same tier require human arbitration.

---

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
