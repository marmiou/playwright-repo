# Test Automation Framework — Architecture Overview

## 1. Purpose

This document describes the architecture, structure and responsibilities of the automated testing framework.

The framework uses:

- **Playwright Test** for test automation and execution.
- **TypeScript** as the primary programming language.
- **Node.js** as the runtime environment.

It supports automated Web UI and API testing through a modular, maintainable and extensible architecture.

The architecture aims to provide:

- Clear separation of responsibilities.
- Reusable automation components.
- Independent Web UI and API testing layers.
- Centralised configuration.
- Test isolation and parallel execution.
- CI/CD integration.
- Compatibility with AI-assisted engineering workflows.

Detailed engineering practices and Quality Engineering principles are documented separately.

## 2. Architectural Principles

### Separation of Concerns

Each layer has a clear responsibility. Tests express scenarios and expected outcomes, while automation components encapsulate reusable technical interactions.

### Modularity and Reusability

Components should be focused and independently maintainable. Shared functionality should be introduced when it provides a genuine maintenance or consistency benefit.

Avoid unnecessary abstractions and premature generalisation.

### Explicit Dependencies

Dependencies should be clear and controlled. Avoid circular references, hidden dependencies and unnecessary coupling.

### Extensibility

The architecture should support additional test scenarios, application pages, API clients, environments, execution projects and diagnostic capabilities without requiring unrelated structural changes.

### Configuration Separation

Environment-specific values and execution settings must remain separate from test implementation. Secrets must be handled through approved secret management mechanisms.

## 3. High-Level Architecture

The framework is organised into the following logical layers:

```text
                  ┌───────────────────────────┐
                  │           Tests           │
                  │                           │
                  │        Web UI | API       │
                  └─────────────┬─────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │          Fixtures         │
                  │                           │
                  │  Setup | Context | Cleanup│
                  └─────────────┬─────────────┘
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
    ┌─────────▼──────────┐             ┌──────────▼─────────┐
    │     Web UI Layer   │             │      API Layer     │
    │                    │             │                    │
    │ Pages              │             │ Clients            │
    │ Components         │             │ Models             │
    └─────────┬──────────┘             └──────────┬─────────┘
              │                                   │
              └─────────────────┬─────────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │        Shared Layer      │
                  │                           │
                  │ Config | Data | Utilities│
                  └───────────────────────────┘
```

The diagram represents logical responsibilities, not mandatory runtime call sequences. Tests may use fixtures and automation interfaces as appropriate. Fixtures manage dependencies and lifecycle rather than acting as a mandatory execution layer.

## 4. Project Structure

The framework follows a responsibility-based directory structure.

```text
.
├── .claude/
│   ├── agents/
│   ├── rules/
│   └── skills/
│
├── .github/
│   ├── agents/
│   ├── instructions/
│   └── workflows/
│
├── docs/
│   ├── architecture/
│   │   ├── decisions/
│   │   ├── overview.md
│   │   └── test-execution.md
│   │
│   └── quality-engineering/
│       ├── ai/
│       ├── engineering-practices/
│       ├── foundations/
│       ├── governance/
│       ├── lifecycle/
│       ├── references/
│       └── workflows/
│
├── src/
│   ├── api/
│   │   ├── clients/
│   │   └── models/
│   ├── fixtures/
│   ├── shared/
│   │   ├── config/
│   │   ├── data/
│   │   └── utils/
│   └── web/
│       ├── components/
│       └── pages/
│
├── tests/
│   ├── api/
│   └── web/
│
├── AGENTS.md
├── CLAUDE.md
├── playwright.config.ts
├── package.json
├── tsconfig.json
└── yarn.lock
```

The structure describes the intended logical organisation. Additional directories may be introduced when justified by actual framework requirements.

## 5. Architectural Components

### 5.1 Tests Layer

**Location:** `tests/web/` and `tests/api/`

Contains executable test scenarios.

Responsibilities:

- Define the behaviour being verified.
- Establish preconditions using appropriate setup mechanisms.
- Perform relevant actions.
- Assert expected outcomes.
- Maintain traceability to requirements where supported.

Tests should express verification intent rather than duplicate reusable technical implementation.

Web UI and API tests remain logically separated.

### 5.2 Fixtures Layer

**Location:** `src/fixtures/`

Manages reusable test dependencies and lifecycle operations.

Responsibilities may include:

- Browser and page setup.
- Authenticated and unauthenticated contexts.
- API request contexts.
- Shared test dependencies.
- Resource initialisation and cleanup.
- Dependency injection into tests.

Fixtures should remain focused on setup and lifecycle management rather than business assertions.

### 5.3 Web UI Layer

**Location:** `src/web/`

Encapsulates Web UI interactions.

**Pages (`src/web/pages/`)**

Page objects represent application pages or meaningful page-level areas. They encapsulate page-specific locators and expose meaningful actions and information.

**Components (`src/web/components/`)**

