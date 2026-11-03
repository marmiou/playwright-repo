---
name: verify-implementation
description: Verifies a Quality Engineering change using proportionate execution, static checks, evidence review and repository quality gates. Use after adding or modifying tests, fixtures, configuration or automation code, before reporting completion or requesting independent review.
---

# Verify Implementation

## Purpose

Establish evidence that a QE implementation is correct, maintainable and consistent with repository standards. Verification must be based on commands actually executed and results actually observed.

This skill verifies a change. It does not independently approve its own implementation or make release decisions.

## Governing Documentation

Follow:
- `AGENTS.md` and `CLAUDE.md`
- `docs/architecture/overview.md`
- `docs/architecture/test-execution.md`
- `docs/quality-engineering/engineering-practices/test-automation-standards.md`
- `docs/quality-engineering/engineering-practices/test-reliability.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/governance/maker-checker.md`

## Workflow

### 1. Establish the change

Inspect the diff and identify:
- Intended behaviour and requirement.
- Files changed.
- Relevant tests and architectural boundaries.
- Potential side effects.
- Required validation.
- Environment and dependency constraints.

Do not rely only on the implementer's summary. Inspect the actual changes.

### 2. Review static correctness

Where relevant, check:
- TypeScript types and compiler errors.
- Lint and formatting.
- Imports, unused code and dependency changes.
- Configuration and environment handling.
- Test naming, structure and fixture lifecycle.
- Data isolation, cleanup and parallel safety.
- Secret and sensitive-data exposure.
- Architecture boundaries and duplication.
- Assertions and expected-result quality.

Use repository scripts from `package.json`. Do not invent commands or silently modify scripts to make validation appear successful.

### 3. Execute proportionate validation

Run checks in increasing scope:
1. Focused test(s) for the changed behaviour.
2. Relevant project or test group.
3. Typecheck and lint, if available.
4. Broader relevant suite.
5. Additional browser projects or environments when required by risk and feasible.

Avoid running unrelated expensive suites without reason. If a required check cannot run, state why and its impact.

### 4. Classify outcomes accurately

Use:
- **PASS:** command completed and relevant assertions/checks passed.
- **FAIL:** validation ran and identified a real failure.
- **BLOCKED:** validation could not be completed because of environment, dependency, access, configuration or other external constraint.
- **NOT RUN:** check was not attempted.
- **NOT APPLICABLE:** check is irrelevant to this change.

Do not classify a failing test as an environment issue without evidence. Do not classify an environment failure as a product defect without evidence.

### 5. Inspect evidence

For failed or unexpected outcomes, preserve:
- Exact command.
- Exit code or reported result.
- Relevant assertion, error or stack trace.
- Browser, project, environment and configuration where relevant.
- Trace, screenshot, video or report location when generated.
- Whether the issue reproduces.

Do not paste secrets or sensitive data into reports.

### 6. Assess completion

Compare results against:
- Requirement and designed scenarios.
- Risk priorities.
- Repository quality gates.
- Change-specific acceptance criteria.

A green suite does not prove complete coverage. Report untested risks and residual limitations.

### 7. Prepare independent review

Where Maker–Checker governance applies, provide the reviewer with:
- Original task and expected behaviour.
- Change summary and diff.
- Test design and risk rationale.
- Commands and evidence.
- Known limitations and unresolved questions.

Do not claim the independent review has passed before a separate reviewer has performed it.

## Verification Report

### Change
- Objective:
- Requirement / scenario:
- Files changed:

### Checks

| Check | Command / evidence | Result | Notes |
|---|---|---|---|

### Test Results
- Passed:
- Failed:
- Skipped:
- Blocked:
- Not run:

### Findings
List defects, risks, warnings and follow-up actions.

### Coverage and Residual Risk
Identify scenarios or environments not verified and explain impact.

### Overall Verification
**Outcome:** PASS / FAIL / BLOCKED / PARTIAL

Explain the outcome. PASS means all required checks for this change completed successfully; it does not imply independent review or release approval.

## Stop Conditions

Do not report PASS when:
- Required checks have not run.
- Relevant tests fail.
- Type or lint errors remain where those checks are required.
- Evidence is missing or contradictory.
- The implementation violates documented architecture or governance.
- A material risk remains undisclosed.

## Anti-Patterns

Never:
- Claim tests passed without running them.
- Report only the happy result while hiding failures.
- Change assertions or tests merely to achieve green status.
- Add retries to conceal intermittent failures.
- Skip focused validation after a code change.
- Treat a partial run as a full-suite pass.
- Approve your own work as independent Checker.
- Treat green automation as a release decision.

## Related Skills
- `qe-workflow`
- `add-web-test`
- `add-api-test`
- `investigate-failure`
- `review-tests`
- `evaluate-quality`
