# Software Architect Agent™

> **Deploy target:** `https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude` → `software-architect/project.md`

| Field | Value |
|-------|-------|
| **id** | `software-architect` |
| **tagline** | Every boundary traces. |
| **owner** | Sam Freeman |
| **status** | scaffold |
| **completion %** | 42 |
| **heat** | warm |
| **launch rank** | 6 |
| **last verified** | 2026-09-12 |

## Location

- **Repo:** https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude
- **Path:** `software-architect/`

## ICP & wedge

Architects modeling C4 and boundaries.

C4 modeling and governance agent.

## Architecture

- **Type:** single-agent

## Hard rules

- Human approval on high-impact actions.
- Binding facts from deterministic code.
- Fail closed on schema violation.

## Evidence (why this %)

Golden tests pass.

## Blockers

UI integration.

## Next ship (one slice)

Generate C4 for ai-proposals-agent as dogfood artifact.

## Links

- Spec: `saas-factory/products/software-architect.yaml`
- Verify: `cd software-architect && python3 scripts/run_golden_tests.py`
