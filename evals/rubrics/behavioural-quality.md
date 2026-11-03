# Behavioural Quality Rubric

Score the actual generated artifact, not whether the skill fired or whether the response sounds convincing. Apply only dimensions relevant to the skill; mark genuinely inapplicable dimensions N/A and explain why. For each score, cite output, diff, trace or source evidence.

## Scale

- **4 — Meets fully:** all stated indicators are evidenced; no material omission.
- **3 — Mostly meets:** correct overall; only minor, non-blocking omissions.
- **2 — Partially meets:** useful work but one material gap or multiple minor gaps.
- **1 — Mostly fails:** major omissions, unsupported assumptions or incorrect work.
- **0 — Fails:** absent, fundamentally incorrect or contradicts the requirement.
- **N/A — Not applicable:** dimension does not apply to this case; exclude from denominator with rationale.
- **NE — Not evaluable:** required source/evidence unavailable; do not convert to zero or PASS.

## Dimensions and observable indicators

| Dimension | Weight | Indicators |
|---|---:|---|
| Correctness | 25% | Assertions, calculations, diagnoses or recommendations match approved requirements/contracts and actual inspected code. No fabricated API behaviour or unsupported conclusion. |
| Completeness | 15% | All case-specific mandatory expectations addressed; important positive/negative/boundary/failure paths included as appropriate. |
| Risk identification | 15% | Material business, security, privacy, data-integrity, reliability and regression risks identified and prioritised with rationale. |
| Traceability | 10% | Outputs map to source requirement/risk and identify evidence; assumptions are not presented as approved facts. |
| Evidence and epistemic discipline | 15% | Claims link to actual source, diff, trace or command output; unknowns and confidence are calibrated; no invented execution. |
| Maintainability and architecture | 10% | Follows repository patterns, layer boundaries, isolation and simplicity; no unjustified abstractions/dependencies. |
| Repository convention compliance | 5% | Correct paths, language, scripts, naming, configuration and documented patterns. |
| Communication and actionability | 5% | Output is structured, specific, prioritised and usable; clarifications and next actions have owners where relevant. |

Weighted score = sum(score / 4 × weight) over applicable dimensions, divided by sum(applicable weights), multiplied by 100. Round to one decimal. Exclude NE dimensions from the score and set verdict BLOCKED if any mandatory dimension cannot be evaluated.

## Verdict thresholds

- **PASS:** 85–100, no critical failure, Correctness >= 3, Evidence >= 3, and all case-specific mandatory expectations pass.
- **PASS WITH OBSERVATIONS:** 75–84.9, no critical failure, Correctness >= 3 and no mandatory expectation fails. Requires human acceptance of minor observations before benchmark baseline.
- **FAIL:** below 75, Correctness < 3, any mandatory expectation fails, or any critical failure.
- **BLOCKED:** authoritative source, output, diff or required execution evidence is missing such that a fair assessment cannot be made.

Thresholds do not override critical-failure rules. A high numerical score cannot rescue a failed mandatory expectation.

## Case-level expectation grading

For every `expectations[]` item in the case:
- PASS: directly evidenced.
- PARTIAL: attempted but incomplete or weakly evidenced.
- FAIL: omitted, contradicted or materially incorrect.
- NOT ASSESSABLE: required evidence is unavailable.

A response's claim that it performed an action is not evidence that it did so. For implementation cases, inspect the actual diff; for execution claims, inspect actual command output/artifacts.

## Skill-specific application

- Requirement analysis: source authority, ambiguity/conflict handling, readiness and decision ownership.
- Strategy/cases: risk-to-test-level rationale, observable oracle, boundary/negative coverage and traceability.
- Web/API implementation: correct layer, assertions/contracts, data isolation, security and actual validation.
- Verification/investigation: evidence preservation, calibrated classification, exact run scope and no false PASS.
- Review/quality: independent inputs, severity, residual risk and decision authority.
- Workflow orchestration: correct sequence, proportionality and blocked gates.
