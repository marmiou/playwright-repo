---
name: add-web-test
description: Analyse, design, implement, and verify Playwright web UI tests. Use when asked to add, automate, or improve browser-based tests.
---

# Add Web Test

## Objective

Create maintainable, reliable Playwright UI tests that validate meaningful
user behaviour and product requirements.

Follow the shared engineering standards in `AGENTS.md` and the
Quality Engineering lifecycle.

## Workflow

### 1. Understand the task

- Read `AGENTS.md` and relevant project instructions.
- Inspect the existing Playwright configuration, fixtures, tests,
  and related page objects or components.
- Understand the feature and expected behaviour before writing code.
- Identify missing requirements or ambiguities.
- Ask for clarification when essential information is missing.
- Do not invent expected behaviour.

### 2. Analyse quality and risk

Identify:

- The user journey or functionality being tested.
- Relevant business rules and acceptance criteria.
- Positive, negative, and boundary scenarios.
- Important dependencies and test data requirements.
- Potential failure points and regression risks.

Prioritise scenarios based on risk and business impact.

### 3. Design the test

Before implementation:

- Define the test scenarios and expected outcomes.
- Choose appropriate assertions.
- Identify reusable fixtures, page objects, and components.
- Prefer accessible locators and user-facing behaviour.
- Avoid unnecessary abstraction.
- Keep tests independent and deterministic.

Do not introduce a page object or abstraction unless it provides
a clear maintenance or reuse benefit.

### 4. Implement

- Follow the existing TypeScript and Playwright conventions.
- Keep test files under `tests/web/`.
- Put reusable web abstractions under `src/web/`.
- Put shared test fixtures under `src/fixtures/`.
- Use meaningful test and describe names.
- Use explicit assertions that validate the expected behaviour.
- Avoid arbitrary timeouts and hard-coded sleeps.
- Do not use `page.waitForTimeout()` as a substitute for proper
  synchronisation.
- Do not weaken assertions to make tests pass.
- Do not introduce unnecessary dependencies.

### 5. Verify

Run the relevant checks:

- Targeted Playwright test.
- TypeScript type checking.
- ESLint.

Investigate failures instead of assuming they are unrelated.

Do not report a check as successful unless it was actually executed.

### 6. Review

Review the implementation for:

- Requirement coverage.
- Assertion quality.
- Locator reliability.
- Test independence.
- Readability and maintainability.
- Unnecessary complexity.
- Compliance with project architecture.

If an independent reviewer agent is available, request a review.

Address valid findings before completing the task.

### 7. Report

Summarise:

- What was implemented.
- Which scenarios are covered.
- Files created or modified.
- Checks executed and their results.
- Known limitations or remaining questions.

## Constraints

- Do not modify Playwright configuration unless required.
- Do not modify unrelated tests or framework components.
- Do not add dependencies without explaining why.
- Do not change application behaviour.
- Do not claim coverage that has not been verified.
