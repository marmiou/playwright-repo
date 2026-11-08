"""Unit tests for the deterministic Tier 1 QE case validator."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_cases import validate_repository


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_IDS = [
    "add-api-test",
    "add-web-test",
    "analyze-requirement",
    "design-test-cases",
    "design-test-strategy",
    "evaluate-quality",
    "investigate-failure",
    "qe-workflow",
    "review-tests",
    "verify-implementation",
]


def _case(skill: str, index: int, case_type: str) -> dict:
    case = {
        "id": f"{skill}-{index}",
        "type": case_type,
        "prompt": f"Synthetic prompt for {skill} case {index}.",
        "expected_routing": "do_not_activate" if case_type == "negative" else "activate",
        "expectations": [f"Observable expectation {number}." for number in range(1, 6 if case_type == "behavioral" else 2)],
        "fixture": None,
    }
    if case_type == "negative":
        case["routing_expectation"] = {
            "expected_primary_skill": None,
            "expected_action": "direct_response",
            "allowed_companion_skills": [],
            "forbidden_skills": [skill],
            "direct_response_allowed": True,
            "rationale": "A direct response is the appropriate alternative.",
        }
    return case


def _write_synthetic_repository(root: Path) -> None:
    (root / "evals" / "schemas").mkdir(parents=True)
    shutil.copy2(
        REPO_ROOT / "evals" / "schemas" / "case.schema.json",
        root / "evals" / "schemas" / "case.schema.json",
    )
    (root / ".claude" / "skills").mkdir(parents=True)
    (root / "evals" / "cases").mkdir(parents=True)

    for skill in SKILL_IDS:
        description = f"Description for {skill}."
        skill_dir = root / ".claude" / "skills" / skill
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {skill}\ndescription: {description}\n---\n\n# {skill}\n",
            encoding="utf-8",
        )
        cases = (
            [_case(skill, number, "positive") for number in range(1, 4)]
            + [_case(skill, number, "negative") for number in range(4, 6)]
            + [_case(skill, 6, "behavioral")]
        )
        data = {
            "schema_version": "1.0.0",
            "skill": skill,
            "source": {
                "path": f".claude/skills/{skill}/SKILL.md",
                "description": description,
            },
            "cases": cases,
        }
        (root / "evals" / "cases" / f"{skill}.json").write_text(
            json.dumps(data, indent=2) + "\n",
            encoding="utf-8",
        )


class ValidateCurrentDatasetTests(unittest.TestCase):
    def test_repository_dataset_is_valid(self) -> None:
        self.assertEqual(validate_repository(REPO_ROOT), [])


class ValidateSyntheticDatasetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        _write_synthetic_repository(self.root)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _case_file(self, skill: str) -> Path:
        return self.root / "evals" / "cases" / f"{skill}.json"

    def _read_case_file(self, skill: str) -> dict:
        return json.loads(self._case_file(skill).read_text(encoding="utf-8"))

    def _write_case_file(self, skill: str, data: dict) -> None:
        self._case_file(skill).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def test_duplicate_case_id_across_files_is_rejected(self) -> None:
        first = self._read_case_file(SKILL_IDS[0])
        second = self._read_case_file(SKILL_IDS[1])
        second["cases"][0]["id"] = first["cases"][0]["id"]
        self._write_case_file(SKILL_IDS[1], second)

        errors = validate_repository(self.root)
        self.assertTrue(any("duplicate case id" in error for error in errors), errors)

    def test_source_description_drift_is_rejected(self) -> None:
        data = self._read_case_file(SKILL_IDS[0])
        data["source"]["description"] = "Outdated description."
        self._write_case_file(SKILL_IDS[0], data)

        errors = validate_repository(self.root)
        self.assertTrue(any("source.description" in error for error in errors), errors)

    def test_negative_case_must_forbid_its_target_skill(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"][3]["routing_expectation"]["forbidden_skills"] = []
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("must forbid its target skill" in error for error in errors), errors)

    def test_unknown_routing_skill_is_rejected(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"][3]["routing_expectation"]["allowed_companion_skills"] = ["not-a-real-skill"]
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("unknown skills" in error for error in errors), errors)

    def test_unresolved_fixture_is_rejected(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"][0]["fixture"] = "fixtures/missing.json"
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("fixture does not resolve" in error for error in errors), errors)

    def test_fixture_path_escape_is_rejected(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"][0]["fixture"] = "../outside.json"
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("fixture path escapes evals/" in error for error in errors), errors)

    def test_invalid_case_composition_is_rejected_by_schema(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"].pop()
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("schema validation" in error for error in errors), errors)

    def test_allowed_and_forbidden_overlap_is_rejected(self) -> None:
        skill = SKILL_IDS[0]
        data = self._read_case_file(skill)
        data["cases"][3]["routing_expectation"]["allowed_companion_skills"] = [skill]
        self._write_case_file(skill, data)

        errors = validate_repository(self.root)
        self.assertTrue(any("both allowed_companion_skills and forbidden_skills" in error for error in errors), errors)

    def test_skill_frontmatter_name_must_match_directory(self) -> None:
        skill_file = self.root / ".claude" / "skills" / SKILL_IDS[0] / "SKILL.md"
        content = skill_file.read_text(encoding="utf-8").replace(
            f"name: {SKILL_IDS[0]}", "name: mismatched-name", 1
        )
        skill_file.write_text(content, encoding="utf-8")

        errors = validate_repository(self.root)
        self.assertTrue(any("frontmatter name" in error for error in errors), errors)

    def test_duplicate_json_object_keys_are_rejected(self) -> None:
        skill = SKILL_IDS[0]
        path = self._case_file(skill)
        content = path.read_text(encoding="utf-8")
        content = content.replace(
            f'"skill": "{skill}",',
            f'"skill": "{skill}",\n  "skill": "{skill}",',
            1,
        )
        path.write_text(content, encoding="utf-8")

        errors = validate_repository(self.root)
        self.assertTrue(any("duplicate JSON object key" in error for error in errors), errors)

    def test_extra_skill_without_dataset_is_rejected(self) -> None:
        extra_skill = self.root / ".claude" / "skills" / "unexpected-skill"
        extra_skill.mkdir()
        (extra_skill / "SKILL.md").write_text(
            "---\nname: unexpected-skill\ndescription: Extra skill.\n---\n",
            encoding="utf-8",
        )

        errors = validate_repository(self.root)
        self.assertTrue(any("expected exactly 10 skill files" in error for error in errors), errors)
        self.assertTrue(any("missing case files" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
