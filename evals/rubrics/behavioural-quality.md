# Behavioural Quality Rubric

Assess the actual output or artifact against the original task, authoritative requirements and repository evidence. Do not score whether a skill activated; routing is assessed separately in `skill-selection.md`. Do not award credit for confident wording, plausible intent or unverified claims.

Apply the dimensions below to each behavioural case. All case expectations are mandatory for the current seed cases. Correctness is mandatory for every behavioural case and must never be marked N/A. If evidence needed to assess Correctness is unavailable, mark it NE and identify the missing evidence. Before scoring other dimensions, identify which are applicable and mandatory for that case. Use the case's stated expectations as the primary scope; do not invent additional acceptance criteria during evaluation.

## Rating scale

Use the same scale for every dimension, applying the dimension-specific anchors below:

- **4 — Fully meets:** all relevant indicators are satisfied with direct evidence; no material gap.
- **3 — Substantially meets:** outcome is correct and usable; only a minor omission remains, with no material effect on correctness, risk or use.
- **2 — Partially meets:** some useful work is present, but there is at least one material gap, or several minor gaps reduce reliability or usability.
- **1 — Largely fails:** major required elements are missing, materially incorrect, or unsupported; the output is not safe/reliable to use without substantial rework.
- **0 — Fails:** the dimension is wholly absent where required, fundamentally incorrect, or directly contradicts an authoritative requirement or safety boundary.
- **N/A — Not applicable:** the dimension genuinely does not apply to this case. Give a short reason; exclude its weight from the denominator.
- **NE — Not evaluable:** evidence needed to judge the dimension is unavailable or inaccessible. State exactly what is missing. Do not convert NE to zero, N/A or PASS.

A score of 1 or 3 is the intermediate judgement between the adjacent anchors. Evaluators must cite evidence for every 0–4 score. N/A and NE require a reason.

## Dimensions and dimension-specific anchors

### 1. Correctness — 25%

Assess factual, technical and behavioural correctness against authoritative requirements, contracts and inspected repository state.

- **4:** All material conclusions, assertions, calculations, recommendations and code behaviour match the authoritative sources and observed implementation.
- **3:** Core outcome is correct; only a minor imprecision or non-material defect remains.
- **2:** Partly correct, but at least one material conclusion, assertion, calculation or recommendation is unresolved or wrong.
- **1:** Major parts are incorrect, rely on unsupported assumptions, or conflict with an authoritative source.
- **0:** Fundamentally wrong or directly contradicts an approved requirement in a way that invalidates the result.

### 2. Completeness — 15%

Assess coverage of the case's required deliverables and mandatory expectations, not an evaluator's preferred extras.

- **4:** All mandatory expectations and material parts of the requested deliverable are addressed.
- **3:** All critical content is present; only minor, non-blocking detail is omitted.
- **2:** One material requirement or several important details are missing.
- **1:** Multiple mandatory elements are missing; the deliverable is substantially incomplete.
- **0:** The requested deliverable or its essential content is absent.

### 3. Risk identification — 15%

Assess whether material product, business, security, privacy, data-integrity, reliability and regression risks are identified and prioritised where relevant.

- **4:** Relevant material risks are identified, prioritised and connected to proportionate mitigations, tests or decisions.
- **3:** Main risks and appropriate responses are identified; a minor risk or rationale is missing.
- **2:** Some risks are identified, but a material risk, priority or mitigation is missing.
- **1:** Major foreseeable risks are overlooked, misprioritised or treated superficially.
- **0:** The output ignores a critical risk or recommends an action that creates an unacceptable risk.

### 4. Traceability — 10%

Assess links between the task, approved sources, risks, test design, implementation and conclusions, as applicable.

- **4:** Material conclusions and deliverables are traceable to specific requirements, risks or source evidence; assumptions and unknowns are clearly labelled.
- **3:** Main links are clear; minor references or mappings are missing.
- **2:** Partial traceability exists, but important conclusions cannot be reliably mapped to their source.
- **1:** Traceability is largely absent or materially misleading.
- **0:** The output fabricates source authority or presents assumptions as approved requirements.

### 5. Evidence and epistemic discipline — 15%

Assess whether claims are supported by evidence actually available to and inspected by the executor, and whether uncertainty and execution status are represented honestly.

- **4:** Material claims cite or identify the relevant source, diff, trace, artifact or command output; uncertainty and limitations are accurately stated; no unsupported execution claim.
- **3:** Evidence supports the main claims; a minor citation, detail or confidence qualification is missing.
- **2:** Some claims are evidenced, but a material claim lacks support or evidence scope is unclear.
- **1:** Several material claims are unsupported, evidence is misrepresented, or hypotheses are presented as facts.
- **0:** The output fabricates execution, results, artifacts, approvals or evidence, or knowingly misstates what was observed.

### 6. Maintainability and architecture — 10%

