# Mission control dashboard — specification (Phase D)

Optional UI for the heavy Claude Business OS. **Do not build until Phase B skills run reliably without it.**

## Goals

- See hub freshness and audit score at a glance
- List in-flight deliverables under `deliverables/`
- Open hub files and last session log
- Trigger no write actions without human click (read-only v1)

## Non-goals v1

- Replacing Claude Code chat
- Auto-running ad spend or deploy
- Storing API keys

## Views

### 1. Mission control (home)

| Widget | Data source |
|--------|-------------|
| Hub health | Parse `Last updated` in `hub/**/*.md` |
| Last audit score | Latest `deliverables/hub-audits/*.md` |
| Open gaps | Parse tier-1 from last audit |
| Active projects | `projects/*/`.claude or config |

### 2. Workflows

| Column | Source |
|--------|--------|
| Ad packs | `deliverables/ad-packs/` mtime |
| PWA specs | `deliverables/pwa-specs/` |
| Pricing memos | `deliverables/pricing-memos/` |

### 3. Agent registry (read-only)

Render `hub/agents/REGISTRY.md` as table.

### 4. Kanban (v2)

Columns: Spec → Build → Review → Ship  
Cards: manual or synced from Linear/ClickUp MCP.

## Tech options

| Stack | Notes |
|-------|--------|
| **Static + markdown** | Vite SPA; build script scans hub |
| **Local FastAPI** | Same pattern as open-source claude-os UI |
| **Obsidian** | Already a “dashboard” if you use Dataview |

## Build prompt (when ready)

```text
Build a local read-only dashboard that:
- Reads HUB_PATH and deliverables/ from env
- Shows hub file staleness (>30 days yellow)
- Lists latest audit score from hub-audits
- Links to open files in OS
No auth, no network, no API keys in browser
```

## Logging (optional)

Append `dashboard/activity.jsonl` when skills complete (via hook) for timeline view.
