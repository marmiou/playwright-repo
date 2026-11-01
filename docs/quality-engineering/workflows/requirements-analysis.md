# Requirements Analysis Workflow

## 1. Purpose

This workflow defines how product requirements are analysed to establish whether they are clear, complete, consistent, testable and ready for implementation and verification.

It applies to:

- Functional requirements.
- Non-functional requirements.
- User stories and acceptance criteria.
- API and integration requirements.
- Changes to existing product behaviour.
- Defect fixes and regression requirements.

The objective is to identify gaps and risks early, establish testable expectations and prevent incorrect assumptions from entering the development and testing lifecycle.

## 2. Ownership and Principles

- The Product Owner or authorised product representative owns business requirements and product decisions.
- Engineering owns technical design and implementation decisions.
- Quality Engineering evaluates requirements for clarity, completeness, consistency and testability.
- AI may assist with analysis but has no authority to approve or redefine requirements.

Requirements must remain the authoritative source of expected product behaviour.

QA, Engineering and AI MUST NOT silently invent, reinterpret or weaken approved behaviour.

## 3. Requirements Analysis Workflow

**COLLECT → UNDERSTAND → ANALYSE → CLARIFY → VALIDATE → APPROVE → BASELINE**

### Step 1: COLLECT

Gather the available requirement information.

Sources may include:

- Product requirements and specifications.
- User stories and acceptance criteria.
- Business rules.
- API contracts.
- UX designs and prototypes.
- Non-functional requirements.
- Relevant existing documentation.
- Approved decisions and change records.

Identify the source and ownership of each requirement.

### Step 2: UNDERSTAND

Establish the intended behaviour and business context.

Identify:

- The problem or user need.
- Intended users and stakeholders.
- Expected system behaviour.
- Preconditions and business rules.
- Inputs, outputs and state changes.
- Dependencies and integrations.
- Constraints and non-functional expectations.
- Impact on existing functionality.

Distinguish explicitly stated requirements from assumptions and interpretations.

### Step 3: ANALYSE

Evaluate requirements against the following quality characteristics:

| Characteristic | Evaluation |
|---|---|
| Clarity | Is the expected behaviour understandable and unambiguous? |
| Completeness | Are relevant conditions, outcomes and exceptions covered? |
| Consistency | Does the requirement conflict with other approved requirements? |
| Testability | Can the expected behaviour be objectively verified? |
| Feasibility | Can Engineering assess a viable implementation approach? |
| Traceability | Can the requirement be linked to its source and verification? |
| Relevance | Does it address the intended business or user need? |

Identify missing scenarios, boundary conditions, error handling, permissions, data constraints and relevant non-functional expectations.

### Step 4: CLARIFY

Raise questions and document unresolved issues.

Examples include:

- Missing or ambiguous expected results.
- Conflicting business rules.
- Undefined validation behaviour.
- Unclear error handling.
- Missing permissions or access rules.
- Undefined boundary conditions.
- Incomplete API contracts.
- Unspecified performance or security expectations.

Each clarification must have an accountable owner.

QA may recommend possible interpretations but must not select a business outcome without appropriate authority.

If unresolved ambiguity affects implementation or verification, dependent work must remain BLOCKED until an authorised decision is available.

### Step 5: VALIDATE

Confirm that the requirement is suitable for implementation and verification.

Check that:

- Expected behaviour is explicit.
- Acceptance criteria are objectively verifiable.
- Relevant positive and negative scenarios are identifiable.
- Important boundaries and exceptions are addressed.
- Dependencies and constraints are understood.
- Functional and relevant non-functional expectations are represented.
- Requirements are consistent with approved product decisions.

Quality Engineering provides testability feedback. Product ownership remains responsible for approving business behaviour.

### Step 6: APPROVE

The authorised Product Owner or relevant stakeholder reviews and approves business requirements.

Engineering confirms technical feasibility and identifies implementation constraints.

Quality Engineering confirms whether the requirements provide a sufficient basis for test design.

Approval responsibilities must not be transferred to AI agents or automated checks.

### Step 7: BASELINE

Establish the approved requirement version as the reference for implementation and verification.

Maintain traceability between:

- Requirement.
- Acceptance criteria.
- Test scenarios and cases.
- Automated tests, where applicable.
- Defects and change requests.

Changes to approved requirements must follow the authorised change process.

Affected test designs and automated tests must be reviewed and updated when requirements change.

## 4. Handling Ambiguity and Conflicts

When requirements are missing, ambiguous or contradictory:

1. Record the issue and affected requirement.
2. Describe the missing or conflicting behaviour.
3. Identify the appropriate decision owner.
4. Request clarification or an authorised decision.
5. Update the requirement source after approval.
6. Reassess affected test designs and implementation.

Do not resolve ambiguity by changing expected results in test cases or automation without an approved decision.

An assumption may be used only when explicitly documented and authorised by the appropriate owner, including its limitations and impact.

## 5. AI-Assisted Requirements Analysis

AI tools may assist with:

- Summarising requirement documents.
- Identifying ambiguity and inconsistencies.
- Suggesting missing scenarios and edge cases.
- Reviewing acceptance criteria for testability.
- Identifying dependencies and potential risks.
- Proposing clarification questions.
- Suggesting traceability relationships.

AI-generated interpretations and suggestions must be checked against authoritative sources.

AI MUST NOT:

- Invent missing business rules.
- Approve or change product requirements.
- Resolve conflicting requirements without an authorised decision.
- Convert assumptions into approved acceptance criteria.
- Modify expected behaviour to make implementation or testing easier.

## 6. Exit Criteria

Requirements analysis is complete when:

- Relevant requirement sources have been identified.
- Business behaviour is understood.
- Significant gaps and conflicts have been resolved or explicitly recorded.
- Acceptance criteria are sufficiently clear and testable.
- Ownership and approval are established.
- Relevant dependencies and risks are identified.
- Traceability can be maintained.

If essential information is missing, the outcome must be BLOCKED rather than treated as ready.

## 7. Related Guidance

- `../lifecycle/requirements-engineering.md`
- `../lifecycle/test-strategy-and-design.md`
- `../governance/requirements-integrity-and-product-ownership.md`
- `../governance/quality-gates-and-readiness.md`
- `../foundations/quality-engineering-principles.md`
- `../ai/ai-assisted-quality-engineering.md`
