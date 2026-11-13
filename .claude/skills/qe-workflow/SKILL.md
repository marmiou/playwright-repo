---
name: qe-workflow
description: Routes Quality Engineering tasks through the appropriate requirements, risk assessment, test design, automation, verification, investigation, review, and improvement skills. Use when starting a QA task, feature, bug investigation, test automation request, or quality assessment in this repository.
---

# Quality Engineering Workflow

## Purpose

Act as the entry point and workflow coordinator for the repository's Quality Engineering skills.

Select a proportionate workflow across the Software Testing Life Cycle (STLC) and Software Development Life Cycle (SDLC). Do not force every task through every phase.

## Governing Sources

Follow:
- `AGENTS.md` for shared engineering principles, lifecycle, architecture and Maker–Checker governance.
- `CLAUDE.md` for Claude Code-specific instructions.
- `docs/architecture/overview.md` for framework architecture and boundaries.
- `docs/architecture/test-execution.md` for execution and reporting.
- Relevant documents under `docs/quality-engineering/` for QE standards and governance.

Repository documentation defines the standards. Skills operationalise them. Do not duplicate or silently override documented policies. Verify referenced paths exist before relying on them.

## Workflow Selection

| Task | Skill / agent |
|---|---|
| Analyse a story, requirement, feature or defect | `analyze-requirement` |
| Assess risks, test levels, scope and coverage priorities | `design-test-strategy` |
| Create traceable scenarios and expected outcomes | `design-test-cases` |
| Implement browser UI automation | `add-web-test` |
| Implement API automation | `add-api-test` |
| Validate implementation and evidence | `verify-implementation` |
| Investigate failed or unstable tests | `investigate-failure` |
| Independently assess implementation quality | `review-tests` and Test Reviewer agent |
| Evaluate quality outcomes and improvements | `evaluate-quality` |
| Make significant framework or test architecture decisions | Test Architect agent |

A task may require multiple skills. For example:

Feature:
`analyze-requirement` → `design-test-strategy` → `design-test-cases` → implementation skill → `verify-implementation` → independent review where required → `evaluate-quality`.

Bug:
`analyze-requirement` → `design-test-cases` → `investigate-failure` → appropriate implementation skill → verification → review where required.

A small, unambiguous maintenance task may need only one skill and proportionate verification.

## Workflow Principles

### Requirements before implementation

Understand expected behaviour, authoritative sources, scope, ambiguity and risks before designing tests or implementing behaviour-sensitive automation.

### Separate facts, assumptions and recommendations

- **Fact:** supported by an authoritative source or observed evidence.
- **Assumption:** plausible but unconfirmed interpretation.
- **Recommendation:** proposed approach, not an approved decision.
- **Unknown:** information is unavailable.

Never present assumptions as approved product behaviour.

### Risk determines depth

Scale the workflow to potential impact. A low-risk isolated change does not need a lengthy strategy document. Payments, permissions, sensitive data, critical integrations and irreversible operations require deeper analysis and stronger evidence.

### Preserve requirements integrity

Product behaviour and business decisions belong to the Product Owner or authorised representative. QA and AI agents may identify gaps and recommend options, but must not approve or redefine product behaviour.

### Evidence before claims

Record actual validation evidence. Never claim a check passed unless it was run and passed. Distinguish product defects from automation and environment failures.

### Independent review

Maker and Checker responsibilities remain separate where Maker–Checker governance applies. An agent must not describe reviewing its own implementation in the same working context as independent approval.

## Workflow Gates

Use these gates for meaningful feature work; mark irrelevant phases as not applicable rather than manufacturing activity.

| Gate | Question | Outcome |
|---|---|---|
| Requirement readiness | Is expected behaviour sufficiently understood? | READY / READY WITH OPEN QUESTIONS / BLOCKED |
| Strategy readiness | Are relevant risks and test priorities understood? | READY / NOT REQUIRED / BLOCKED |
| Design readiness | Are scenarios and expected results verifiable? | READY / NOT REQUIRED / BLOCKED |
| Implementation | Does the change follow approved scope and architecture? | IMPLEMENTED / BLOCKED |
| Verification | Is sufficient execution evidence available? | PASS / FAIL / BLOCKED |
| Independent review | Has the work been independently assessed? | PASS / FAIL / BLOCKED / NOT REQUIRED |
| Closure | Are outcomes, residual risks and limitations visible? | COMPLETE / INCOMPLETE |

Do not advance through a blocked gate by silently assuming missing information.

## Handling Ambiguity

When essential information is missing or conflicting:

1. Stop dependent activity.
2. Identify the exact ambiguity.
3. Explain its impact on correctness or verification.
4. Identify the decision owner.
5. Ask a focused clarification question.
6. Resume when sufficient information is available.

Do not ask questions already answered by authoritative documentation. Non-blocking assumptions may be documented only when they do not redefine product behaviour or violate governance.

## Context Management

Load only the information needed for the current task.

- Requirements analysis: requirement sources, requirements-analysis workflow, requirements ownership and AI governance.
- Test strategy/design: approved requirements, QE principles, test-design guidance and relevant risk standards.
- Web automation: architecture, automation standards, reliability, test-data management and existing web code.
- API automation: architecture, API contracts, API standards and existing API code.
- Review: original task, actual changes, verification evidence and Maker–Checker guidance.

Prefer directly relevant authoritative sources over loading every document.

## Common Rationalisations

| Rationalisation | Required behaviour |
|---|---|
| "The feature is obvious." | Establish expected behaviour and acceptance criteria. |
| "We can clarify later." | Resolve ambiguity that affects correctness before dependent work. |
| "More tests mean better coverage." | Prioritise meaningful scenarios by risk. |
| "The test passes, so the feature works." | Check whether assertions prove the expected outcome. |
| "It only failed once." | Preserve and investigate the failure. |
| "The implementation already behaves this way." | Existing behaviour is not automatically an approved requirement. |
| "I reviewed my own work." | Do not claim independent verification. |
| "The task is small, so skip quality." | Use a proportionate workflow, not an absent one. |

## Final Reporting

For meaningful tasks, report:
1. Objective and scope.
2. Workflow stages or skills applied.
3. Relevant requirements and risks.
4. Implementation or analysis outcome.
5. Verification evidence, if applicable.
6. Independent review outcome, if applicable.
7. Outstanding questions, limitations and risks.

Use PASS, FAIL or BLOCKED where applicable. Never manufacture a PASS when evidence is incomplete.

## Definition of Success

The correct workflow was selected; authoritative requirements and repository architecture were respected; relevant risks were considered; applicable verification was performed; review responsibilities were respected; and limitations remain visible.
