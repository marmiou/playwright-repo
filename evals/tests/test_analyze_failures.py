"""Tests for deterministic CI failure analysis and report generation."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analyze_failures import analyze, render_report


class AnalyzeFailuresTests(unittest.TestCase):
    def test_same_commit_validator_failure_and_pass_is_classified_flaky(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            failed = root / "101" / "evals"
            passed = root / "102" / "evals"
            failed.mkdir(parents=True)
            passed.mkdir(parents=True)
            (failed / "results.json").write_text(json.dumps({
                "status": "failed",
                "failure_count": 1,
                "failures": [{
                    "case_id": "add-api-test-4",
                    "file": "evals/cases/add-api-test.json",
                    "rule": "skill_or_routing_invariant",
                    "message": "negative case must forbid target skill",
                }],
            }), encoding="utf-8")
            (passed / "results.json").write_text(json.dumps({
                "status": "passed",
                "failure_count": 0,
                "failures": [],
            }), encoding="utf-8")
            runs = [
                {"databaseId": 101, "headSha": "same-sha", "url": "https://example.test/runs/101"},
                {"databaseId": 102, "headSha": "same-sha", "url": "https://example.test/runs/102"},
            ]

            groups = analyze(runs, root)

        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["bucket"], "flaky (failed in some runs, passed in others)")
        self.assertEqual(groups[0]["failed_run_count"], 1)
        self.assertEqual(groups[0]["passed_run_count"], 1)
        self.assertEqual(groups[0]["skill"], "add-api-test")

    def test_playwright_failure_is_grouped_by_test_and_has_run_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / "201" / "playwright"
            results.mkdir(parents=True)
            (results / "results.json").write_text(json.dumps({
                "suites": [{
                    "title": "example.spec.ts",
                    "file": "tests/web/example.spec.ts",
                    "specs": [{
                        "title": "loads the dashboard",
                        "file": "tests/web/example.spec.ts",
                        "tests": [{
                            "results": [{
                                "status": "failed",
                                "error": {"message": "Expected title to be visible"},
                            }],
                        }],
                    }],
                }],
            }), encoding="utf-8")
            groups = analyze([{
                "databaseId": 201,
                "headSha": "playwright-sha",
                "url": "https://example.test/runs/201",
            }], root)

        self.assertEqual(len(groups), 1)
        self.assertIn("loads the dashboard", groups[0]["key"])
        self.assertEqual(groups[0]["failed_run_count"], 1)
        self.assertIn("https://example.test/runs/201", groups[0]["evidence"])

    def test_missing_artifacts_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            groups = analyze([{"databaseId": 301, "headSha": "missing"}], Path(directory))

        self.assertEqual(groups, [])

    def test_empty_report_states_no_failures(self) -> None:
        report = render_report([], 1)
        self.assertIn("No CI failure artifacts", report)
        self.assertIn("No issue should be created or updated", report)


if __name__ == "__main__":
    unittest.main()
