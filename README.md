# Playwright Automation Framework

A TypeScript-based test automation framework built with Playwright, designed to support web UI and API testing, with a future extension for native mobile automation using Appium.

The project focuses on maintainability, reusability, scalability, and clear separation of responsibilities.

---

## Table of Contents

- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Code Quality](#code-quality)
- [Test Reporting](#test-reporting)
- [Test Strategy](#test-strategy)
- [CI/CD](#cicd)
- [Git Workflow & Commit Conventions](#git-workflow--commit-conventions)
- [Future Improvements](#future-improvements)

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Node.js | JavaScript runtime |
| TypeScript | Primary programming language |
| Yarn 4 | Package manager |
| Playwright | Web UI and API automation |
| ESLint | Static code analysis |
| Prettier | Code formatting |
| Allure | Test reporting |
| GitHub Actions | CI/CD |
| dotenv | Environment configuration |

### Current versions

| Tool | Version |
|---|---|
| Node.js | 24.14.0 |
| Yarn | 4.18.1 |
| Playwright | 1.64.1 |
| TypeScript | 5.9.3 |
| ESLint | 10.x |
| Prettier | 3.8.1 |
| Allure Playwright | 3.4.5 |

---

## Prerequisites

Before setting up the project, make sure you have:

- Node.js 24 or later
- Yarn 4
- Git
- An IDE (Visual Studio Code or IntelliJ IDEA recommended)

### Installing Homebrew (macOS)

Homebrew is a package manager for macOS that simplifies installing and managing development tools.

If Homebrew is not already installed, run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify the installation:

```bash
brew --version
```

### Installing Node.js

Install Node.js using Homebrew:

```bash
brew install node
```

Verify the installation:

```bash
node -v
npm -v
```

### Installing Yarn 4

Enable Corepack:

```bash
corepack enable
```

Activate the required Yarn version:

```bash
corepack prepare yarn@4.18.1 --activate
```

Verify:

```bash
yarn -v
```

The expected version is:

```text
4.18.1
```

---

## Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/marmiou/playwright-repo.git
```

Navigate into the project:

```bash
cd playwright-repo
```

### 2. Install dependencies

```bash
yarn install
```

### 3. Install Playwright browsers

```bash
yarn playwright install
```

This installs the browsers configured in the Playwright project:

- Chromium
- Firefox
- WebKit

For Linux environments, install the required browser system dependencies as well:

```bash
yarn playwright install --with-deps
```

### 4. Verify the installation

List the available tests:

```bash
yarn test --list
```

Run the test suite:

```bash
yarn test
```

---

## Project Structure

Current repository structure:

```text
playwright-repo/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── src/
│   ├── fixtures/
│   ├── pages/
│   └── utils/
│
├── tests/
│   └── example.spec.ts
│
├── .editorconfig
├── .gitignore
├── .yarnrc.yml
├── eslint.config.mjs
├── package.json
├── playwright.config.ts
├── tsconfig.json
├── yarn.lock
├── README.md
├── test-plan.md
└── test-data-strategy.md
```

### Directory responsibilities

| Directory | Responsibility |
|---|---|
| `src/fixtures` | Reusable Playwright fixtures |
| `src/pages` | Page Object Model implementation |
| `src/utils` | Shared helper functions |
| `tests` | Automated test scenarios |
| `.github/workflows` | CI/CD workflows |

The current structure is the initial framework foundation. The directories will be expanded as the framework evolves.

---

## Running Tests

Playwright supports multiple browsers and execution modes.

### Run all tests

```bash
yarn test
```

### Run tests in a specific browser

Chromium:

```bash
yarn test:chromium
```

Firefox:

```bash
yarn test:firefox
```

WebKit:

```bash
yarn test:webkit
```

### Run tests in headed mode

```bash
yarn test:headed
```

This opens the browser UI while tests are executing.

### Run tests in UI mode

```bash
yarn test:ui
```

Playwright UI mode provides an interactive interface for exploring and debugging tests.

### Run tests in debug mode

```bash
yarn test:debug
```

This launches Playwright Inspector and allows step-by-step test execution.

### View the HTML report

```bash
yarn test:report
```

---

## Code Quality

Code quality is maintained through TypeScript, ESLint, and Prettier.

### TypeScript

The project uses strict TypeScript settings to improve type safety and catch potential issues during development.

Run type checking:

```bash
yarn typecheck
```

### ESLint

ESLint performs static code analysis and enforces consistent coding practices.

Run linting:

```bash
yarn lint
```

Automatically fix supported issues:

```bash
yarn lint:fix
```

### Prettier

Prettier is used to maintain consistent code formatting.

Format the project:

```bash
yarn prettier --write .
```

Check formatting without modifying files:

```bash
yarn prettier --check .
```

---

## Test Reporting

The framework uses Allure Playwright for test reporting.

Allure collects test execution information and generates detailed reports containing test results, execution details, and failure information.

### Generate an Allure report

After test execution, the results are stored in:

```text
allure-results/
```

To generate an HTML report using the Allure Commandline:

```bash
yarn dlx allure-commandline generate allure-results --clean -o allure-report
```

Open the generated report:

```bash
yarn dlx allure-commandline open allure-report
```

Note: Allure Commandline may require Java to be installed.

---

## Test Strategy

The framework follows a structured approach to test automation, focusing on maintainability, risk coverage, and reliable feedback.

The test strategy is documented in:

- `test-plan.md`
- `test-data-strategy.md`

These documents describe the testing approach, scope, test coverage, and test data management principles.

### Planned testing layers

| Layer | Tool | Status |
|---|---|---|
| Web UI | Playwright | Foundation established |
| API | Playwright API | Planned |
| Native Android | Appium | Planned |
| Native iOS | Appium | Planned |

---

## CI/CD

The project uses GitHub Actions for continuous integration.

The workflow is located at:

```text
.github/workflows/playwright.yml
```

The CI pipeline is intended to execute automated tests and provide feedback on changes pushed to the repository.

The pipeline will evolve as the framework grows, including additional test execution, reporting, and potentially mobile automation.

---

## Git Workflow & Commit Conventions

This project follows [Conventional Commits](https://www.conventionalcommits.org/) to maintain a clear, consistent, and meaningful commit history.

### Commit message format

```text
<type>(<optional scope>): <description>
```

### Commit types

| Type | Purpose | Example |
|---|---|---|
| `feat` | Introduce new functionality | `feat: add API client` |
| `fix` | Fix a defect | `fix: resolve login issue` |
| `chore` | Maintenance and dependency updates | `chore: update dependencies` |
| `test` | Add or modify tests | `test: add login scenarios` |
| `refactor` | Improve code structure without changing behaviour | `refactor: reorganize fixtures` |
| `docs` | Documentation updates | `docs: update README` |
| `ci` | CI/CD pipeline changes | `ci: update GitHub Actions workflow` |
| `style` | Formatting-only changes | `style: apply Prettier formatting` |

### Examples

```bash
git commit -m "feat(web): add login page object"

git commit -m "feat(api): add authentication client"

git commit -m "test: add login scenarios"

git commit -m "refactor: improve test fixtures"

git commit -m "docs: update framework architecture"

git commit -m "ci: update GitHub Actions workflow"
```

### Guidelines

- Use the imperative mood (e.g. `add`, `update`, `fix`).
- Keep descriptions concise and meaningful.
- Use lowercase types and scopes.
- Avoid vague messages such as `updates`, `changes`, or `fixes`.
- Each commit should represent a logical change.

---

## Future Improvements

The framework is designed to evolve incrementally.

### 1. Web automation

- Introduce the Page Object Model.
- Implement reusable fixtures.
- Improve browser coverage.
- Introduce environment-specific configuration.
- Add authentication and session management.

### 2. API automation

- Create reusable API clients.
- Introduce request and response models.
- Implement API authentication.
- Add positive, negative, and contract-oriented test scenarios.
- Reuse API operations for test data setup and cleanup.

### 3. Mobile automation

Native mobile automation will be introduced as an independent layer using Appium 3 and TypeScript.

The intention is to support:

- Android native applications.
- iOS native applications.
- Reusable screen objects.
- Mobile-specific fixtures.
- Device and platform configuration.

Playwright will remain responsible for web and API automation. Appium will handle native mobile automation.

### 4. CI/CD improvements

- Separate web and API execution where appropriate.
- Introduce configurable browser and environment matrices.
- Improve test reporting and artifact retention.
- Evaluate mobile execution through simulators, emulators, and device clouds.

### 5. Framework maintainability

- Introduce shared test data builders.
- Improve logging and debugging.
- Establish consistent coding conventions.
- Evaluate automated commit message validation.
- Keep dependencies and framework abstractions as lightweight as possible.

---

## Project Philosophy

The framework follows a few core principles:

1. **Maintainability over complexity:** Avoid unnecessary abstractions and dependencies.
2. **Reusability where it makes sense:** Share common utilities, data, and configuration without coupling unrelated automation layers.
3. **Separation of concerns:** Keep web, API, and native mobile responsibilities independent.
4. **Reliability:** Prioritise stable, meaningful automated tests.
5. **Scalability:** Build a foundation that can evolve without requiring a complete redesign.
6. **Continuous improvement:** Introduce tools and patterns when they solve an actual problem.

