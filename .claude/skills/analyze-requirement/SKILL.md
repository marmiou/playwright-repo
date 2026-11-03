---
name: analyze-requirement
description: Analyses product requirements, user stories, acceptance criteria, defects and feature requests for clarity, completeness, consistency, testability, dependencies and quality risks. Use before test strategy, test design or implementation when expected behaviour needs to be understood or assessed.
---

# Requirement Analysis

## Purpose

Establish whether a requirement is sufficiently understood, clear, complete, consistent and testable before dependent implementation or verification begins.

Act as a Senior Quality Engineer analysing requirements from product-quality and technical perspectives. Prevent ambiguity, missing business rules and unverified assumptions from entering test design and automation.

This skill produces a structured requirement analysis. It does not implement automation or approve product requirements.

## Governing Documentation

Read and apply:
- `AGENTS.md`
- `CLAUDE.md`
- `docs/quality-engineering/workflows/requirements-analysis.md`
- `docs/quality-engineering/governance/requirements-integrity-and-product-ownership.md`
- `docs/quality-engineering/foundations/quality-engineering-principles.md`
- `docs/quality-engineering/ai/ai-agent-governance.md`
- `docs/quality-engineering/ai/ai-assisted-quality-engineering.md`

When relevant, also consult:
- `docs/architecture/overview.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/engineering-practices/test-automation-standards.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`

Verify that referenced paths exist. If a reference is missing, report it and use the closest authoritative source that actually exists; do not invent its contents.

## When to Use

Use for new features, stories, acceptance criteria, defects, behavioural changes, requirement ambiguity, testability assessment, regression-impact analysis, or when an agent needs to understand a task before test design or implementation.

## When Not to Use

A full analysis is usually unnecessary for formatting-only changes, documentation corrections, isolated non-behavioural refactoring, or clearly specified test-maintenance tasks. Perform a proportionate assessment and proceed to the relevant skill.

## Operating Rules

### 1. Identify authoritative sources

Gather available product requirements, stories, acceptance criteria, approved business rules, API specifications, UX designs, approved technical decisions, defect reports and authorised clarifications.

Identify each source and its approval status where possible.

Existing application behaviour, tests, comments, historical defects and AI interpretations may provide context, but are not authoritative product requirements by default.

### 2. Understand business context

Establish:
- What problem is being solved?
- Who is the intended user or system actor?
- What outcome is expected?
- Which capability or journey is affected?
- Which business rules apply?
- Which systems and integrations are involved?
- What existing behaviour could be affected?

Do not jump directly to test cases.

### 3. Separate explicit behaviour from inference

Classify important information as:
- Explicitly stated.
- Supported by an approved source.
- Inferred from context.
- Assumed but unconfirmed.
- Missing or contradictory.

Never turn an inference into an approved requirement. If implementation differs from an approved requirement, record the discrepancy rather than changing expected behaviour to match the implementation.

### 4. Assess requirement quality

| Dimension | Questions |
|---|---|
| Clarity | Is expected behaviour understandable and unambiguous? |
| Completeness | Are important conditions, outcomes and exceptions described? |
| Consistency | Does it conflict with another approved requirement? |
| Testability | Can success or failure be objectively observed? |
| Feasibility | Can Engineering assess a viable implementation? |
| Traceability | Can it be linked to a source and later verification? |
| Relevance | Does it address the intended user or business need? |

Use these classifications:
- **CLEAR:** sufficiently explicit and understandable.
- **PARTIAL:** important details are missing.
- **AMBIGUOUS:** multiple reasonable interpretations exist.
- **CONFLICTING:** authoritative sources disagree.
- **NOT TESTABLE:** expected outcomes cannot be objectively verified.
- **UNKNOWN:** insufficient information to assess.

These are analysis classifications, not product approval statuses.

## Analysis Workflow

### Phase 1 — Collect

Inspect the supplied requirement and relevant repository context.

