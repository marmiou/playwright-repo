---
name: design-test-strategy
description: Creates a risk-based test strategy for an understood feature, change or defect, defining test scope, levels, types, priorities, coverage, data, environments, dependencies and exit criteria. Use after requirement analysis when deciding how quality will be evaluated.
---

# Test Strategy Design

## Purpose

Translate understood requirements and product risks into a proportionate, actionable test strategy. Decide what should be tested, at which level, why, in what order, and what evidence is required.

This skill defines the testing approach. It does not create a detailed test-case catalogue or implement automation.

## Governing Documentation

Follow:
- `AGENTS.md`
- `CLAUDE.md`
- `docs/quality-engineering/foundations/quality-engineering-principles.md`
- `docs/quality-engineering/workflows/test-design.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/engineering-practices/test-automation-standards.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`
- `docs/quality-engineering/engineering-practices/test-reliability.md`
- `docs/architecture/overview.md`
- `docs/architecture/test-execution.md`

Consult requirements analysis and AI governance documents where relevant. Verify paths before use.

## Entry Criteria

Before creating a strategy:
- The requirement has been analysed using `analyze-requirement`, or the task is sufficiently clear for a proportionate assessment.
- Expected behaviour and known acceptance criteria are available.
- Blocking ambiguities are resolved or explicitly identified.
- Relevant product, architecture and integration context has been inspected.

If the requirement is BLOCKED, do not present a final strategy as ready. Identify what can be assessed provisionally and what requires clarification.

## When to Use

Use for features, significant changes, integration work, high-risk defects, cross-cutting changes, release readiness planning, or when test scope and priorities need to be agreed.

For a trivial, isolated change, use a concise strategy rather than a heavyweight document.

## Strategy Principles

1. Risk determines testing depth and priority.
2. Test at the lowest practical level that provides reliable evidence; use higher levels for integration and user-journey confidence.
3. Avoid duplicating the same assertion at multiple layers without a clear reason.
4. Prefer observable outcomes and independent oracles over implementation-coupled assertions.
5. Include negative, boundary, failure and recovery behaviour where relevant.
6. Consider security, privacy, accessibility, performance, compatibility and reliability according to product risk.
7. Automation is a means of repeatable feedback, not a substitute for exploratory testing or sound test design.
8. Make constraints, exclusions and residual risks explicit.
9. Do not promise coverage that cannot be demonstrated.
10. Product acceptance and release decisions remain with authorised owners.

## Workflow

### Phase 1 — Establish the baseline

Review:
- Requirement Analysis Report and acceptance criteria.
- User journeys and affected capabilities.
- Existing test coverage and known defects.
- Architecture, components, APIs and integrations.
- Data classification and data lifecycle.
- Deployment, configuration and environment constraints.
- Existing automation conventions and execution model.

Record source gaps and stale or unverified evidence.

### Phase 2 — Identify quality risks

Identify what could go wrong, the affected user or system, the consequence, and how the risk could be detected.

Consider:
- Core business outcomes and critical user journeys.
- Incorrect calculations, state changes or persistence.
- Authentication, authorisation and access boundaries.
- Invalid, malformed, missing or excessive input.
- API contracts, integration failures and partial success.
- Concurrency, retries, duplicate requests and idempotency.
- Data consistency, privacy, retention and isolation.
- Performance, availability, resilience and recovery.
- Browser/device compatibility and accessibility where relevant.
- Regression in shared components and dependent journeys.
- Observability and diagnosability.

Use qualitative priorities (Critical, High, Medium, Low) unless the project has an approved risk model. Explain why each important risk has its priority. Do not invent likelihood or impact scores.

### Phase 3 — Define scope

State:
- In-scope functionality and journeys.
- Out-of-scope functionality and rationale.
- Affected components, APIs and integrations.
- User roles and permission boundaries.
- Relevant data states and lifecycle.
- Regression areas.
- Constraints and assumptions.

Do not quietly exclude a risky area because it is difficult to automate.

### Phase 4 — Select test levels and types

Select only levels that add useful evidence.

| Level | Typical purpose | Examples |
|---|---|---|
| Unit / component | Isolated rules and transformations | Validation, calculations, mapping |
| API / service | Contracts, business logic and service behaviour | Status, schema, persistence, errors |
| Integration | Communication and consistency across boundaries | Service dependencies, events, databases |
| UI / end-to-end | Critical user-visible journeys | Navigation, workflows, rendered outcomes |
| Exploratory | Unscripted learning and unexpected behaviour | Usability, edge combinations, workflow gaps |

Consider relevant test types:
- Functional, regression, smoke and acceptance.
- Negative, boundary, equivalence and state-transition testing.
- Contract, integration and compatibility.
- Security and privacy.
- Accessibility and usability.
- Performance and resilience.
- Recovery and operational behaviour.

Do not prescribe UI automation for behaviour better and more reliably verified at API or component level.

### Phase 5 — Prioritise coverage

Organise coverage by risk and business importance:
- **P0 / Critical:** must be verified before the relevant quality gate can pass.
- **P1 / High:** required for meaningful release confidence.
- **P2 / Medium:** valuable coverage, scheduled according to capacity and risk.
- **P3 / Low:** lower-risk or opportunistic coverage.

These labels are prioritisation guidance, not an automatic release policy. Align actual gate decisions with repository quality-gate documentation and authorised release criteria.

