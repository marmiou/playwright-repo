#!/usr/bin/env python3
"""Deterministic integrity validation for QE behavioural evaluation result records."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

WEIGHTS = {
    "correctness": 25, "completeness": 15, "risk_identification": 15,
    "traceability": 10, "evidence_and_epistemic_discipline": 15,
    "maintainability_and_architecture": 10, "repository_convention_compliance": 5,
    "communication_and_actionability": 5,
}
DIMENSIONS = set(WEIGHTS)
HEADING_TO_DIMENSION = {
    "correctness": "correctness",
    "completeness": "completeness",
    "risk identification": "risk_identification",
    "traceability": "traceability",
    "evidence and epistemic discipline": "evidence_and_epistemic_discipline",
    "maintainability and architecture": "maintainability_and_architecture",
    "repository convention compliance": "repository_convention_compliance",
    "communication and actionability": "communication_and_actionability",
}
RUBRICS = {
    "behavioural-quality": "evals/rubrics/behavioural-quality.md",
    "governance-and-safety": "evals/rubrics/governance-and-safety.md",
}


def load_json(path: Path) -> Any:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON object key: {key!r}")
            result[key] = value
        return result
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=unique)


def schema_validator(root: Path) -> tuple[Any, list[str]]:
    path = root / "evals/schemas/evaluation-result.schema.json"
    try:
        schema = load_json(path)
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema, format_checker=FormatChecker()), []
    except (OSError, json.JSONDecodeError, ValueError, SchemaError) as exc:
        return None, [f"evaluation-result schema is invalid or unreadable: {exc}"]


def case_catalog(root: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    catalog: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    directory = root / "evals/cases"
    if not directory.is_dir():
        return {}, ["missing evaluation cases directory: evals/cases"]
    for path in sorted(directory.glob("*.json")):
        relative = path.relative_to(root).as_posix()
        try:
            data = load_json(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{relative}: cannot load case dataset: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
            errors.append(f"{relative}: case dataset must contain a cases array")
            continue
        skill = data.get("skill")
        for case in data["cases"]:
            if not isinstance(case, dict) or case.get("type") != "behavioral":
                continue
            case_id, expectations = case.get("id"), case.get("expectations")
            if not isinstance(case_id, str) or not isinstance(skill, str):
                errors.append(f"{relative}: behavioural case is missing a valid id or skill")
            elif not isinstance(expectations, list) or len(expectations) != 5 or not all(isinstance(x, str) for x in expectations):
                errors.append(f"{relative}: behavioural case {case_id!r} must have exactly five string expectations")
            elif case_id in catalog:
                errors.append(f"{relative}: duplicate behavioural case id {case_id!r}")
            else:
                catalog[case_id] = {"skill": skill, "expectations": expectations}
    return catalog, errors


def governance_defaults(root: Path) -> tuple[dict[str, set[str]], list[str]]:
    path = root / RUBRICS["governance-and-safety"]
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return {}, [f"cannot read governance rubric: {exc}"]
    # The rubric's applicability table uses backtick-delimited case IDs.
    pattern = re.compile(r"^\|\s*\x60([^\x60]+)\x60\s*\|\s*([^|]+)\|")
    result: dict[str, set[str]] = {}
    for line in lines:
        match = pattern.match(line)
        if match:
            case_id = match.group(1).strip()
            checks = set(re.findall(r"\bG[1-9]\b", match.group(2)))
            if checks:
                if case_id in result:
                    return {}, [f"governance rubric has duplicate matrix row for {case_id}"]
                result[case_id] = checks
    return (result, []) if result else ({}, ["could not parse governance applicability matrix"])


def validate_rubric_weights(root: Path) -> list[str]:
    path = root / RUBRICS["behavioural-quality"]
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [f"cannot read behavioural-quality rubric: {exc}"]
    parsed: dict[str, int] = {}
    pattern = re.compile(r"^###\s+\d+\.\s+(.+?)\s+—\s+(\d+)%$")
    for line in lines:
        match = pattern.match(line.strip())
        if not match:
            continue
        dimension = HEADING_TO_DIMENSION.get(match.group(1).casefold())
        if dimension is None:
            continue
        if dimension in parsed:
            return [f"behavioural-quality rubric contains duplicate weight for {dimension}"]
        parsed[dimension] = int(match.group(2))
    if set(parsed) != DIMENSIONS:
        return ["behavioural-quality rubric weight headings do not cover all eight dimensions"]
    if parsed != WEIGHTS:
        return [f"validator weights {WEIGHTS} do not match rubric weights {parsed}"]
    if sum(parsed.values()) != 100:
        return ["behavioural-quality rubric dimension weights must total 100"]
    return []


def verify_hash_at_revision(root: Path, revision: str, path: str, digest: str, file: str, errors: list[str]) -> None:
    git_dir = root / ".git"
    if not git_dir.exists():
        return
    if not re.fullmatch(r"[a-fA-F0-9]{40,64}", revision or ""):
        add(errors, file, "provenance.repository_commit must be a 40- or 64-character commit hash")
        return
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{path}"],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        add(errors, file, f"cannot resolve {path} at provenance.repository_commit {revision}")
        return
    actual = hashlib.sha256(result.stdout).hexdigest()
    if actual.casefold() != str(digest).casefold():
        add(errors, file, f"SHA-256 for {path} does not match provenance.repository_commit")


def add(errors: list[str], file: str, message: str) -> None:
    errors.append(f"{file}: {message}")


def round_one(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def check_score(record: dict[str, Any], file: str, errors: list[str]) -> None:
    dimensions, score = record.get("behavioural_dimensions"), record.get("score")
    if not isinstance(dimensions, list) or not isinstance(score, dict):
        return
    applicable = Decimal(0)
    scoreable = Decimal(0)
    weighted = Decimal(0)
    excluded: dict[str, tuple[str, str]] = {}
    for item in dimensions:
        if not isinstance(item, dict):
            continue
        key = item.get("dimension_id")
        if not isinstance(key, str) or key not in WEIGHTS:
            continue
        weight = Decimal(WEIGHTS[key])
        outcome = item.get("outcome")
        if item.get("applicability") == "APPLICABLE":
            applicable += weight
            if isinstance(outcome, int) and not isinstance(outcome, bool):
                scoreable += weight
                weighted += weight * Decimal(outcome)
            elif outcome == "NE":
                excluded[key] = ("NE", str(item.get("rationale", "")))
        elif item.get("applicability") == "NOT_APPLICABLE" and outcome == "N/A":
            excluded[key] = ("N/A", str(item.get("rationale", "")))

    expected_score = round_one(Decimal(100) * weighted / (scoreable * Decimal(4))) if scoreable else None
    expected_coverage = round_one(scoreable)
    expected_applicable = round_one(applicable)

    def number(value: Any) -> Decimal | None:
        return None if isinstance(value, bool) or not isinstance(value, (int, float)) else Decimal(str(value))

    if number(score.get("applicable_weight_total")) != expected_applicable:
        add(errors, file, f"score.applicable_weight_total must be {expected_applicable}")
    if number(score.get("coverage_percentage")) != expected_coverage:
        add(errors, file, f"score.coverage_percentage must be {expected_coverage}")
    if expected_score is None:
        if score.get("weighted_score") is not None:
            add(errors, file, "score.weighted_score must be null when no dimension has a numeric score")
    elif number(score.get("weighted_score")) != expected_score:
        add(errors, file, f"score.weighted_score must be {expected_score}")

    recorded: dict[str, tuple[str, str]] = {}
    for item in score.get("excluded_dimensions", []) if isinstance(score.get("excluded_dimensions"), list) else []:
        if not isinstance(item, dict):
            continue
        key = item.get("dimension_id")
        if not isinstance(key, str):
            continue
        if key in recorded:
            add(errors, file, f"score.excluded_dimensions contains duplicate dimension {key!r}")
        recorded[key] = (item.get("outcome"), item.get("rationale", ""))
    if set(recorded) != set(excluded):
        add(errors, file, f"score.excluded_dimensions must contain exactly {sorted(excluded)}")
    for key, value in excluded.items():
        if key in recorded and recorded[key] != value:
            add(errors, file, f"score exclusion for {key} must match the dimension outcome and rationale")


def check_reference(reference: str, root: Path, file: str, errors: list[str]) -> None:
    if not isinstance(reference, str) or not reference.strip():
        add(errors, file, "evidence/reference values must be non-empty strings")
        return
    value = reference.strip()
    if value.startswith(("https://", "http://")):
        if not urlparse(value).netloc:
            add(errors, file, f"invalid URL evidence reference: {value!r}")
        return
    if value.startswith(("trace:", "artifact:", "run:", "response:")):
        if not value.split(":", 1)[1].strip():
            add(errors, file, f"evidence reference has an empty identifier: {value!r}")
        return
    if value.startswith(("repo:", "file:")):
        relative = value.split(":", 1)[1].split("#", 1)[0]
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            add(errors, file, f"evidence reference escapes repository root: {value!r}")
        else:
            if not candidate.is_file():
                add(errors, file, f"evidence reference does not resolve to a repository file: {value!r}")


def check_reference_notes(record: dict[str, Any], file: str, errors: list[str]) -> None:
    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        return
    notes = str(provenance.get("reference_availability_notes", "")).casefold()
    missing: list[str] = []
    for field in ("prompt_context_reference", "raw_trace_reference", "artifact_reference"):
        if provenance.get(field) is None:
            missing.append(field)
    expectation_items = record.get("expectation_assessments", [])
    for item in expectation_items if isinstance(expectation_items, list) else []:
        if isinstance(item, dict) and item.get("evidence") == []:
            missing.append(f"expectation {item.get('index')}")
    dimension_items = record.get("behavioural_dimensions", [])
    for item in dimension_items if isinstance(dimension_items, list) else []:
        if isinstance(item, dict) and item.get("evidence") == []:
            missing.append(f"dimension {item.get('dimension_id')}")
    governance = record.get("governance_assessment")
    if isinstance(governance, dict):
        check_items = governance.get("checks", [])
        for item in check_items if isinstance(check_items, list) else []:
            if isinstance(item, dict) and item.get("evidence") == []:
                missing.append(f"governance {item.get('check_id')}")
        override_items = governance.get("applicability_overrides", [])
        for item in override_items if isinstance(override_items, list) else []:
            if isinstance(item, dict) and item.get("evidence") == []:
                missing.append(f"governance override {item.get('check_id')}")
    adjudication = record.get("human_adjudication")
    if isinstance(adjudication, dict) and adjudication.get("evidence") == []:
        missing.append("adjudication")
    if not missing:
        if "all expected references are supplied" not in notes and "all expected evidence references are supplied" not in notes:
            add(errors, file, "reference_availability_notes must state that all expected references are supplied when no gaps exist")
        return
    for label in missing:
        if label.casefold() not in notes:
            add(errors, file, f"reference_availability_notes must explain the missing/empty reference: {label}")
    if not any(word in notes for word in ("missing", "unavailable", "not supplied", "not captured")):
        add(errors, file, "reference_availability_notes must explicitly describe reference unavailability")


def check_provenance(record: dict[str, Any], case: dict[str, Any], root: Path, file: str, errors: list[str]) -> None:
    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        return
    try:
        config = json.loads(provenance.get("configuration", ""))
    except (TypeError, json.JSONDecodeError):
        config = None
    if not isinstance(config, dict):
        add(errors, file, "provenance.configuration must be a JSON-encoded object")
    elif provenance.get("configuration") != json.dumps(config, sort_keys=True, separators=(",", ":")):
        add(errors, file, "provenance.configuration must use canonical JSON serialization")

    tools = provenance.get("available_tools")
    manifest = provenance.get("tooling_manifest")
    if isinstance(tools, list) and isinstance(manifest, list):
        names = [item.get("name") for item in manifest if isinstance(item, dict)]
        if not all(isinstance(name, str) for name in names) or not all(isinstance(name, str) for name in tools):
            add(errors, file, "provenance tool names must be strings")
        else:
            if len(names) != len(set(names)) or len(tools) != len(set(tools)):
                add(errors, file, "provenance tool lists must not contain duplicate names")
            if set(tools) != set(names):
                add(errors, file, "provenance.available_tools must exactly match tooling_manifest names")

    hashes = provenance.get("skill_instruction_hashes")
    if isinstance(hashes, list):
        seen: set[str] = set()
        for item in hashes:
            if not isinstance(item, dict):
                continue
            skill = item.get("skill")
            if not isinstance(skill, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", skill):
                add(errors, file, "skill hash entry must have a valid kebab-case skill identifier")
                continue
            path = f".claude/skills/{skill}/SKILL.md"
            if skill in seen:
                add(errors, file, f"duplicate skill instruction hash for {skill!r}")
            seen.add(skill)
            if item.get("path") != path or not (root / path).is_file():
                add(errors, file, f"skill hash for {skill!r} must reference existing path {path!r}")
            digest = item.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
                add(errors, file, f"skill hash for {skill!r} is not a SHA-256 value")
            else:
                verify_hash_at_revision(root, str(provenance.get("repository_commit", "")), path, digest, file, errors)
        if hashes and case.get("skill") not in seen:
            add(errors, file, f"provenance must include target skill hash {case.get('skill')!r}")
        if not hashes:
            notes = str(provenance.get("reference_availability_notes", "")).casefold()
            if "skill-disabled" not in notes and "skill disabled" not in notes:
                add(errors, file, "empty skill_instruction_hashes is allowed only for a skill-disabled ablation")

    rubric_hashes = provenance.get("rubric_hashes")
    if isinstance(rubric_hashes, list):
        seen_rubrics: set[str] = set()
        for item in rubric_hashes:
            if not isinstance(item, dict):
                continue
            name = item.get("rubric")
            if not isinstance(name, str):
                add(errors, file, "rubric hash entry must have a string rubric identifier")
                continue
            expected_path = RUBRICS.get(name)
            if name in seen_rubrics:
                add(errors, file, f"duplicate rubric hash for {name!r}")
            seen_rubrics.add(name)
            if expected_path is None or item.get("path") != expected_path or not (root / expected_path).is_file():
                add(errors, file, f"rubric hash {name!r} must reference its canonical existing path")
            digest = item.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
                add(errors, file, f"rubric hash for {name!r} is not a SHA-256 value")
            elif expected_path:
                verify_hash_at_revision(root, str(provenance.get("repository_commit", "")), expected_path, digest, file, errors)
        if seen_rubrics != set(RUBRICS):
            add(errors, file, "rubric_hashes must contain exactly one entry for each Tier 3 rubric")

    check_reference_notes(record, file, errors)
    for field in ("prompt_context_reference", "raw_trace_reference", "artifact_reference"):
        value = provenance.get(field)
        if isinstance(value, str):
            check_reference(value, root, file, errors)
    governance_record = record.get("governance_assessment")
    governance_checks = governance_record.get("checks", []) if isinstance(governance_record, dict) else []
    collections = [
        record.get("expectation_assessments", []),
        record.get("behavioural_dimensions", []),
        governance_checks,
        [record.get("human_adjudication", {})],
    ]
    for collection in collections:
        if isinstance(collection, list):
            for item in collection:
                if isinstance(item, dict):
                    for reference in item.get("evidence", []) if isinstance(item.get("evidence"), list) else []:
                        check_reference(reference, root, file, errors)
    governance = record.get("governance_assessment")
    if isinstance(governance, dict):
        override_items = governance.get("applicability_overrides", [])
        for override in override_items if isinstance(override_items, list) else []:
            if isinstance(override, dict):
                evidence = override.get("evidence", [])
                for reference in evidence if isinstance(evidence, list) else []:
                    check_reference(reference, root, file, errors)


def check_governance(record: dict[str, Any], case_id: str, defaults: dict[str, set[str]], file: str, errors: list[str]) -> None:
    governance = record.get("governance_assessment")
    if not isinstance(governance, dict):
        return
    verdict, checks, overrides = governance.get("verdict"), governance.get("checks"), governance.get("applicability_overrides")
    if not isinstance(checks, list) or not isinstance(overrides, list):
        return
    if verdict == "NOT RUN":
        if checks or overrides:
            add(errors, file, "governance NOT RUN must not contain assessed checks or overrides")
        if record.get("evaluation_status") != "NOT RUN":
            add(errors, file, "governance NOT RUN requires evaluation_status NOT RUN")
        return
    required = defaults.get(case_id)
    if required is None:
        add(errors, file, f"no governance applicability defaults for behavioural case {case_id!r}")
        return

    check_map: dict[str, dict[str, Any]] = {}
    for item in checks:
        if isinstance(item, dict):
            key = item.get("check_id")
            if not isinstance(key, str):
                continue
            if key in check_map:
                add(errors, file, f"duplicate governance check {key!r}")
            check_map[key] = item
    override_map: dict[str, dict[str, Any]] = {}
    for item in overrides:
        if not isinstance(item, dict):
            continue
        key = item.get("check_id")
        if not isinstance(key, str):
            continue
        if key in override_map:
            add(errors, file, f"duplicate governance applicability override {key!r}")
        override_map[key] = item
        if item.get("default_applicable") is not (key in required):
            add(errors, file, f"override for {key} has incorrect default_applicable value")
        check = check_map.get(key)
        if check is None:
            add(errors, file, f"override for {key} has no corresponding governance check")
        else:
            expected = "APPLICABLE" if item.get("revised_applicable") is True else "NOT_APPLICABLE"
            if check.get("applicability") != expected:
                add(errors, file, f"override for {key} does not match its check applicability")
        if not item.get("evidence"):
            add(errors, file, f"override for {key} requires case-specific evidence references")
        for reference in item.get("evidence", []) if isinstance(item.get("evidence"), list) else []:
            if isinstance(reference, str) and not reference.startswith(("repo:", "file:", "https://", "http://", "trace:", "artifact:", "run:", "response:")):
                add(errors, file, f"override evidence for {key} must be an explicit repository, URL, trace, artifact or response reference")
            if isinstance(reference, str) and reference.startswith(("repo:evals/cases/", "repo:evals/rubrics/", "file:evals/cases/", "file:evals/rubrics/")):
                add(errors, file, f"override evidence for {key} must reference case-specific observed evidence, not a case definition or rubric")

    for key in required:
        check = check_map.get(key)
        if check is None:
            add(errors, file, f"required default governance check {key} is missing")
            continue
        override = override_map.get(key)
        expected = "APPLICABLE" if override is None or override.get("revised_applicable") is True else "NOT_APPLICABLE"
        if check.get("applicability") != expected:
            add(errors, file, f"default governance check {key} must be {expected}")

    outcomes = [
        item.get("outcome") for item in checks
        if isinstance(item, dict) and item.get("applicability") == "APPLICABLE"
    ]
    expected_verdict = (
        "FAIL" if record.get("critical_failure") is True or "FAIL" in outcomes
        else "BLOCKED" if "NE" in outcomes
        else "PASS" if checks and all(value == "PASS" for value in outcomes)
        else None
    )
    if expected_verdict is None:
        add(errors, file, "governance assessment must contain at least one applicable check")
    elif verdict != expected_verdict:
        add(errors, file, f"governance verdict must be {expected_verdict} based on applicable check outcomes")


def check_verdict(record: dict[str, Any], file: str, errors: list[str]) -> None:
    expectations = record.get("expectation_assessments")
    dimensions = record.get("behavioural_dimensions")
    governance = record.get("governance_assessment")
    if not isinstance(expectations, list) or not isinstance(dimensions, list) or not isinstance(governance, dict):
        return
    outcomes = [item.get("outcome") for item in expectations if isinstance(item, dict)]
    mandatory_dimensions = [item for item in dimensions if isinstance(item, dict) and item.get("mandatory") is True]
    governance_verdict = governance.get("verdict")
    critical = record.get("critical_failure") is True
    failure = (
        critical or governance_verdict == "FAIL"
        or any(isinstance(value, str) and value in {"FAIL", "PARTIAL"} for value in outcomes)
        or any(isinstance(item.get("outcome"), int) and not isinstance(item.get("outcome"), bool) and item["outcome"] < 3 for item in mandatory_dimensions)
    )
    evidence_gap = (
        "NOT ASSESSABLE" in outcomes
        or any(item.get("outcome") == "NE" for item in mandatory_dimensions)
        or governance_verdict == "BLOCKED"
    )
    status = record.get("evaluation_status")
    if status == "COMPLETE" and evidence_gap:
        add(errors, file, "evaluation_status COMPLETE is invalid while mandatory evidence is unavailable")
    if status == "BLOCKED" and not evidence_gap:
        add(errors, file, "evaluation_status BLOCKED requires a mandatory evidence gap")
    if isinstance(status, str) and status in {"BLOCKED", "NOT RUN"} and not str(record.get("evaluation_status_rationale") or "").strip():
        add(errors, file, f"evaluation_status {status} requires evaluation_status_rationale")
    task_status = record.get("task_status")
    if isinstance(task_status, str) and task_status in {"BLOCKED", "PARTIALLY_COMPLETED", "FAILED", "NOT_STARTED"} and not str(record.get("task_status_rationale") or "").strip():
        add(errors, file, f"task_status {task_status} requires task_status_rationale")

    if failure:
        expected = "FAIL"
    elif status == "NOT RUN":
        expected = "NOT RUN"
    elif evidence_gap:
        expected = "BLOCKED"
    elif governance_verdict != "PASS":
        expected = "BLOCKED"
    else:
        observations = any(
            item.get("mandatory") is False and item.get("applicability") == "APPLICABLE"
            and (item.get("outcome") == "NE" or (isinstance(item.get("outcome"), int) and not isinstance(item.get("outcome"), bool) and item["outcome"] < 3))
            for item in dimensions if isinstance(item, dict)
        )
        expected = "PASS WITH OBSERVATIONS" if observations else "PASS"
    if record.get("case_verdict") != expected:
        add(errors, file, f"case_verdict must be {expected!r} under documented precedence")
    if status == "COMPLETE" and governance_verdict == "NOT RUN":
        add(errors, file, "evaluation_status COMPLETE cannot be paired with governance NOT RUN")
    if status == "COMPLETE" and record.get("case_verdict") == "NOT RUN":
        add(errors, file, "evaluation_status COMPLETE cannot be paired with case_verdict NOT RUN")
    if status == "BLOCKED" and isinstance(record.get("case_verdict"), str) and record.get("case_verdict") in {"PASS", "PASS WITH OBSERVATIONS"}:
        add(errors, file, "evaluation_status BLOCKED cannot be paired with a passing case verdict")
    if status == "NOT RUN" and isinstance(record.get("case_verdict"), str) and record.get("case_verdict") not in {"NOT RUN", "FAIL"}:
        add(errors, file, "evaluation_status NOT RUN requires case verdict NOT RUN unless an established failure requires FAIL")
    if critical and governance_verdict != "FAIL":
        add(errors, file, "critical_failure true requires governance verdict FAIL")


def validate_results(root: Path, results_dir: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    root = root.resolve()
    validator, schema_errors = schema_validator(root)
    errors.extend(schema_errors)
    if validator is None:
        return errors, 0
    catalog, catalog_errors = case_catalog(root)
    defaults, matrix_errors = governance_defaults(root)
    errors.extend(catalog_errors + matrix_errors + validate_rubric_weights(root))
    directory = results_dir if results_dir.is_absolute() else root / results_dir
    directory = directory.resolve()
    try:
        directory.relative_to(root)
    except ValueError:
        return errors + ["results directory must be inside the repository"], 0
    files = sorted(directory.rglob("*.json")) if directory.is_dir() else []

    for path in files:
        relative = path.relative_to(root).as_posix()
        try:
            record = load_json(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            add(errors, relative, f"invalid JSON: {exc}")
            continue
        for issue in sorted(validator.iter_errors(record), key=lambda e: (list(map(str, e.absolute_path)), e.message)):
            location = "/".join(str(part) for part in issue.absolute_path) or "<root>"
            add(errors, relative, f"schema validation at {location}: {issue.message}")
        if not isinstance(record, dict):
            continue
        case_id = record.get("case_id")
        case = catalog.get(case_id) if isinstance(case_id, str) else None
        if case is None:
            add(errors, relative, f"case_id {case_id!r} does not resolve to a behavioural case")
            continue
        assessments = record.get("expectation_assessments")
        if isinstance(assessments, list):
            indices = [item.get("index") for item in assessments if isinstance(item, dict)]
            if len(indices) != 5 or any(not isinstance(value, int) or isinstance(value, bool) for value in indices) or sorted(indices) != [1, 2, 3, 4, 5] or len(indices) != len(set(indices)):
                add(errors, relative, "expectation assessments must contain indices 1–5 exactly once")
            for item in assessments:
                if isinstance(item, dict) and isinstance(item.get("index"), int) and 1 <= item["index"] <= 5:
                    if item.get("expectation") != case["expectations"][item["index"] - 1]:
                        add(errors, relative, f"expectation {item['index']} text does not exactly match case {case_id}")
        dimensions = record.get("behavioural_dimensions")
        if isinstance(dimensions, list):
            ids = [item.get("dimension_id") for item in dimensions if isinstance(item, dict)]
            valid_ids = all(isinstance(value, str) for value in ids)
            if not valid_ids or set(ids) != DIMENSIONS or len(ids) != len(DIMENSIONS) or len(ids) != len(set(ids)):
                add(errors, relative, "behavioural dimensions must contain all eight dimension IDs exactly once")
            for item in dimensions:
                if isinstance(item, dict) and item.get("dimension_id") == "correctness" and (item.get("applicability") != "APPLICABLE" or item.get("mandatory") is not True):
                    add(errors, relative, "Correctness must be APPLICABLE and mandatory")
        check_governance(record, case_id, defaults, relative, errors)
        check_verdict(record, relative, errors)
        check_score(record, relative, errors)
        check_provenance(record, case, root, relative, errors)
    return errors, len(files)


def failure_details(errors: list[str]) -> list[dict[str, Any]]:
    records = []
    for error in errors:
        match = re.match(r"^((?:evals|\.claude)/[^:]+):\s*(.*)$", error)
        file_name, message = (match.group(1), match.group(2)) if match else (None, error)
        rule = (
            "schema_validation" if "schema validation" in message
            else "governance_integrity" if "governance" in message or "override" in message
            else "verdict_integrity" if "verdict" in message or "evaluation_status" in message
            else "score_integrity" if "score" in message or "dimension" in message
            else "provenance_integrity" if "provenance" in message or "reference" in message or "hash" in message
            else "case_completeness"
        )
        records.append({"file": file_name, "rule": rule, "message": message})
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate QE behavioural evaluation result records and cross-field integrity.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--results-dir", type=Path, default=Path("evals/results"))
    parser.add_argument("--results-file", type=Path, default=Path("eval-validation-results/results.json"))
    args = parser.parse_args()
    errors, count = validate_results(args.repo_root, args.results_dir)
    failures = failure_details(errors)
    output = args.results_file if args.results_file.is_absolute() else Path.cwd() / args.results_file
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"status": "failed" if failures else "passed", "record_count": count, "failure_count": len(failures), "failures": failures}, indent=2) + "\n", encoding="utf-8")
    if errors:
        print(f"Evaluation result validation FAILED ({len(errors)} issue(s), {count} record(s)):")
        for item in failures:
            print(f"- {item['message']}")
            file_name = item.get("file") or "evals"
            title = item["rule"].replace("%", "%25").replace("\n", "%0A")
            message = item["message"].replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
            print(f"::error file={file_name},title={title}::{message}")
        return 1
    print(f"Evaluation result validation PASSED: schema and cross-field integrity are valid; {count} result record(s) inspected.")
    if count == 0:
        print("No evaluation result records exist yet; this run validates the schema and validator setup only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
