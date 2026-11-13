---
name: review-tests
description: Performs an independent Maker–Checker review of test automation changes, test designs and QE implementation against requirements, risks, architecture, reliability, security and verification evidence. Use after implementation and verification when an independent quality assessment is required.
---

# Independent Test Review

## Purpose

Act as the independent Checker for a QE change. Assess whether the work is correct, meaningful, maintainable, risk-aligned and supported by evidence. Challenge the implementation rather than restating the maker's summary.

## Governing Documentation

Follow `AGENTS.md`, `CLAUDE.md`, `docs/quality-engineering/governance/maker-checker.md`, `docs/quality-engineering/workflows/independent-review.md`, `docs/quality-engineering/governance/quality-gates-and-readiness.md`, `docs/quality-engineering/engineering-practices/test-automation-standards.md`, `docs/quality-engineering/engineering-practices/test-reliability.md`, `docs/quality-engineering/ai/ai-agent-governance.md` and `docs/architecture/overview.md`. Verify paths before relying on them.

## Independence Requirements

- Review the actual diff and evidence, not only the maker's description.
- Do not assume the maker's reasoning is correct.
- Do not silently modify the implementation while reviewing it.
- If you authored the change in the same working context, do not claim this is an independent review. Request a separate reviewer/agent context or report that independent review remains outstanding.
- Do not approve a change merely because tests pass.
- Use the Test Reviewer agent when available and appropriate.

## Review Workflow

### 1. Understand the change

Collect the original task and approved expected behaviour, requirement analysis and test strategy where applicable, scenarios and risk priorities, changed files and surrounding implementation, verification commands and artifacts, known limitations and open questions. If required inputs are missing, state the limitation.

### 2. Requirement alignment

Check traceability to approved requirements or risks, authoritative expected outcomes, unapproved behaviour, acceptance criteria coverage, and visibility of assumptions and requirement gaps.

### 3. Test quality

Check correct test level, meaningful assertions and independent oracles, risk-appropriate positive/negative/boundary/failure coverage, redundancy, naming and diagnostic output, deterministic setup, isolation, cleanup, parallel safety, stable UI locators and synchronisation, API contract and side-effect assertions.

### 4. Architecture and maintainability

Check reuse of existing abstractions, separation of responsibilities, API/UI boundaries, justified abstractions and dependencies, type safety, fixture lifecycle, configuration, scope and required documentation updates.

### 5. Security and data

Check for hardcoded credentials, tokens or sensitive data; unsafe production data; inadequate isolation or cleanup; sensitive information in logs/reports; and missing permission-boundary coverage.

### 6. Verification evidence

Inspect actual focused and broader test results, typecheck/lint where required, browser/project coverage, failure artifacts and unresolved warnings. A command listed in a report is not proof it passed.

### 7. Classify findings

- **BLOCKER:** invalidates correctness, safety or a required quality gate.
- **MAJOR:** significant risk, missing coverage or maintainability issue; resolve before acceptance unless an authorised owner explicitly accepts the risk.
- **MINOR:** limited impact; correction recommended.
- **OBSERVATION:** improvement or clarification with no immediate acceptance impact.

Each finding includes identifier, severity, file/location or scenario, evidence, impact and required corrective action. Do not present subjective style preferences as defects.

### 8. Decide

- **APPROVED:** no blocker or major finding; required evidence is sufficient.
- **APPROVED WITH OBSERVATIONS:** acceptable with minor findings or observations recorded.
- **CHANGES REQUIRED:** blocker or major finding exists, or required evidence is insufficient.
- **REVIEW BLOCKED:** missing context or access prevents a meaningful review.

Approval is a review outcome, not release authorisation.

## Review Report

### Review Context
Change, maker, reviewer, requirement, scope and evidence inspected.

### Findings
Prioritised findings with severity, location, evidence, impact and required action. State explicitly when none are identified.

### Verification Assessment
Checks and results inspected, plus missing evidence.

### Decision
One of the four review outcomes with concise reasoning.

### Follow-up
Required corrections, re-review conditions and unresolved risks.

## Stop Conditions

Do not approve when expected behaviour is unapproved or materially ambiguous; a blocker or major defect remains; required verification evidence is absent; security or data-handling risks are unresolved; or independence cannot be established where required.

## Anti-Patterns

Never rubber-stamp; treat green tests as sufficient review; approve based on code appearance alone; hide findings in general comments; change code and approve your own changes as Checker; downgrade material severity to avoid blocking; or treat review approval as release authorisation.

## Related Skills

`qe-workflow`, `verify-implementation`, `investigate-failure`, `evaluate-quality`.
