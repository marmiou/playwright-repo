# Test Data Management

## 1. Purpose

This document defines how test data is created, isolated, managed and cleaned up across Web UI and API automation.

Test data MUST be predictable, secure, traceable and suitable for repeatable and parallel execution.

## 2. Core Principles

- **Independence:** Tests establish their own prerequisites and MUST NOT depend on execution order.
- **Isolation:** Mutable resources MUST be isolated or explicitly coordinated.
- **Uniqueness:** Tests creating or modifying resources MUST avoid unintended collisions.
- **Repeatability:** Test data MUST establish predictable initial conditions.
- **Ownership:** Every mutable resource MUST have a clear owner and lifecycle.
- **Cleanup:** Tests SHOULD clean up resources they own when safe and appropriate.
- **Security:** Prefer synthetic or anonymised data. Never expose credentials, secrets or unnecessary personal information.

Shared immutable reference data MAY be reused when it is safe for concurrent access.

## 3. Data Creation Strategies

Choose the simplest approved setup mechanism that supports the purpose of the test.

| Strategy | Appropriate use |
|---|---|
| API setup | Establishing prerequisites efficiently without bypassing the behaviour under test |
| Factories/builders | Creating consistent data with controlled variations |
| Static reference data | Reusing immutable, predictable values |
| UI setup | Testing the creation workflow itself or when no suitable alternative exists |
| Database setup | Only when explicitly authorised and technically appropriate |

API setup is generally preferred for unrelated prerequisites. However, when testing a UI creation workflow, the resource MUST be created through the UI.

Database setup MUST NOT be introduced without appropriate architectural and security approval. It MUST NOT bypass the behaviour being tested.

Factories and builders SHOULD produce valid defaults, support explicit overrides, generate unique identifiers where needed and avoid hidden external side effects.

## 4. Ownership, Isolation and Parallel Execution

Every mutable resource MUST have a clear ownership and lifecycle model.

Ownership defines:

- Who creates and modifies the resource.
- Whether it can be shared.
- Who is responsible for cleanup.
- Whether concurrent access is safe.

Prefer test-scoped resources for mutable data. Worker-scoped resources MAY be used when sharing is intentional and safe.

Tests MUST NOT:

- Reuse mutable resources across unrelated scenarios without coordination.
- Depend on another test's data.
- Assume shared resources remain unchanged.
- Modify resources owned by other tests or workers.
- Leave implicit dependencies for subsequent executions.

Use unique identifiers such as UUIDs or execution-specific values when necessary. Random data MUST still satisfy application validation rules.

Do not reduce parallelism as the default solution to data collisions. First investigate and address the underlying isolation problem.

## 5. Setup, Cleanup and Environment Management

Setup MUST establish the minimum required initial state. It SHOULD be explicit, repeatable and fail clearly when prerequisites cannot be established.

Cleanup MUST:

- Target only resources owned by the test or fixture.
- Be safe when setup partially fails.
- Avoid deleting shared or unrelated resources.
- Report meaningful cleanup failures.
- Avoid hiding the original test failure.

Use Playwright fixture lifecycle mechanisms where appropriate. Cleanup SHOULD be idempotent where practical, without suppressing genuine ownership or data-integrity problems.

Do not assume environments are clean or that reset operations always execute successfully.

Destructive operations, including database resets and bulk deletion, MUST be restricted to approved environments, verify their target and scope, and require appropriate authorisation.

## 6. Security and Privacy

Test data MUST follow applicable security and privacy requirements.

- Never hardcode or commit real credentials, tokens or secrets.
- Prefer synthetic or anonymised personal data.
- Use approved secret management.
- Avoid exposing sensitive values in logs, reports, traces and screenshots.
- Restrict access to sensitive datasets and environments.
- Do not use test data setup to bypass security controls that are part of the behaviour under test.

## 7. Diagnostics and AI-Assisted Test Data Management

Data-related failures SHOULD be distinguishable from product and automation failures.

Where useful, record the test name, execution and worker identifiers, environment, resource identifiers, setup result and cleanup result.

Never include secrets or unnecessary personal data in diagnostics.

AI agents MAY assist with data modelling, factories, synthetic data generation, isolation analysis, cleanup design and failure investigation.

They MUST respect resource ownership, security requirements and environment boundaries. Destructive operations require explicit authorisation. AI-generated setup MUST NOT bypass the behaviour under test.

## 8. Related Documents

- `test-automation-standards.md` — Fixtures, implementation and automation architecture.
- `test-reliability.md` — Failure classification and diagnostics.
- `continuous-improvement.md` — Evidence-based framework improvement.
- `../governance/requirements-integrity-and-product-ownership.md` — Requirements authority.
- `../../architecture/overview.md` — Framework architecture.
- `../../architecture/test-execution.md` — Execution configuration and CI/CD.

## Governing Principle

**Every test must have a controlled and understandable data state. Test setup supports the behaviour under test; it must never replace it.**
