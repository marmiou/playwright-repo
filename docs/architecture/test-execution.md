# Test Execution

## 1. Purpose

This document describes how automated tests are configured, executed and reported within the Playwright and TypeScript framework.

It covers local and CI execution, test selection, parallelism, configuration, reporting and execution evidence.

It complements the Quality Engineering workflows, which define how tests are designed, implemented and investigated.

## 2. Execution Model

The framework uses Playwright Test to execute web and API tests.

Tests are organised by test type:

- `tests/web/` — web application tests.
- `tests/api/` — API tests.

Execution is controlled through `playwright.config.ts` and the scripts defined in `package.json`.

The same configuration principles should apply locally and in CI to support consistent and reproducible results.

## 3. Execution Environments

Tests may run in the following contexts:

| Environment | Purpose |
|---|---|
| Local | Development, debugging and targeted verification. |
| CI | Automated validation of changes and regression coverage. |
| Target test environment | Verification against an agreed application and service deployment. |

Environment-specific values must be supplied through configuration or environment variables.

Secrets must never be committed to the repository or exposed in execution logs and reports.

## 4. Test Selection

Tests should be selected according to the purpose of the execution.

Common execution scopes include:

- A single test.
- A specific test file.
- A test directory or suite.
- Tests matching a configured tag or project.
- The full regression suite.

Prefer targeted execution during development and broader regression execution at appropriate CI or release stages.

Test selection must not silently exclude relevant coverage from required quality gates.

## 5. Local Execution

Use the repository's package scripts as the standard entry point for test execution.

Typical Playwright commands include:

```bash
yarn playwright test
yarn playwright test tests/web
yarn playwright test tests/api
yarn playwright test --list
yarn playwright test --debug
yarn playwright show-report
```

The actual supported commands and scripts must be maintained in `package.json`.

Use the configured test environment and ensure required services, credentials and test data are available before execution.

## 6. Parallel Execution

Playwright supports parallel test execution.

Parallelism should be configured according to:

- Available execution resources.
- Environment capacity.
- Test data isolation.
- Application and service stability.
- External dependency limits.

Tests must not depend on execution order or shared mutable state.

Tests that cannot safely run in parallel must have their constraints explicitly documented and addressed through an appropriate execution strategy.

Reducing parallelism may help diagnose resource or concurrency issues, but must not conceal test isolation defects.

## 7. Configuration

Execution configuration is managed through `playwright.config.ts` and environment-specific settings.

Relevant configuration may include:

- Test directories and discovery patterns.
- Browser and project selection.
- Base URLs and API endpoints.
- Timeouts and expectations.
- Worker count and parallelism.
- Retries.
- Reporters and output directories.
- Trace, screenshot and video capture.
- Environment-specific configuration.

Configuration changes must be reviewed and verified.

Retries and timeouts must be deliberate and evidence-based. They must not be used to hide unstable tests or application defects.

## 8. Reporting and Evidence

Execution must produce sufficient information to understand its outcome.

Depending on configuration, evidence may include:

- Passed, failed, skipped and interrupted test counts.
- Playwright HTML reports.
- Error messages and stack traces.
- Screenshots.
- Browser traces.
- Relevant logs.
- CI execution results.

Reports and artifacts must be accessible to the appropriate reviewers while respecting data protection and security requirements.

A test execution result must accurately reflect the actual outcome.

## 9. CI Execution

CI execution should provide repeatable verification for relevant repository changes.

The pipeline may include:

1. Dependency installation.
2. Static checks and TypeScript validation.
3. Test discovery or configuration validation.
4. Relevant web and API test execution.
5. Report and artifact publication.
6. Pipeline result evaluation.

CI quality gates must reflect the agreed project requirements.

A failed, interrupted or incomplete required check must not be reported as successful.

The workflow configuration is maintained in `.github/workflows/playwright.yml`.

## 10. Execution Outcomes

Execution results must distinguish between:

| Outcome | Meaning |
|---|---|
| PASS | Required tests completed successfully. |
| FAIL | One or more required tests failed. |
| BLOCKED | Execution could not be completed because of missing prerequisites or unavailable dependencies. |
| INTERRUPTED | Execution was stopped or terminated before completion. |

Skipped tests must remain visible in reports and must not be counted as passing tests.

A successful pipeline does not automatically prove that all product risks have been addressed.

## 11. Related Guidance

- `overview.md`
- `../quality-engineering/workflows/automation-implementation.md`
- `../quality-engineering/workflows/failure-investigation.md`
- `../quality-engineering/engineering-practices/test-reliability.md`
- `../quality-engineering/engineering-practices/test-automation-standards.md`
- `../../.github/workflows/playwright.yml`
- `../../playwright.config.ts`
- `../../package.json`
