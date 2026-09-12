#!/usr/bin/env python3
"""
Validate Revenue Intel Agent JSON output (v5.1+).

Usage:
  python3 validate_run.py path/to/run.json
  python3 validate_run.py path/to/agent_output.txt   # extracts ===JSON_START=== block
  python3 validate_run.py --stdin

Exit 0 if valid; 1 if validation errors; 2 if parse failure.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

GROSS_PROFIT_TOLERANCE = 1.0
SCORE_TOLERANCE = 0.002
REQUIRED_GATES = ("Evidence", "Bias", "Math", "Feasibility", "Compliance", "Novelty")
CREDIBILITY_FLOORS = {"primary": 0.90, "secondary": 0.60, "vendor": 0.30}
CREDIBILITY_CEILINGS = {"primary": 1.00, "secondary": 0.85, "vendor": 0.60}


def extract_json_payload(text: str) -> dict[str, Any]:
    m = re.search(r"===JSON_START===\s*(\{.*?\})\s*===JSON_END===", text, re.DOTALL)
    raw = m.group(1) if m else text.strip()
    return json.loads(raw)


def revenue_potential_value(gross_profit: float) -> float:
    if gross_profit < 5000:
        return 0.2
    if gross_profit < 25000:
        return 0.5
    if gross_profit < 100000:
        return 0.8
    return 1.0


def compute_gross_profit(inputs: dict[str, Any]) -> float:
    units = float(inputs.get("units", 0))
    price = float(inputs.get("price_per_unit", 0))
    var = float(inputs.get("variable_cost_per_unit", 0))
    fixed = float(inputs.get("fixed_cost_90d", 0))
    return units * (price - var) - fixed


def compute_priority_score(
    opp: dict[str, Any], weights: dict[str, float]
) -> float:
    bd = opp.get("score_breakdown") or {}
    conf = float(opp.get("confidence", bd.get("confidence_value", 0)))
    urg = float(bd.get("urgency_value", 0))
    rev = float(bd.get("revenue_potential_value", 0))
    icp = float(bd.get("icp_fit_value", 0))
    ease = float(bd.get("ease_value", 0))
    total = (
        weights.get("confidence", 0.2) * conf
        + weights.get("urgency", 0.2) * urg
        + weights.get("revenue_potential", 0.2) * rev
        + weights.get("icp_fit", 0.2) * icp
        + weights.get("ease", 0.2) * ease
    )
    return round(total, 3)


def validate_source_ledger(ledger: list[dict[str, Any]], errors: list[str]) -> None:
    for i, src in enumerate(ledger):
        sid = src.get("id", f"index_{i}")
        st = src.get("source_type")
        score = src.get("credibility_score")
        if st not in CREDIBILITY_FLOORS:
            errors.append(f"source {sid}: invalid source_type {st!r}")
            continue
        if score is None:
            errors.append(f"source {sid}: missing credibility_score")
            continue
        lo, hi = CREDIBILITY_FLOORS[st], CREDIBILITY_CEILINGS[st]
        if not (lo <= float(score) <= hi + 1e-6):
            errors.append(
                f"source {sid}: credibility_score {score} outside [{lo}, {hi}] for {st}"
            )


def validate_opportunity(
    opp: dict[str, Any],
    ledger_ids: set[str],
    confidence_gate: float,
    weights: dict[str, float],
    errors: list[str],
) -> None:
    oid = opp.get("id", opp.get("headline", "?"))
    status = opp.get("status")
    gates = opp.get("gate_results") or {}

    # Math gate
    calc = opp.get("example_calc") or {}
    inputs = calc.get("inputs")
    if not inputs:
        errors.append(f"{oid}: example_calc.inputs missing")
    else:
        expected = compute_gross_profit(inputs)
        reported = float(calc.get("gross_profit", 0))
        if abs(expected - reported) > GROSS_PROFIT_TOLERANCE:
            errors.append(
                f"{oid}: gross_profit {reported} != recomputed {expected} (Math gate)"
            )
        rev_val = revenue_potential_value(reported)
        bd = opp.get("score_breakdown") or {}
        rpv = bd.get("revenue_potential_value")
        if rpv is not None and abs(float(rpv) - rev_val) > 1e-6:
            errors.append(
                f"{oid}: revenue_potential_value {rpv} should be {rev_val} from gross_profit band"
            )

    # Priority score
    if "priority_score" in opp:
        expected_ps = compute_priority_score(opp, weights)
        if abs(float(opp["priority_score"]) - expected_ps) > SCORE_TOLERANCE:
            errors.append(
                f"{oid}: priority_score {opp['priority_score']} != recomputed {expected_ps}"
            )

    # Gate results present
    for g in REQUIRED_GATES:
        if g not in gates:
            errors.append(f"{oid}: gate_results missing {g}")

    all_pass = all(gates.get(g) == "pass" for g in REQUIRED_GATES if g in gates)
    conf = float(opp.get("confidence", 0))

    if status == "Validated":
        if not all_pass:
            errors.append(f"{oid}: Validated but gate_results not all pass")
        if conf < confidence_gate:
            errors.append(
                f"{oid}: Validated but confidence {conf} < gate {confidence_gate}"
            )
        ev_ids = opp.get("evidence_source_ids") or []
        if len(ev_ids) < 3:
            errors.append(f"{oid}: Validated requires >=3 evidence_source_ids")
        for eid in ev_ids:
            if eid not in ledger_ids:
                errors.append(f"{oid}: evidence_source_id {eid} not in source_ledger")

    if status == "Hypothesis":
        vplan = opp.get("validation_plan") or []
        if conf < confidence_gate and len(vplan) < 3:
            errors.append(
                f"{oid}: Hypothesis below confidence_gate needs validation_plan (3 steps)"
            )


def validate_payload(
    data: dict[str, Any],
    confidence_gate: float | None = None,
    weights: dict[str, float] | None = None,
) -> list[str]:
    errors: list[str] = []
    meta = data.get("run_meta") or {}
    gate = confidence_gate if confidence_gate is not None else float(meta.get("confidence_gate", 0.65))
    w = weights or {
        "confidence": 0.2,
        "urgency": 0.2,
        "revenue_potential": 0.2,
        "icp_fit": 0.2,
        "ease": 0.2,
    }
    if meta.get("score_weights"):
        w = {**w, **meta["score_weights"]}

    ledger = data.get("source_ledger") or []
    validate_source_ledger(ledger, errors)
    ledger_ids = {s.get("id") for s in ledger if s.get("id")}

    for opp in data.get("opportunities") or []:
        validate_opportunity(opp, ledger_ids, gate, w, errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Revenue Intel JSON run")
    parser.add_argument("path", nargs="?", help="JSON file or raw agent output")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument(
        "--confidence-gate", type=float, default=None, help="Override confidence gate"
    )
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read()
    elif args.path:
        text = Path(args.path).read_text(encoding="utf-8")
    else:
        parser.error("provide path or --stdin")

    try:
        data = extract_json_payload(text)
    except json.JSONDecodeError as e:
        print(f"PARSE ERROR: {e}", file=sys.stderr)
        return 2

    errors = validate_payload(data, confidence_gate=args.confidence_gate)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
