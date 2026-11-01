
# GitHub Copilot Instructions

## 1. Project Context

This repository is an AI-assisted Quality Engineering automation framework.

Technology scope:

- Web UI automation: Playwright and TypeScript.
- API automation: Playwright APIRequestContext and TypeScript.
- Native mobile automation: Appium 3 and TypeScript (future implementation).

The framework combines:

- Software Testing Life Cycle (STLC).
- Software Development Life Cycle (SDLC).
- Risk-based testing.
- AI-assisted automation development.
- Independent Maker–Checker reviews.
- Continuous quality improvement.

## 2. Shared Engineering Contract

Follow the engineering principles and lifecycle defined in the repository's `AGENTS.md`.

Key principles:

- Understand requirements before implementing automation.
- Define clear, measurable acceptance criteria.
- Prioritise risk-based test coverage.
- Treat automation as production-quality software.
- Prefer simple, explicit and maintainable solutions.
- Follow existing architecture and conventions.
- Use strict TypeScript typing.
- Avoid unnecessary abstractions and dependencies.
- Never weaken assertions or remove coverage just to obtain passing tests.
- Never fabricate validation results.

## 3. Repository Architecture

Respect the following boundaries:

- `src/web/`: Web UI abstractions.
- `src/api/`: API clients and models.
- `src/shared/`: Reusable configuration, data and utilities.
- `src/fixtures/`: Shared Playwright fixtures.
- `tests/web/`: Web UI tests.
- `tests/api/`: API tests.
- `mobile/`: Future independent Appium implementation.

Keep web, API and mobile concerns separated.

## 4. Quality Engineering Workflow

Select the applicable activities for each task.

### Requirement Analysis

- Understand expected behaviour.
- Identify acceptance criteria.
- Identify ambiguities, risks and dependencies.

### Test Planning and Design

- Define test scope and priorities.
- Consider positive, negative, boundary and edge cases.
- Identify test data and environment requirements.
- Maintain requirement-to-test traceability where appropriate.

### Automation Development

- Inspect existing implementation before changing it.
- Reuse established patterns.
- Write independent, deterministic tests.
- Use meaningful assertions and reliable locators.
- Keep implementation maintainable.

### Verification

Run applicable tests, TypeScript checks, ESLint and regression checks.

Report actual results and disclose skipped checks.

### Independent Review

Evaluate the implementation against the original requirements and acceptance criteria.

Do not treat the Maker's self-review as independent verification.

Review outcomes:

- PASS: All mandatory criteria are satisfied.
- FAIL: Actionable findings require correction.
- BLOCKED: Verification cannot be completed.

### Closure

Report implementation changes, validation evidence, review outcome and outstanding risks.

## 5. Maker–Checker Principles

For meaningful implementation tasks:

**Maker responsibilities:**
- Analyse the task.
- Define the implementation approach.
- Implement the agreed scope.
- Execute applicable validation.
- Report changes and results.

**Checker responsibilities:**
- Independently inspect the changed implementation.
- Verify acceptance criteria.
- Assess coverage and assertion quality.
- Review architecture, maintainability and reliability.
- Identify security and data-handling issues.
- Provide specific findings and a PASS, FAIL or BLOCKED outcome.

Re-review changes after corrections.

## 6. Definition of Done

A task is complete only when all applicable conditions are met:

- [ ] Agreed scope implemented.
- [ ] Acceptance criteria addressed.
- [ ] Relevant risks considered.
- [ ] Tests and assertions provide meaningful validation.
- [ ] Architecture and coding standards followed.
- [ ] Applicable automated checks executed.
- [ ] No secrets or sensitive data introduced.
- [ ] Final diff reviewed.
- [ ] Independent Checker returns PASS when required.
- [ ] Limitations and outstanding risks disclosed.

## 7. Security and Change Boundaries

- Never hardcode secrets or credentials.
- Never commit `.env` files or authentication state.
- Do not perform destructive actions without explicit approval.
- Do not access production systems without authorisation.
- Do not install dependencies without a clear reason.
- Do not modify unrelated files.
- Do not commit, push or deploy without explicit user approval.

## 8. Continuous Improvement

When recurring issues are identified, recommend improvements to shared instructions, testing standards, skills or architecture.

Avoid creating duplicate rules or unnecessary process overhead.

The objective is reliable, maintainable automation and meaningful quality assurance—not simply passing test executions.
