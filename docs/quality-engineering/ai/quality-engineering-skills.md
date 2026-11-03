# Quality Engineering Agent Skills

This catalogue describes the repository's Claude Code skills and specialist agents. The skills operationalise the policies and workflows documented under `docs/quality-engineering/`; they do not replace those documents.

## How to use

Start with `/qe-workflow` for a new or cross-cutting Quality Engineering task. For a focused task, invoke the relevant skill directly. Claude Code can also select skills from their descriptions when the task matches.

Use the smallest workflow that provides adequate quality evidence. A skill is a repeatable workflow, not an approval authority.

## Skills

| Skill | Responsibility | Typical point in the lifecycle |
|---|---|---|
| `qe-workflow` | Routes work to appropriate QE skills and quality gates | Entry point / orchestration |
| `analyze-requirement` | Assesses requirement clarity, completeness, consistency and testability | Before strategy and design |
| `design-test-strategy` | Defines risk-based scope, test levels, priorities, data, environments and exit criteria | Planning |
| `design-test-cases` | Produces traceable scenarios, detailed cases and expected results | Test design |
| `add-web-test` | Implements browser UI automation using repository conventions | Implementation |
| `add-api-test` | Implements API and contract automation using repository conventions | Implementation |
| `verify-implementation` | Runs proportionate checks and reports evidence | Verification |
| `investigate-failure` | Diagnoses failed or flaky tests using evidence | Investigation / maintenance |
| `review-tests` | Coordinates independent Maker–Checker review | Independent review |
| `evaluate-quality` | Evaluates coverage, risks, execution evidence and residual risk | Closure / readiness |

## Specialist Agents

| Agent | Responsibility |
|---|---|
| `test-architect` | Strategy, test architecture, test-layer selection and cross-cutting QE decisions |
| `test-reviewer` | Independent review of test design, implementation, architecture and evidence |

## Typical workflows

### Feature

`analyze-requirement` → `design-test-strategy` → `design-test-cases` → implementation skill → `verify-implementation` → independent review where required → `evaluate-quality`.

### Defect

`analyze-requirement` → `design-test-cases` → `investigate-failure` → relevant implementation skill → verification → review where required.

### Test maintenance

Relevant implementation or investigation skill → `verify-implementation` → review where required.

## Governance

- `AGENTS.md` and `CLAUDE.md` remain the shared instruction sources.
- The documents under `docs/quality-engineering/` remain the policy and process sources of truth.
- Skills must not invent product behaviour, approve requirements or accept release risk.
- Maker–Checker independence must be preserved where required.
- Verification claims must be supported by actual execution evidence.
- Update this catalogue when skills or agents are added, renamed or retired.
