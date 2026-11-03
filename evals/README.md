# QE Agent Skill Evaluations

This directory evaluates the repository's ten Claude Code QE skills. It is a **test design and evidence repository**, not a runner. No model calls, skill executions, generated results, dependencies, MCP servers or CI workflow changes are introduced by this framework.

## Scope and inventory

Each `cases/<skill>.json` contains six cases:

- 3 positive routing prompts (`positive`): the skill should be selected.
- 2 negative routing prompts (`negative`): the skill under test should not be selected; a better alternative route or direct response is expected.
- 1 behavioural case (`behavioral`): the skill should perform its actual job against observable expectations.

The ten evaluated skills are `analyze-requirement`, `design-test-strategy`, `design-test-cases`, `add-web-test`, `add-api-test`, `verify-implementation`, `investigate-failure`, `review-tests`, `evaluate-quality` and `qe-workflow`. Specialist agents are supporting roles, not skills, and are not yet evaluated as a separate agent-selection benchmark.

## Case schema

All case files use JSON with:

- `schema_version`: schema version for this dataset.
- `skill`: skill name under test.
- `source.path` and `source.description`: the exact skill instruction location and description under evaluation. Keep the description synchronised with the skill's frontmatter.
- `cases[]`: stable `id`, `type`, verbatim `prompt`, `expected_routing`, observable `expectations[]` and optional `fixture`.

`expected_routing` remains `activate` for positive and behavioural cases, and `do_not_activate` for negative cases. Each negative case also has `routing_expectation`:

- `expected_primary_skill`: the expected alternative skill, or `null` when a direct response/local action is the appropriate route.
- `allowed_companion_skills`: other skills that may reasonably be used alongside the primary route.
- `forbidden_skills`: skills that should not be invoked for the case.
- `direct_response_allowed`: whether a direct response without a skill is acceptable.
- `rationale`: why the expected alternative is appropriate.

A negative case is not a pass merely because the skill under test was not selected. The evaluator must also assess whether the alternative route or direct response was appropriate. A behavioural case may assert that the skill itself declines an unsafe action or blocks pending clarification. The routing label is not a behavioural pass.

Fixtures are optional. Keep them synthetic, minimal, deterministic, and clearly separated from real credentials or production data. Prefer inline scenario context for small cases; add files under `fixtures/<skill>/` only when a real file artifact is necessary to evaluate the skill. Reference fixture paths relative to `evals/`.

## Evaluation tiers

### Tier 1 — Structural (deterministic, no model)

Manually or with a future lightweight validator check:
- Every skill has exactly three positive, two negative and one behavioural case.
- Case IDs are unique within the dataset; required fields and allowed enums are valid JSON.
- Skill name, source path and source description match the current repository.
- Negative routing metadata is complete and internally consistent.
- Expectations are observable and case-specific, not generic praise.
- Fixture references resolve; fixtures contain no secrets or real personal data.
- No case asks the executor to bypass repository safety, permissions or destructive-action restrictions.

Structural validity says nothing about model behaviour. A structurally valid test can still be a poor test.

### Tier 2 — Skill selection and routing

The intended target-host evaluation is Claude Code. Run positive and negative prompts in that host and record whether the intended skill was invoked, whether an inappropriate skill was invoked, and which alternative skill was selected. Measure separately:
- Positive recall = correctly activated positive prompts / positive prompts.
- Negative specificity = correctly not activated negative prompts / negative prompts.
- Alternative-route accuracy = negative prompts routed to the expected alternative skill or accepted direct response / negative prompts.
- Wrong-skill rate = prompts routed to an inappropriate skill / all routing prompts.

Do not treat keyword matching or a model's claim that it used a skill as proof. Where the host exposes invocation traces, retain the trace. Repeat stochastic cases (minimum 3 runs for exploratory baselines; 5+ for comparisons) with model and host version pinned. Report per-case outcomes, not just aggregate percentages. A single failure on a safety-critical negative case warrants investigation regardless of the aggregate.

**Current host limitation:** ChatGPT can simulate description-based skill selection when given the descriptions and can attempt to follow supplied skill instructions. That is not a test of Claude Code's native skill discovery, activation, or host orchestration. Any ChatGPT pilot must be labelled as a *routing simulation* or *instruction-following evaluation*, never as a Claude Code activation result. Native activation claims require execution in Claude Code with suitable invocation evidence.

### Tier 3 — Behavioural quality

Execute the behavioural prompt with the skill available. Capture the original task, authoritative source documents, skill instructions, relevant repository context, generated output and any execution/tool trace. Score the output against the independent rubric in `rubrics/behavioural-quality.md` and `rubrics/governance-and-safety.md`.

Behavioural evaluation must inspect the deliverable, not merely activation or the agent's self-reported summary. For code-producing skills, inspect actual diffs and test evidence; do not accept proposed code as implemented code. For dialogue/report skills, evaluate the report and its evidence claims. Cases explicitly labelled dialogue-only assess safe reasoning and honest limitation reporting; they do not demonstrate implementation or execution capability.

