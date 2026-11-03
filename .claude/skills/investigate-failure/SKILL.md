---
name: investigate-failure
description: Investigates failed, flaky or unexpected automated tests using execution evidence, reproduction, failure classification and root-cause analysis. Use when a Playwright test, API test, CI run or quality check fails or behaves inconsistently.
---

# Failure Investigation

## Purpose

Determine why a test or quality check failed, using evidence to distinguish product defects from automation defects, test-data problems, environment issues and configuration failures.

The objective is diagnosis and a justified next action, not making the failure disappear.

## Governing Documentation

Follow:
- `AGENTS.md` and `CLAUDE.md`
- `docs/quality-engineering/workflows/failure-investigation.md`
- `docs/quality-engineering/engineering-practices/test-reliability.md`
- `docs/quality-engineering/engineering-practices/test-data-management.md`
- `docs/architecture/test-execution.md`
- `docs/quality-engineering/governance/maker-checker.md`

## Workflow

### 1. Preserve the original evidence

Collect:
- Exact failing command and run context.
- Test name, project, browser and environment.
- Failure message, assertion and stack trace.
- Playwright trace, screenshot, video and report if available.
- CI job, commit and relevant configuration.
- Frequency and reproduction history.
- Recent changes to product, tests, data, dependencies or infrastructure.

Do not delete evidence, rewrite the failing test or immediately rerun in a way that overwrites the only useful artifacts.

### 2. Classify the failure

Use one primary classification, with secondary contributing factors if needed.

| Classification | Indicators |
|---|---|
| Product defect | Actual behaviour violates an approved requirement or contract. |
| Automation defect | Locator, assertion, synchronisation, fixture or test logic is incorrect. |
| Test-data defect | Missing, stale, conflicting or shared mutable data causes the failure. |
| Environment / dependency | Service, browser, network, infrastructure or dependency is unavailable or unhealthy. |
| Configuration / secrets | Incorrect base URL, feature flag, permissions, credentials or runtime configuration. |
| Contract / requirement gap | Expected behaviour is ambiguous, conflicting or unsupported by an authoritative source. |
| Intermittent / flaky | Same test and conditions produce inconsistent outcomes; root cause remains to be established. |
| Unknown | Evidence is insufficient to classify confidently. |

Do not force a classification when evidence is incomplete.

### 3. Reconstruct what happened

Build a short timeline:
1. Preconditions and test setup.
2. Actions executed.
3. System responses and state changes.
4. First point of divergence from expected behaviour.
5. Subsequent errors or cleanup effects.

Separate the first causal failure from cascading symptoms.

### 4. Compare actual and expected behaviour

Verify expected behaviour against authoritative requirements, acceptance criteria, API contracts or approved decisions.

Compare:
- Expected result.
- Actual result.
- Evidence source.
- Reproducibility.
- Scope and impact.

Existing test assertions are not automatically authoritative. If the expected result itself is questionable, use `analyze-requirement`.

### 5. Reproduce safely

If safe and practical:
- Re-run the narrowest relevant test.
- Preserve the same relevant environment and data conditions.
- Change one variable at a time.
- Compare passing and failing runs.
- Check whether failure correlates with browser, worker count, order, time, data or environment.
- Avoid destructive operations and production mutations.

Do not repeatedly rerun a flaky test until it happens to pass and then declare it fixed.

### 6. Investigate likely causes

Inspect only relevant code and configuration:
- Test and assertion logic.
- Page objects, API clients and fixtures.
- Locator stability and asynchronous behaviour.
- Data creation, uniqueness, isolation and cleanup.
- Parallel execution and shared state.
- Network calls, dependency health and service logs where available.
- Browser differences and runtime configuration.
- Recent code or dependency changes.

For timing issues, prefer understanding the awaited condition and application state over adding fixed sleeps.

### 7. Establish root cause and confidence

Report:
- Most likely root cause.
- Evidence supporting it.
- Alternative explanations considered.
- Confidence: HIGH / MEDIUM / LOW.
- What additional evidence would change the conclusion.

If the root cause is unknown, say so. A symptom description is not a root-cause analysis.

### 8. Recommend or implement remediation

Recommend the smallest correction that addresses the cause:
- Product fix.
- Test / locator / assertion fix.
- Data isolation or cleanup fix.
- Environment or configuration correction.
- Contract or requirement clarification.
- Infrastructure or dependency remediation.

Do not weaken assertions, remove coverage, add arbitrary retries or change expected behaviour to suppress a failure.

If asked to implement a fix, follow the relevant implementation skill and then `verify-implementation`. Significant changes require independent review.

## Investigation Report

### 1. Failure Summary
- Test / check:
- Run and environment:
- First observed:
- Frequency:

### 2. Expected vs Actual
- Expected:
- Actual:
- Authoritative source:

### 3. Evidence
- Command and result:
- Error / assertion:
- Trace / report:
- Reproduction:

### 4. Classification
- Primary:
- Contributing factors:
- Confidence:

### 5. Root Cause
Explain the causal mechanism. If unknown, state what remains unproven.

### 6. Impact and Risk
Identify affected functionality, users, environments, confidence and potential release impact.

### 7. Recommended Remediation
Describe the smallest appropriate corrective action and owner.

### 8. Follow-up Verification
State how the fix should be verified and what regression coverage is required.

## Stop Conditions

Stop or escalate when:
- Reproduction may damage data or affect production.
- Required logs, traces or environment access are unavailable.
- Expected behaviour is not authoritative.
- The failure implicates security, privacy or data integrity.
- A proposed remediation requires a product or architecture decision.

## Anti-Patterns

Never:
- Assume every test failure is a product defect.
- Assume every intermittent failure is harmless flakiness.
- Add fixed waits as a first response.
- Add retries to hide root cause.
- Remove assertions to obtain a green run.
- Change expected behaviour without approval.
- Destroy the only available evidence.
- Report root cause with low evidence or false certainty.

## Exit Criteria

The failure is classified with evidence, actual and expected behaviour are compared, root cause and confidence are stated, impact is visible, and a justified remediation and verification path are provided.

## Related Skills
- `qe-workflow`
- `analyze-requirement`
- `add-web-test`
- `add-api-test`
- `verify-implementation`
- `review-tests`
