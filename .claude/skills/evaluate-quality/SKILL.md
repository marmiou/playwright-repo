---
name: evaluate-quality
description: Evaluates the quality outcome of a feature, change or release candidate using requirement coverage, risk treatment, execution evidence, independent review and residual risk. Use at QE closure or when communicating quality readiness to stakeholders.
---

# Quality Outcome Evaluation

## Purpose

Provide an evidence-based assessment of the quality outcome for a feature, change or release candidate.

Connect requirements, risks, test design, execution results, review findings and unresolved limitations into a clear quality assessment. Do not turn test metrics into unsupported claims or make release decisions on behalf of authorised owners.

## Governing Documentation

Follow:
- `AGENTS.md` and `CLAUDE.md`
- `docs/quality-engineering/foundations/quality-engineering-principles.md`
- `docs/quality-engineering/governance/quality-gates-and-readiness.md`
- `docs/quality-engineering/governance/maker-checker.md`
- `docs/quality-engineering/ai/ai-agent-governance.md`
- `docs/architecture/test-execution.md`
- Relevant requirement, strategy, design, implementation and failure-investigation records.

## Required Inputs

Use available evidence:
- Requirement Analysis Report or approved requirements.
- Test Strategy Report or documented risk assessment.
- Test Design and traceability matrix.
- Implementation summary and changed files.
- Actual execution results and reports.
- Failure investigations and unresolved defects.
- Independent review outcome where required.
- Known environment, data and scope limitations.

If important inputs are missing, state that the evaluation is partial. Do not infer results.

## Evaluation Dimensions

### 1. Requirement coverage

Assess whether in-scope requirements and acceptance criteria have meaningful verification evidence. Distinguish Verified, Partially verified, Not verified, Blocked and Not applicable.

A test existing is not proof that it passed or that it adequately verifies the requirement.

### 2. Risk treatment

Assess whether Critical and High risks have appropriate verification, mitigation or an explicit authorised acceptance. Identify untreated risks.

### 3. Execution evidence

Review passed, failed, skipped and blocked checks; browser, API, environment and configuration scope; stability and repeatability; relevant artifacts and timestamps; and whether the run represents the intended commit and configuration.

Do not combine results from unrelated runs as if they were one validated baseline.

### 4. Defects and failures

Summarise confirmed product defects, automation defects, environment/configuration failures, unresolved or intermittent failures, severity, impact, owner and status where known.

Do not label an unresolved failure as harmless.

### 5. Review and governance

Check whether independent review was required and completed. Record the actual review outcome and outstanding findings. Respect authorised ownership of product acceptance and release decisions.

### 6. Residual risk and limitations

Identify untested requirements or scenarios, excluded browsers/environments/integrations, unavailable data or dependencies, deferred non-functional testing, known defects and confidence limitations.

### 7. Improvement opportunities

Recommend specific, actionable improvements to requirements, coverage, automation reliability, test data, observability, environments or workflow. Separate immediate release concerns from longer-term improvements.

## Quality Evaluation Workflow

1. Establish the evaluated change, version and scope.
2. Gather and verify source evidence.
3. Map requirements and risks to designed tests.
4. Map designed tests to actual execution outcomes.
5. Assess failures, review findings and unresolved issues.
6. Evaluate residual risks and limitations.
7. Determine the quality assessment.
8. Communicate recommendation and decision ownership.

## Quality Outcome Report

### 1. Evaluation Context
- Feature / release candidate:
- Version / commit:
- Evaluation date:
- Scope:
- Evidence sources:

### 2. Requirement Coverage

| Requirement / acceptance criterion | Evidence | Outcome | Gap |
|---|---|---|---|

### 3. Risk Treatment

| Risk | Priority | Verification / mitigation | Status | Residual risk |
|---|---|---|---|---|

### 4. Execution Summary

| Check / suite | Environment / project | Result | Evidence |
|---|---|---|---|

### 5. Defects and Review Findings
Summarise confirmed defects, unresolved failures and independent review findings.

### 6. Limitations and Residual Risk
State what has not been verified and the likely impact.

### 7. Quality Assessment

Choose one:
- **SUFFICIENT EVIDENCE:** required quality activities completed and no known blocking issue remains within the evaluated scope.
- **SUFFICIENT WITH RESIDUAL RISK:** evidence is adequate for the stated scope, but material limitations or accepted risks remain.
- **INSUFFICIENT EVIDENCE:** important requirements or risks lack adequate verification.
- **QUALITY CONCERNS:** evidence identifies unresolved defects or failures that undermine expected quality.
- **BLOCKED:** the evaluation cannot be completed because critical evidence or access is unavailable.

Explain the assessment. It is not a release approval.

### 8. Recommendation and Decision Owner
State the recommended next action and identify who owns product acceptance, risk acceptance or release authorisation.

### 9. Improvement Actions

| Action | Expected benefit | Suggested owner | Priority |
|---|---|---|---|

## Stop Conditions

Do not provide a positive quality assessment when critical evidence is missing, a required quality gate has failed, Critical or High risks remain untreated without authorised acceptance, results cannot be tied to the evaluated change, required independent review has not occurred, or known failures and limitations are concealed.

## Anti-Patterns

Never equate pass rate with product quality; claim complete coverage based on test count; omit skipped, blocked or unexecuted checks; treat an uninvestigated failure as harmless; accept product or release risk on behalf of its owner; claim release approval from a QE assessment; or hide limitations to produce a positive summary.

## Exit Criteria

The quality outcome is traceable to evidence, coverage and risks are visible, execution and review results are accurately represented, residual risk is explicit, and recommendations and decision ownership are clear.

## Related Skills
- `qe-workflow`
- `analyze-requirement`
- `design-test-strategy`
- `design-test-cases`
- `verify-implementation`
- `investigate-failure`
- `review-tests`