Components represent reusable UI elements or sections, such as navigation bars, dialogs, menus, tables and forms.

Introduce abstractions when they improve reuse or maintainability. Avoid unnecessary layers for individual UI elements.

### 5.4 API Layer

**Location:** `src/api/`

Encapsulates API communication and related data structures.

**Clients (`src/api/clients/`)**

Provide reusable API operations, request construction and response access.

**Models (`src/api/models/`)**

Define request interfaces, response interfaces and relevant domain data structures.

Models should reflect the actual API contracts.

API clients must remain independent of Web UI implementation and test scenario assertions.

### 5.5 Shared Layer

**Location:** `src/shared/`

Contains functionality genuinely shared across architectural boundaries.

- **Config:** Environment configuration, base URLs and framework settings.
- **Data:** Data factories, synthetic data generators and reusable reference data.
- **Utils:** Small, focused technical utilities.

Shared functionality should avoid application-specific coupling, hidden side effects and unrelated responsibilities.

Test data ownership, isolation and cleanup are defined in `../quality-engineering/engineering-practices/test-data-management.md`.

### 5.6 Configuration and Execution

The root Playwright configuration and supporting execution files control test discovery, browser projects, environment selection, parallelism, retries, reporting and diagnostics.

Detailed execution responsibilities are defined in `test-execution.md`.

## 6. Web UI and API Separation

Web UI and API automation are separate architectural concerns.

They may share approved configuration, data definitions, utilities and fixtures where appropriate.

The following boundaries must be maintained:

- API clients must not depend on page objects.
- Page objects must not become API client implementations.
- Tests should use the appropriate layer for the behaviour being verified.
- Shared code must not introduce unnecessary coupling.
- API setup may support UI scenarios when it does not bypass the behaviour under test.

Tests may compose multiple layers when a scenario requires it.

## 7. Dependency Direction

Dependencies should follow controlled and predictable relationships.

The intended logical direction is:

```text
             Tests
               │
       ┌───────┴────────┐
       ▼                ▼
    Fixtures       Automation Interfaces
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              Web UI        API
                 │           │
                 └─────┬─────┘
                       ▼
                    Shared
```

The shared layer must not depend on test scenarios or application-specific automation implementations.

Avoid circular dependencies between Web UI, API and shared components.

Fixtures provide lifecycle management and dependency setup. They do not require every test interaction to pass through them.

## 8. Architecture and AI-Assisted Engineering

AI agents and coding assistants may contribute to framework development and maintenance.

They must operate within established architectural boundaries and repository instructions.

AI-assisted changes should:

- Reuse existing components where appropriate.
- Respect layer responsibilities and dependency direction.
- Follow approved TypeScript and Playwright standards.
- Preserve requirements and expected behaviour.
- Avoid unnecessary abstractions and unsupported dependencies.
- Verify changes through applicable checks.
- Request clarification when architectural requirements are incomplete.

Significant architectural changes require justification and review. AI agents must not independently redefine architectural responsibilities or governing rules.

## 9. Architectural Decisions

Significant architectural decisions should be documented as Architecture Decision Records (ADRs).

Examples include:

- Introducing a new architectural layer.
- Changing dependency direction.
- Introducing a new framework dependency.
- Changing Web UI and API separation.
- Introducing a new configuration mechanism.
- Changing fixture ownership or lifecycle.
- Changing execution or reporting architecture.

ADRs should capture:

- Context and problem.
- Decision.
- Alternatives considered.
- Consequences and trade-offs.
- Relevant constraints.

Store decision records under:

`docs/architecture/decisions/`

Avoid creating ADRs for routine implementation details.

## 10. Related Documents

- `test-execution.md` — Playwright execution, configuration and CI/CD.
- `../quality-engineering/foundations/quality-engineering-principles.md` — Quality Engineering principles.
- `../quality-engineering/lifecycle/agile-quality-engineering.md` — Agile QE operating model.
- `../quality-engineering/lifecycle/requirements-engineering.md` — Requirements analysis and ownership.
- `../quality-engineering/lifecycle/test-strategy-and-design.md` — Test strategy and design.
- `../quality-engineering/engineering-practices/test-automation-standards.md` — Playwright and TypeScript implementation standards.
- `../quality-engineering/engineering-practices/test-data-management.md` — Test data lifecycle and ownership.
- `../quality-engineering/engineering-practices/test-reliability.md` — Test reliability and diagnostics.
- `../quality-engineering/governance/maker-checker-and-independent-review.md` — Independent review governance.
- `../quality-engineering/ai/ai-agent-governance.md` — AI agent governance.
- `../../AGENTS.md` — Shared engineering instructions.
- `../../CLAUDE.md` — Claude Code instructions.

## 11. Governing Principle

The framework architecture must remain understandable, modular and maintainable.

Each component must have a clear responsibility, dependencies must be controlled, and shared functionality must be introduced intentionally.

**Architecture provides the structure. Quality Engineering principles guide how the structure is used.**
