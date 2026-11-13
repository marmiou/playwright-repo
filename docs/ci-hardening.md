# CI Hardening

This document describes the repository's GitHub Actions quality gates and the repository settings that must accompany them.

## CI check matrix

| Change/event | Required checks |
|---|---|
| Every pull request to `main` or `master` | Change detection, CI policy unit tests, lint, type check, Playwright tests, CI Summary |
| Changes under `evals/**`, `.claude/skills/**`, or the CI workflow | Additionally run QE validator unit tests, evaluation-case validation, and evaluation-result validation |
| Push to `main` | The same applicable checks; deploy the Allure report only after successful Playwright tests |
| Daily/manual failure analysis | Read recent CI run metadata and available artifacts; report when collection reaches its configured limit |

The three evaluation jobs are intentionally skipped when no evaluation/skill/workflow files changed. Those skips are expected only in that case. The Playwright job requires successful change detection, CI policy tests, lint and type checking, and either successful evaluation jobs or the expected evaluation skips. An unexpected skip is a CI failure, not a pass.

The CI Summary is the aggregate required check. Its status policy is covered by automated unit tests in `scripts/tests/test_ci_status.py`. It accepts only successful required jobs and explicitly expected skips:
- Evaluation validator jobs may be skipped only when the change filter says evaluation files did not change.
- Allure deployment may be skipped outside a push to `main`, or when Playwright did not succeed.
- Change detection, CI policy tests, lint, type check and Playwright tests must succeed. Unknown, skipped, cancelled, or failed statuses for these required jobs fail the summary.

## Action and toolchain pinning

Third-party GitHub Actions are pinned to immutable commit SHAs. The adjacent version comments identify the corresponding upstream release tag. Dependabot is configured to propose weekly updates for GitHub Actions, npm/Yarn dependencies, and the Python evaluation dependency.

The Allure CLI is installed at version `2.46.1` rather than resolving the latest release at runtime. Update action SHAs and the Allure CLI version deliberately, then review the resulting CI run.

## Workflow permissions

The main CI workflow defaults to read-only repository contents. The Pages deployment job receives `contents: write` only for its publishing step. The failure-analysis workflow grants `issues: write` only to its analysis job because that job may create or comment on the daily analysis issue; its other permissions are read-only.

Do not add write permissions at workflow scope unless every job needs them. Keep checkout credentials disabled in jobs that do not need authenticated Git operations.

## Required repository setting — protect `main`

At the time this document was written, the `main` branch API reported branch protection disabled. The GitHub integration available for this change can read repository settings but cannot write branch-protection/ruleset configuration, so this setting still requires a repository-admin action.

In GitHub, open **Settings → Rules → Rulesets** (or **Branches → Branch protection rules**) and create a rule targeting `main`:
1. Require a pull request before merging.
2. Require status checks to pass before merging.
3. Select **`8 · CI Summary`** as the required check after it appears in the checks list.
4. Require the branch to be up to date before merging if that matches the repository's merge policy.
5. Block force pushes and branch deletion; restrict direct pushes to trusted administrators only if that is the intended policy.

Do not select individual conditional evaluation jobs as required checks: they are intentionally skipped when their path filter does not match. The aggregate CI Summary is designed to enforce the expected skip policy.

## Security feature verification

Dependabot update configuration is version-controlled in `.github/dependabot.yml`. Code scanning, secret scanning, push protection, dependency-graph availability, and alert enforcement are repository settings/features; their state must be checked in **Settings → Security → Code security and analysis** and the repository's Security tab. This change does not claim those features are enabled merely because their configuration surface exists.

## Failure-analysis collection limit

The daily analysis workflow requests up to 1,000 successful and 1,000 failed runs for the selected date range. If either category reaches that limit, it adds an explicit warning to the report and workflow log so the output is not mistaken for exhaustive. Narrow the date range or implement paginated API collection if this becomes a recurring limit.
