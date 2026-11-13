import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ci_status import status_is_acceptable


class StatusPolicyTests(unittest.TestCase):
    def evaluate(self, step, result, *, evals_changed=False, is_main_push=False, tests_result="success"):
        return status_is_acceptable(
            step,
            result,
            evals_changed=evals_changed,
            is_main_push=is_main_push,
            tests_result=tests_result,
        )

    def test_required_jobs_must_succeed(self):
        for result in ("skipped", "failure", "cancelled", "timed_out", "neutral"):
            with self.subTest(result=result):
                self.assertFalse(self.evaluate("4", result))

    def test_evaluation_jobs_may_skip_when_no_evaluation_files_changed(self):
        for step in ("1", "2", "3"):
            with self.subTest(step=step):
                self.assertTrue(self.evaluate(step, "skipped", evals_changed=False))

    def test_evaluation_jobs_must_not_skip_when_evaluation_files_changed(self):
        for step in ("1", "2", "3"):
            with self.subTest(step=step):
                self.assertFalse(self.evaluate(step, "skipped", evals_changed=True))

    def test_evaluation_jobs_accept_success(self):
        for step in ("1", "2", "3"):
            with self.subTest(step=step):
                self.assertTrue(self.evaluate(step, "success", evals_changed=True))

    def test_deployment_skip_is_expected_outside_main_push(self):
        self.assertTrue(self.evaluate("7", "skipped", is_main_push=False))

    def test_deployment_must_run_after_successful_main_push_tests(self):
        self.assertFalse(self.evaluate("7", "skipped", is_main_push=True, tests_result="success"))
        self.assertTrue(self.evaluate("7", "success", is_main_push=True, tests_result="success"))

    def test_deployment_skip_is_expected_when_tests_did_not_succeed(self):
        self.assertTrue(self.evaluate("7", "skipped", is_main_push=True, tests_result="failure"))
        self.assertFalse(self.evaluate("6", "skipped", is_main_push=True, tests_result="failure"))


if __name__ == "__main__":
    unittest.main()
