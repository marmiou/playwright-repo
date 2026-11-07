---
name: design-test-cases
description: Designs risk-based, traceable test scenarios and test cases from understood requirements and an agreed test strategy. Defines preconditions, data, actions, expected results, negative and boundary coverage, and automation suitability. Use before implementing or executing tests.
---

# Test Case Design

## Purpose

Convert approved, understood requirements and the test strategy into clear, independently verifiable test scenarios and cases.

Produce test designs that expose meaningful product risk, have observable expected results, and can be executed manually or automated at the appropriate layer.

This skill designs tests. It does not approve product behaviour, create a test strategy from scratch, or implement automation.

## Governing Documentation

Follow:
- `AGENTS.md`
- `CLAUDE.md`
- `docs/quality-engineering/workflows/test-design.md`
- `docs/quality-engineering/foundations/quality-engineering-principles.md`
- `docs/quality-engineering/governance/requirements-integrity-and-product-ownership.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`
- `docs/quality-engineering/engineering-practices/test-automation-standards.md`
- `docs/architecture/overview.md`

Also consult the relevant Requirement Analysis Report and Test Strategy Report. Verify referenced paths exist.

## Entry Criteria

Before detailed design:
- Expected behaviour is sufficiently understood.
- Blocking requirement questions are resolved.
- Relevant risks and coverage priorities are known, or the task is small enough for proportionate design.
- Relevant system and data context is available.

If the requirement is blocked, do not invent expected outcomes. Record provisional scenarios only where their expected results are already authoritative.

## When to Use

Use when preparing manual or automated coverage for a feature, defect, API, user journey, regression area or acceptance criterion.

## When Not to Use

Do not create a large formal catalogue for a trivial change. Design only the cases needed to prove the relevant behaviour and risk.

## Design Principles

1. Every case has a clear purpose and traceable requirement or risk.
2. Expected results describe externally observable behaviour, not implementation assumptions.
3. Prefer a small set of high-value cases over redundant permutations.
4. Cover positive, negative, boundary, state and failure behaviour according to risk.
5. Use equivalence partitioning, boundary value analysis, decision tables and state-transition techniques where appropriate.
6. Keep cases independent, repeatable and diagnosable.
7. Separate test data from test logic where appropriate.
8. Select automation candidates based on stability, value and suitable test layer.
9. Avoid asserting incidental details that are not part of the contract.
10. Identify gaps instead of silently fabricating expected behaviour.

## Workflow

### Phase 1 — Establish traceability

Identify:
- Requirement / story / acceptance criterion.
- Risk from the strategy.
- User journey, API operation or system behaviour.
- Relevant priority and quality gate.

Assign stable identifiers in the output, such as `TC-001`, for the scope of the design. Do not imply these are persisted in an external test management system unless they are.

### Phase 2 — Identify behaviours and conditions

Break the requirement into distinct behaviours:
- Preconditions and initial state.
- Actors, roles and permissions.
- Inputs and validation rules.
- Main and alternate flows.
- State transitions and persistence.
- Outputs and side effects.
- Errors and recovery.
- Integration interactions.
- Relevant non-functional expectations.

Separate independent behaviours so a failure can be diagnosed clearly.

### Phase 3 — Select design techniques

Use techniques that fit the behaviour.

**Equivalence partitioning**
Group inputs or states expected to behave equivalently. Include representative values from valid and invalid partitions.

**Boundary value analysis**
Test values at, immediately below and immediately above meaningful boundaries where applicable.

**Decision tables**
Use for combinations of business rules, conditions, permissions or outcomes. Avoid exhaustive combinations when risk-based pairwise or representative coverage is more appropriate.

**State-transition testing**
Cover valid transitions, invalid transitions, repeated actions, terminal states and recovery where relevant.

**Error guessing / exploratory ideas**
Use domain knowledge and past failure patterns to identify likely weaknesses, but label these as risk-based ideas rather than specified behaviour.

Do not apply techniques mechanically. Explain why a case is valuable.

### Phase 4 — Design scenario coverage

Consider the following categories where relevant:

- Primary success path.
- Alternate and optional paths.
- Required-field and input validation.
- Invalid, malformed, missing and out-of-range data.
- Boundary conditions.
- Authentication and authorisation.
- Role and ownership restrictions.
- State transitions and persistence.
- Duplicate submissions and idempotency.
- Integration success, timeout, unavailable dependency and partial failure.
- Retry and recovery.
- Concurrency and ordering.
- Data isolation and cleanup.
- Regression of related journeys.
- Accessibility, compatibility, performance or security cases when included in scope.

Do not force irrelevant categories into every feature.

### Phase 5 — Define expected results

For every case, state:
- What must be observed.
- At which system boundary it is observed.
- What data or state should exist before and after.
- Which contract, requirement or rule supports the expectation.

Expected results must be specific enough for an independent tester to decide pass or fail.

Avoid:
- "Works as expected."
- "Displays correctly."
- "Returns an error."
- "The API is successful."

Prefer observable outcomes such as a defined response contract, permitted state transition, visible validation message where specified, unchanged persisted state, or absence of an unauthorised side effect.

If the exact message, status code, sorting order or other detail is not specified, do not invent it. Mark it as a clarification.

### Phase 6 — Define test data and isolation

For each case, specify only the data needed to execute and verify it:
- Entity state and relationships.
- User role and permissions.
- Valid / invalid / boundary values.
- Unique identifiers.
- Existing versus newly created records.
- Cleanup and reset expectations.

