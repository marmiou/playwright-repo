# Failure Investigation Workflow

## 1. Purpose

This workflow defines how automated test failures and unexpected verification results are investigated, classified and resolved.

It applies to:

- Playwright web test failures.
- API test failures.
- Regression failures.
- CI pipeline failures.
- Intermittent and flaky tests.
- Environment and dependency failures.

The objective is to identify the actual cause of a failure and ensure that corrective actions address the underlying problem.

## 2. Core Principles

Failure investigation MUST:

- Be based on observable evidence.
- Distinguish product defects from test and environment problems.
- Preserve the original failure information.
- Avoid assumptions before sufficient investigation.
- Avoid hiding failures through retries, skipped tests or weakened assertions.
- Record unresolved issues and limitations.
- Verify corrective actions before closing an investigation.

A failed test must not automatically be classified as a test defect or infrastructure issue.

## 3. Failure Investigation Workflow

**DETECT → COLLECT → CLASSIFY → INVESTIGATE → IDENTIFY → FIX → VERIFY → CLOSE**

### Step 1: DETECT

Identify the failed or unexpected verification result.

Capture:

- Test name and identifier.
- Execution environment.
- Build or commit reference.
- Failure message and assertion details.
- Execution timestamp.
- Relevant test and application context.

Determine whether the failure is isolated or part of a broader failure pattern.

### Step 2: COLLECT

Collect evidence before modifying the test or application.

Relevant evidence may include:

- Playwright test reports.
- Stack traces and assertion output.
- Screenshots and browser traces.
- Browser console and network logs.
- API requests and responses.
- Application and service logs.
- CI pipeline output.
- Test data and environment state.
- Recent code and configuration changes.

Preserve useful evidence so the investigation can be reproduced where practical.

Sensitive information, credentials and personal data must be handled according to repository security requirements.

### Step 3: CLASSIFY

Assign a provisional failure category.

| Category | Description |
|---|---|
| Product defect | Application behaviour violates approved requirements. |
| Test automation defect | Test logic, assertions, locators or setup are incorrect. |
| Test data issue | Required data is missing, invalid, inconsistent or incorrectly isolated. |
| Environment or infrastructure issue | Environment, network, service or execution infrastructure prevents reliable verification. |
| Dependency or integration issue | An external or internal dependency behaves unexpectedly or is unavailable. |
| Requirement or test design issue | Expected behaviour is unclear, incomplete or incorrectly represented. |
| Unknown | Available evidence is insufficient to establish the cause. |

Classification may change as new evidence becomes available.

Unknown is a valid provisional classification. It must not be replaced with an unsupported assumption.

### Step 4: INVESTIGATE

Analyse the failure using the collected evidence.

Consider:

- Whether the failure is reproducible.
- Whether the behaviour matches the approved requirement.
- Whether the assertion is valid.
- Whether the test data and system state are correct.
- Whether the application or dependency changed.
- Whether timing, concurrency or synchronisation is involved.
- Whether the failure occurs consistently or intermittently.
- Whether similar tests or environments are affected.

For web tests, examine relevant locators, browser state, navigation, network activity and Playwright traces.

For API tests, examine request construction, authentication, response contracts, status codes, data consistency and dependency behaviour.

Reproduction is useful evidence but is not always required to establish a cause.

### Step 5: IDENTIFY

Establish the most likely root cause using supporting evidence.

Document:

- The observed failure.
- The confirmed or suspected cause.
- Evidence supporting the conclusion.
- Affected functionality or tests.
- Potential impact.
- Remaining uncertainty.

Distinguish confirmed root causes from hypotheses.

If the evidence remains insufficient, retain the UNKNOWN classification and continue investigation or escalate.

### Step 6: FIX

Apply a corrective action appropriate to the identified cause.

Examples include:

| Cause | Possible corrective action |
|---|---|
| Product defect | Correct application behaviour and add appropriate regression coverage. |
| Automation defect | Correct test logic, locators, assertions or synchronisation. |
| Test data issue | Improve data setup, isolation or cleanup. |
| Environment issue | Restore or correct the affected environment or infrastructure. |
| Integration issue | Correct dependency handling, contracts or configuration. |
| Test design issue | Clarify requirements and update the test design. |

Corrective actions must address the actual cause rather than merely suppress the observed failure.

### Step 7: VERIFY

Verify that the corrective action resolves the identified issue.

Depending on the change, perform:

- Targeted test execution.
- Relevant regression testing.
- Repeated execution when investigating intermittent failures.
- Type checking and linting where applicable.
- Integration or environment validation.
- Independent review when required.

Confirm that the correction has not introduced new failures or weakened existing verification.

### Step 8: CLOSE

An investigation may be closed when:

- The cause is sufficiently established.
- The corrective action has been verified, or an authorised disposition has been documented.
- Relevant regression risks have been addressed.
- Evidence and findings are recorded.
- Outstanding limitations and follow-up actions are visible.

An unresolved failure must not be marked as fixed.

## 4. Handling Flaky Tests

A flaky test produces inconsistent results under apparently equivalent conditions.

Flakiness may arise from:

- Timing and synchronisation problems.
- Shared or uncontrolled test data.
- Test execution order dependencies.
- Concurrency and race conditions.
- Unstable external dependencies.
- Environment instability.
- Non-deterministic application behaviour.

Flaky tests must be investigated rather than normalised as expected failures.

Retries may provide diagnostic information, but a retry passing does not prove that the original failure was harmless.

Quarantining or disabling a test requires documented justification, appropriate ownership and a follow-up plan. It must not silently remove important coverage.

Detailed reliability practices are defined in `../engineering-practices/test-reliability.md`.

## 5. AI-Assisted Investigation

AI tools may assist with:

- Analysing test reports and stack traces.
- Reviewing Playwright traces and screenshots.
- Identifying failure patterns.
- Comparing execution results.
- Suggesting potential root causes.
- Recommending targeted diagnostic steps.
- Proposing corrective changes.

AI-generated explanations are hypotheses until supported by evidence.

AI MUST NOT:

- Classify an unknown failure as harmless without evidence.
- Automatically weaken assertions to eliminate failures.
- Hide failures through retries or skipped tests.
- Claim a root cause without sufficient support.
- Report a fix as successful without verification.

Human review and authorised decisions remain necessary where required by risk and governance.

## 6. Reporting

Investigation records should contain, where applicable:

- Failure identifier and affected test.
- Environment and execution reference.
- Failure category.
- Relevant evidence.
- Root cause or current hypothesis.
- Corrective action.
- Verification results.
- Final status.
- Outstanding risks or follow-up actions.

Reports must distinguish confirmed findings from assumptions.

## 7. Related Guidance

- `../engineering-practices/test-reliability.md`
- `../engineering-practices/test-data-management.md`
- `../engineering-practices/test-automation-standards.md`
- `../governance/quality-gates-and-readiness.md`
- `../governance/maker-checker-and-independent-review.md`
- `automation-implementation.md`
- `../ai/ai-assisted-quality-engineering.md`
