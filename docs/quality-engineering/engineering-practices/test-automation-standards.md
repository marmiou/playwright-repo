# Test Automation Standards

## 1. Purpose

This document defines the engineering standards for automated testing within the QE framework.

The framework uses:

- **Playwright Test** for test execution and browser automation.
- **TypeScript** as its primary programming language.
- **Playwright APIRequestContext** for API testing.

These standards apply to human engineers and AI agents. Automation is software engineering: tests, fixtures, clients and utilities must be reliable, readable, maintainable and aligned with approved requirements.

## 2. Core Engineering Principles

Automation MUST:

- Validate approved requirements, acceptance criteria and documented contracts.
- Make test intent and expected outcomes clear.
- Keep responsibilities separated between tests, fixtures, page objects, components and API clients.
- Use abstractions where they provide genuine reuse or maintainability.
- Remain independently executable and safe for parallel execution where supported.
- Provide meaningful assertions and diagnostic information.

Automation MUST NOT:

- Invent or silently redefine expected behaviour.
- Weaken assertions or remove required scenarios to make tests pass.
- Hide failures or introduce unnecessary complexity.
- Depend on undocumented application behaviour as an approved requirement.

Missing or contradictory requirements MUST be raised with the Product Owner. Requirements ownership and integrity are defined in `../governance/requirements-integrity-and-product-ownership.md`.

## 3. TypeScript Standards

- Keep TypeScript strict mode enabled.
- Prefer explicit, meaningful types.
- Avoid `any` unless technically justified.
- Handle nullable and optional values explicitly.
- Avoid non-null assertions used merely to suppress compiler errors.
- Use consistent naming: `PascalCase` for types and classes; `camelCase` for variables and functions.
- Use `async`/`await` and handle asynchronous operations deliberately.
- Avoid unawaited operations that may outlive a test or fixture.
- Reuse types only when they represent the same underlying contract.

## 4. Playwright Test Standards

### 4.1 Test Structure

Use `@playwright/test` and its built-in capabilities for fixtures, assertions, isolation, projects, parallel execution, retries and diagnostics.

Structure tests around Arrange–Act–Assert where appropriate:

1. **Arrange:** Establish the required initial conditions.
2. **Act:** Perform the action under test.
3. **Assert:** Verify the expected outcome.

Test names MUST describe the behaviour being verified, not merely the feature or implementation.

### 4.2 Assertions

- Use Playwright's `expect` assertions.
- Prefer web-first assertions for UI behaviour.
- Verify meaningful outcomes, not just that an action was attempted.
- API tests SHOULD verify relevant status codes, response data, headers and business behaviour.
- Expected results MUST come from approved requirements or documented contracts.

### 4.3 Test Independence

Tests MUST NOT depend on execution order or state created by another test.

Use controlled setup, isolated data and appropriate fixtures. Avoid shared mutable state unless concurrency and ownership are explicitly managed.

See `test-data-management.md` for data isolation and cleanup requirements.

## 5. Web UI Automation

### 5.1 Locators

Prefer resilient, user-facing locators:

1. `getByRole()`
2. `getByLabel()`
3. `getByPlaceholder()`
4. `getByText()` when the text uniquely identifies the element.
5. `getByTestId()` when semantic locators are insufficient.

Use CSS or XPath only when necessary.

Avoid fragile selectors based on dynamic classes, generated IDs, DOM hierarchy or arbitrary positions.

Locators SHOULD identify the intended element unambiguously. Do not use `.first()`, `.last()` or `.nth()` to conceal ambiguity.

### 5.2 Page Objects and Components

Use page objects and components when they provide meaningful encapsulation.

- Tests express scenarios and verify outcomes.
- Page objects encapsulate page-level interactions.
- Components encapsulate reusable UI behaviour.
- Fixtures manage dependencies and resource lifecycles.

Avoid oversized page objects, unnecessary wrappers and hidden assertions. Direct Playwright interaction is acceptable when it is clearer.

### 5.3 Synchronisation and Interaction

Prefer Playwright's automatic waiting, locator actions and web-first assertions.

