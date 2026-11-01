# Terminology and Definitions

## 1. Purpose

This document establishes common terminology for Quality Engineering and Software Testing across this repository.

The definitions provide a consistent vocabulary for engineering documentation, workflows, test artefacts, reviews and AI-assisted activities.

Where a term has an established meaning in a recognised standard or framework, that meaning should be preferred over informal or project-specific interpretations.

## 2. Software Development and Quality Engineering

### Software Development Lifecycle (SDLC)

The complete lifecycle of software development, from initial concept and requirements through design, implementation, verification, deployment, operation and maintenance.

### Software Testing Lifecycle (STLC)

The set of testing-related activities performed throughout software development and delivery. These may include test planning, analysis, design, implementation, execution, evaluation and completion.

The STLC is not necessarily a separate sequential process. Testing activities are integrated into the wider SDLC and may overlap or repeat iteratively.

### Quality Engineering (QE)

An engineering discipline focused on building, evaluating, maintaining and continuously improving software quality throughout the product lifecycle.

### Quality Assurance (QA)

Planned and systematic activities intended to provide confidence that quality requirements and processes are being fulfilled.

QA is broader than executing tests and may include process assessment, prevention, reviews and quality governance.

### Quality Control (QC)

Activities focused on evaluating a product or deliverable to identify whether it meets specified quality expectations.

Testing and inspection are common quality control activities.

### Shift Left

An approach that moves appropriate quality activities earlier in the development lifecycle to identify risks, ambiguities and defects sooner.

### Shift Right

An approach that extends quality evaluation into production and operational environments through monitoring, feedback, experimentation and analysis of real-world behaviour.

## 3. Requirements and Product Definition

### Requirement

A documented capability, condition, constraint or expectation that a product, system or component must satisfy.

### Functional Requirement

A requirement describing a behaviour, capability or function that a system must provide.

### Non-Functional Requirement

A requirement describing a quality attribute, constraint or condition under which a system must operate.

Examples include performance, reliability, security, usability and compatibility.

### Acceptance Criteria

Conditions that a product increment, feature or requirement must satisfy to be accepted by the authorised stakeholder.

Acceptance criteria should be clear, testable and aligned with approved product expectations.

### Source of Truth

The authoritative and approved source used to establish expected product behaviour or a specific engineering decision.

### Requirements Traceability

The ability to establish and maintain relationships between requirements and relevant engineering artefacts, such as design decisions, test scenarios, test cases, defects and implementation changes.

### Requirements Integrity

The preservation of the meaning, ownership, approval and traceability of requirements throughout their lifecycle.

Requirements integrity prevents unauthorised assumptions or modifications from becoming accepted product behaviour.

## 4. Testing Concepts

### Verification

The evaluation of a work product to determine whether specified requirements or engineering expectations have been fulfilled.

A typical verification question is:

*Are we building the product correctly?*

### Validation

The evaluation of a product to determine whether it satisfies its intended purpose and stakeholder needs.

A typical validation question is:

*Are we building the right product?*

### Test Basis

The information used to derive test conditions and expected results.

Examples include requirements, specifications, acceptance criteria, architecture, interfaces and risk assessments.

### Test Condition

An aspect of the test basis that can be verified through one or more test cases.

### Test Scenario

A high-level description of a situation, workflow or behaviour that should be evaluated.

### Test Case

A set of preconditions, inputs, actions and expected results designed to verify a specific behaviour or condition.

### Test Procedure

A defined sequence of actions used to execute one or more test cases.

### Test Data

Data required to perform testing, including input values, expected results, configuration data and relevant system state.

### Expected Result

The predicted outcome of a test, derived from an approved requirement, specification or authorised expected behaviour.

### Actual Result

The observed outcome produced when a test is executed.

### Test Oracle

A mechanism, source or method used to determine whether an observed result is correct.

Examples include approved requirements, expected outputs, business rules, reference datasets and independent calculations.

## 5. Test Levels and Test Types

### Test Level

A grouping of testing activities associated with a particular stage or scope of the software development process.

Common test levels include:

- Component testing.
- Component integration testing.
- System testing.
- System integration testing.
- Acceptance testing.

The applicable levels depend on the architecture and delivery context.

### Test Type

A classification of testing based on its objective or quality characteristic.

Common test types include:

- Functional testing.
- Performance testing.
- Security testing.
- Usability testing.
- Compatibility testing.
- Reliability testing.
- Accessibility testing.
- Regression testing.

Test levels and test types are different dimensions. A test type may be performed at more than one test level.

### Functional Testing

Testing that evaluates whether the system provides the required functions and behaviours.

### Non-Functional Testing

Testing that evaluates quality characteristics such as performance, security, reliability, usability and compatibility.

### Regression Testing

Testing performed to determine whether changes have adversely affected previously working functionality or quality characteristics.

### Exploratory Testing

An approach in which test design, execution and learning occur concurrently.

The tester uses investigation, observation and critical thinking to explore system behaviour, identify risks and discover issues that may not be covered by predefined test cases.

### Smoke Testing

A relatively small set of checks used to determine whether a build or environment is sufficiently functional for further testing.

### Sanity Testing

A focused evaluation of a particular change or area to determine whether it behaves as expected after a modification.

The terms smoke testing and sanity testing are sometimes used differently across organisations. Their precise scope should be defined by the relevant project.

## 6. Defects and Risk

### Defect

An imperfection or flaw in a work product that may cause it to fail to meet specified requirements or expected behaviour.

### Failure

An observed deviation between actual system behaviour and expected behaviour during execution or operation.

### Error

A human action or decision that produces an incorrect result.

