# Quality Engineering Principles

**Category:** Foundations  
**Applies to:** All engineering and quality activities in this repository

## 1. Purpose

This document establishes the fundamental principles governing Quality Engineering (QE) within this project.

It defines the expectations that guide requirements analysis, test strategy, test design, automation engineering, verification, review and continuous improvement.

These principles are technology-independent wherever possible. Their implementation is documented separately in the architecture documentation, engineering practices and AI instructions.

## 2. What Is Quality Engineering?

Quality Engineering is a systematic engineering discipline focused on building, evaluating, maintaining and continuously improving software quality throughout the product lifecycle.

It extends beyond traditional software testing by integrating:

- Defect prevention and early risk identification.
- Requirements analysis and validation.
- Test strategy and design.
- Engineering quality controls.
- Automated and exploratory verification.
- Continuous feedback and observability.
- Independent review.
- Continuous improvement.

Quality is not an activity performed exclusively by QA at the end of development. It is a shared responsibility across the engineering lifecycle.

## 3. Fundamental Principles

### QE-01 — Quality Is a Shared Responsibility

Quality is owned collectively by the people involved in defining, designing, developing, testing and delivering the product.

- Developers are responsible for the quality of their implementation.
- Quality Engineers provide testing expertise, risk assessment and objective quality feedback.
- Product Owners are responsible for product decisions and approved expected behaviour.
- Engineering leadership is responsible for establishing appropriate quality practices and accountability.

QA MUST NOT become the sole owner of product quality.

### QE-02 — Quality Is Built Throughout the Lifecycle

Quality activities MUST be integrated throughout the Software Development Lifecycle (SDLC), rather than treated as a final testing phase.

Quality considerations should begin during requirements definition and continue through implementation, verification, release and production monitoring.

Teams SHOULD identify defects, ambiguities and risks as early as reasonably possible.

### QE-03 — Prevention Is Preferable to Late Detection

Preventing defects is generally more effective than discovering them late in the delivery process.

Engineering activities SHOULD prioritise:

- Clear and testable requirements.
- Early technical and quality reviews.
- Appropriate design validation.
- Static analysis and automated checks.
- Continuous integration and fast feedback.
- Root-cause analysis of recurring problems.

Testing remains essential, but it should complement rather than replace defect prevention.

### QE-04 — Approved Requirements Define Expected Behaviour

Approved requirements, acceptance criteria and authorised product decisions establish the expected behaviour of the system.

- Tests MUST be based on approved requirements or explicitly authorised quality objectives.
- Missing, ambiguous or contradictory requirements MUST be raised for clarification.
- Developers, QA and AI agents MUST NOT silently invent or modify expected product behaviour.
- Changes to approved requirements MUST follow an authorised change-management process.
- Tests MUST be updated when approved requirements change.

Tests validate implementation against requirements; they do not create or redefine requirements.

### QE-05 — Quality Activities Are Risk-Based

Not all features and failure conditions have equal significance.

Testing and verification effort SHOULD reflect the assessed risk, considering:

- Business impact.
- User impact.
- Likelihood of failure.
- Technical complexity.
- Security and privacy implications.
- Operational and financial consequences.
- Dependencies and integration points.

Risk assessments SHOULD be revisited when the system, requirements or operating conditions change.

### QE-06 — Verification and Validation Are Both Necessary

Verification and validation are complementary quality activities.

- **Verification:** Evaluates whether specified requirements and engineering expectations have been fulfilled.
- **Validation:** Evaluates whether the resulting product satisfies its intended purpose and stakeholder needs.

A successful test suite does not automatically establish that a product is fit for purpose.

Quality activities SHOULD consider functional and relevant non-functional characteristics, including performance, reliability, security, usability and compatibility.

### QE-07 — Quality Decisions Require Evidence

Quality assessments and release decisions MUST be supported by relevant and trustworthy evidence.

Evidence may include:

- Test execution results.
- Requirements and test traceability.
- Code reviews.
- Static analysis.
- Security assessments.
- Performance measurements.
- Defect and risk reports.
- Production monitoring and incident information.

Test pass rates and automation coverage MUST NOT be treated as standalone measures of overall product quality.

Known limitations, unresolved failures and residual risks MUST be communicated.

