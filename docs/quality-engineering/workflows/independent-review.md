# Independent Review Workflow

## 1. Purpose

This workflow defines how changes are independently reviewed using the Maker–Checker model.

It applies to test automation changes, framework updates, shared QE assets and other changes requiring independent verification.

The governance principles are defined in `../governance/maker-checker.md`.

## 2. Workflow

**DEFINE → PLAN → MAKE → VERIFY → REVIEW → FIX → RE-VERIFY → COMPLETE**

### Step 1: DEFINE

The Maker establishes:

- The objective and scope of the change.
- The relevant approved requirements.
- Acceptance criteria and expected behaviour.
- Dependencies, assumptions and risks.
- The verification required.

Unclear or conflicting requirements must be escalated before dependent implementation proceeds.

### Step 2: PLAN

The Maker identifies:

- Files and components expected to change.
- Implementation approach.
- Potential impact on existing functionality.
- Required tests and validation.
- Relevant risks and dependencies.

The plan should be proportionate to the change.

### Step 3: MAKE

The Maker implements the approved change.

During implementation:

- Follow applicable repository instructions and engineering standards.
- Keep changes within the agreed scope.
- Avoid unrelated modifications.
- Do not weaken existing assertions or quality controls to obtain passing results.
- Document necessary deviations and unresolved issues.

### Step 4: VERIFY

The Maker performs initial verification.

Depending on the change, this may include:

- TypeScript compilation and type checking.
- Linting and static analysis.
- Relevant automated tests.
- Regression checks.
- Configuration validation.
- Review of generated reports and test results.

The Maker records the commands executed, their results and any checks that could not be completed.

### Step 5: REVIEW

The Checker independently examines:

1. **Requirements:** Does the change satisfy the approved scope and expected behaviour?
2. **Correctness:** Is the implementation logically correct?
3. **Coverage:** Are relevant positive, negative and boundary scenarios addressed?
4. **Reliability:** Are tests deterministic, isolated and maintainable?
5. **Regression risk:** Could the change affect existing functionality?
6. **Standards:** Does it follow the applicable framework and repository conventions?
7. **Evidence:** Do the reported results support the claimed outcome?
8. **Scope:** Are there unrelated or unauthorised changes?

The Checker must inspect the actual changes and relevant evidence, not rely exclusively on the Maker's explanation.

The review produces one outcome:

- **PASS:** No blocking findings remain.
- **FAIL:** One or more issues require correction.
- **BLOCKED:** Review cannot be completed because required information, access or evidence is unavailable.

Findings should identify the affected area, the issue, its impact and the expected correction.

### Step 6: FIX

When the outcome is FAIL, the Maker addresses the findings.

Corrections should remain within the approved scope. If a finding reveals an unclear requirement or requires a product or architectural decision, the appropriate owner must resolve it.

The Maker must not dismiss or bypass a finding simply to obtain approval.

### Step 7: RE-VERIFY

After corrections, the Maker repeats the relevant verification activities.

The Checker then reviews the corrections and supporting evidence.

Additional changes may require further review and verification.

### Step 8: COMPLETE

A change may be marked complete when:

- Required verification has passed.
- Required independent review has passed.
- Blocking findings have been resolved.
- Required approvals have been obtained.
- Relevant evidence and exceptions have been recorded.

A BLOCKED review remains incomplete until the missing information or dependency is resolved.

## 3. Review Evidence

The review record should contain, as appropriate:

- Change objective and scope.
- Relevant requirements or acceptance criteria.
- Files or components changed.
- Verification commands and results.
- Review findings and their resolution.
- Final review outcome.
- Required approvals.
- Known limitations or accepted exceptions.

Evidence should be concise, reproducible where practical and accessible to relevant reviewers.

## 4. Handling Disagreements

If the Maker and Checker disagree:

1. Identify the specific disputed behaviour or finding.
2. Refer to the approved requirement, standard or technical evidence.
3. Clarify whether the disagreement concerns implementation, expected behaviour or governance.
4. Escalate unresolved product decisions to the Product Owner.
5. Escalate unresolved architectural or framework decisions to the authorised technical owner.

Neither party should silently redefine the expected behaviour to resolve a disagreement.

## 5. Exceptions

An exception to the normal review process must be:

- Justified by the circumstances and risk.
- Documented with its scope and potential impact.
- Approved by an authorised owner.
- Limited to the minimum necessary scope.

Exceptions must not be used to conceal failed checks, missing evidence or unresolved requirements.

## 6. AI-Assisted Execution

AI agents may perform Maker or Checker activities within their assigned permissions.

When AI is involved:

- The role and scope of the agent must be clear.
- Generated changes must be verified.
- Review conclusions must be supported by evidence.
- An agent must not independently approve its own work where independent review is required.
- Required human approvals must remain in place.

AI governance requirements are defined in `../ai/ai-agent-governance.md`.

## 7. Related Guidance

- `../governance/maker-checker.md`
- `../governance/requirements-integrity-and-product-ownership.md`
- `../governance/quality-gates-and-readiness.md`
- `../engineering-practices/test-reliability.md`
- `../engineering-practices/continuous-improvement.md`
