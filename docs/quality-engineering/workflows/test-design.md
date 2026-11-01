# Test Design Workflow

## 1. Purpose

This workflow defines how approved requirements and acceptance criteria are translated into structured, risk-based test scenarios and cases.

It applies to functional, non-functional, API, web, integration and regression testing.

The objective is to establish what needs to be verified, under which conditions and with which expected results before automation or execution begins.

## 2. Principles

- Test design MUST be based on approved requirements.
- Expected results MUST be traceable to an authoritative source.
- Coverage SHOULD be risk-based.
- Positive, negative and boundary conditions SHOULD be considered.
- Tests MUST verify behaviour rather than implementation details unless technical behaviour is explicitly required.
- Missing expected behaviour must be clarified, not invented.
- Test design and automation implementation are separate activities.

## 3. Test Design Workflow

**UNDERSTAND → IDENTIFY RISKS → DEFINE COVERAGE → DESIGN → REVIEW → BASELINE**

### Step 1: UNDERSTAND

Review the approved requirements and acceptance criteria.

Identify:

- Intended behaviour and business rules.
- Preconditions and postconditions.
- Inputs, outputs and state transitions.
- User roles and permissions.
- Relevant integrations and dependencies.
- Functional and non-functional expectations.
- Constraints and known limitations.

Clarify ambiguities before defining expected results.

### Step 2: IDENTIFY RISKS

Assess what could fail and the potential impact.

Consider:

- Business and user impact.
- Critical workflows.
- Data integrity and consistency.
- Security and access control.
- Integration and dependency risks.
- Error handling and recovery.
- Regression impact.

Use risk to determine testing depth and priority.

### Step 3: DEFINE COVERAGE

Identify the scenarios needed to verify the requirements.

Consider:

- Positive and negative scenarios.
- Boundary and edge conditions.
- Input validation.
- Business rules and decision paths.
- Permissions and roles.
- State transitions.
- Error and recovery behaviour.
- Integration behaviour.
- Relevant non-functional requirements.
- Regression scenarios.

Avoid unnecessary duplication while ensuring important risks are covered.

### Step 4: DESIGN

Translate coverage into clear, verifiable test scenarios and cases.

Each test should define, where applicable:

- Requirement or acceptance criterion.
- Scenario and objective.
- Preconditions.
- Test data.
- Actions or conditions.
- Expected results.
- Relevant dependencies.
- Priority or risk classification.

Expected results must be objective and observable.

Apply suitable test design techniques where useful:

- Equivalence partitioning.
- Boundary value analysis.
- Decision tables.
- State transition testing.
- Use-case and scenario testing.
- Pairwise or combinatorial testing.
- Exploratory testing.

Select techniques according to the behaviour and risk being evaluated.

### Step 5: REVIEW

Review the test design for:

- Requirement alignment and traceability.
- Coverage of relevant risks.
- Correctness of expected results.
- Positive, negative and boundary conditions.
- Completeness of preconditions and test data.
- Clarity and repeatability.
- Unnecessary duplication.
- Feasibility of execution or automation.

Resolve findings before baselining the design.

Independent review must follow the applicable Maker–Checker governance requirements.

### Step 6: BASELINE

Establish the reviewed test design as the reference for execution and automation.

Maintain traceability between:

- Approved requirements.
- Acceptance criteria.
- Test scenarios and cases.
- Automated tests, where applicable.
- Defects and relevant changes.

When requirements change, reassess affected test designs and update them through the authorised change process.

## 4. Handling Gaps

If test design reveals missing, ambiguous or conflicting expected behaviour:

1. Record the gap.
2. Identify the affected requirement.
3. Raise the question with the authorised owner.
4. Obtain an approved clarification.
5. Update the test design accordingly.

QA and AI must not invent expected behaviour or change approved requirements.

If a gap prevents reliable test design, the affected work must remain BLOCKED.

## 5. AI-Assisted Test Design

AI tools may assist with:

- Analysing requirements.
- Suggesting scenarios and edge cases.
- Identifying coverage gaps.
- Applying test design techniques.
- Reviewing test cases for clarity and completeness.
- Suggesting risk classifications.

AI-generated scenarios and expected results must be validated against approved requirements.

AI MUST NOT invent business rules, approve test designs or silently alter expected behaviour.

## 6. Exit Criteria

Test design is complete when:

- Approved requirements have been analysed.
- Relevant risks and coverage have been identified.
- Test scenarios and expected results are documented.
- Test data and preconditions are understood.
- Traceability is established.
- Review requirements have been satisfied.
- Outstanding gaps and limitations are documented.

The resulting test design can proceed to execution planning or automation implementation.

## 7. Related Guidance

- `../lifecycle/test-strategy-and-design.md`
- `../lifecycle/requirements-engineering.md`
- `requirements-analysis.md`
- `automation-implementation.md`
- `independent-review.md`
- `../engineering-practices/test-data-management.md`
- `../governance/quality-gates-and-readiness.md`
- `../governance/maker-checker-and-independent-review.md`
