# Rule: `project.md` (session + file standard)

**Authoritative session prompts:** [`PROJECT_MD_SESSION_PROMPTS.md`](PROJECT_MD_SESSION_PROMPTS.md) (VARIANT 1 / 2 / 3).

**File template:** [`../templates/project.md`](../templates/project.md).

## Purpose

`project.md` is the **single source of truth per product** for humans and agents: scope, tasks, % complete, decisions, and blockers. It is created with **PROJECT NEW** and maintained with **PROJECT UPDATE** or **PROJECT STATUS**.

## When agents MUST use it

1. **Start of session** — If the user pastes `project.md` or says PROJECT NEW/UPDATE/STATUS, follow the matching variant in `PROJECT_MD_SESSION_PROMPTS.md`.
2. **Before coding** — Read `project.md` at the product root (see location below).
3. **End of meaningful work** — User should run **PROJECT UPDATE** (or agent proposes update) with a bullet list of what changed; recalculate **% from tasks** (`done / total × 100`).

## Where the file lives

| Layout | Path |
|--------|------|
| Single-product repo | `<repo-root>/project.md` |
| Monorepo SKU | `<repo-root>/<product-folder>/project.md` |
| `push` branch kits | `ai-agent-team/products/<kit-name>/project.md` |
| Branch-only MVP | On that branch, at the product’s top-level folder (e.g. `autoborder/project.md`) |

Commit `project.md` **with the code** it describes.

## Standard template sections

1. **Overview** — one paragraph (from PROJECT NEW description)
2. **Audience & success** — ICP, metric, urgency
3. **Stack & constraints**
4. **Tasks** — checkbox list; **% complete derived only from this list** unless user overrides
5. **Decisions** — dated log
6. **Blockers & open questions**
7. **Portfolio cross-ref** (optional) — link to `REGISTRY.yaml` id for CRO/matrix
8. **Gaps [TBD]** — from PROJECT NEW when info is missing

## Factory / B2B agent products (extra context)

For SKUs in `-build-ai-agents-with-claude`, also keep the **YAML spec** in `saas-factory/products/*.yaml` as technical canon (pipeline, hard_rules). `project.md` is the **execution and launch** view; the spec is the **product definition**. Do not contradict `hard_rules` in the spec.

## Portfolio registry

Master list: [`../REGISTRY.yaml`](../REGISTRY.yaml). Add a row when PROJECT NEW creates a new product; set **Portfolio cross-ref** in `project.md`.

## Relation to earlier audit rubric

Portfolio audits may still use **evidence-based** estimates (tests, deploy) in `REGISTRY.yaml` / `PRODUCT_MATRIX.md`. When both exist, **tasks in `project.md` win for day-to-day %**; sync registry on weekly CRO review.
