# Quality Gates and Readiness

## 1. Purpose

This document defines the quality controls and readiness criteria used to evaluate changes throughout the Software Development Lifecycle (SDLC).

Quality gates provide evidence-based checkpoints to determine whether a change can safely progress to the next stage or be considered ready for release.

Passing a quality gate provides confidence against defined criteria. It does not guarantee that a product is defect-free.

## 2. Core Principles

Quality gates MUST:

- Be aligned with approved requirements and acceptance criteria.
- Reflect the risk and impact of the change.
- Use objective, observable evidence wherever practical.
- Be defined before the relevant decision point.
- Distinguish successful, failed and blocked activities.
- Make unresolved risks and limitations visible.
- Avoid unnecessary checks that do not contribute meaningful quality assurance.

Quality gates must not be weakened simply to allow a change to progress.

## 3. Gate Outcomes

Every formal quality gate must produce one of the following outcomes:

| Outcome | Meaning |
|---|---|
| PASS | All applicable criteria have been satisfied with sufficient evidence. |
| FAIL | One or more mandatory criteria have not been satisfied. |
| BLOCKED | The gate cannot be evaluated because required information, access, dependencies or evidence is unavailable. |

**BLOCKED is not PASS.**

A failed or blocked gate must not be represented as successful.

Where an exception is permitted, it must be explicitly authorised and documented. An exception does not change the underlying verification result.

## 4. Quality Gate Lifecycle

Quality gates may be applied at relevant points throughout delivery.

### 4.1 Requirements Readiness

Before implementation begins, relevant requirements should be:

- Available from an identifiable authoritative source.
- Sufficiently clear and consistent.
- Supported by testable acceptance criteria where appropriate.
- Reviewed for relevant functional and non-functional quality risks.
- Assessed for important dependencies and constraints.

Unresolved requirements that prevent correct implementation must be clarified before dependent work proceeds.

### 4.2 Implementation Readiness

Before verification begins, the change should:

- Address the approved scope.
- Follow applicable engineering standards.
- Include appropriate error handling.
- Avoid unauthorised or unrelated changes.
- Have relevant dependencies and configuration identified.
- Be available in an appropriate verification environment.

### 4.3 Verification Readiness

Before verification is considered complete:

- Relevant test scenarios must be identified.
- Test data and environments must be suitable.
- Required automated and manual checks must be executed.
- Results must be available and interpretable.
- Failures and blocked checks must be classified.
- Relevant regression and integration risks must be evaluated.

Detailed execution practices are defined in the engineering standards and workflows.

### 4.4 Review Readiness

Where independent review is required:

- The change must be available for inspection.
- Relevant requirements and acceptance criteria must be identifiable.
- Verification evidence must be accessible.
- Known limitations and risks must be disclosed.
- Required findings must be resolved or handled through an authorised exception.

The Maker–Checker process is defined in `maker-checker.md`.

### 4.5 Release Readiness

Before release, the authorised decision-makers should evaluate:

- Fulfilment of approved release scope.
- Verification results against agreed criteria.
- Status of critical and high-severity defects.
- Relevant regression and integration results.
- Performance, security and other non-functional evidence where required.
- Outstanding risks and dependencies.
- Required approvals and documented exceptions.
- Deployment and rollback considerations.
- Operational monitoring and support readiness where applicable.

Release approval belongs to the authorised release or business decision-maker, not automatically to QA or an AI agent.

## 5. Defect and Risk Handling

Defects and risks must be evaluated according to their potential impact.

Considerations include:

- Business and user impact.
- Security and privacy implications.
- Data integrity.
- Functional correctness.
- Availability and reliability.
- Scope of affected functionality.
- Availability of workarounds.
- Likelihood of occurrence.

Critical or unacceptable risks must prevent progression until resolved or handled through an explicitly authorised decision where permitted.

Lower-severity issues may be accepted for a release when their impact, ownership and mitigation are documented.

Defect counts alone must not determine release readiness.

## 6. Evidence and Reporting

Quality decisions must be supported by relevant evidence.

Evidence may include:

- Test execution results.
- CI pipeline results.
- Test reports and diagnostics.
- Requirement-to-test traceability.
- Independent review outcomes.
- Defect records.
- Performance and security results.
- Risk assessments.
- Approval and exception records.

Reports must accurately distinguish:

- Checks that passed.
- Checks that failed.
- Checks that were blocked.
- Checks that were not executed.
- Known limitations and accepted risks.

Missing evidence must not be interpreted as successful verification.

## 7. Exceptions and Risk Acceptance

An exception to a quality gate may be considered only when the applicable governance process permits it.

Every exception must identify:

- The unmet criterion.
- The reason for the exception.
- The associated risk and potential impact.
- Affected functionality or release scope.
- Mitigation or containment measures.
- The authorised decision-maker.
- Any follow-up action or expiry condition.

Exceptions must not be used to conceal failures, bypass mandatory security controls or misrepresent quality status.

The authority to accept risk belongs to the authorised business or organisational owner.

## 8. AI and Automated Quality Gates

Automated checks and AI tools may support quality gate evaluation.

Examples include:

- CI pipeline validation.
- Automated test execution.
- Static analysis and linting.
- Type checking.
- Dependency and security scanning.
- Test result analysis.
- Evidence summarisation.

Automation and AI MUST NOT independently grant release approval unless explicitly authorised within an approved organisational process.

AI-generated summaries must reflect actual execution evidence and clearly disclose missing or inconclusive results.

## 9. Continuous Evaluation

Quality gates SHOULD be reviewed when:

- Product risks change.
- New technologies or dependencies are introduced.
- Production incidents reveal missing controls.
- Defect patterns indicate insufficient verification.
- Delivery practices change.
- Existing gates create unnecessary friction or fail to detect meaningful issues.

Changes to gate criteria must follow the applicable governance and independent review process.

## 10. Related Guidance

- `maker-checker.md`
- `requirements-integrity-and-product-ownership.md`
- `../lifecycle/requirements-engineering.md`
- `../lifecycle/test-strategy-and-design.md`
- `../engineering-practices/test-reliability.md`
- `../engineering-practices/continuous-improvement.md`
- `../ai/ai-agent-governance.md`
