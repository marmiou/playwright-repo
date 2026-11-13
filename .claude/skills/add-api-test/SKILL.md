---
name: add-api-test
description: Adds or updates API tests in this repository using its established API clients, fixtures, contracts, data strategy and reporting. Use when implementing automated service or HTTP contract coverage for understood and designed requirements.
---

# Add API Test

## Purpose

Implement reliable API tests that verify service behaviour, contract expectations, business outcomes and relevant integration boundaries. Follow repository conventions and keep API automation independent of browser-specific abstractions.

## Governing Documentation

Follow `AGENTS.md`, `CLAUDE.md`, `docs/architecture/overview.md`, `docs/architecture/test-execution.md`, `docs/quality-engineering/engineering-practices/test-automation-standards.md`, `docs/quality-engineering/engineering-practices/test-data-management.md`, `docs/quality-engineering/engineering-practices/test-reliability.md`, `docs/quality-engineering/workflows/automation-implementation.md`, and `docs/quality-engineering/governance/requirements-integrity-and-product-ownership.md`. Follow Maker–Checker guidance where applicable. Verify paths before relying on them.

## Entry Criteria

- API behaviour or contract is understood from an authoritative source.
- Relevant scenarios and expected results are defined.
- Authentication, data setup and environment requirements are known.
- API is an appropriate layer for the behaviour.

If the response contract or business rule is ambiguous, return to requirement analysis. Never invent status codes, schema fields or error contracts.

## Workflow

### 1. Inspect existing API architecture

Inspect tests under `tests/api`, clients and abstractions under `src/api`, shared fixtures under `src/fixtures`, shared types/utilities, Playwright configuration, package scripts and approved API specifications.

Reuse current patterns. Do not create another HTTP client or fixture system without a demonstrated need and architectural justification.

### 2. Establish the contract

Identify the HTTP method and endpoint, authentication and authorisation, request headers/parameters/body, expected status and response contract, business side effects and persisted state, error and validation behaviour, and relevant idempotency, retry, pagination or concurrency expectations.

Only assert details supported by an authoritative contract or approved requirement.

### 3. Implement at the correct boundary

- Put API specs under `tests/api` using existing naming conventions.
- Use the established API client or Playwright request facilities.
- Keep API-specific logic in `src/api`.
- Reuse fixtures and shared code only where responsibilities genuinely overlap.
- Keep browser page objects and UI interaction out of API clients.
- Keep test intent visible in the spec.
- Prefer schema or contract assertions where a contract exists.
- Assert meaningful business outcomes and side effects, not just a successful HTTP response.
- Cover invalid input, permission boundaries, missing resources, duplicate operations and dependency failures when required by risk.
- Avoid brittle assertions on unspecified response ordering, messages or incidental fields.

### 4. Manage data and state

Use unique and isolated test entities. Establish prerequisites explicitly. Verify persisted state when required. Clean up created resources where safe and supported. Make cleanup resilient and diagnosable. Do not assume tests can run against production or share mutable records across parallel tests without isolation. Never put credentials, tokens, personal data or production secrets in source control or reports.

### 5. Configuration

Use approved environment variables and existing configuration patterns. The repository has `dotenv` installed but loading is commented out in configuration; inspect actual setup before assuming `.env` is loaded. Do not log secrets. Document variable names, never values.

### 6. Verify

Run the focused API test first, then relevant broader validation using scripts that actually exist in `package.json`. Typical checks include focused API specs, relevant API groups, typecheck and lint if available, and the full relevant suite when feasible.

Report exact commands and outcomes. Distinguish assertion failures from connection, authentication, configuration, data and environment failures.

## Review Checklist

- [ ] Contract and expected behaviour have an authoritative source.
- [ ] Test maps to a requirement, risk or API contract.
- [ ] Correct API boundary selected.
- [ ] Existing API client and fixtures reused.
- [ ] Request and response assertions are meaningful.
- [ ] Business side effects are verified where relevant.
- [ ] Negative and permission cases are risk-appropriate.
- [ ] Test data is isolated and cleanup is safe.
- [ ] Parallel execution is safe.
- [ ] Secrets and sensitive data are protected.
- [ ] Focused validation was executed and reported.

## Stop Conditions

Stop or report BLOCKED if the API contract is unavailable or materially ambiguous; credentials or environment access are missing; the test would mutate uncontrolled or production data; expected error behaviour is not approved; or the change requires an unapproved architectural decision.

## Anti-Patterns

Never guess status codes or response schemas; assert only 2xx when business behaviour matters; use UI automation to verify an API contract; couple API clients to page objects; share mutable records without isolation; ignore side effects and persistence; suppress failed assertions; log secrets; or treat a connection failure as a product defect without investigation.

## Output

Report contract and scenarios covered, files changed and design rationale, data and cleanup approach, commands executed and exact results, unexecuted checks and blockers, and known limitations.

## Related Skills

`qe-workflow`, `analyze-requirement`, `design-test-cases`, `verify-implementation`, `investigate-failure`, `review-tests`.
