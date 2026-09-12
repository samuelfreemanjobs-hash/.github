# Rule: `project.md` (session + file standard)

**Session prompts:** [`PROJECT_MD_SESSION_PROMPTS.md`](PROJECT_MD_SESSION_PROMPTS.md) (VARIANT 1 / 2 / 3).

**File template:** [`../templates/project.md`](../templates/project.md) (official layout).

## Purpose

`project.md` is the **single source of truth per product**: scope, outcome, value, done/to-do, stack, artifacts, agents, and notes. Created with **PROJECT NEW**; maintained with **PROJECT UPDATE** or **PROJECT STATUS**.

## When agents MUST use it

1. **Start of session** — Follow the matching variant when the user pastes `project.md` or says PROJECT NEW / UPDATE / STATUS.
2. **Before coding** — Read `project.md` at the product root (see location below).
3. **After work** — **PROJECT UPDATE**: move items ✅ Done ↔ ☐ To Do; recalculate **Progress** in the header.

## Progress %

```
Progress = round(100 × |✅ Done| / (|✅ Done| + |☐ To Do|))
```

Count only checkbox lines under **✅ Done** and **☐ To Do**. Put unknowns in **Notes** as `[TBD]` (VARIANT 1).

## Where the file lives

| Layout | Path |
|--------|------|
| Single-product repo | `<repo-root>/project.md` |
| Monorepo SKU | `<repo-root>/<product-folder>/project.md` |
| `push` Etsy kits | `ai-agent-team/products/<kit-name>/project.md` |
| Branch-only MVP | Product folder on that branch (e.g. `autoborder/project.md`) |

Commit `project.md` with the code it describes. Footer: `*[Brand] · project.md — updated YYYY-MM-DD*`.

## Template sections (required)

| Section | Purpose |
|---------|---------|
| Header | Date, **Urgency**, **Progress** % |
| Scope | 3–5 sentences |
| Proposed Outcome + **For:** | Success definition & audience |
| Opportunity Value | Revenue / strategic / time value |
| ✅ Done / ☐ To Do | Only source for Progress % |
| Stack | Tools & platforms |
| Artifacts | Table: name, path, status |
| AI Agents Created | Agents in this SKU or "None" |
| Alternative Uses / Re-Niching | Pivots |
| API Keys Needed | Names only — never secrets |
| Notes | Blockers, decisions, `[TBD]` gaps |

## Factory / B2B agents

Keep `saas-factory/products/*.yaml` as technical canon. `project.md` is the **launch & execution** view; do not contradict spec `hard_rules`.

## Portfolio registry

[`../REGISTRY.yaml`](../REGISTRY.yaml) — add new products after PROJECT NEW; optional cross-ref in **Notes**.

## Registry vs day-to-day

`REGISTRY.yaml` / `PRODUCT_MATRIX.md` may use audit rubrics weekly; **header Progress in `project.md` wins** during build sessions until you sync the registry.
