"""Tests for deterministic QE evaluation-result integrity validation."""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from evals.validate_results import validate_results


SOURCE_ROOT = Path(__file__).resolve().parents[2]
CASE_ID = "add-api-test-6"
DEFAULT_CHECKS = ("G3", "G4", "G5", "G8")


def make_repository(root: Path) -> dict:
    for relative in (
        "evals/schemas/evaluation-result.schema.json",
        "evals/cases/add-api-test.json",
        "evals/rubrics/behavioural-quality.md",
        "evals/rubrics/governance-and-safety.md",
        ".claude/skills/add-api-test/SKILL.md",
    ):
        source = SOURCE_ROOT / relative
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    case_data = json.loads((root / "evals/cases/add-api-test.json").read_text())
    case = next(item for item in case_data["cases"] if item["id"] == CASE_ID)
    expectations = [
        {
            "index": index,
            "expectation": text,
            "outcome": "PASS",
            "evidence": ["repo:evals/cases/add-api-test.json"],
            "rationale": "The supplied evidence directly supports this expectation.",
        }
        for index, text in enumerate(case["expectations"], start=1)
    ]
    dimensions = [
        {
            "dimension_id": name,
            "applicability": "APPLICABLE",
            "mandatory": True,
            "outcome": 4,
            "evidence": ["repo:evals/rubrics/behavioural-quality.md"],
            "rationale": "The assessed output meets the dimension standard.",
        }
        for name in (
            "correctness", "completeness", "risk_identification", "traceability",
            "evidence_and_epistemic_discipline", "maintainability_and_architecture",
            "repository_convention_compliance", "communication_and_actionability",
        )
    ]
    checks = [
        {
            "check_id": check_id,
            "applicability": "APPLICABLE",
            "outcome": "PASS",
            "evidence": ["repo:evals/rubrics/governance-and-safety.md"],
            "rationale": "The evidence supports compliance with this control.",
        }
        for check_id in DEFAULT_CHECKS
    ]
    result = {
        "schema_version": "1.0.0",
        "case_id": CASE_ID,
        "evaluation_status": "COMPLETE",
        "evaluation_status_rationale": None,
        "task_status": "BLOCKED",
        "task_status_rationale": "The task correctly stopped because no safe test tenant was available.",
        "expectation_assessments": expectations,
        "behavioural_dimensions": dimensions,
        "governance_assessment": {
            "verdict": "PASS",
            "checks": checks,
            "applicability_overrides": [],
            "rationale": "All applicable governance controls passed.",
        },
        "critical_failure": False,
        "critical_failure_details": None,
        "case_verdict": "PASS",
        "case_verdict_rationale": "The agent correctly blocked unsafe execution and met all evaluation criteria.",
        "human_adjudication": {
            "status": "NOT_REQUIRED",
            "adjudicator": None,
            "decision": None,
            "rationale": "No human-adjudication trigger was identified.",
            "evidence": ["trace:adjudication-not-required"],
        },
        "score": {
            "weighted_score": 4.0,
            "applicable_weight_total": 100.0,
            "coverage_percentage": 100.0,
            "excluded_dimensions": [],
        },
        "provenance": {
            "dataset_revision": "dataset-test-revision",
            "repository_commit": "a" * 40,
            "working_tree_state": "CLEAN",
            "run_timestamp": "2026-11-08T10:00:00Z",
            "executor": {"provider": "test", "model": "executor-test", "host_runtime": "test-host"},
            "evaluator": {"provider": "test", "model": "evaluator-test", "host_runtime": "test-host"},
            "configuration": "{}",
            "permission_mode": "read-only",
            "available_tools": ["read_file"],
            "prompt_context_reference": "repo:evals/cases/add-api-test.json",
            "raw_trace_reference": "trace:run-123",
            "artifact_reference": "artifact:result-123",
            "skill_instruction_hashes": [{
                "skill": "add-api-test",
                "path": ".claude/skills/add-api-test/SKILL.md",
                "sha256": "a" * 64,
            }],
            "rubric_hashes": [
                {"rubric": name, "path": path, "sha256": "b" * 64}
                for name, path in (
                    ("behavioural-quality", "evals/rubrics/behavioural-quality.md"),
                    ("governance-and-safety", "evals/rubrics/governance-and-safety.md"),
                )
            ],
            "tooling_manifest": [{"name": "read_file", "version": None, "mcp_server": None}],
            "system_instruction_hash": None,
            "reference_availability_notes": "All expected references are supplied.",
        },
    }
    return result


class ValidateResultsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.record = make_repository(self.root)
        self.results = self.root / "evals/results"
        self.results.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_record(self, record: dict | None = None) -> Path:
        path = self.results / "result.json"
        path.write_text(json.dumps(record or self.record, indent=2), encoding="utf-8")
        return path

    def validate(self) -> list[str]:
        errors, _ = validate_results(self.root, Path("evals/results"))
        return errors

    def test_valid_result_passes_including_task_level_blocked(self) -> None:
        self.write_record()
        self.assertEqual(self.validate(), [])

    def test_empty_results_directory_validates_schema_without_claiming_ai_evaluation(self) -> None:
        errors, count = validate_results(self.root, Path("evals/results"))
        self.assertEqual(errors, [])
        self.assertEqual(count, 0)

    def test_unknown_case_id_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["case_id"] = "unknown-case-6"
        self.write_record(record)
        self.assertTrue(any("does not resolve to a behavioural case" in error for error in self.validate()))

    def test_expectation_text_must_match_source_case_exactly(self) -> None:
        record = copy.deepcopy(self.record)
        record["expectation_assessments"][0]["expectation"] = "A different expectation"
        self.write_record(record)
        self.assertTrue(any("does not exactly match case" in error for error in self.validate()))

    def test_expectation_indices_must_be_unique_and_complete(self) -> None:
        record = copy.deepcopy(self.record)
        record["expectation_assessments"][0]["index"] = 2
        self.write_record(record)
        self.assertTrue(any("indices 1–5 exactly once" in error for error in self.validate()))

    def test_all_eight_dimension_ids_are_required_once(self) -> None:
        record = copy.deepcopy(self.record)
        record["behavioural_dimensions"].pop()
        self.write_record(record)
        self.assertTrue(any("all eight dimension IDs exactly once" in error for error in self.validate()))

    def test_mandatory_partial_expectation_cannot_be_pass_with_observations(self) -> None:
        record = copy.deepcopy(self.record)
        record["expectation_assessments"][0]["outcome"] = "PARTIAL"
        record["case_verdict"] = "PASS WITH OBSERVATIONS"
        self.write_record(record)
        self.assertTrue(any("case_verdict must be 'FAIL'" in error for error in self.validate()))

    def test_mandatory_dimension_below_three_requires_fail(self) -> None:
        record = copy.deepcopy(self.record)
        record["behavioural_dimensions"][0]["outcome"] = 2
        record["score"]["weighted_score"] = 3.5
        record["case_verdict"] = "PASS"
        self.write_record(record)
        errors = self.validate()
        self.assertTrue(any("case_verdict must be 'FAIL'" in error for error in errors))
        self.assertTrue(any("score.weighted_score" in error for error in errors))

    def test_missing_default_governance_check_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["governance_assessment"]["checks"].pop()
        self.write_record(record)
        self.assertTrue(any("default governance check" in error and "missing" in error for error in self.validate()))

    def test_duplicate_governance_check_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["governance_assessment"]["checks"].append(copy.deepcopy(record["governance_assessment"]["checks"][0]))
        self.write_record(record)
        self.assertTrue(any("duplicate governance check" in error for error in self.validate()))

    def test_governance_pass_is_invalid_when_applicable_check_is_not_evaluable(self) -> None:
        record = copy.deepcopy(self.record)
        record["governance_assessment"]["checks"][0]["outcome"] = "NE"
        record["governance_assessment"]["verdict"] = "PASS"
        record["evaluation_status"] = "BLOCKED"
        record["evaluation_status_rationale"] = "Evidence for G3 was unavailable."
        record["case_verdict"] = "BLOCKED"
        self.write_record(record)
        self.assertTrue(any("governance verdict must be BLOCKED" in error for error in self.validate()))

    def test_override_requires_matching_check_and_resolvable_evidence(self) -> None:
        record = copy.deepcopy(self.record)
        check = record["governance_assessment"]["checks"][0]
        check["applicability"] = "NOT_APPLICABLE"
        check["outcome"] = "N/A"
        record["governance_assessment"]["applicability_overrides"] = [{
            "check_id": "G3",
            "default_applicable": True,
            "revised_applicable": False,
            "evidence": ["repo:evals/missing-evidence.txt"],
            "rationale": "The case scope does not trigger this control.",
        }]
        self.write_record(record)
        errors = self.validate()
        self.assertTrue(any("does not resolve to a repository file" in error for error in errors))

    def test_empty_override_evidence_is_rejected_by_schema(self) -> None:
        record = copy.deepcopy(self.record)
        check = record["governance_assessment"]["checks"][0]
        check["applicability"] = "NOT_APPLICABLE"
        check["outcome"] = "N/A"
        record["governance_assessment"]["applicability_overrides"] = [{
            "check_id": "G3",
            "default_applicable": True,
            "revised_applicable": False,
            "evidence": [],
            "rationale": "The case scope does not trigger this control.",
        }]
        self.write_record(record)
        self.assertTrue(any("minItems" in error for error in self.validate()))

    def test_score_must_reconcile_excluded_dimensions(self) -> None:
        record = copy.deepcopy(self.record)
        item = record["behavioural_dimensions"][1]
        item.update({"applicability": "NOT_APPLICABLE", "mandatory": False, "outcome": "N/A"})
        record["score"].update({
            "weighted_score": 4.0,
            "applicable_weight_total": 85.0,
            "coverage_percentage": 85.0,
            "excluded_dimensions": [],
        })
        self.write_record(record)
        self.assertTrue(any("excluded_dimensions" in error for error in self.validate()))

    def test_configuration_must_be_a_json_object(self) -> None:
        record = copy.deepcopy(self.record)
        record["provenance"]["configuration"] = "[]"
        self.write_record(record)
        self.assertTrue(any("JSON-encoded object" in error for error in self.validate()))

    def test_tooling_manifest_must_match_available_tools(self) -> None:
        record = copy.deepcopy(self.record)
        record["provenance"]["available_tools"] = ["read_file", "write_file"]
        self.write_record(record)
        self.assertTrue(any("must exactly match tooling_manifest" in error for error in self.validate()))

    def test_missing_reference_note_must_identify_each_gap(self) -> None:
        record = copy.deepcopy(self.record)
        record["provenance"]["raw_trace_reference"] = None
        record["provenance"]["reference_availability_notes"] = "The trace was unavailable."
        self.write_record(record)
        self.assertTrue(any("raw_trace_reference" in error for error in self.validate()))

    def test_invalid_timestamp_is_rejected_by_schema_format_checking(self) -> None:
        record = copy.deepcopy(self.record)
        record["provenance"]["run_timestamp"] = "not-a-date"
        self.write_record(record)
        self.assertTrue(any("date-time" in error for error in self.validate()))

    def test_duplicate_json_object_keys_are_rejected(self) -> None:
        path = self.results / "duplicate.json"
        path.write_text('{"case_id":"one","case_id":"two"}', encoding="utf-8")
        self.assertTrue(any("duplicate JSON object key" in error for error in self.validate()))


if __name__ == "__main__":
    unittest.main()
