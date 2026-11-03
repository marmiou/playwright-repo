# AI-Assisted Quality Engineering Framework

A TypeScript automation framework using Playwright for web UI and API testing, supported by a risk-based Quality Engineering approach and governed AI-assisted development workflows.

The project combines the Software Testing Life Cycle (STLC)—requirements, risk assessment, test design, execution and evaluation—with the Software Development Life Cycle (SDLC)—architecture, implementation, review and maintenance.

The objective is not simply to generate tests. It is to build reliable, maintainable automation that provides meaningful product-quality feedback while keeping decisions evidence-based and human-accountable.

> **Status:** The automation foundation, architecture boundaries and shared AI-agent instructions are established. The reusable skills and specialist-agent workflows are being developed incrementally. Documented or planned capabilities should not be interpreted as completed implementations.

---

## Contents

- [Objectives](#objectives)
- [Technology Stack](#technology-stack)
- [Current Status](#current-status)
- [Quality Engineering Workflow](#quality-engineering-workflow)
- [AI Assistance and Governance](#ai-assistance-and-governance)
- [Project Structure](#project-structure)
- [Prerequisites and Setup](#prerequisites-and-setup)
- [Running Tests](#running-tests)
- [Code Quality](#code-quality)
- [Test Reporting](#test-reporting)
- [Configuration and Security](#configuration-and-security)
- [Native Mobile Automation](#native-mobile-automation)
- [Git Workflow](#git-workflow)
- [Roadmap](#roadmap)

## Objectives

- Build maintainable web UI and API automation with Playwright and TypeScript.
- Keep web, API, shared and future native mobile responsibilities separate.
- Derive test coverage from requirements, acceptance criteria and risk.
- Prefer independent, deterministic tests with meaningful assertions.
- Use AI to assist analysis, design, implementation and review without delegating human accountability.
- Make implementation decisions traceable to acceptance criteria and validation evidence.

## Technology Stack

| Technology | Purpose |
|---|---|
| Node.js | JavaScript runtime |
| TypeScript | Primary language |
| Yarn 4 | Package manager |
| Playwright | Web UI and API automation |
| ESLint | Static analysis |
| Prettier | Code formatting |
| Allure Playwright | Test reporting |
| dotenv | Environment-variable loading support |
| GitHub Actions | CI automation (where configured) |
| Claude Code | AI-assisted engineering |

### Current dependency versions

| Tool | Version |
|---|---|
| Node.js | 24.14.0 |
| Yarn | 4.18.1 |
| Playwright | 1.64.1 |
| TypeScript | 5.9.3 |
| ESLint | 10.x |
| Prettier | 3.8.1 |
| Allure Playwright | 3.4.5 |

Dependency declarations are maintained in `package.json` and `yarn.lock`.

## Current Status

| Area | Status |
|---|---|
| Playwright / TypeScript foundation | Configured |
| Chromium, Firefox and WebKit projects | Configured |
| Web test directory | Established at `tests/web/` |
| API test directory | Established at `tests/api/`; coverage is evolving |
| Source boundaries | `src/web/`, `src/api/`, `src/shared/`, `src/fixtures/` |
| Type checking and linting | Configured |
| HTML and Allure reporting | Configured |
| Shared QE and agent instructions | Defined in `AGENTS.md` |
| Claude Code instructions | Defined in `CLAUDE.md` |
| Maker–Checker governance | Defined; operational reviewer workflow is in progress |
| Reusable skills and specialist agents | In progress |
| Native mobile automation | Future independent Appium implementation |

A directory or documented workflow does not, by itself, indicate a complete implementation or test suite. The executable code and tests in the repository are the source of truth for implementation status.

## Quality Engineering Workflow

The workflow is risk-based and proportionate to the task. Not every change requires every phase.

1. **Requirement analysis**
   - Understand the objective, scope and acceptance criteria.
   - Identify ambiguity, assumptions, dependencies and constraints.
   - Ask for clarification when missing information materially affects correctness.
   - Do not invent business rules or expected behaviour.

2. **Test planning and risk assessment**
   - Identify relevant test levels and types.
   - Prioritise scenarios by likelihood, impact and risk.
   - Identify environments, dependencies and test-data needs.
   - Define the evidence needed to demonstrate acceptance.

3. **Test design**
   - Derive scenarios from requirements and risks.
   - Define preconditions, actions and observable expected outcomes.
   - Consider positive, negative, boundary, edge and failure paths.
   - Maintain requirement-to-test traceability where useful.

4. **Automation design and implementation**
   - Inspect existing architecture, fixtures and conventions.
   - Keep web and API concerns separate.
   - Use resilient locators, meaningful assertions and typed models.
   - Keep tests readable, independent and deterministic.
   - Avoid arbitrary waits, duplicated logic and unnecessary abstractions.

5. **Verification**
   - Run targeted tests and applicable regression tests.
   - Run TypeScript checks and ESLint where relevant.
   - Inspect failures, traces and reports.
   - Distinguish product defects from automation and environment failures.
   - Never report a check as passed unless it was actually run and passed.

6. **Independent review — Maker–Checker**
   - **Maker:** analyses, designs and implements the agreed change, then reports evidence and limitations.
   - **Checker:** independently inspects the implementation against the original task and acceptance criteria.
   - The Checker evaluates correctness, coverage, assertions, maintainability, reliability, security and validation evidence.
   - A self-review in the same working context must not be represented as independent verification.

   Review outcomes:

   | Outcome | Meaning |
   |---|---|
   | PASS | Mandatory criteria and applicable quality checks are satisfied |
   | FAIL | One or more criteria are not satisfied; actionable findings are provided |
   | BLOCKED | Review cannot be completed because requirements, access or dependencies are missing |

   After corrections, the changed implementation is reviewed again.

7. **Quality evaluation and closure**
   - Confirm which acceptance criteria have been met.
   - Report remaining risks, gaps and limitations.
   - Identify flaky tests, automation defects and improvement opportunities.
   - Close the task only when its applicable Definition of Done is satisfied.

## AI Assistance and Governance

AI is an engineering assistant, not an authority on product behaviour or a replacement for human accountability.

- `AGENTS.md` contains shared engineering principles, architecture boundaries, the QE lifecycle, Maker–Checker expectations and Definition of Done.
- `CLAUDE.md` contains Claude Code-specific working instructions and imports the shared instructions from `AGENTS.md`.
- Reusable skills and specialist agents are being developed to operationalise the workflow without duplicating governance rules.

Core principles:

- Requirements first; do not invent business rules.
- Human accountability for scope, risk acceptance and decisions.
- Evidence over assumptions; disclose unrun checks and limitations.
- Independent verification for meaningful implementation tasks.
- Least privilege for tools, agents and external systems.
- Quality over test count; prioritise meaningful coverage.
- Never hide failures, weaken assertions or add arbitrary retries and waits just to obtain a passing result.

## Project Structure

```text
playwright-repo/
├── AGENTS.md
├── CLAUDE.md
├── docs/
│   ├── architecture/
│   └── quality-engineering/
├── mobile/
├── src/
│   ├── api/
│   ├── fixtures/
│   ├── shared/
│   └── web/
├── tests/
│   ├── api/
│   └── web/
├── eslint.config.mjs
├── package.json
├── playwright.config.ts
├── tsconfig.json
├── yarn.lock
└── README.md
```

Generated/local directories such as `node_modules/`, `test-results/`, `playwright-report/` and `allure-results/` are omitted.

| Path | Responsibility |
|---|---|
| `src/web/` | Web page objects, components and supporting abstractions |
| `src/api/` | API clients, models and supporting abstractions |
| `src/shared/` | Utilities, data and configuration genuinely shared across layers |
| `src/fixtures/` | Shared Playwright fixtures |
| `tests/web/` | Web UI scenarios |
| `tests/api/` | API scenarios |
| `mobile/` | Reserved for independent native mobile automation |
| `docs/architecture/` | Architecture and design documentation |
| `docs/quality-engineering/` | QE strategy, governance and engineering guidance |
| `AGENTS.md` | Shared instructions for agents and contributors |
| `CLAUDE.md` | Claude Code-specific instructions |

## Prerequisites and Setup

Prerequisites:

- Node.js 24.14.0 or a compatible Node.js 24 release
- Yarn 4.18.1 through Corepack
- Git
- An IDE such as Visual Studio Code or IntelliJ IDEA

On macOS, Node.js can be installed with Homebrew:

```bash
brew install node
```

Enable Corepack and activate the project Yarn version:

```bash
corepack enable
corepack prepare yarn@4.18.1 --activate
yarn --version
```

Clone the repository and install dependencies:

```bash
git clone https://github.com/marmiou/playwright-repo.git
cd playwright-repo
yarn install
```

Install Playwright browsers:

```bash
yarn playwright install
```

On Linux, install browser system dependencies too:

```bash
yarn playwright install --with-deps
```

Check test discovery and run the suite:

```bash
yarn test --list
yarn test
```

## Running Tests

Run the full suite:

```bash
yarn test
```

Run a browser project:

```bash
yarn test:chromium
yarn test:firefox
yarn test:webkit
```

Run in headed, UI or debug mode:

```bash
yarn test:headed
yarn test:ui
yarn test:debug
```

Run one test file (replace the example path as needed):

```bash
yarn playwright test tests/web/example.spec.ts
```

Open the Playwright HTML report:

```bash
yarn test:report
```

## Code Quality

TypeScript type checking:

```bash
yarn typecheck
```

ESLint:

```bash
yarn lint
yarn lint:fix
```

Prettier formatting:

```bash
yarn prettier --check .
yarn prettier --write .
```

## Test Reporting

The Playwright configuration enables the HTML reporter and Allure Playwright reporter.

- Playwright HTML report data is written to `playwright-report/`.
- Allure result files are written to `allure-results/`.

Generate and open an Allure report with the Allure Commandline:

```bash
yarn dlx allure-commandline generate allure-results --clean -o allure-report
yarn dlx allure-commandline open allure-report
```

The Allure Commandline may require Java. Report and result directories are generated execution artifacts, not source code.

## Configuration and Security

The current `playwright.config.ts` configures:

- `tests/` as the test discovery directory.
- Chromium, Firefox and WebKit projects.
- Parallel execution locally.
- CI-aware retries and worker settings through the `CI` environment variable.
- HTML and Allure reporters.
- Trace collection on the first retry.

The `dotenv` package is listed as a dependency, but loading an environment file is currently commented out in `playwright.config.ts`. Enable and document it when environment-based configuration is introduced.

Never commit credentials, tokens, `.env` files or authentication state. Use environment variables or an approved secret store for sensitive configuration. Do not access production systems or modify production data without explicit authorisation.

## Native Mobile Automation

Native mobile automation is intentionally separate from Playwright. The planned stack is Appium 3 with TypeScript, supporting Android and iOS applications, screen objects, mobile-specific fixtures and device execution.

Playwright remains responsible for web UI and API automation. Appium will own native mobile execution. Do not couple Appium execution to the Playwright Test runner without an explicit architecture decision.

## Git Workflow

The project follows [Conventional Commits](https://www.conventionalcommits.org/).

Format:

```text
<type>(<optional scope>): <description>
```

Examples:

```bash
git commit -m "feat(api): add users client"
git commit -m "test(web): cover checkout validation"
git commit -m "fix(web): stabilise dialog locator"
git commit -m "refactor(fixtures): simplify setup"
git commit -m "docs: update quality workflow"
git commit -m "chore: update dependencies"
```

Use imperative descriptions, lowercase types and scopes, and concise messages. Each commit should represent a logical change.

## Roadmap

1. **Representative automation coverage**
   - Add meaningful web UI scenarios against a stable target application.
   - Add API scenarios for successful, invalid and boundary requests.
   - Introduce reusable page objects, API clients and fixtures where justified.
   - Make test data and environment configuration explicit.

2. **Operational AI-assisted workflow**
   - Implement requirement-analysis and risk-based test-design skills.
   - Complete web and API implementation skills.
   - Implement verification and structured review skills.
   - Define the Test Architect and Test Reviewer specialist agents.
   - Make Maker–Checker review evidence-based and independent.

3. **Execution and diagnostics**
   - Improve test data setup and cleanup.
   - Improve failure diagnostics and reporting.
   - Strengthen CI execution and artifact handling.
   - Review isolation and reliability as coverage grows.

4. **Native mobile**
   - Establish the independent Appium 3 and TypeScript foundation.
   - Add Android and iOS execution.
   - Define device, platform and reporting strategies.

---

## Project Principles

1. Quality before automation: understand requirements and risks first.
2. Maintainability over complexity: avoid unnecessary abstractions and dependencies.
3. Meaningful coverage over test count: automate scenarios that provide useful feedback.
4. Separation of concerns: keep web, API and mobile responsibilities independent.
5. Reliability: favour deterministic tests and useful diagnostics.
6. Evidence-based decisions: distinguish verified facts from assumptions.
7. Human accountability: people remain responsible for decisions and risk acceptance.
8. Continuous improvement: evolve the framework in response to real needs.