## Independent evaluation protocol

Use separate executor and evaluator roles:

1. **Executor (Maker):** the target host runs the prompt with the target skill and permitted repository context. Capture the raw transcript, tool calls, generated files/diff and command outputs. Do not ask the executor to grade itself.
2. **Evidence bundle:** provide the evaluator with (a) original user task verbatim, (b) authoritative requirements and relevant source docs with paths/versions, (c) exact skill instructions and description, (d) actual generated output and changed-file diff, (e) raw execution/tool trace and command output, (f) case expectations and applicable rubric, (g) model/provider/version, host/runtime version, configuration, permissions and timestamp. Redact secrets without removing evidence needed for assessment.
3. **Independent evaluator:** use a model/provider distinct from the executor where practical. A separate conversation using the same model/provider is a context separation measure, not proof of model independence. Instruct the evaluator to judge against original requirements and authoritative sources, not the Maker's explanation. Require criterion-by-criterion scores, quoted evidence or file/line references, missing evidence, critical-failure checks and a verdict. It must not infer a successful tool call from narrative claims.
4. **Blind and calibrate:** where practical, hide the target skill identity and expected result from the evaluator during initial scoring; randomise case order. Provide expected criteria only after initial independent observations when needed for adjudication. Use a second evaluator on a sample and compare criterion-level judgements.
5. **Human adjudication:** required for safety/governance critical failures, requirement or policy conflicts, release decisions, and material evaluator disagreement. Human reviewer records the resolution and rationale.
6. **Preserve provenance:** retain the executor output and evaluator assessment as separate artifacts. Never replace raw evidence with a polished summary.

An independent evaluator should receive only the evidence needed for the case, but enough to reconstruct the basis of judgement. If source documentation is missing or contradictory, mark the affected criterion BLOCKED/NOT ASSESSABLE rather than guessing.

### Evaluator prompt template

> You are the independent QE evaluator, not the executor. Assess the generated artifact against the original task, approved requirements and repository standards. Do not trust the executor's summary or claims. Inspect the supplied skill instructions, sources, output, diff and execution evidence. For each expectation, mark PASS / PARTIAL / FAIL / NOT ASSESSABLE and cite exact evidence. Score the applicable rubric dimensions 0–4. Check all critical-failure conditions before calculating a verdict. Do not award points for fluent explanations unsupported by artifacts. If the evidence is insufficient, return BLOCKED/NOT ASSESSABLE. Identify disagreements with the skill instructions or source documentation; do not silently reconcile them.

## Results and provenance

`results/` is reserved for actual evaluation runs. No illustrative scores or fabricated run outputs belong here. Store each run in a timestamped directory or file and include:
- case ID and dataset revision/commit;
- executor and evaluator model/provider, exact model version and host/runtime version;
- run timestamp, configuration, sampling settings and permission mode;
- repository commit and working-tree state, skill description/instruction hashes, prompt/context and available tools/MCP configuration;
- raw transcript/tool trace, artifact diff and command output;
- criterion-level evaluator assessment, score and critical-failure flags;
- human adjudication and final disposition, if applicable.

Do not commit sensitive traces, credentials, customer data or production data. If results are later committed, clearly label them as actual runs and include provenance. Keep illustrative examples in documentation and label them explicitly.

## Tool and MCP evaluation (future, not configured)

The case schema can later add tool expectations without binding to a provider: `tool_expectations` may describe capability, reason, expected/forbidden use, permission boundary and fallback. Evaluate whether the agent selects a relevant available tool, avoids needless calls, reports unavailable tools honestly, respects least privilege, and does not exceed granted permissions. Do not add MCP configuration or dependencies as part of this framework.

## Limitations and next steps

- The current cases are curated, human-authored seed cases, not a statistically representative benchmark.
- Routing behaviour depends on host/model versions and invocation configuration; record these before comparing runs.
- LLM-as-judge scoring is itself fallible. Use criterion-level evidence, independent review and human adjudication for consequential findings.
- One behavioural case per skill is a minimum smoke evaluation, not sufficient statistical confidence.
- The current set does not establish whether a skill improves output compared with the same task without that skill. A controlled skill-disabled baseline (ablation) is required before making incremental-contribution claims.
- No automated runner, JSON Schema validator, CI job or provider adapter is included yet. Add these only after the case format and rubric have been independently reviewed and exercised manually.

## References

- Addy Osmani, [agent-skills evals](https://github.com/addyosmani/agent-skills/tree/main/evals): positive/negative activation, behavioural expectations, fixtures, structural/routing/behaviour tiers and separation of results.
- Repository policy: `AGENTS.md`, `CLAUDE.md`, `docs/quality-engineering/ai/ai-agent-governance.md`, `docs/quality-engineering/governance/maker-checker.md`.
