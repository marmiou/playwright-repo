#!/usr/bin/env python3
"""Deterministic Tier 1 validation for the QE skill evaluation case dataset."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


EXPECTED_SKILL_COUNT = 10
EXPECTED_CASE_COMPOSITION = {"positive": 3, "negative": 2, "behavioral": 1}


def _load_json(path: Path) -> Any:
    """Load JSON while rejecting duplicate object keys."""

    def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON object key: {key!r}")
            result[key] = value
        return result

    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=reject_duplicate_keys)


def _frontmatter_fields(skill_file: Path) -> tuple[str | None, str | None, str | None]:
    """Read the simple name/description fields from a skill's YAML frontmatter.

    Skill descriptions in this repository are single-line plain scalars. This
    deliberately avoids pretending to be a general YAML parser.
    """
    try:
        lines = skill_file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return None, None, f"cannot read skill file: {exc}"

    if not lines or lines[0].strip() != "---":
        return None, None, "missing opening YAML frontmatter delimiter"

    try:
        closing = lines.index("---", 1)
    except ValueError:
        return None, None, "missing closing YAML frontmatter delimiter"

    fields: dict[str, list[str]] = {"name": [], "description": []}
    for line in lines[1:closing]:
        for field in fields:
            prefix = f"{field}:"
            if line.startswith(prefix):
                fields[field].append(line[len(prefix):].strip())

    for field, values in fields.items():
        if len(values) != 1 or not values[0]:
            return None, None, f"frontmatter must contain exactly one non-empty {field!r} field"

    # The current repository convention uses unquoted, single-line scalars.
    # Reject quoted/block scalar forms rather than silently mis-parse them.
    name, description = fields["name"][0], fields["description"][0]
    if name[:1] in {"'", '"', "|", ">"} or description[:1] in {"'", '"', "|", ">"}:
        return None, None, "quoted or block YAML scalars are not supported by the current frontmatter convention"
    return name, description, None


def _format_schema_error(error: Any) -> str:
    location = ".".join(str(part) for part in error.absolute_path)
    return f"schema validation at {location or '<root>'}: {error.message}"


def validate_repository(repo_root: Path) -> list[str]:
    """Return all deterministic Tier 1 validation errors for a repository."""
    errors: list[str] = []
    repo_root = repo_root.resolve()
    evals_dir = repo_root / "evals"
    cases_dir = evals_dir / "cases"
    skills_dir = repo_root / ".claude" / "skills"
    schema_path = evals_dir / "schemas" / "case.schema.json"

    if not schema_path.is_file():
        return [f"missing case schema: {schema_path}"]

    try:
        schema = _load_json(schema_path)
        Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, ValueError, SchemaError) as exc:
        return [f"case schema is invalid or unreadable: {exc}"]

    schema_validator = Draft202012Validator(schema, format_checker=FormatChecker())

    if not skills_dir.is_dir():
        return [f"missing skills directory: {skills_dir}"]
    if not cases_dir.is_dir():
        return [f"missing case directory: {cases_dir}"]

    skill_files = sorted(
        path / "SKILL.md"
        for path in skills_dir.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )
    skill_ids = {path.parent.name for path in skill_files}

    if len(skill_files) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"expected exactly {EXPECTED_SKILL_COUNT} skill files under .claude/skills/*/SKILL.md; "
            f"found {len(skill_files)}"
        )

    case_files = sorted(cases_dir.glob("*.json"))
    case_stems = {path.stem for path in case_files}
    if case_stems != skill_ids:
        missing_cases = sorted(skill_ids - case_stems)
        orphan_cases = sorted(case_stems - skill_ids)
        if missing_cases:
            errors.append(f"missing case files for skills: {', '.join(missing_cases)}")
        if orphan_cases:
            errors.append(f"case files have no matching skill directory: {', '.join(orphan_cases)}")

    if len(case_files) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"expected exactly {EXPECTED_SKILL_COUNT} case JSON files; found {len(case_files)}"
        )

    skill_metadata: dict[str, tuple[str | None, str | None]] = {}
    for skill_file in skill_files:
        skill_id = skill_file.parent.name
        frontmatter_name, description, frontmatter_error = _frontmatter_fields(skill_file)
        if frontmatter_error:
            errors.append(f"{skill_file.relative_to(repo_root)}: {frontmatter_error}")
        skill_metadata[skill_id] = (frontmatter_name, description)
        if frontmatter_name is not None and frontmatter_name != skill_id:
            errors.append(
                f"{skill_file.relative_to(repo_root)}: frontmatter name {frontmatter_name!r} "
                f"does not match directory name {skill_id!r}"
            )

    seen_case_ids: dict[str, str] = {}

    for case_file in case_files:
        relative_file = case_file.relative_to(repo_root).as_posix()
        try:
            data = _load_json(case_file)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{relative_file}: invalid JSON: {exc}")
            continue

        for schema_error in sorted(
            schema_validator.iter_errors(data),
            key=lambda item: (list(map(str, item.absolute_path)), item.message),
        ):
            errors.append(f"{relative_file}: {_format_schema_error(schema_error)}")

        if not isinstance(data, dict):
            continue

        skill_id = data.get("skill")
        if not isinstance(skill_id, str):
            continue

        if case_file.stem != skill_id:
            errors.append(
                f"{relative_file}: filename stem {case_file.stem!r} does not match skill {skill_id!r}"
            )

        expected_source = f".claude/skills/{skill_id}/SKILL.md"
        source = data.get("source")
        if isinstance(source, dict):
            source_path = source.get("path")
            if source_path != expected_source:
                errors.append(
                    f"{relative_file}: source.path must be {expected_source!r}, got {source_path!r}"
                )
            skill_file = repo_root / expected_source
            if not skill_file.is_file():
                errors.append(f"{relative_file}: source skill file does not exist: {expected_source}")
            else:
                expected_description = skill_metadata.get(skill_id, (None, None))[1]
                if expected_description is not None and source.get("description") != expected_description:
                    errors.append(
                        f"{relative_file}: source.description does not exactly match "
                        f"{expected_source} frontmatter"
                    )

        cases = data.get("cases")
        if not isinstance(cases, list):
            continue

        type_counts = {case_type: 0 for case_type in EXPECTED_CASE_COMPOSITION}
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                continue

            case_id = case.get("id")
            if isinstance(case_id, str):
                if case_id in seen_case_ids:
                    errors.append(
                        f"{relative_file}: duplicate case id {case_id!r}; first seen in {seen_case_ids[case_id]}"
                    )
                else:
                    seen_case_ids[case_id] = relative_file

            case_type = case.get("type")
            if case_type in type_counts:
                type_counts[case_type] += 1

            fixture = case.get("fixture")
            if isinstance(fixture, str):
                fixture_candidate = (evals_dir / fixture).resolve()
                try:
                    fixture_candidate.relative_to(evals_dir.resolve())
                except ValueError:
                    errors.append(
                        f"{relative_file}: fixture path escapes evals/: {fixture!r}"
                    )
                else:
                    if not fixture_candidate.is_file():
                        errors.append(
                            f"{relative_file}: fixture does not resolve to a file: {fixture!r}"
                        )
            elif fixture is not None:
                # The JSON Schema reports the invalid type; keep this guard safe.
                pass

            if case_type == "negative":
                routing = case.get("routing_expectation")
                if not isinstance(routing, dict):
                    continue

                allowed = routing.get("allowed_companion_skills", [])
                forbidden = routing.get("forbidden_skills", [])
                primary = routing.get("expected_primary_skill")

                if isinstance(allowed, list) and isinstance(forbidden, list):
                    overlap = sorted(set(allowed) & set(forbidden))
                    if overlap:
                        errors.append(
                            f"{relative_file}: case {case_id!r} has skills in both "
                            f"allowed_companion_skills and forbidden_skills: {', '.join(overlap)}"
                        )

                if skill_id not in forbidden:
                    errors.append(
                        f"{relative_file}: negative case {case_id!r} must forbid its target skill {skill_id!r}"
                    )

                referenced_skills = []
                if isinstance(primary, str):
                    referenced_skills.append(primary)
                    if primary == skill_id:
                        errors.append(
                            f"{relative_file}: negative case {case_id!r} selects its own target skill as primary"
                        )
                if isinstance(allowed, list):
                    referenced_skills.extend(item for item in allowed if isinstance(item, str))
                if isinstance(forbidden, list):
                    referenced_skills.extend(item for item in forbidden if isinstance(item, str))

                unknown = sorted(set(referenced_skills) - skill_ids)
                if unknown:
                    errors.append(
                        f"{relative_file}: negative case {case_id!r} references unknown skills: {', '.join(unknown)}"
                    )

        if type_counts != EXPECTED_CASE_COMPOSITION:
            errors.append(
                f"{relative_file}: expected case composition {EXPECTED_CASE_COMPOSITION}, "
                f"found {type_counts}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate QE skill evaluation case schemas and repository-level dataset invariants."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (defaults to the parent of evals/).",
    )
    args = parser.parse_args()

    errors = validate_repository(args.repo_root)
    if errors:
        print(f"Tier 1 case validation FAILED ({len(errors)} issue(s)):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Tier 1 case validation PASSED: {EXPECTED_SKILL_COUNT} skills, "
        f"{EXPECTED_SKILL_COUNT * sum(EXPECTED_CASE_COMPOSITION.values())} cases; "
        "Draft 2020-12 schema and repository-level invariants are valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
