# Playwright Test Automation Framework

This repository contains a modern end-to-end test automation framework built with **Playwright**, **TypeScript**, and **Yarn 4**, following the **Page Object Model (POM)** pattern.

It is designed to test the LearnWorlds platform, including UI purchase flows, admin validations, and API endpoints.

---

# 🚀 Tech Stack

* [Playwright](https://playwright.dev/)
* TypeScript
* Yarn 4
* Allure Reporting
* Playwright HTML Reporting
* Node.js 18+

---

# 📦 Prerequisites

## 1. Install Homebrew (macOS)

If not already installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:

```bash
brew --version
```

---

## 2. Install Node.js

Install via Homebrew:

```bash
brew install node
```

Verify:

```bash
node -v
npm -v
```

Node 18+ required.

---

## 3. Enable Yarn 4 via Corepack

Corepack is included with Node.

Enable it:

```bash
corepack enable
corepack prepare yarn@stable --activate
```

Verify:

```bash
yarn -v
```

---

## 4. Install Allure CLI

Required for Allure reports:

```bash
brew install allure
```

Verify:

```bash
allure --version
```

---

# 📥 Project Installation

Clone the repository:

```bash
git clone <repo-url>
cd playwright-repo
```

Install dependencies:

```bash
yarn install
```

Install Playwright browsers:

```bash
npx playwright install
```

---

# ▶️ Running Tests

## Run all tests

```bash
yarn playwright test
```

---

## Run tests in headed mode

Opens a visible browser:

```bash
yarn playwright test --headed
```

---

## Run a specific test file

```bash
yarn playwright test tests/e2e/example.spec.ts
```

---

## Debug tests

```bash
yarn playwright test --debug
```

---

# 📊 Reporting

This project supports two reporting systems:

* Playwright HTML Reporter
* Allure Reporter

---

# Playwright HTML Report

Generate report:

```bash
yarn playwright show-report
```

Opens:

```
http://localhost:9323
```

---

# Allure Report

Run tests first:

```bash
yarn playwright test
```

Then generate report:

```bash
allure serve allure-results
```

This will:

* generate report
* open browser automatically

---

# 📁 Project Structure

```
playwright-repo/

playwright.config.ts

tests/
  e2e/
  api/

src/
  pages/
  fixtures/
  utils/

test-data/

package.json
```

---

# 🧱 Framework Architecture

This project follows the **Page Object Model (POM)** pattern:

* `pages/` → page objects
* `fixtures/` → shared test setup
* `utils/` → helper utilities
* `tests/` → test specifications

---

# ⚙️ Playwright Configuration

Main config file:

```
playwright.config.ts
```

Includes:

* reporters
* browser settings
* timeouts

---

# 📊 Allure Integration

Configured via:

```ts
reporter: [
  ['html'],
  ['allure-playwright'],
]
```

Results stored in:

```
allure-results/
```

---

# 🧹 Ignored Folders

These folders are not committed:

```
node_modules/
playwright-report/
test-results/
allure-results/
allure-report/
```

---

# 🧪 Verify Installation

Run:

```bash
yarn playwright test
```

Expected:

```
1 passed
```

---

# 🧑‍💻 Useful Commands Summary

| Command                       | Description            |
| ----------------------------- | ---------------------- |
| yarn playwright test          | Run tests              |
| yarn playwright test --headed | Run with browser UI    |
| yarn playwright show-report   | Open Playwright report |
| allure serve allure-results   | Open Allure report     |

---

# 📚 References

Playwright:

https://playwright.dev/

Allure:

https://allurereport.org/

---

# 👩‍💻 Author

Markella Efthymiou

---

# 📌 Notes

This framework was created as part of the LearnWorlds QA Automation assignment.

---
