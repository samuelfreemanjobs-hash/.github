# What you actually need (MVP)

Skip optional layers until Phase A is boring.

## Required (start here)

| Piece | Purpose | Without it |
|-------|---------|------------|
| **`~/claude-business/hub/`** | Sections 1–8 truth | Every chat re-explains your business |
| **`~/.claude/skills/`** (5 skills) | Workflows with agent steps | Back to one-off prompts |
| **`~/claude-business/.claude/CLAUDE.md`** | HUB_PATH + rules | Skills won’t find hub |
| **`deliverables/`** folders | Filed outputs | Work lost in chat |
| **One `/business-hub-init` run** | Filled hub | Templates stay empty |
| **Monthly `/business-hub-audit`** | Stays accurate | Drift and wrong ads/pricing |

## Not required to start

| Piece | When to add |
|-------|-------------|
| **`settings.json` MCP block** | Phase B, when you build apps or read analytics in-tool |
| **Obsidian** | When you want mobile/notes UX on same files |
| **Session hooks** | When you forget to save decisions |
| **Vector RAG / Memory MCP / Redis** | When hub + deliverables are too big to search |
| **Mission control dashboard** | When juggling many projects hurts |
| **24 agents “running” at once** | Never — 3–7 per workflow only |

## Do you need the extra checklist / MCP example?

**No** for day one. One install prompt + hub init is enough. MCP example file is reference only when you connect GitHub.

## Minimum daily use

1. Claude Code opened in `~/claude-business` (or project with symlink to hub).
2. Run a skill (`/ad-pack-from-offer`, etc.) — it loads hub files.
3. Approve human gates; commit hub + deliverables to git when you use git.

That is the whole heavy OS **behavior**; the rest is acceleration.