Apply primarily to implementation and design artifacts. For non-code outputs, assess whether the proposed approach is proportionate and compatible with the stated architecture.

- **4:** Fits established architecture and patterns; clear, simple, isolated and maintainable; no unjustified complexity or dependencies.
- **3:** Sound and maintainable overall; only a minor convention or design refinement is needed.
- **2:** Usable but introduces a material maintainability, isolation, layering or complexity concern.
- **1:** Poorly aligned with architecture or difficult to maintain; substantial redesign is needed.
- **0:** Violates a critical architectural boundary or creates an inherently unsafe/unmaintainable solution.

### 7. Repository convention compliance — 5%

Apply when repository-specific work is requested or produced. Do not penalise a conceptual answer for not changing repository files.

- **4:** Uses the correct repository paths, language, scripts, naming, configuration and documented conventions, verified against the repository.
- **3:** Correct overall; only a minor convention deviation.
- **2:** One material convention is missed or repository alignment is only partly demonstrated.
- **1:** Multiple conventions are violated or the approach relies on assumed repository structure.
- **0:** The result materially conflicts with repository constraints or claims repository changes that did not occur.

### 8. Communication and actionability — 5%

Assess whether the output makes its findings, limitations and next steps understandable and usable by the intended audience.

- **4:** Clear, specific and prioritised; separates facts, assumptions, decisions and actions; owners or required decision-makers are identified where relevant.
- **3:** Clear and usable; a minor prioritisation, ownership or explanation detail is missing.
- **2:** Understandable but important next steps, rationale or ownership are ambiguous.
- **1:** Vague, poorly structured or difficult to act on; material decisions or next steps are obscured.
- **0:** Misleading or unusable communication prevents a responsible next action.

## Case expectation assessment

Assess every `expectations[]` item separately:

- **PASS:** directly supported by the supplied output or artifact and, where relevant, execution evidence.
- **PARTIAL:** addressed but incomplete, weakly evidenced or only partly correct.
- **FAIL:** omitted, contradicted or materially incorrect.
- **NOT ASSESSABLE:** the required source or evidence is unavailable.

Do not infer that a criterion passed because a related criterion passed. Cite the smallest useful evidence location (file and line, diff hunk, trace/event, command output or quoted response). A response's claim that it performed an action is not proof that it did so.

## N/A and NE controls

- Use **N/A** only when the dimension is genuinely outside the case's scope. Example: repository convention compliance may be N/A for a purely conceptual explanation that requests no repository inspection or change.
- **Correctness must never be N/A.** It is mandatory in every behavioural case. If correctness cannot be judged because required evidence is missing, use NE, not N/A.
- Do not use N/A merely because the executor omitted the work, lacked skill, or failed to obtain evidence.
- Use **NE** when the evidence needed to judge a relevant dimension is missing, inaccessible or not supplied. Identify the missing evidence and who or what must provide it.
- If a case-mandatory expectation is NOT ASSESSABLE, or a mandatory dimension is NE, the case cannot receive an unqualified PASS; its overall disposition must be considered BLOCKED by the verdict rules.
- If a non-mandatory dimension is NE, disclose it and exclude its weight from the numerical score; do not silently treat the missing evidence as success.
- Never convert a missing artifact, missing log or unprovided requirement into a zero unless the case explicitly requires the executor to produce it and the executor failed to do so.

## Weighted score calculation

For dimensions scored 0–4, calculate:

`weighted score = 100 × Σ((dimension score ÷ 4) × dimension weight) ÷ Σ(applicable dimension weights)`

Exclude N/A and NE dimensions from both numerator and denominator. Report the applicable weight total (out of 100) and coverage percentage alongside the score so readers can see how much of the rubric was assessed. Coverage is the sum of weights for scoreable dimensions; it is not a pass threshold. Identify excluded dimensions and their N/A/NE reasons. Do not compare scores as if equivalent when their coverage materially differs. Round the score and coverage to one decimal place. If no dimensions are scoreable, report **NO SCORE**.

The weighted score is descriptive evidence, not a verdict by itself. Do not use a numerical threshold here to override failed mandatory expectations or governance checks. The overall case verdict and governance precedence are defined in the evaluation protocol, not by this rubric alone.

## Application guidance by skill family

- **Requirement analysis:** source authority, ambiguity/conflict handling, readiness and decision ownership.
- **Strategy and test design:** risk-to-test-level rationale, observable oracle, boundary/negative coverage and traceability.
- **Web/API implementation:** correct test layer, meaningful assertions/contracts, data isolation, security and actual validation.
- **Verification and investigation:** evidence preservation, calibrated classification, exact run scope and no false PASS.
- **Review and quality evaluation:** independent inputs, severity, residual risk and decision authority.
- **Workflow orchestration:** correct routing is assessed separately; assess behavioural sequencing, proportionality, dependencies and blocked gates here.
