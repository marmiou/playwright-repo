# Requirements Integrity and Product Ownership

## 1. Purpose

This document defines ownership, authority and controls for maintaining the integrity of product requirements throughout the Software Development Lifecycle (SDLC).

Its objective is to ensure that implementation, testing and AI-assisted activities remain aligned with approved product expectations.

## 2. Core Principles

The following principles apply:

- **Single source of truth:** Approved requirements and specifications define the expected product behaviour.
- **Clear ownership:** Product decisions belong to the authorised Product Owner or designated business representative.
- **No silent assumptions:** Missing or ambiguous behaviour must be clarified rather than invented.
- **Independent verification:** Tests evaluate implementation against approved expectations; they do not define those expectations.
- **Change transparency:** Requirement changes must be authorised, documented and communicated to affected stakeholders.
- **Traceability:** Important requirements should remain traceable to their verification activities and outcomes.

## 3. Roles and Responsibilities

### 3.1 Product Owner

The Product Owner is accountable for product requirements and business decisions within their authorised scope.

Responsibilities include:

- Defining product objectives and expected behaviour.
- Establishing and prioritising requirements.
- Providing and approving acceptance criteria.
- Resolving conflicting or ambiguous business rules.
- Evaluating proposed requirement changes.
- Communicating approved decisions to relevant stakeholders.

Product decisions must not be delegated implicitly to QA, developers or AI agents.

### 3.2 Quality Engineering

Quality Engineering is responsible for evaluating requirements from a quality and testability perspective.

Responsibilities include:

- Reviewing requirements for clarity, consistency and testability.
- Identifying missing conditions and expected outcomes.
- Highlighting functional and non-functional quality risks.
- Deriving test conditions and scenarios.
- Identifying ambiguities and requesting clarification.
- Maintaining appropriate requirement-to-test traceability.
- Verifying implementation against approved expectations.

QA may recommend improvements to requirements but must not independently redefine product behaviour.

### 3.3 Engineering

Engineering is responsible for evaluating and implementing requirements within the agreed technical and architectural constraints.

Responsibilities include:

- Assessing technical feasibility.
- Identifying implementation dependencies and constraints.
- Highlighting technical risks and inconsistencies.
- Proposing technical solutions.
- Implementing approved behaviour.
- Reporting deviations and technical limitations.

Engineering decisions must not silently change approved business behaviour.

### 3.4 AI Agents

AI agents may support requirements analysis, clarification, testability assessment and documentation.

They may identify gaps and propose improvements but MUST NOT:

- Approve or redefine product requirements.
- Invent missing business rules.
- Resolve conflicting requirements without an authorised decision.
- Convert assumptions into approved expectations.
- Modify acceptance criteria without explicit authorisation.

AI-generated analysis remains advisory until reviewed and accepted by the appropriate owner.

## 4. Requirements as the Source of Truth

Approved requirements establish the expected behaviour against which implementation and testing are evaluated.

Relevant sources may include:

- Approved product requirements.
- User stories and acceptance criteria.
- Functional specifications.
- API contracts.
- Documented business rules.
- Approved architectural or technical decisions.
- Authorised requirement changes.

The authoritative source and approval status must be identifiable.

Code, existing application behaviour, historical tests or AI-generated outputs must not automatically be treated as authoritative requirements.

When sources conflict, the conflict must be escalated to the appropriate owner.

## 5. Handling Ambiguity and Missing Requirements

When a requirement is unclear, incomplete or contradictory:

1. Identify the specific ambiguity or missing information.
2. Document its potential impact on implementation and testing.
3. Request clarification from the Product Owner or authorised owner.
4. Record the resulting decision.
5. Update affected requirements and verification activities.

Dependent implementation or testing MUST remain blocked when an unresolved decision is necessary to establish correct behaviour.

A temporary assumption may be used only when explicitly documented and authorised by the appropriate owner, with its limitations and impact clearly identified.

An assumption must never be presented as an approved requirement.

## 6. Requirement Changes

Requirement changes must follow an authorised and traceable process.

A proposed change should identify:

- The requirement being changed.
- The reason for the change.
- The expected behavioural impact.
- Affected features and dependencies.
- Impact on existing tests and automation.
- Relevant risks and acceptance considerations.

The Product Owner or authorised representative approves product requirement changes.

After approval, affected documentation, implementation plans, test designs and traceability relationships should be updated.

Previously approved expectations must not be silently overwritten.

## 7. Requirements Integrity During Testing

Test cases and automated checks must reflect approved expectations.

The following practices are prohibited:

- Changing expected results merely to match the current implementation.
- Weakening assertions to make failing tests pass.
- Removing scenarios because the implementation does not support them.
- Treating existing behaviour as correct without an authoritative requirement.
- Using test automation as the authority for defining product behaviour.

When a test reveals a disagreement between implementation and approved requirements, the discrepancy must be investigated and resolved.

A test failure must not automatically be treated as an incorrect test.

## 8. Traceability and Impact Analysis

Requirements should remain traceable to relevant verification activities.

Where applicable, traceability should connect:

- Requirements and acceptance criteria.
- Identified risks.
- Test conditions and scenarios.
- Automated and manual tests.
- Execution results.
- Defects and approved deviations.

When a requirement changes, impact analysis should identify affected implementation, tests, dependencies and release considerations.

Traceability should provide useful evidence of coverage and change impact without creating unnecessary documentation overhead.

## 9. Escalation and Decision Authority

Issues must be escalated to the appropriate decision owner.

| Issue | Decision authority |
|---|---|
| Business rules and expected product behaviour | Product Owner |
| Requirement priority and scope | Product Owner |
| Technical feasibility and implementation approach | Engineering owner |
| Test strategy and verification approach | Quality Engineering owner |
| Quality framework and governance changes | Authorised QE or engineering owner |
| Security and privacy decisions | Authorised security or privacy owner |

Quality Engineering may challenge requirements and recommend changes, but must not approve product decisions outside its authority.

Unresolved disagreements must be documented and escalated rather than settled through undocumented assumptions.

## 10. Related Guidance

- `../lifecycle/requirements-engineering.md`
- `../lifecycle/test-strategy-and-design.md`
- `maker-checker-and-independent-review.md`
- `quality-gates-and-readiness.md`
- `../ai/ai-agent-governance.md`
- `../workflows/requirements-analysis.md`
