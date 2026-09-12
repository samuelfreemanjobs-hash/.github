# Freeman Product Management System (PMS)

Knowledge-bank–ready system for inventorying, scoring, and launching products across `samuelfreemanjobs-hash` on GitHub.

## What this folder is

| Artifact | Purpose |
|----------|---------|
| [`REGISTRY.yaml`](REGISTRY.yaml) | Machine-readable source of truth (products, repos, paths, scores) |
| [`PRODUCT_MATRIX.md`](PRODUCT_MATRIX.md) | Human CRO/PM view: % complete, heat, launch rank |
| [`REPO_CATALOG.md`](REPO_CATALOG.md) | All ~140 repos classified (original vs fork vs reference) |
| [`rules/PROJECT_MD_SESSION_PROMPTS.md`](rules/PROJECT_MD_SESSION_PROMPTS.md) | PROJECT NEW / UPDATE / STATUS session prompts |
| [`rules/PROJECT_MD_RULE.md`](rules/PROJECT_MD_RULE.md) | Agent rules + where `project.md` lives |
| [`templates/project.md`](templates/project.md) | Standard template (task-based % complete) |
| [`prompts/ELITE_PORTFOLIO_CRO_AGENT.md`](prompts/ELITE_PORTFOLIO_CRO_AGENT.md) | Reusable elite agent prompt for future audits |
| [`project-files/`](project-files/) | Pre-filled `project.md` per product (deploy into target repos) |

## How to install in your knowledge bank

1. **Index** — Add this entire `product-management/` tree to your KB (Obsidian vault, Notion, Claude Project files, or Cursor rules path).
2. **Pin** — Link `REGISTRY.yaml` and `PRODUCT_MATRIX.md` on your dashboard note.
3. **Sync rule** — Pin [`rules/PROJECT_MD_SESSION_PROMPTS.md`](rules/PROJECT_MD_SESSION_PROMPTS.md) in Claude Project instructions; add [`rules/PROJECT_MD_RULE.md`](rules/PROJECT_MD_RULE.md) for agents.
4. **Deploy `project.md`** — For each row in `project-files/`, copy the file to the **Target path** listed in the file header (or run the sync script below when you add repos locally).

### Optional: sync `project.md` into a cloned monorepo

```bash
# From a machine with both repos cloned
SRC="$HOME/kb/product-management/project-files"
DEST="$HOME/src/-build-ai-agents-with-claude"
cp "$SRC/build-ai-agents-with-claude/ai-proposals-agent/project.md" \
   "$DEST/ai-proposals-agent/project.md"
# Repeat per product — see project-files/README.md
```

## Operating rhythm (weekly)

1. **Monday** — Agent reads `REGISTRY.yaml`, updates `% complete` from CI/tests/deploy status.
2. **Wednesday** — CRO review: adjust `launch_rank` and `heat` in matrix.
3. **Friday** — Ship one “launch slice” on rank #1 product only.

## Audit notes (2026-09-12, revised)

- **GitHub “original” repos:** 4 roots — `push`, `openclaw-framework`, `-build-ai-agents-with-claude`, `VSTSampling`.
- **Actual portfolio size:** **Much larger** — products on **`push` branches** (29 Etsy/agent-kit folders on one branch alone) and **29 monorepo feature branches** (Autoborder, Hunter OS, Freeman Intelligence, prompt library platform, etc.). Read **[`PORTFOLIO_DEEP_MAP.md`](PORTFOLIO_DEEP_MAP.md)**.
- **Primary B2B suite on `main`:** `-build-ai-agents-with-claude` (SaaS Factory + engineering agents; `freeman-intel` spec on `main`, folder on some branches only).
- **`project.md`:** Session prompts captured in [`rules/PROJECT_MD_SESSION_PROMPTS.md`](rules/PROJECT_MD_SESSION_PROMPTS.md); file shape in [`templates/project.md`](templates/project.md).
