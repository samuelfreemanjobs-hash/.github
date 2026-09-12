# AI Proposals Agent™

> **Deploy target:** `https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude` → `ai-proposals-agent/project.md`

| Field | Value |
|-------|-------|
| **id** | `ai-proposals-agent` |
| **tagline** | Every number traces. |
| **owner** | Sam Freeman |
| **status** | scaffold |
| **completion %** | 52 |
| **heat** | hot |
| **launch rank** | 1 |
| **last verified** | 2026-09-12 |

## Location

- **Repo:** https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude
- **Path:** `ai-proposals-agent/`

## ICP & wedge

Logistics BD, sales, and solutions teams (Detroit corridor).

Logistics RFP proposals in ~75 minutes with auditable pricing and compliance.

## Architecture

- **Type:** single-agent

## Hard rules

- No generated numerics in binding fields.
- Compliance fail-closed.
- Schema violation is HALT.

## Evidence (why this %)

Golden test runner GREEN for component logic; frontend+ui present; KB required for full fixture runs.

## Blockers

Configured knowledge base for golden fixtures; production deploy; first pilot customer.

## Next ship (one slice)

Wire KB + run full golden fixtures; deploy `ai-proposals-agent/deploy` to staging; record 1 Loom demo for logistics ICP.

## Links

- Spec: `saas-factory/products/ai-proposals-agent.yaml`
- Verify: `cd ai-proposals-agent && python3 scripts/run_golden_tests.py`
