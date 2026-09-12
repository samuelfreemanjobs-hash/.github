# Freeman Intel

> **Deploy target:** `https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude` → `freeman-intel/project.md`

| Field | Value |
|-------|-------|
| **id** | `freeman-intel` |
| **tagline** | Plant inbound readiness before the truck arrives. |
| **owner** | Sam Freeman |
| **status** | design |
| **completion %** | 18 |
| **heat** | hot |
| **launch rank** | 3 |
| **last verified** | 2026-09-12 |

## Location

- **Repo:** https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude
- **Path:** `freeman-intel/`

## ICP & wedge

Manufacturing plant inbound logistics (Metro Detroit auto/industrial).

Email-first ASN validation and dock readiness — no TMS API for v1.

## Architecture

- **Type:** multi-agent

## Hard rules

- Human approval before gate/OTIF/chargeback actions.
- Email-first intake.
- Every record traces to source email.

## Evidence (why this %)

Full YAML spec in factory; README references folder but tree not scaffolded in repo.

## Blockers

Run `saas-factory scaffold freeman-intel`; build deterministic modules; approval UI.

## Next ship (one slice)

Scaffold tree to `freeman-intel/`; implement routing-guide-rules deterministic stub; human approval queue mock.

## Links

- Spec: `saas-factory/products/freeman-intel.yaml`
- Verify: `saas-factory show freeman-intel`
