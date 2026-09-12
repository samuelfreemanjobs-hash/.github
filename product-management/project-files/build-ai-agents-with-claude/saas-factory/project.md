# SaaS Factory

> **Deploy target:** `https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude` → `saas-factory/project.md`

| Field | Value |
|-------|-------|
| **id** | `saas-factory` |
| **tagline** | Agent SaaS in a repeatable factory. |
| **owner** | Sam Freeman |
| **status** | mvp |
| **completion %** | 65 |
| **heat** | hot |
| **launch rank** | 2 |
| **last verified** | 2026-09-12 |

## Location

- **Repo:** https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude
- **Path:** `saas-factory/`

## ICP & wedge

Founders and platform engineers building Claude B2B agents.

YAML spec → validated scaffold → standard agent SaaS tree.

## Architecture

- **Type:** hybrid

## Hard rules

- Human approval on high-impact actions.
- Binding facts from deterministic code.
- Fail closed on schema violation.

## Evidence (why this %)

CLI (`saas-factory list/validate/scaffold`), JSON schema, templates, unit tests.

## Blockers

Public docs site; npm/pip publish optional.

## Next ship (one slice)

Record `saas-factory init` + `scaffold freeman-intel` demo; add GitHub Action validate on PR.

## Links

- Spec: `saas-factory/products/registry.yaml`
- Verify: `cd saas-factory && pip install -e '.[dev]' && saas-factory validate`
