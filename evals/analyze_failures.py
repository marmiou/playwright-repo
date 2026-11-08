#!/usr/bin/env python3
"""Aggregate CI failure artifacts into a human-reviewed daily analysis report."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


BUCKETS = (
    "skill instructions unclear or missing",
    "eval case ambiguous or wrong expectation",
    "routing error (wrong skill chosen)",
    "flaky (failed in some runs, passed in others)",
    "environment/infra",
    "unknown",
)
MAX_GROUPS = 30
MAX_EVIDENCE_LINKS = 5
MAX_MESSAGE_LENGTH = 500


def _read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _run_url(run: dict[str, Any]) -> str:
    return str(run.get("url") or "")


def _skill_from_failure(failure: dict[str, Any]) -> str | None:
    file_name = str(failure.get("file") or "")
    match = re.search(r"evals/cases/([^/]+)\.json$", file_name)
    if match:
        return match.group(1)
    case_id = str(failure.get("case_id") or "")
    for suffix in ("-positive-", "-negative-", "-behavioral-"):
        if suffix in case_id:
            return case_id.split(suffix, 1)[0]
    return None


def _group_key(kind: str, failure: dict[str, Any]) -> str:
    if kind == "validator":
        identity = failure.get("case_id") or failure.get("file") or "dataset"
        return f"validator:{failure.get('rule', 'unknown')}:{identity}"
    return f"playwright:{failure.get('test_key', 'unknown-test')}"


def _classification(text: str, mixed_outcomes: bool) -> tuple[str, str]:
    value = text.lower()
    if mixed_outcomes:
        return BUCKETS[3], "Heuristic guess: the same failure key passed and failed on the same commit."
    if any(term in value for term in (
        "connection refused", "econnreset", "enotfound", "dns", "browser closed",
        "browser executable", "no space left", "out of memory", "worker process",
        "network error", "service unavailable", "timed out waiting for the browser",
        "unable to launch", "infrastructure", "runner",
    )):
        return BUCKETS[4], "Heuristic guess based on infrastructure or execution symptoms."
    if any(term in value for term in (
        "expected_primary_skill", "forbidden_skills", "allowed_companion_skills",
        "wrong skill", "routing", "route to", "skill selection",
    )):
        return BUCKETS[2], "Heuristic guess based on routing-related evidence."
    if any(term in value for term in (
        "skill.md", "skill instructions", "instruction is missing",
        "instructions are unclear", "description is missing", "skill description",
    )):
        return BUCKETS[0], "Heuristic guess based on skill-instruction references."
    if any(term in value for term in (
        "expectation", "expected result", "ambiguous", "wrong expectation",
        "assertion", "schema validation", "case composition", "fixture",
    )):
        return BUCKETS[1], "Heuristic guess based on evaluation-case or assertion evidence."
    return BUCKETS[5], "Heuristic guess; available evidence does not support a more specific bucket."


def _suggested_action(bucket: str) -> str:
    return {
        BUCKETS[0]: "Review the owning SKILL.md for missing decision rules, examples and explicit boundaries; propose a focused change for human review.",
        BUCKETS[1]: "Review the case prompt, fixture and expected evidence; clarify the oracle before changing the skill.",
        BUCKETS[2]: "Inspect the skill descriptions and competing routes; add a discriminating positive/negative regression case after human confirmation.",
        BUCKETS[3]: "Re-run the same commit and inspect traces, retries and shared state before changing expectations.",
        BUCKETS[4]: "Check runner health, browser installation, dependencies, network and external service availability.",
        BUCKETS[5]: "Inspect the linked run, test output and relevant source; gather more evidence before assigning ownership.",
    }[bucket]


def _record(
    groups: dict[str, dict[str, Any]],
    key: str,
    *,
    kind: str,
    run: dict[str, Any],
    failure: dict[str, Any],
    outcome: str,
) -> None:
    group = groups.setdefault(key, {
        "key": key,
        "kind": kind,
        "rule_or_test": failure.get("rule") or failure.get("test_key") or key,
        "skill": _skill_from_failure(failure),
        "message": str(failure.get("message") or failure.get("error") or "")[:MAX_MESSAGE_LENGTH],
        "observations": [],
        "runs": {},
        "evidence": [],
    })
    sha = str(run.get("headSha") or run.get("head_sha") or "unknown-sha")
    group["observations"].append({"sha": sha, "outcome": outcome})
    group["runs"][sha] = outcome
    url = _run_url(run)
    if url and url not in group["evidence"]:
        group["evidence"].append(url)


def _parse_validator(
    path: Path, run: dict[str, Any], groups: dict[str, dict[str, Any]]
) -> None:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        return
    failures = payload.get("failures", [])
    if not isinstance(failures, list):
        return
    if not failures and payload.get("status") == "passed":
        # A successful validator run is retained as evidence for same-commit comparisons.
        return
    for item in failures:
        if not isinstance(item, dict):
            continue
        _record(
            groups,
            _group_key("validator", item),
            kind="validator",
            run=run,
            failure=item,
            outcome="failed",
        )


def _playwright_tests(payload: Any) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []

    def visit(suites: list[Any], parents: list[str]) -> None:
        for suite in suites:
            if not isinstance(suite, dict):
                continue
            title = str(suite.get("title") or "")
            path = str(suite.get("file") or "")
            next_parents = parents + ([title] if title else [])
            for spec in suite.get("specs", []):
                if not isinstance(spec, dict):
                    continue
                spec_title = str(spec.get("title") or "")
                for test in spec.get("tests", []):
                    if not isinstance(test, dict):
                        continue
                    results = test.get("results", [])
                    states = [
                        str(result.get("status") or "")
                        for result in results
                        if isinstance(result, dict)
                    ]
                    if not states:
                        continue
                    final = states[-1]
                    outcome = "passed" if final == "passed" else (
                        "failed" if final in {"failed", "timedOut", "interrupted"} else "other"
                    )
                    retry_flake = "failed" in states[:-1] and final == "passed"
                    name = " › ".join(part for part in next_parents + [spec_title] if part)
                    test_key = f"{path or suite.get('file', '')}::{name or spec_title}"
                    error_messages = []
                    for result in results:
                        if isinstance(result, dict) and result.get("error"):
                            error = result["error"]
                            if isinstance(error, dict):
                                error_messages.append(str(error.get("message") or ""))
                            else:
                                error_messages.append(str(error))
                    found.append({
                        "test_key": test_key,
                        "message": " | ".join(error_messages)[:MAX_MESSAGE_LENGTH],
                        "outcome": "flaky" if retry_flake else outcome,
                    })
            visit(suite.get("suites", []), next_parents)

    if isinstance(payload, dict):
        visit(payload.get("suites", []), [])
    return found


def _parse_playwright(
    path: Path, run: dict[str, Any], groups: dict[str, dict[str, Any]]
) -> None:
    payload = _read_json(path)
    if payload is None:
        return
    for test in _playwright_tests(payload):
        if test["outcome"] == "other":
            continue
        failure = {
            "test_key": test["test_key"],
            "message": test["message"] or test["outcome"],
        }
        _record(
            groups,
            _group_key("playwright", failure),
            kind="playwright",
            run=run,
            failure=failure,
            outcome="failed" if test["outcome"] == "failed" else "passed",
        )


def _parse_future_behavioural(
    path: Path, run: dict[str, Any], groups: dict[str, dict[str, Any]]
) -> None:
    """Best-effort extension point for future behavioural evaluation result JSON."""
    payload = _read_json(path)
    if payload is None:
        return
    records = payload if isinstance(payload, list) else payload.get("results", [])
    if not isinstance(records, list):
        return
    for item in records:
        if not isinstance(item, dict):
            continue
        verdict = str(item.get("verdict") or item.get("status") or "").upper()
        if verdict not in {"FAIL", "FAILED"}:
            continue
        failure = {
            "case_id": item.get("case_id"),
            "file": item.get("file"),
            "rule": item.get("rule") or "behavioural_evaluation",
            "message": item.get("message") or item.get("rationale") or "Behavioural evaluation failed.",
        }
        _record(
            groups,
            _group_key("validator", failure),
            kind="behavioural",
            run=run,
            failure=failure,
            outcome="failed",
        )


def analyze(runs: list[dict[str, Any]], artifacts_dir: Path) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for run in runs:
        run_id = str(run.get("databaseId") or run.get("id") or "")
        if not run_id:
            continue
        root = artifacts_dir / run_id
        validator = root / "evals" / "results.json"
        playwright = root / "playwright" / "results.json"
        behavioural_files = list(root.glob("behavioural/**/*.json"))

        if validator.is_file():
            _parse_validator(validator, run, groups)
        if playwright.is_file():
            _parse_playwright(playwright, run, groups)
        for file in behavioural_files:
            _parse_future_behavioural(file, run, groups)

    results = []
    for group in groups.values():
        failed_runs = sum(outcome == "failed" for outcome in group["runs"].values())
        passed_runs = sum(outcome == "passed" for outcome in group["runs"].values())
        mixed = failed_runs > 0 and passed_runs > 0
        text_for_classification = " ".join(
            [group["key"], group["message"], str(group["skill"] or "")]
        )
        bucket, confidence = _classification(text_for_classification, mixed)
        group["bucket"] = bucket
        group["classification_note"] = confidence
        group["failed_run_count"] = failed_runs
        group["passed_run_count"] = passed_runs
        group["recurrence_count"] = failed_runs
        group["suggested_next_action"] = _suggested_action(bucket)
        group["evidence"] = group["evidence"][:MAX_EVIDENCE_LINKS]
        results.append(group)

    return sorted(
        results,
        key=lambda item: (-item["recurrence_count"], item["key"]),
    )[:MAX_GROUPS]


def render_report(groups: list[dict[str, Any]], days: int) -> str:
    if not groups:
        return (
            f"# Daily failure analysis\n\n"
            f"No CI failure artifacts were found in the last {days} day(s). "
            "No issue should be created or updated.\n"
        )

    counts = Counter(group["bucket"] for group in groups)
    lines = [
        "# Daily failure analysis",
        "",
        f"Window: last **{days} day(s)**. Groups are based on available CI artifacts.",
        "",
        "> Classification is deterministic and heuristic. It is not a confirmed root cause. "
        "Recurrence counts are evidence from the linked runs; suggested actions require human review.",
        "",
        "## Bucket counts",
        "",
        "| Bucket | Groups |",
        "|---|---:|",
    ]
    for bucket in BUCKETS:
        lines.append(f"| {bucket} | {counts.get(bucket, 0)} |")

    lines.extend(["", "## Top recurring failures", ""])
    for index, group in enumerate(groups[:MAX_GROUPS], start=1):
        lines.extend([
            f"### {index}. {group['key']}",
            "",
            f"- **Type:** {group['kind']}",
            f"- **Skill:** {group.get('skill') or 'Not identified'}",
            f"- **Failed runs:** {group['failed_run_count']}",
            f"- **Passed runs for same commit:** {group['passed_run_count']}",
            f"- **Classification:** {group['bucket']}",
            f"- **Confidence:** {group['classification_note']}",
            f"- **Evidence:** {group['message'] or 'No error message captured.'}",
            f"- **Suggested next action:** {group['suggested_next_action']}",
        ])
        if group["evidence"]:
            lines.append("- **Run links:** " + ", ".join(group["evidence"]))
        else:
            lines.append("- **Run links:** No run URL was available.")
        lines.append("")

    report = "\n".join(lines)
    return report[:60_000] + ("\n\n_Report truncated to 60,000 characters._\n" if len(report) > 60_000 else "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-file", type=Path, required=True)
    parser.add_argument("--artifacts-dir", type=Path, required=True)
    parser.add_argument("--days", type=int, default=1)
    parser.add_argument("--output", type=Path, default=Path("failure-analysis.md"))
    args = parser.parse_args()

    runs = _read_json(args.runs_file)
    if not isinstance(runs, list):
        raise SystemExit("Runs input must be a JSON array.")
    groups = analyze(runs, args.artifacts_dir)
    report = render_report(groups, max(1, args.days))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    summary = Path(__import__("os").environ.get("GITHUB_STEP_SUMMARY", ""))
    if str(summary) not in {"", "."}:
        with summary.open("a", encoding="utf-8") as stream:
            stream.write(report)
    print(f"Analyzed {len(runs)} CI run(s); found {len(groups)} failure group(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
