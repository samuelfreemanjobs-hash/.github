# Rule: `project.md` (portfolio governance)

> **Provenance:** Intended as your Claude “new rule.” No matching file was found in public GitHub code search on 2026-09-12. This rule is **aligned with** `saas-factory/schemas/product-spec.schema.json` and your monorepo README principles.

## When agents MUST read `project.md`

Before planning, coding, refactoring, or estimating on **any product**, the agent MUST:

1. Read that product’s `project.md` at the repo path in **Location**.
2. Treat **Hard rules** and **Status** as binding unless the human explicitly overrides in the current message.
3. Update `project.md` **Completion %** and **Last verified** when the agent finishes a meaningful slice of work.

## Required location

Each sellable product or product-ready project keeps **one** `project.md` at:

```
<repo-root>/<product-path>/project.md
```

Examples:

- `samuelfreemanjobs-hash/-build-ai-agents-with-claude/ai-proposals-agent/project.md`
- `samuelfreemanjobs-hash/VSTSampling/project.md`

Meta-systems (e.g. SaaS Factory) use the same pattern at their root: `saas-factory/project.md`.

## Required sections (in order)

1. **Identity** — `id`, `name`, `tagline`, `owner`
2. **Location** — GitHub repo URL + path inside repo
3. **Status** — `concept` | `design` | `scaffold` | `mvp` | `production` (matches factory enum)
4. **Completion %** — 0–100 with **evidence** (tests, deploy, paying users)
5. **ICP & wedge** — who pays and why now
6. **Architecture** — `single-agent` | `multi-agent` | `hybrid`
7. **Pipeline** — stages with `agent` | `deterministic` | `human` | `export`
8. **Hard rules** — fail-closed behaviors (no invented numerics, HALT on schema, etc.)
9. **Launch** — `heat` (cold/warm/hot), `launch_rank`, `blockers`, `next_ship`
10. **Links** — spec YAML, README, deploy guide, golden tests command

## Scoring `% complete` (standard rubric)

| Signal | Weight |
|--------|--------|
| Product spec validated (`saas-factory validate`) | 10% |
| Scaffold tree present | 10% |
| Deterministic modules + golden tests green | 25% |
| Skills + agent prompts complete | 15% |
| API/UI deployable | 20% |
| Production deploy + first external user | 20% |

Adjust with a one-line justification in `project.md` under **Evidence**.

## Portfolio registry

The master list lives in [`../REGISTRY.yaml`](../REGISTRY.yaml). Any new product MUST be added there before work begins.
