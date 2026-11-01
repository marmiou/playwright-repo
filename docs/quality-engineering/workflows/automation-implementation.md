# Automation Implementation Workflow

## 1. Purpose

This workflow defines how approved test designs are translated into maintainable, reliable automated tests using Playwright and TypeScript.

It applies to:

- Web application tests.
- API tests.
- Regression automation.
- Integration and end-to-end verification.
- Changes to existing automated tests.

The objective is to produce meaningful, deterministic and maintainable automation that verifies approved requirements.

## 2. Entry Criteria

Before implementation begins, the following should be available:

- An identifiable approved requirement or acceptance criterion.
- A defined test scenario and expected result.
- Relevant test data requirements.
- Identified dependencies and environmental constraints.
- An agreed automation approach.

If expected behaviour is unclear, it must be clarified before dependent test implementation proceeds.

## 3. Implementation Workflow

**ANALYSE → PLAN → IMPLEMENT → VERIFY → REVIEW → COMPLETE**

### Step 1: ANALYSE

Understand the test design and its context.

Identify:

- The behaviour being verified.
- Preconditions and expected outcomes.
- Relevant test data and system state.
- Required web pages, components or API endpoints.
- Dependencies and integration boundaries.
- Potential failure and regression risks.
- Whether the scenario is suitable for automation.

Automation must verify the intended behaviour, not simply reproduce the current implementation.

### Step 2: PLAN

Determine the implementation approach.

Consider:

- Whether the test belongs in the web or API test suite.
- Existing fixtures, clients, models and shared utilities.
- Appropriate test isolation and data setup.
- Required authentication and configuration.
- Locator and interaction strategies for web tests.
- Request and response validation for API tests.
- Relevant cleanup and diagnostics.

Reuse existing abstractions where they provide genuine value. Avoid introducing unnecessary layers or duplicating existing functionality.

### Step 3: IMPLEMENT

Implement the automated test using Playwright and TypeScript.

#### General requirements

Tests MUST:

- Use clear, descriptive names.
- Verify observable behaviour and meaningful outcomes.
- Use explicit, relevant assertions.
- Remain independent and repeatable.
- Avoid hidden dependencies on execution order.
- Use controlled test data.
- Follow established fixtures and shared utilities.
- Avoid hardcoded secrets and environment-specific assumptions.
- Provide useful failure diagnostics.

#### Web automation

Web tests SHOULD:

- Use Playwright's recommended locator strategies.
- Prefer accessible roles, labels and other user-facing locators.
- Use web-first assertions and Playwright auto-waiting.
- Interact with the application through realistic user behaviour.
- Avoid unnecessary implementation-specific selectors.
- Use page objects or reusable components where they improve maintainability.
- Avoid arbitrary sleeps and fixed timing assumptions.

#### API automation

API tests SHOULD:

- Use Playwright's API testing capabilities.
- Reuse established API clients and request configuration where appropriate.
- Validate status codes, response bodies and relevant headers.
- Verify business behaviour and data integrity.
- Cover relevant validation and error responses.
- Consider authentication, authorisation and dependency behaviour.
- Avoid relying solely on successful HTTP status codes.
- Handle test data creation and cleanup appropriately.

### Step 4: VERIFY

Run the relevant checks using the repository's configured scripts and tooling.

Verification should include, as applicable:

- TypeScript type checking.
- ESLint validation.
- Relevant test execution.
- Regression checks.
- Configuration and test discovery validation.
- Review of test reports and failure diagnostics.

A test that compiles successfully is not necessarily a correct test.

A passing assertion must demonstrate the intended behaviour rather than merely confirm that the application responded.

Any failed or blocked verification must be reported accurately.

### Step 5: REVIEW

Review the implementation against the approved test design and repository standards.

Evaluate:

- Alignment with requirements and expected results.
- Correctness and completeness of assertions.
- Positive, negative and boundary coverage.
- Test independence and data isolation.
- Synchronisation and reliability.
- Reuse and maintainability.
- Error handling and diagnostics.
- Unnecessary complexity or duplication.
- Potential regressions.

Independent review must be performed when required by the change's risk and the Maker–Checker governance rules.

### Step 6: COMPLETE

Automation implementation is complete when:

- The approved scenario has been implemented.
- Relevant verification has passed.
- Assertions demonstrate the expected behaviour.
- Test data and dependencies are appropriately controlled.
- Review requirements have been satisfied.
- Known limitations and outstanding issues are documented.

A failed or blocked check must not be reported as PASS.

## 4. Handling Implementation Issues

During implementation, issues may reveal:

- Missing or ambiguous requirements.
- Incorrect or incomplete test designs.
- Application defects.
- API contract inconsistencies.
- Environment or dependency problems.
- Test data limitations.
- Framework or tooling limitations.

The issue must be classified and escalated to the appropriate owner.

The Maker must not silently change expected behaviour or weaken the test design to work around an implementation problem.

## 5. AI-Assisted Implementation

AI agents may assist with analysis, planning, code generation, refactoring and verification.

AI-generated automation MUST:

- Follow the approved test design.
- Follow repository instructions and coding standards.
- Reuse existing framework capabilities where appropriate.
- Preserve meaningful assertions.
- Avoid introducing arbitrary waits or indiscriminate retries.
- Report assumptions and unresolved questions.
- Provide accurate verification results.

AI-generated tests must be reviewed before acceptance. An agent must not approve its own work where independent review is required.

Relevant execution skills:

- `.claude/skills/add-web-test/SKILL.md`
- `.claude/skills/add-api-test/SKILL.md`
- `.claude/skills/review-tests/SKILL.md`

AI governance is defined in `../ai/ai-agent-governance.md`.

## 6. Related Guidance

- `../engineering-practices/test-automation-standards.md`
- `../engineering-practices/test-data-management.md`
- `../engineering-practices/test-reliability.md`
- `../lifecycle/test-strategy-and-design.md`
- `../governance/maker-checker-and-independent-review.md`
- `independent-review.md`