An error may introduce a defect, which may subsequently cause a failure.

### Defect Severity

The degree of impact a defect has on the system, users, business operations or other relevant stakeholders.

### Defect Priority

The relative urgency with which a defect should be addressed.

Severity and priority are related but distinct concepts.

### Risk

The potential for an uncertain event or condition to affect objectives.

In Quality Engineering, risks may relate to product behaviour, delivery, technical implementation, security, operations or user impact.

### Risk-Based Testing

An approach in which testing activities are prioritised according to assessed risks.

## 7. Coverage and Quality Metrics

### Test Coverage

A measure of the extent to which a defined scope has been exercised or addressed by testing.

Coverage may refer to requirements, risks, code, interfaces, scenarios or other defined elements.

A coverage percentage is meaningful only when its scope and calculation method are clear.

### Requirements Coverage

The extent to which approved requirements are addressed by relevant verification activities.

### Code Coverage

A measure of the extent to which source code is exercised by tests.

Examples include statement, branch and function coverage.

Code coverage does not independently demonstrate that requirements or business risks have been adequately tested.

### Test Effectiveness

An assessment of how well testing activities identify relevant defects and provide confidence in the product.

### Test Efficiency

An assessment of the resources and effort required to achieve useful testing outcomes.

### Flaky Test

An automated test that produces inconsistent results under apparently equivalent conditions without a corresponding change in the product behaviour being evaluated.

Flakiness may result from timing, shared state, environment instability, test data, dependencies or defects in the test itself.

### False Positive

A test result that indicates a failure when the behaviour being evaluated is actually correct.

### False Negative

A test result that indicates success when an actual defect or failure condition exists.

## 8. Automation and Engineering

### Test Automation

The use of software and automated mechanisms to execute checks, evaluate results and provide feedback about system behaviour.

### Automated Check

An automated evaluation of a specific condition or expected behaviour.

### Test Framework

A collection of libraries, utilities, conventions and infrastructure that supports the design, implementation, execution and maintenance of automated tests.

### Test Architecture

The structural organisation of test automation components, responsibilities, dependencies, interfaces and execution mechanisms.

### Test Reliability

The ability of testing activities and automated checks to produce consistent, trustworthy and reproducible results under defined conditions.

### Continuous Integration (CI)

The practice of frequently integrating code changes into a shared codebase and validating them through automated build and verification processes.

### Continuous Delivery (CD)

An approach in which software changes are kept in a deployable state and can be released through a controlled delivery process.

### Continuous Deployment

An approach in which changes that pass the required automated controls are deployed to production without a separate manual release decision.

Continuous delivery and continuous deployment are related but not interchangeable.

## 9. Quality Governance

### Quality Gate

A defined control point at which specified quality expectations and evidence are evaluated before a subsequent activity or decision is allowed to proceed.

### Definition of Ready (DoR)

A set of agreed conditions used to determine whether work is sufficiently understood and prepared to enter a particular stage of delivery.

### Definition of Done (DoD)

A shared set of conditions that work must satisfy before it is considered complete.

### Release Readiness

An assessment of whether a product or change is sufficiently verified, understood and controlled to be considered for release.

### Independent Review

An evaluation performed by someone other than the original author or producer of the work, with an appropriate degree of independence.

### Maker–Checker

A control principle in which one party produces or performs an activity and another party independently reviews or verifies it.

### Residual Risk

The risk that remains after applicable risk treatment or mitigation measures have been implemented.

## 10. AI-Assisted Engineering

### AI-Assisted Engineering

The use of artificial intelligence tools to support engineering activities such as analysis, design, implementation, testing, investigation and documentation.

### AI Agent

An AI-enabled system capable of carrying out one or more tasks through a defined set of instructions, tools and permissions.

### Human Oversight

The ability of an accountable person to supervise, evaluate, intervene in and, where necessary, stop AI-assisted or automated activities.

### AI-Generated Output

Any artefact or result produced wholly or partially by an AI system, including requirements interpretations, test cases, code, reports and recommendations.

### Human-in-the-Loop

An approach in which a human must participate in a defined activity or decision before it can proceed or be considered complete.

### Human-on-the-Loop

An approach in which a human supervises an activity while the system performs tasks, with the ability to intervene when necessary.

### Human-out-of-the-Loop

An approach in which a system operates without routine human intervention for a defined activity.

This approach requires appropriate authorisation, safeguards, monitoring and accountability according to the activity's risk.

## 11. Terminology Usage Rules

The following rules apply throughout this repository:

1. Terms SHOULD be used consistently with their definitions in this document.
2. Established industry terminology SHOULD be preferred over informal or ambiguous alternatives.
3. Acronyms MUST be expanded on first use in a document unless they are universally understood in the relevant context.
4. Where a term has multiple accepted meanings, the intended meaning MUST be made clear.
5. Project-specific terminology MUST be explicitly defined before it is used in normative requirements.
6. AI-generated documentation MUST use these definitions consistently and MUST NOT invent industry-standard definitions.

## 12. References

Terminology should be interpreted in alignment with relevant authoritative sources, including:

- ISO/IEC/IEEE 29119 — Software testing.
- ISO/IEC/IEEE 12207 — Software lifecycle processes.
- ISTQB Glossary of Testing Terms.
- ISO/IEC 25010 — Systems and software quality models.
- Agile Manifesto and established Agile practices.

The applicable editions and source links are maintained in:

`docs/quality-engineering/references/standards-and-frameworks.md`

Where an external standard defines a term differently from this project document, the relevant source and context should be examined before adopting a definition.

This document provides working terminology for the repository; it does not replace or reproduce the full terminology of external standards.