Wait for meaningful application conditions rather than arbitrary delays. Do not treat `networkidle` as a universal indication that an application is ready.

Avoid fixed sleeps and direct DOM manipulation unless the test has a specific reason to use them.

See `test-reliability.md` for synchronisation and reliability practices.

## 6. API Automation

API tests verify service behaviour independently of the UI.

They SHOULD cover relevant aspects of the documented contract, including:

- Status codes, response structure and data.
- Authentication and authorisation.
- Input validation and error handling.
- Business rules and persistence.
- Relevant boundary conditions and integration behaviour.

Use dedicated API clients for reusable request construction and common configuration. Keep scenario-specific business assertions in tests.

Use TypeScript models to describe API contracts, but remember that TypeScript types do not validate runtime responses. Apply runtime validation when required.

API setup MAY be used to establish test prerequisites, but MUST NOT bypass the behaviour being tested.

Credentials and secrets MUST NOT be hardcoded or exposed in logs and reports.

## 7. Fixtures and Resource Management

Use Playwright fixtures to manage dependencies and resource lifecycles, such as pages, API clients, authenticated contexts and test data helpers.

Fixtures MUST have clear responsibilities, predictable lifecycles and appropriate cleanup.

Choose fixture scope deliberately:

- Use test scope for mutable resources requiring isolation.
- Use worker scope only when sharing is safe and intentional.

Avoid hidden side effects, shared mutable state and opaque business workflows inside fixtures.

## 8. Architecture and Separation of Concerns

Keep Web UI and API automation logically separate.

The repository's architecture defines the authoritative directory structure and component boundaries.

As a general rule:

- `tests/web/` contains Web UI scenarios.
- `tests/api/` contains API scenarios.
- `src/web/` contains browser interaction abstractions.
- `src/api/` contains API clients and models.
- `src/shared/` contains genuinely layer-independent utilities.
- `src/fixtures/` contains Playwright fixtures.

Do not place API-specific logic in page objects or browser-specific logic in API clients.

Avoid duplicating shared functionality, but do not force unrelated responsibilities into common abstractions.

## 9. Configuration, Security and Diagnostics

- Externalise environment-specific configuration.
- Validate mandatory configuration before execution.
- Use approved secret management; never hardcode real credentials or tokens.
- Avoid exposing sensitive information in logs, traces, screenshots or reports.
- Handle errors explicitly; do not silently suppress failures or return misleading defaults.
- Preserve useful diagnostics for investigation, including relevant errors, traces and response context.

Execution configuration is defined in `docs/architecture/test-execution.md`. Failure investigation and reliability practices are defined in `test-reliability.md`.

## 10. Code Verification and AI Contributions

Automation changes MUST receive verification appropriate to their scope.

Applicable checks include:

- TypeScript type checking.
- Linting and formatting.
- Relevant automated tests.
- Regression checks for affected functionality.
- Configuration or build validation where applicable.

Use the repository's standard scripts. Report only checks that were actually executed and their real outcomes.

AI agents MUST follow the same engineering standards as human contributors. They MUST understand the relevant requirements, respect architecture boundaries, preserve meaningful assertions, use approved test data practices and report assumptions, changes and verification evidence.

Generated code is not considered correct merely because it compiles or executes. It remains subject to review and verification.

See `ai/ai-agent-governance.md` for agent controls and `workflows/independent-review.md` for the review process.

## 11. Related Documents

- `../foundations/quality-engineering-principles.md` — QE principles.
- `../governance/requirements-integrity-and-product-ownership.md` — Requirements authority.
- `../lifecycle/requirements-engineering.md` — Requirements lifecycle.
- `../lifecycle/test-strategy-and-design.md` — Test strategy and design.
- `test-data-management.md` — Test data isolation and cleanup.
- `test-reliability.md` — Reliability and diagnostics.
- `continuous-improvement.md` — Framework improvement.
- `../../architecture/overview.md` — Framework architecture.
- `../../architecture/test-execution.md` — Test execution configuration.

## Governing Principle

**Requirements define expected behaviour. Automation verifies that behaviour through reliable, maintainable and meaningful tests.**
