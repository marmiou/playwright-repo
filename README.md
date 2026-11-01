# Playwright Test Automation Framework

A scalable, maintainable test automation framework built with **Playwright and TypeScript**. The goal is to support web UI and API automation, with a modular architecture that can later be extended to native Android and iOS automation using Appium.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Prerequisites](#prerequisites)
4. [Environment Setup](#environment-setup)
5. [Clone the Repository](#clone-the-repository)
6. [Install Dependencies](#install-dependencies)
7. [Project Structure](#project-structure)
8. [Running Tests](#running-tests)
9. [Debugging Tests](#debugging-tests)
10. [TypeScript](#typescript)
11. [Code Quality and Formatting](#code-quality-and-formatting)
12. [Test Reporting with Allure](#test-reporting-with-allure)
13. [Test Architecture and Design Principles](#test-architecture-and-design-principles)
14. [Test Data Strategy](#test-data-strategy)
15. [CI/CD Integration](#cicd-integration)
16. [Future Enhancements](#future-enhancements)

---

## Project Overview

This repository contains a test automation framework designed around the following principles:

- Maintainability and reusability.
- Clear separation of test logic and application interaction.
- Scalable architecture for different testing layers.
- Reusable fixtures and utilities.
- Reliable test execution across multiple browsers.
- Integration with CI/CD pipelines.
- Consistent reporting and test diagnostics.

The framework currently provides a Playwright and TypeScript foundation with Chromium, Firefox and WebKit browser projects.

API automation and native mobile automation are planned extensions.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Node.js 24 | JavaScript runtime |
| TypeScript 5.9 | Programming language |
| Playwright 1.64 | Browser automation and test runner |
| Yarn 4 | Package manager |
| ESLint 10 | Static analysis and code quality |
| Prettier 3 | Code formatting |
| Allure Playwright | Test reporting |
| GitHub Actions | CI/CD |
| dotenv | Environment configuration |

### Planned technologies

| Technology | Purpose |
|---|---|
| Playwright APIRequestContext | API testing |
| Appium | Native Android and iOS automation |
| XCUITest | iOS automation backend |
| UiAutomator2 | Android automation backend |

---

## Prerequisites

The following tools are required:

- macOS
- Homebrew
- Node.js 24.x
- Yarn 4.x
- Git
- An IDE such as Visual Studio Code or IntelliJ IDEA

### 1. Install Homebrew

Homebrew is a package manager for macOS.

If it is not already installed, run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify the installation:

```bash
brew --version
```

### 2. Install Node.js

Install Node.js using Homebrew:

```bash
brew install node
```

Verify the installation:

```bash
node -v
npm -v
```

The project has been set up and tested with Node.js `v24.14.0`.

### 3. Install Yarn

Enable Corepack:

```bash
corepack enable
```

Install the project-compatible Yarn version:

```bash
corepack prepare yarn@4.18.1 --activate
```

Verify:

```bash
yarn -v
```

Expected version:

```text
4.18.1
```

The repository also specifies its package manager version in `package.json`.

---

## Clone the Repository

Clone the project:

```bash
git clone https://github.com/marmiou/playwright-repo.git
```

Navigate to the project directory:

```bash
cd playwright-repo
```

Verify the repository:

```bash
git status
```

---

## Install Dependencies

Install all project dependencies:

```bash
yarn install
```

Install Playwright browser binaries:

```bash
yarn playwright install
```

To install the browser dependencies required by Playwright on Linux CI environments:

```bash
yarn playwright install --with-deps
```

Note: `--with-deps` is primarily intended for Linux environments. On macOS, `yarn playwright install` is sufficient for the browser installation.

---

## Project Structure

The repository follows a modular structure. Some directories are currently placeholders for future framework components.

```text
playwright-repo/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── src/
│   ├── fixtures/          # Shared test fixtures (planned)
│   ├── pages/             # Page Object Models (planned)
│   └── utils/             # Shared utilities (planned)
│
├── tests/
│   └── example.spec.ts    # Initial Playwright tests
│
├── .editorconfig
├── .gitignore
├── .yarnrc.yml
├── eslint.config.mjs
├── package.json
├── playwright.config.ts
├── README.md
├── test-data-strategy.md
├── test-plan.md
├── tsconfig.json
└── yarn.lock
```

### Directory responsibilities

**src/fixtures**

Reusable Playwright fixtures, test setup and teardown, and shared test context.

**src/pages**

Page Object Models (POM), encapsulating page locators and user interactions.

**src/utils**

Reusable helper functions, configuration utilities and common framework functionality.

**tests**

Test specifications organized by feature or application area.

---

## Running Tests

Playwright supports Chromium, Firefox and WebKit.

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

### Run tests with a visible browser

By default, Playwright executes tests in headless mode.

To open the browser during execution:

```bash
yarn test:headed
```

### Open Playwright UI Mode

```bash
yarn test:ui
```

UI Mode provides an interactive interface for running, inspecting and debugging tests.

---

## Debugging Tests

Playwright provides several debugging options.

### Debug Mode

```bash
yarn test:debug
```

This opens the Playwright Inspector, allowing you to step through test execution.

### Run a specific test file

```bash
yarn playwright test tests/example.spec.ts
```

### Run tests by name

```bash
yarn playwright test -g "has title"
```

### Run with trace

The current configuration uses:

```typescript
trace: 'on-first-retry'
```

This means Playwright records a trace when a test is retried after failure.

---

## TypeScript

The project uses TypeScript with strict type checking.

Run the type checker:

```bash
yarn typecheck
```

The command executes:

```bash
tsc --noEmit
```

The TypeScript compiler checks the project without generating JavaScript output.

TypeScript configuration is maintained in `tsconfig.json`.

---

## Code Quality and Formatting

### ESLint

ESLint is configured using the modern Flat Config format.

Configuration file:

```text
eslint.config.mjs
```

Run linting:

```bash
yarn lint
```

Automatically fix supported issues:

```bash
yarn lint:fix
```

The configuration includes:

- ESLint recommended rules.
- TypeScript ESLint recommended rules.
- Playwright-specific linting rules.
- Node.js global definitions.

### Prettier

Prettier is included for consistent code formatting.

Format a specific file:

```bash
yarn prettier --write tests/example.spec.ts
```

Check formatting:

```bash
yarn prettier --check .
```

---

## Test Reporting with Allure

The framework uses `allure-playwright` to generate test execution results.

Allure results are written to:

```text
allure-results/
```

This directory is generated during test execution and should not be committed to Git.

### Generate Allure results

Run the tests:

```bash
yarn test
```

### Open the Allure report

If the Allure command-line tool is installed:

```bash
allure serve allure-results
```

The command generates and opens a local interactive report.

The Allure CLI is a separate tool from the `allure-playwright` npm package. Install it separately if you want to use the `allure` command.

---

## Test Architecture and Design Principles

The framework aims to follow these design principles.

### Page Object Model

Page Object Model will be used to separate page interactions from test specifications.

Responsibilities:

- Encapsulate locators.
- Provide reusable page actions.
- Keep tests focused on business behavior.
- Reduce duplication.
- Improve maintainability.

### Fixtures

Playwright fixtures will be used for:

- Shared setup and teardown.
- Page and browser configuration.
- Authentication and test context.
- Reusable test dependencies.

### Test Organization

Tests should be grouped by feature or functional area rather than by implementation details.

### Test Independence

Tests should be independent and repeatable.

Avoid dependencies between test cases and minimize shared mutable state.

---

## Test Data Strategy

Test data should be managed separately from test implementation.

The repository includes:

```text
test-data-strategy.md
```

The intended strategy is to support:

- Reusable test data.
- Environment-specific configuration.
- Data-driven testing where appropriate.
- Controlled test data creation and cleanup.
- Avoiding hardcoded credentials or sensitive information.

Environment variables should be stored in local `.env` files and excluded from Git.

Example:

```text
BASE_URL=https://example.com
API_BASE_URL=https://api.example.com
```

Never commit credentials, access tokens or secrets.

---

## CI/CD Integration

The repository includes a GitHub Actions workflow:

```text
.github/workflows/playwright.yml
```

The intended CI pipeline should support:

1. Dependency installation.
2. Playwright browser installation.
3. TypeScript validation.
4. ESLint checks.
5. Automated test execution.
6. Test artifact collection.
7. Report generation.

The workflow should be updated as the framework evolves to include linting and type checking alongside browser tests.

---

## Future Enhancements

The framework will evolve incrementally.

### Web UI Automation

- Page Object Model.
- Custom fixtures.
- Authentication handling.
- Environment configuration.
- Reusable components.
- Cross-browser execution.

### API Automation

- API client abstraction.
- Request and response validation.
- Reusable API fixtures.
- API test data management.
- Authentication and authorization testing.

Playwright's `APIRequestContext` will be used for API automation, allowing UI and API tests to share the same TypeScript ecosystem.

### Mobile Automation

Native mobile automation is planned using Appium.

The intended architecture will separate mobile automation from Playwright browser automation while allowing shared utilities, configuration and test data where appropriate.

Planned capabilities:

- Android automation using UiAutomator2.
- iOS automation using XCUITest.
- Mobile screen objects.
- Device and platform configuration.
- Reusable mobile fixtures.

Playwright browser automation and native mobile automation will use separate execution tools.

---

## Development Workflow

Before committing changes, run:

```bash
yarn lint
yarn typecheck
yarn test
```

Review the Git changes:

```bash
git status
git diff
```

Commit changes using descriptive messages:

```bash
git add .
git commit -m "feat: add initial automation framework"
```

Push changes:

```bash
git push origin main
```

---

## Useful Commands Reference

| Command | Description |
|---|---|
| `yarn install` | Install dependencies |
| `yarn playwright install` | Install Playwright browsers |
| `yarn test` | Run all tests |
| `yarn test:headed` | Run tests with visible browser |
| `yarn test:ui` | Open Playwright UI Mode |
| `yarn test:debug` | Run in debug mode |
| `yarn test:chromium` | Run Chromium tests |
| `yarn test:firefox` | Run Firefox tests |
| `yarn test:webkit` | Run WebKit tests |
| `yarn test:report` | Open Playwright HTML report |
| `yarn typecheck` | Run TypeScript checks |
| `yarn lint` | Run ESLint |
| `yarn lint:fix` | Automatically fix supported lint issues |

---

## Notes

This project is under active development. The initial focus is to establish a reliable, maintainable Playwright foundation before introducing additional abstractions and automation layers.

New framework capabilities should be introduced incrementally, with a preference for simplicity, clear responsibilities and reusable components.