For existing functionality:
1. Identify relevant implementation files.
2. Inspect nearby tests and conventions.
3. Inspect API contracts or models where available.
4. Review architecture and dependencies.
5. Identify relevant documentation.

Do not modify code during requirement analysis. Do not assume implementation represents intended behaviour.

### Phase 2 — Understand

Describe the requirement in plain language. Identify objective, intended actor, trigger, preconditions, main behaviour, inputs and outputs, state changes, postconditions, dependencies, constraints and expected outcome.

If information is unspecified, say so. Do not invent details.

### Phase 3 — Analyse

Assess relevant dimensions.

**Functional behaviour**
- Main success and alternative paths.
- Validation and business rules.
- State transitions and persistence.
- Error handling and recovery.
- Permissions and roles.
- Duplicate or repeated actions.
- Boundaries and edge conditions.

**Data**
- Required and optional fields.
- Valid and invalid values.
- Relationships and consistency.
- Data persistence, ownership and lifecycle.
- Privacy and sensitive information.

**Integrations**
- Upstream and downstream systems.
- API contracts, authentication and authorisation.
- Dependency availability, timeouts and failures.
- Retries, idempotency and eventual consistency.
- Partial failures.

**Non-functional quality**

Consider relevant ISO/IEC 25010 characteristics: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability and portability.

Do not create non-functional acceptance criteria without an approved requirement or authorised decision. Identify material missing expectations.

**Regression impact**
Identify potentially affected functionality, shared components, services, integrations, journeys, data and compatibility.

### Phase 4 — Identify gaps and risks

For each significant gap, record:
- Identifier.
- Requirement or area affected.
- What is missing or unclear.
- Why it matters.
- Potential implementation or testing impact.
- Appropriate decision owner.
- Whether dependent work can proceed.

Consider business-critical behaviour, financial or transactional integrity, security, sensitive data, integration failures, data corruption or loss, availability, recovery, regression and state transitions.

Do not assign numerical risk scores unless the project defines a scoring model. Otherwise use qualitative priority:
- **Critical:** potential severe business, security, financial or data impact.
- **High:** significant user, business or system impact.
- **Medium:** material but limited impact.
- **Low:** limited impact or inconvenience.

Explain the reasoning behind significant classifications.

### Phase 5 — Assess testability

Check whether:
- Initial conditions can be established.
- Inputs and constraints are understood.
- Expected results are explicit and observable.
- Negative outcomes are defined.
- Boundaries are identifiable.
- Roles and permissions are defined.
- Dependencies are understood.
- Test data can be prepared safely.
- Expected results are independent of implementation details.

Do not design the full test suite at this stage. Decide whether the requirement is ready for strategy and test design.

### Phase 6 — Clarify

Prepare focused questions, prioritising those that affect:
1. Correct business behaviour.
2. Acceptance criteria.
3. Security or data integrity.
4. Integration contracts.
5. Important error and recovery behaviour.
6. Testability.

Ask one question at a time in interactive conversations unless several independent decisions are clearly more efficient together. Do not ask questions answered by authoritative documentation.

For each question, briefly explain why the answer matters and identify the likely owner:
- Product Owner / authorised business representative.
- Engineering / technical owner.
- Security or privacy owner.
- API or integration owner.
- Operations / infrastructure owner.

QA may recommend options but must not select an unapproved business outcome.

### Phase 7 — Determine readiness

Choose one outcome:

**READY** — Requirements provide a sufficient basis for the next QE activity. Minor non-blocking details may remain if they do not affect expected behaviour or correctness.

**READY WITH OPEN QUESTIONS** — Main behaviour is sufficiently clear, but questions remain. State which activities may proceed and which depend on resolution.

**BLOCKED** — Essential expected behaviour is missing, ambiguous or conflicting. Dependent test design or implementation must not proceed until an authorised decision is available.

Do not use READY merely because a plausible implementation can be imagined.

### Phase 8 — Report

Produce a Requirement Analysis Report using this structure.

## Requirement Analysis Report