### QE-08 — Independent Review Strengthens Quality

Engineering outputs SHOULD receive appropriate review according to their complexity and risk.

Independent review helps identify errors, unsupported assumptions, omissions and bias.

The level of independence SHOULD be proportionate to the significance of the decision or artefact being reviewed.

Reviewers MUST evaluate evidence objectively and MUST NOT approve work solely because it was produced by an automated tool or another engineer.

### QE-09 — Automation Must Deliver Meaningful Feedback

Test automation is an engineering capability that supports repeatability, consistency, efficiency and timely feedback.

Automation is not an objective in itself.

- Automated checks MUST have clear objectives and expected outcomes.
- Automation SHOULD focus on valuable and repeatable verification activities.
- Automated tests MUST be maintainable and reliable.
- Flaky tests MUST be investigated rather than routinely ignored.
- Automation coverage MUST NOT be confused with risk coverage or product quality.

Automation MUST complement exploratory testing and human judgement.

### QE-10 — Quality Must Be Observable

Engineering teams need sufficient visibility into system behaviour and quality outcomes to make informed decisions.

Relevant evidence SHOULD be accessible and understandable to the people responsible for engineering and delivery decisions.

Quality metrics MUST be interpreted in context. Metrics SHOULD support improvement rather than encourage superficial optimisation.

### QE-11 — Quality Improves Continuously

Quality Engineering practices SHOULD evolve through feedback and learning.

Teams SHOULD use information from:

- Test failures.
- Production incidents.
- Defect trends.
- Code and design reviews.
- Delivery performance.
- User feedback.
- Retrospectives and improvement activities.

Recurring problems SHOULD lead to appropriate corrective or preventive actions.

### QE-12 — AI-Generated Engineering Outputs Require Validation

AI tools and agents can support requirements analysis, test design, implementation, investigation and review.

However, AI-generated outputs are not inherently correct or complete.

- AI-generated requirements interpretations MUST be checked against approved source material.
- AI-generated tests MUST have traceable and justified expected outcomes.
- AI-generated code MUST undergo appropriate verification and review.
- AI agents MUST operate within their defined scope and permissions.
- AI MUST NOT independently approve product decisions or bypass established quality controls.
- Human accountability MUST remain clear.

AI assistance does not remove the need for engineering judgement, independent verification or evidence.

## 4. Normative Language

The following terms communicate the strength of expectations throughout this documentation:

| Term | Meaning |
|---|---|
| MUST | Mandatory requirement for conformance with the documented standard. |
| MUST NOT | Prohibited practice. |
| SHOULD | Recommended practice. Deviations require appropriate justification. |
| SHOULD NOT | Practice that should generally be avoided unless justified. |
| MAY | Optional practice. |

These terms should be interpreted consistently across standards, workflows and AI instructions.

## 5. Applicability to This Repository

These principles apply to all relevant activities within this repository, including:

- Web testing.
- API testing.
- Test architecture and implementation.
- Test data management.
- Test execution and reporting.
- CI/CD quality controls.
- AI-assisted engineering.
- Code and test reviews.

Technology-specific implementation requirements are defined in the relevant engineering documentation.

## 6. Relationship with External Standards and Frameworks

These principles are informed by established software engineering, software quality and testing concepts.

Relevant references include:

- ISO/IEC 25010 — Systems and software quality models.
- ISO/IEC/IEEE 29119 — Software testing.
- ISO/IEC/IEEE 12207 — Software lifecycle processes.
- ISTQB — Software testing principles and practices.
- Agile Manifesto — Agile values and principles.
- ISO/IEC 42001 — Artificial intelligence management systems.

The references provide conceptual foundations and do not imply that this repository is certified or compliant with those standards.

Specific editions, official sources, applicability and relevant concepts are maintained in:

`docs/quality-engineering/references/standards-and-frameworks.md`

When external standards are used to justify a specific requirement, their source and applicability MUST be verified. AI-generated references, clause numbers and interpretations MUST NOT be accepted without validation.

## 7. Maintenance

These principles provide the baseline for all other Quality Engineering documentation in this repository.

Changes SHOULD be reviewed for consistency with the existing QE framework and its implementation.

Updates MUST be reflected in the relevant documentation and reviewed AI instructions when they affect engineering behaviour.