Identify:
- Must-test scenarios.
- Regression selection.
- Automation candidates.
- Manual / exploratory activities.
- Deferred coverage and accepted residual risk.

### Phase 6 — Plan test data and environments

Define required:
- Data states, valid and invalid datasets.
- User roles and permission combinations.
- Unique identifiers and isolation strategy.
- Setup, teardown and cleanup.
- Synthetic or approved test data.
- Environment and service dependencies.
- Secrets and configuration handling.
- Reset, repeatability and parallel execution requirements.

Never place credentials, tokens, personal data or production secrets in tests, reports, fixtures or source control. Follow the test-data management policy.

### Phase 7 — Define automation approach

For each automation candidate, explain:
- What behaviour is automated.
- Why that layer is appropriate.
- The observable assertion or oracle.
- Required fixtures, clients, page objects or helpers.
- Data strategy and isolation.
- Expected execution frequency and feedback purpose.
- Known reliability or maintenance risks.

Respect the existing architecture:
- Web tests belong under `tests/web` and use the established web abstractions.
- API tests belong under `tests/api` and use established API abstractions.
- Shared reusable code belongs in the appropriate `src/shared`, `src/web`, `src/api` or fixture location according to responsibility.
- Do not introduce cross-layer coupling or duplicate framework infrastructure.
- Mobile automation is a separate future concern; do not mix it into the current Playwright implementation.

Inspect actual code before naming a specific helper or asserting that an abstraction exists.

### Phase 8 — Define evidence and exit criteria

Specify:
- Required test results and reports.
- Traceability from requirement/risk to test evidence.
- Required environments and configurations.
- What constitutes pass, fail, blocked or not run.
- Known limitations and residual risks.
- Required independent review.
- Who owns the final acceptance or release decision.

A passing automated suite alone does not establish product quality or authorise release.

### Phase 9 — Report the strategy

Use the template below. Keep it concise for small changes and expand only where risk warrants.

## Test Strategy Report

### 1. Context
- Feature / change:
- Requirement reference:
- Analysis readiness:
- Business objective:
- Affected users and systems:

### 2. Scope
- In scope:
- Out of scope:
- Constraints:
- Assumptions and unknowns:

### 3. Risk Assessment

| ID | Risk / failure mode | Impact | Priority | Detection / mitigation |
|---|---|---|---|---|

### 4. Test Approach

| Risk / requirement | Test level | Test type | Rationale | Priority |
|---|---|---|---|---|

### 5. Coverage Priorities
- P0 / Critical:
- P1 / High:
- P2 / Medium:
- P3 / Low:

### 6. Regression Scope
Identify affected existing capabilities and why they are included.

### 7. Test Data and Environment
Describe data, roles, dependencies, environment, configuration, isolation and cleanup.

### 8. Automation Approach
Describe automation candidates, layer selection, assertion strategy and relevant framework boundaries.

### 9. Execution and Evidence
Describe execution order, reports, traceability and evidence required.

### 10. Entry and Exit Criteria
State prerequisites and measurable completion criteria.

### 11. Residual Risks and Decisions
List deferred coverage, unresolved questions, accepted risks and decision owners.

### 12. Recommendation
State whether the approach is ready for detailed test design and identify next steps.

## Stop Conditions

Stop or mark the strategy provisional when:
- Requirement ambiguity changes the scope or expected result.
- Critical dependencies or system boundaries are unknown.
- Data or environment access is unsafe or unauthorised.
- The strategy would require an unapproved product or release decision.
- A critical risk has no viable verification or mitigation approach.

Escalate the gap; do not hide it in assumptions.

## Common Rationalisations

| Rationalisation | Required response |
|---|---|
| "We'll automate everything through the UI." | Select the lowest reliable layer for each behaviour. |
| "The happy path is enough." | Include risk-relevant negative, boundary and failure paths. |
| "We have lots of tests." | Assess whether they cover meaningful risks and have strong oracles. |
| "The test data is shared, but it usually works." | Define isolation and repeatability. |
| "Performance/security are out of scope by default." | Assess relevance and record explicit exclusions. |
| "The suite is green, so release is safe." | Report residual risk and leave release authority with its owner. |
| "We can skip regression analysis." | Inspect affected shared components and journeys. |

## Anti-Patterns

Never:
- Produce a list of test types without linking them to risks.
- Treat automation count as a quality metric.
- Duplicate assertions across layers without justification.
- Design tests around implementation details instead of behaviour.
- Ignore test data, environment or execution constraints.
- Claim full coverage without traceable evidence.
- Treat P0/P1 labels as a replacement for approved release policy.
- Accept residual risk on behalf of Product or Release owners.

## Exit Criteria

The strategy identifies relevant risks, scope, levels, types, priorities, regression, data, environment, automation approach, evidence and exit criteria. Open decisions and residual risks are visible, and detailed test design can proceed without inventing expected behaviour.

## Related Skills
- `qe-workflow`
- `analyze-requirement`
- `design-test-cases`
- `add-web-test`
- `add-api-test`
- `evaluate-quality`

## Related Documentation
- `docs/quality-engineering/workflows/test-design.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`
- `docs/quality-engineering/engineering-practices/test-reliability.md`
- `docs/architecture/overview.md`
- `docs/architecture/test-execution.md`
