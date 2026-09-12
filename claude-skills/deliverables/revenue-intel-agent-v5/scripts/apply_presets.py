#!/usr/bin/env python3
"""
Merge BRIEF-PROFILES.yaml and SECTOR-PROFILES.yaml into a runtime YAML file.

Usage:
  python3 apply_presets.py --brief client_facing --sector automotive_supplier
  python3 apply_presets.py --brief internal_lab --in RUNTIME-CONTEXT.example.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent


def load_yaml(path: Path) -> dict:
    if yaml is None:
        raise SystemExit("PyYAML required: pip install pyyaml")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", default="client_facing", help="brief profile key")
    parser.add_argument("--sector", default=None, help="sector profile key")
    parser.add_argument(
        "--in",
        dest="in_path",
        default=str(ROOT / "RUNTIME-CONTEXT.example.yaml"),
        help="Base runtime YAML",
    )
    args = parser.parse_args()

    base = load_yaml(Path(args.in_path))
    profiles = load_yaml(ROOT / "BRIEF-PROFILES.yaml")
    if args.brief not in profiles:
        raise SystemExit(f"Unknown brief profile: {args.brief}")

    brief = profiles[args.brief]
    base["brief_profile"] = args.brief
    for key in ("allow_hypothesis_in_brief", "confidence_gate", "score_weights"):
        if key in brief:
            base[key] = brief[key]

    if args.sector:
        sectors = load_yaml(ROOT / "SECTOR-PROFILES.yaml")
        if args.sector not in sectors:
            raise SystemExit(f"Unknown sector profile: {args.sector}")
        base["sector_profile"] = args.sector
        sec = sectors[args.sector]
        base["sector_compliance_focus"] = sec.get("compliance_focus", [])
        base["sector_evidence_query_seeds"] = sec.get("evidence_query_seeds", [])
        base["sector_regimes_default"] = sec.get("regimes_default", "")

    print(yaml.dump(base, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
