#!/usr/bin/env python3
"""Apply PM ARTIFACT ADD rows from PM-AIRTABLE-ARTIFACT-QUEUE.json to Freeman PM Airtable.

Requires: AIRTABLE_PAT (personal access token with data.records:write on base appUuhVQHAOv31wJ1)

Usage:
  export AIRTABLE_PAT=pat...
  python3 claude-skills/hub/agents/scripts/airtable_pm_artifact_add.py
  python3 claude-skills/hub/agents/scripts/airtable_pm_artifact_add.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

QUEUE = Path(__file__).resolve().parents[1] / "PM-AIRTABLE-ARTIFACT-QUEUE.json"
API = "https://api.airtable.com/v0"


def request(method: str, url: str, token: str, body: dict | None = None) -> dict:
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def find_project_id(token: str, base_id: str, projects_table: str, name: str) -> str:
    url = f"{API}/{base_id}/{projects_table}?maxRecords=100"
    out = request("GET", url, token)
    for rec in out.get("records") or []:
        fields = rec.get("fields") or {}
        for key, val in fields.items():
            if isinstance(val, str) and val.strip() == name:
                return rec["id"]
    raise SystemExit(f"Project not found: {name!r} (scanned Projects table primary fields)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--queue", type=Path, default=QUEUE)
    args = parser.parse_args()

    token = os.environ.get("AIRTABLE_PAT", "").strip()
    if not token and not args.dry_run:
        print("Set AIRTABLE_PAT to sync.", file=sys.stderr)
        return 1

    queue = json.loads(args.queue.read_text(encoding="utf-8"))
    base_id = queue["base_id"]
    artifacts_table = queue["artifacts_table_id"]
    projects_table = queue["projects_table_id"]
    project_name = queue["project_link_name"]

    if args.dry_run:
        print(json.dumps(queue, indent=2))
        return 0

    project_id = find_project_id(token, base_id, projects_table, project_name)
    created: list[str] = []

    for row in queue["rows"]:
        fields = dict(row["fields"])
        fields["Project"] = [project_id]
        url = f"{API}/{base_id}/{artifacts_table}"
        out = request("POST", url, token, {"fields": fields})
        created.append(out["id"])
        print(f"Created {row['artifact_name']}: {out['id']}")

    queue["sync_status"] = "synced"
    queue["airtable_record_ids"] = created
    args.queue.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