Follow test-data governance:
- Prefer synthetic or explicitly approved test data.
- Do not expose production personal data or secrets.
- Avoid shared mutable state in parallel tests.
- Ensure repeatable setup and cleanup.
- Do not hardcode credentials or sensitive values.

### Phase 7 — Decide automation suitability

For each candidate, recommend:
- Manual / exploratory.
- API automation.
- Web UI automation.
- Component or unit-level coverage owned by the appropriate engineering layer.
- Deferred automation, with rationale.

Consider repeatability, business criticality, frequency, stability, execution cost, diagnostic quality and whether the behaviour has a reliable oracle.

For this repository:
- Browser automation uses the existing Playwright web architecture under `tests/web`.
- API automation uses the existing API architecture under `tests/api`.
- Shared code belongs in the established `src` boundaries.
- Follow existing fixtures, configuration, naming, assertion and reporting conventions.
- Do not create a new framework abstraction before inspecting existing code.
- Do not put API setup in UI page objects or browser interactions in API clients.
- Mobile automation is outside the current Playwright implementation scope.

### Phase 8 — Review completeness and independence

Check:
- Every in-scope acceptance criterion has meaningful coverage or a documented gap.
- Every critical/high risk has one or more appropriate verification activities.
- Positive and negative behaviour are represented where relevant.
- Expected results are explicit and supported.
- Cases are not redundant without reason.
- Cases can be executed independently or dependencies are explicit.
- Data setup and cleanup are defined.
- Automation candidates use an appropriate layer.
- Unspecified product decisions are raised rather than assumed.

## Test Design Output

Use this structure.

### 1. Design Context
- Feature / requirement:
- Requirement readiness:
- Strategy reference:
- Scope:
- Constraints:

### 2. Coverage Matrix

| Requirement / risk | Scenario IDs | Priority | Coverage status |
|---|---|---|---|

Use Covered / Partial / Not covered / Not applicable. Explain gaps.

### 3. Test Scenarios

| Scenario ID | Scenario | Requirement / risk | Priority | Test level |
|---|---|---|---|---|

### 4. Detailed Test Cases

For each case:

**TC-XXX — Title**
- **Objective:**
- **Requirement / risk:**
- **Priority:**
- **Test level / type:**
- **Automation suitability:**
- **Preconditions:**
- **Test data:**
- **Steps:**
  1. ...
  2. ...
- **Expected results:**
  1. ...
  2. ...
- **Cleanup:**
- **Notes / dependencies:**

Use concise steps. A case should verify one coherent behaviour, not bundle unrelated checks.

### 5. Negative and Boundary Coverage
Summarise relevant partitions, boundaries, invalid conditions and error paths. State why any are excluded.

### 6. Data and Environment
Describe setup, isolation, environment dependencies and cleanup.

### 7. Automation Recommendations
Identify cases suitable for API or web automation and explain layer choice. Flag manual or exploratory coverage.

### 8. Gaps and Clarifications
List undefined expected outcomes, missing rules, and uncovered risks with owners. Do not fabricate answers.

### 9. Design Readiness
State READY / READY WITH OPEN QUESTIONS / BLOCKED and explain what can proceed.

## Stop Conditions

Stop detailed design for affected behaviour when:
- Expected outcomes are ambiguous or conflicting.
- Acceptance criteria lack an observable result.
- A test requires an unapproved business decision.
- Test data would require unsafe or unauthorised access.
- The system boundary or contract is unknown and materially changes the expected result.

Continue with independent, unaffected cases where safe, and clearly mark the blocked scope.

## Common Rationalisations

| Rationalisation | Required response |
|---|---|
| "One happy-path test is enough." | Cover material risks and meaningful alternatives. |
| "Let's test every possible combination." | Use risk-based partitions and combinatorial techniques. |
| "The status is probably 400." | Verify the contract; do not guess. |
| "We can assert the current UI text." | Confirm it is specified or approved. |
| "We don't need cleanup." | Ensure cases are repeatable and isolated. |
| "We can put everything in one test." | Keep independent behaviours diagnosable. |
| "Automation will decide expected behaviour." | Expected results must come from requirements and contracts. |
| "All cases should be automated." | Choose the layer and execution mode based on value and reliability. |

## Anti-Patterns

Never:
- Create test cases from inferred product behaviour without labelling the assumption.
- Use vague expected results.
- Design only happy paths for risk-bearing functionality.
- Duplicate tests just to increase test count.
- Couple API tests to browser page objects or vice versa.
- Depend on execution order without documenting the dependency.
- Share mutable test data across parallel tests without isolation.
- Include secrets or real personal data.
- Claim complete traceability when gaps remain.

## Exit Criteria

The design is traceable, risk-aligned, specific, independently executable, and includes expected results and data needs. Automation suitability is identified, coverage gaps are visible, and no unapproved product behaviour has been invented.

## Related Skills
- `qe-workflow`
- `analyze-requirement`
- `design-test-strategy`
- `add-web-test`
- `add-api-test`
- `verify-implementation`

## Related Documentation
- `docs/quality-engineering/workflows/test-design.md`
- `docs/quality-engineering/governance/requirements-integrity-and-product-ownership.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`
- `docs/quality-engineering/engineering-practices/test-automation-standards.md`
- `docs/architecture/overview.md`
