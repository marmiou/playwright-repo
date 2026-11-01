# AI-Assisted Quality Engineering

## 1. Purpose

This document defines how AI tools can support Quality Engineering activities throughout the Software Development Lifecycle (SDLC).

AI should improve analysis, efficiency, coverage and feedback without replacing engineering judgement, approved requirements or human accountability.

## 2. Principles

AI-assisted Quality Engineering MUST follow these principles:

- **Requirements first:** Use approved requirements and specifications as the basis for analysis and verification.
- **Human accountability:** AI outputs are recommendations or generated artefacts until appropriately reviewed and accepted.
- **Evidence over assumptions:** Conclusions must be supported by observable evidence.
- **Risk awareness:** AI assistance should focus on meaningful quality risks rather than maximising generated output.
- **Transparency:** Important assumptions, limitations and uncertainties must be visible.
- **Controlled adoption:** AI-generated changes must follow existing engineering, verification and review standards.

Agent permissions and restrictions are defined in `ai-agent-governance.md`.

## 3. Requirements Analysis

AI tools may assist with:

- Summarising approved requirements.
- Extracting functional and non-functional conditions.
- Identifying ambiguity, inconsistency and missing information.
- Suggesting clarification questions.
- Identifying dependencies and potential risks.
- Reviewing acceptance criteria for testability.
- Identifying traceability gaps.

AI MUST distinguish explicit requirements from inferred behaviour.

It MUST NOT invent business rules or silently resolve conflicting requirements.

Unresolved product decisions must be referred to the appropriate owner.

## 4. Test Strategy and Design

AI may support test design by:

- Identifying relevant test levels and test types.
- Suggesting risk-based testing priorities.
- Deriving test conditions and scenarios.
- Applying equivalence partitioning and boundary value analysis.
- Identifying decision table combinations and state transitions.
- Suggesting positive, negative and boundary cases.
- Identifying integration and regression risks.
- Reviewing test coverage and traceability.
- Suggesting exploratory testing charters.

Generated scenarios and expected results must be evaluated against authoritative requirements.

## 5. Test Automation

AI may assist with:

- Creating Playwright and TypeScript tests.
- Suggesting maintainable test structures.
- Identifying reusable fixtures and utilities.
- Developing API and web automation.
- Improving locator strategies.
- Generating test data and models.
- Refactoring duplicated code.
- Improving assertions and diagnostics.
- Reviewing TypeScript correctness and maintainability.

Generated automation MUST follow the repository's established standards.

AI MUST NOT:

- Generate assertions based solely on observed implementation behaviour.
- Replace meaningful assertions with weaker checks.
- Introduce arbitrary waits to conceal synchronisation problems.
- Add indiscriminate retries to hide flaky behaviour.
- Create dependencies between tests without justification.
- Introduce unnecessary abstractions or duplicated utilities.

Detailed implementation guidance is defined in `../engineering-practices/test-automation-standards.md`.

## 6. Test Review

AI may support independent review by evaluating:

- Alignment with approved requirements.
- Completeness of scenarios.
- Assertion quality and expected results.
- Test isolation and determinism.
- Locator and API interaction strategies.
- Error handling and diagnostics.
- Maintainability and duplication.
- Potential regressions and missing coverage.

AI review findings must be supported by the actual code and relevant evidence.

An AI agent reviewing its own implementation does not constitute independent review where separation of duties is required.

## 7. Failure Investigation

AI may assist with:

- Analysing test failures and execution logs.
- Reviewing Playwright traces, screenshots and reports.
- Identifying likely root causes.
- Distinguishing product defects from test defects and environment failures.
- Identifying flaky behaviour and synchronisation issues.
- Comparing failures across executions.
- Suggesting targeted corrective actions.

AI-generated root-cause analysis must be treated as a hypothesis until supported by evidence.

A test failure must not be classified as an infrastructure issue merely because the cause is unclear.

Detailed investigation practices are defined in `../workflows/failure-investigation.md`.

## 8. Test Data and Quality Risks

AI may assist with:

- Identifying test data requirements.
- Generating representative synthetic data.
- Suggesting boundary and invalid values.
- Identifying data dependencies and isolation risks.
- Reviewing setup and cleanup strategies.
- Identifying privacy and security concerns.

Generated data must remain appropriate for the target environment.

Sensitive production information must not be exposed to unapproved AI services.

Detailed data management practices are defined in `../engineering-practices/test-data-management.md`.

## 9. Documentation and Knowledge Management

AI may help create and maintain:

- Test documentation.
- Technical explanations.
- Review findings.
- Investigation summaries.
- Architecture documentation.
- Quality reports.
- Traceability records.

Generated documentation must be checked for accuracy, consistency and alignment with the actual implementation.

AI must not present unverified information as established repository behaviour.

## 10. Measuring Value

The value of AI-assisted QE should be evaluated through meaningful outcomes, such as:

- Reduced time spent on repetitive analysis.
- Improved identification of missing scenarios.
- Better requirement-to-test traceability.
- Reduced investigation time.
- Improved test maintainability.
- Earlier detection of defects.
- More consistent documentation.
- Improved feedback during development.

The number of generated tests, lines of code or AI interactions is not, by itself, evidence of improved quality.

AI-generated output that increases maintenance effort, introduces defects or weakens verification does not represent a quality improvement.

## 11. Continuous Improvement

AI-assisted practices SHOULD be reviewed using execution evidence, engineering feedback and observed outcomes.

Useful improvements may include:

- Refining prompts and agent instructions.
- Improving context provided to agents.
- Updating reusable skills.
- Improving review criteria.
- Reducing recurring generation errors.
- Identifying tasks where AI adds insufficient value.

Changes to shared agent instructions, permissions or quality controls must follow the applicable governance and review process.

## 12. Related Guidance

- `ai-agent-governance.md`
- `../lifecycle/requirements-engineering.md`
- `../lifecycle/test-strategy-and-design.md`
- `../engineering-practices/test-automation-standards.md`
- `../engineering-practices/test-data-management.md`
- `../engineering-practices/test-reliability.md`
- `../governance/maker-checker-and-independent-review.md`
- `../engineering-practices/continuous-improvement.md`
