# Test Reliability

## 1. Purpose

This document defines the practices required to build and maintain reliable automated tests.

Reliable tests must produce results that are deterministic, repeatable, trustworthy, independently executable and diagnosable.

These standards apply to Web UI and API automation.

## 2. Core Principles

- **Evidence first:** Investigate failures using available evidence.
- **Root cause:** Fix underlying problems rather than masking symptoms.
- **Isolation:** Avoid execution-order dependencies and uncontrolled shared state.
- **Determinism:** Control relevant inputs, time and external dependencies where practical.
- **Failure visibility:** Preserve initial failures, including when retries pass.
- **Integrity:** Never weaken assertions or hide failures to improve pass rates.

A test failure must not automatically be classified as a product, automation or infrastructure defect without investigation.

## 3. Failure Classification and Investigation

Classify failures using the available evidence:

| Category | Description |
|---|---|
| Product defect | Implementation violates approved requirements. |
| Automation defect | Test implementation, locator, assertion or logic is incorrect. |
| Test data failure | Required data is missing, invalid or conflicting. |
| Environment / infrastructure | Execution environment or supporting infrastructure is unavailable or unstable. |
| Unknown | Evidence is insufficient to establish the cause. |

For relevant failures:

1. Identify the failing test and execution.
2. Inspect the error, assertion and available diagnostics.
3. Check environment and test data.
4. Compare successful and unsuccessful executions where possible.
5. Determine the likely root cause.
6. Record the classification and corrective action.
7. Verify the fix.

If evidence is insufficient, retain `Unknown`. Do not invent a root cause.

## 4. Deterministic Execution and Synchronisation

Tests SHOULD produce consistent results under equivalent initial conditions.

Avoid uncontrolled dependencies on:

- Current time and random values.
- Execution order and shared mutable data.
- Network timing and external service availability.
- Environment-specific defaults.
- Uncontrolled background processes.

Use Playwright's built-in waiting and retry mechanisms:

- Locator-based interactions.
- Web-first assertions.
- Explicit condition-based waiting.
- Response and event waiting where required.

Example:

```typescript
await expect(
  page.getByRole('heading', { name: 'Dashboard' })
).toBeVisible();
```

Avoid arbitrary fixed sleeps and do not use `networkidle` as a universal indicator of application readiness.

Wait for the actual condition required by the scenario.

## 5. Retries and Flaky Tests

Retries MUST be limited, controlled and centrally configured.

- Preserve the original failure and all retry outcomes.
- Do not use retries to compensate for unstable test design.
- Do not treat a retry pass as proof of reliability.
- Investigate repeated failures and inconsistent outcomes.
- Do not weaken assertions or increase timeouts without justification.

A test that fails initially and passes on retry MUST remain visible as a potential flaky or transient failure.

A flaky test is one that produces inconsistent results under apparently equivalent conditions.

Quarantine MAY be used when instability threatens shared execution pipelines. A quarantined test MUST have:

- A documented reason.
- An assigned owner.
- A tracking issue.
- A review date.
- Clear restoration criteria.

Where practical, quarantined tests SHOULD continue running separately for diagnostic purposes. Removing a test from a quality gate requires appropriate approval.

## 6. Parallel and API Reliability

### Parallel execution

Tests MUST remain independent when executed concurrently.

Investigate data collisions, shared accounts, concurrent updates, cleanup conflicts, rate limits and environment capacity.

Do not reduce worker count as the default solution to isolation problems.

See `test-data-management.md` for data ownership and isolation requirements.

### API execution

API tests SHOULD account for:

- Connection and response timeouts.
- Transient service failures.
- Eventual consistency.
- Rate limiting.
- Authentication and token expiry.
- Duplicate operations and idempotency.
- Service availability.

For asynchronous operations, verify the expected resulting state using an appropriate condition or polling strategy.

Do not blindly retry state-changing operations. Understand their side effects and idempotency characteristics first.

Timeouts SHOULD be centralised and appropriate to the operation.

## 7. Diagnostics and CI/CD

Failures must provide sufficient evidence for investigation.

Where relevant, collect:

**Web UI**
- Playwright traces and screenshots.
- Browser console and network errors.
- Current URL and relevant page state.

**API**
- HTTP method, endpoint and status.
- Response duration and relevant response data.
- Correlation identifiers and service error details.

**Execution context**
- Test and execution identifiers.
- Environment, browser and project.
- Worker and retry number.
- Timestamp and build or commit reference.

Sensitive information MUST be redacted. Never expose credentials, tokens, secrets or unnecessary personal data in logs, reports or attachments.

CI/CD pipelines SHOULD distinguish test failures from infrastructure and setup failures. They MUST NOT conceal failures through uncontrolled retries, skipped tests or incomplete reporting.

Execution mechanics and retry configuration are defined in `../../architecture/test-execution.md`.

## 8. AI-Assisted Investigation and Continuous Improvement

AI agents MAY assist with failure analysis, trace comparison, race-condition investigation, retry analysis and root-cause hypotheses.

They MUST:

- Base conclusions on available evidence.
- Distinguish confirmed causes from hypotheses.
- Preserve original failure information.
- Avoid weakening assertions or adding arbitrary delays.
- Avoid increasing retries or skipping tests without justification.
- Report uncertainty when the cause is unclear.

Proposed fixes MUST be verified before completion.

Reliability improvements should feed into the framework improvement process defined in `continuous-improvement.md`.

Useful indicators include first-attempt pass rate, flaky test rate, retry frequency, failure categories, diagnosis time, resolution time, quarantine age and execution duration.

Metrics MUST support improvement, not encourage hiding failures or artificially increasing pass rates.

## Related Documents

- `test-automation-standards.md` — Automation engineering standards.
- `test-data-management.md` — Data isolation, ownership and cleanup.
- `continuous-improvement.md` — Framework improvement.
- `../../architecture/overview.md` — Framework architecture.
- `../../architecture/test-execution.md` — Playwright execution and CI/CD.

## Governing Principle

**Do not hide instability. Identify it, investigate it, fix its root cause and preserve the evidence.**
