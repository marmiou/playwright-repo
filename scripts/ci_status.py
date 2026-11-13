"""Shared policy for interpreting conditional GitHub Actions job results."""


def status_is_acceptable(
    step_number: str,
    result: str,
    *,
    evals_changed: bool,
    is_main_push: bool,
    tests_result: str,
) -> bool:
    """Return whether a job result is successful or an explicitly expected skip."""
    if step_number in {"1", "2", "3"}:
        return result == "success" or (result == "skipped" and not evals_changed)

    if step_number == "7":
        deployment_is_expected = is_main_push and tests_result == "success"
        return result == "success" or (result == "skipped" and not deployment_is_expected)

    return result == "success"
