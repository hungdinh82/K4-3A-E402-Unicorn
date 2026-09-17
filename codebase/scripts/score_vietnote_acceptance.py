#!/usr/bin/env python3
"""Score a VietNote 20-case run.

Input JSON: {"backend": "...", "results": [{"id":"VN01", "passed": true}, ...]}
The script rejects duplicate/unknown IDs so the denominator stays exactly 20.
"""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    parser.add_argument("--cases", type=Path, default=Path(__file__).parents[1] / "tests/vietnote_acceptance_cases.json")
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text())
    expected = {case["id"] for case in cases["cases"]}
    payload = json.loads(args.results.read_text())
    results = payload.get("results", [])
    ids = [item.get("id") for item in results]
    if set(ids) != expected or len(ids) != len(set(ids)):
        missing = sorted(expected - set(ids))
        unknown = sorted(set(ids) - expected)
        raise SystemExit(f"Need exactly 20 unique cases; missing={missing}, unknown={unknown}")
    passed = sum(bool(item.get("passed")) for item in results)
    rate = passed / len(expected) * 100
    severe = sum(bool(item.get("severe_error")) for item in results)
    if passed >= 16 and severe == 0:
        verdict = "PASS MVP"
    elif passed >= 12 and severe == 0:
        verdict = "NEEDS IMPROVEMENT"
    else:
        verdict = "FAIL"
    print(json.dumps({"backend": payload.get("backend", "unknown"), "passed": passed,
                      "total": len(expected), "rate_percent": rate,
                      "severe_errors": severe, "verdict": verdict}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
