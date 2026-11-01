# Maker–Checker and Independent Review

## 1. Purpose

This document defines the governance principles for independent review of changes to the Quality Engineering framework, test automation and related artefacts.

The Maker–Checker model establishes separation between implementation and independent verification, helping reduce errors, challenge assumptions and maintain the integrity of quality controls.

## 2. Core Principles

The following principles apply:

- **Separation of responsibilities:** The person or agent implementing a change should not independently approve their own work when independent review is required.
- **Evidence-based review:** Decisions must be supported by the actual changes, relevant requirements and verification evidence.
- **Risk-proportionate control:** Review depth and independence should reflect the potential impact of the change.
- **Transparency:** Findings, assumptions, limitations and decisions must be visible.
- **Requirements integrity:** Review must evaluate changes against approved requirements and standards, not silently redefine them.
- **No false approval:** Incomplete, failed or blocked work must not be represented as approved.

## 3. Roles and Responsibilities

### 3.1 Maker

The Maker is responsible for producing the change.

The Maker MUST:

- Understand the approved scope and relevant requirements.
- Identify assumptions, dependencies and potential risks.
- Implement the change within the authorised scope.
- Perform initial verification.
- Provide relevant test results and supporting evidence.
- Explain known limitations and unresolved issues.
- Address review findings and provide updated verification evidence.

### 3.2 Checker

The Checker independently evaluates the Maker's work.

The Checker MUST:

- Review the actual changes rather than relying solely on the Maker's summary.
- Evaluate alignment with approved requirements and applicable standards.
- Assess correctness, completeness and potential regressions.
- Examine relevant verification evidence.
- Identify defects, risks, omissions and unsupported assumptions.
- Record findings and the review outcome.

The Checker MUST NOT approve work solely because the automated checks pass.

### 3.3 Owner or Approver

An authorised human owner is responsible for decisions that require product, architectural, policy or governance authority.

This includes:

- Resolving ambiguous or conflicting requirements.
- Approving changes to governing principles and quality controls.
- Accepting explicitly documented exceptions where permitted.
- Making decisions outside the authority of the Maker or Checker.

The Checker does not automatically become the owner or approver of product requirements.

## 4. Independence

Where independent review is required, the Checker MUST be distinct from the Maker.

The Checker should have sufficient context, access and authority to challenge the implementation.

An AI agent may assist with independent review when it has been explicitly assigned that responsibility and has access to the relevant requirements, changes and evidence.

An agent reviewing its own implementation does not constitute independent review.

For high-risk changes, governance decisions and changes to quality gates, human review and approval are required.

## 5. Review Outcomes

Every formal review must produce one of the following outcomes:

| Outcome | Meaning |
|---|---|
| PASS | The change satisfies the applicable requirements and review criteria. |
| FAIL | The review identifies issues that must be corrected before approval. |
| BLOCKED | The review cannot be completed because required information, access, dependencies or evidence is unavailable. |

**BLOCKED is not PASS.**

A PASS confirms that the defined review criteria have been satisfied. It does not guarantee the absence of all defects or risks.

A FAIL must be returned to the Maker for correction and subsequent review.

A BLOCKED review must identify what is missing and what is needed to proceed.

## 6. Risk-Based Application

Independent review should be applied according to the impact and risk of a change.

It is particularly important for:

- Changes to shared automation architecture or framework behaviour.
- Changes to quality gates and release-readiness controls.
- Changes to requirements or product behaviour with significant business impact.
- Security, privacy or sensitive-data handling.
- Destructive operations or changes affecting shared environments.
- Changes to AI agent permissions, instructions or governance.
- Changes that could weaken existing verification or quality controls.

Low-risk, local changes may use a lighter review approach where justified.

The decision to reduce or omit independent review for a change that would normally require it must be documented with a rationale and an authorised owner.

## 7. Requirements and Quality Control Integrity

Neither the Maker nor the Checker may silently:

- Change approved requirements.
- Weaken acceptance criteria.
- Remove meaningful assertions to obtain a passing result.
- Hide, suppress or misrepresent failures.
- Treat missing evidence as successful verification.
- Bypass required quality gates without authorised exception.
- Introduce undocumented assumptions as established behaviour.

When expected behaviour is unclear or contradictory, the issue must be referred to the appropriate owner.

The requirements integrity and ownership principles are defined in `requirements-integrity-and-product-ownership.md`.

## 8. AI-Assisted Review

AI tools may support implementation, verification and independent review within their assigned permissions.

AI-assisted activities MUST:

- Preserve the distinction between generated suggestions and approved decisions.
- Evaluate changes against authoritative requirements.
- Report uncertainty and missing information.
- Preserve relevant evidence and review findings.
- Avoid changing governance rules or quality gates without authorised approval.

AI agents MUST NOT grant themselves additional permissions, approve their own governance changes or override required human approval.

Further controls are defined in:

- `../ai/ai-agent-governance.md`
- `../ai/ai-assisted-quality-engineering.md`

## 9. Review Workflow

The standard Maker–Checker lifecycle is:

**DEFINE → PLAN → MAKE → VERIFY → REVIEW → FIX → RE-VERIFY → COMPLETE**

A change is complete only when the required verification and review activities have passed and any necessary approval has been obtained.

The practical review procedure is defined in:

`../workflows/independent-review.md`

## 10. Related Guidance

- `../engineering-practices/continuous-improvement.md`
- `quality-gates-and-readiness.md`
- `requirements-integrity-and-product-ownership.md`
- `../workflows/independent-review.md`
- `../../AGENTS.md`