### 1. Requirement Summary
- **Title:**
- **Objective:**
- **Business / user outcome:**
- **Affected capability:**
- **Requirement source:**
- **Approval status:**

### 2. Scope
**In scope:** explicitly included behaviour.

**Out of scope:** explicitly excluded behaviour.

**Unknown scope:** areas not sufficiently specified.

### 3. Expected Behaviour
Summarise only behaviour supported by authoritative sources. Distinguish explicit requirements from interpretations.

### 4. Requirement Quality Assessment

| Dimension | Status | Findings |
|---|---|---|
| Clarity | | |
| Completeness | | |
| Consistency | | |
| Testability | | |
| Feasibility | | |
| Traceability | | |
| Relevance | | |

### 5. Gaps and Clarification Questions

| ID | Gap / question | Impact | Owner | Blocking? |
|---|---|---|---|---|

If none are identified, state that explicitly.

### 6. Quality Risks

| ID | Risk | Impact | Priority | Reason |
|---|---|---|---|---|

Include only relevant risks.

### 7. Dependencies and Constraints
Identify relevant systems, services, roles, data, environments and technical constraints.

### 8. Regression Considerations
Identify potentially affected existing functionality.

### 9. Assumptions and Unknowns
Separate unconfirmed assumptions from confirmed facts. Identify assumptions requiring approval.

### 10. Recommended Next Steps
Recommend test strategy, test design, clarification, technical investigation, requirement revision or blocking pending an authorised decision.

### 11. Readiness Decision
**Outcome:** READY / READY WITH OPEN QUESTIONS / BLOCKED

Explain the decision and its limitations.

## Stop Conditions

Stop dependent work when:
- Approved requirements conflict.
- Essential expected business behaviour is missing.
- Acceptance criteria cannot be objectively interpreted.
- A security or privacy decision requires an authorised owner.
- Destructive or irreversible behaviour is undefined.
- The task requires an unauthorised product decision.

Report the issue and request clarification. Do not continue by inventing expected results.

## Common Rationalisations

| Rationalisation | Correct response |
|---|---|
| "The developer knows what it should do." | Implementation knowledge does not replace approved requirements. |
| "This is how the application already works." | Existing behaviour is evidence, not automatically the source of truth. |
| "QA can decide expected behaviour." | Product decisions belong to the authorised owner. |
| "We can assume the normal case." | Label assumptions and establish whether they are safe and authorised. |
| "We can add negative cases later." | Identify missing error and boundary behaviour during analysis. |
| "The acceptance criteria are good enough." | Assess clarity, completeness and testability. |
| "AI can infer the missing rule." | AI may suggest possibilities but cannot approve business behaviour. |
| "Let's code and clarify afterwards." | Block dependent implementation when ambiguity affects correctness. |

## Anti-Patterns

Never:
- Generate test cases before understanding expected behaviour.
- Convert assumptions into acceptance criteria.
- Use application behaviour as the sole authority for expected results.
- Resolve conflicting requirements without approval.
- Invent API status codes, response contracts, validation rules or error messages.
- Assume roles and permissions.
- Introduce numerical risk scores without an agreed model.
- Treat missing information as low risk by default.
- Claim requirements are approved without approval evidence.

## Exit Criteria

Analysis is complete when relevant sources are identified; business context and intended behaviour are understood; requirement quality is assessed; significant gaps and conflicts are recorded; dependencies and risks are visible; testability and readiness are assessed; and the next activity is clear.

This skill does not approve requirements or authorise implementation.

## Related Skills
- `qe-workflow`
- `design-test-strategy`
- `design-test-cases`
- `investigate-failure`

## Related Documentation
- `docs/quality-engineering/workflows/requirements-analysis.md`
- `docs/quality-engineering/governance/requirements-integrity-and-product-ownership.md`
- `docs/quality-engineering/foundations/quality-engineering-principles.md`
- `docs/quality-engineering/ai/ai-agent-governance.md`
- `docs/quality-engineering/ai/ai-assisted-quality-engineering.md`
