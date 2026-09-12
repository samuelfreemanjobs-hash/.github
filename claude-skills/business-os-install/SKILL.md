---
name: business-os-install
description: One-time install of Claude Business OS from the claude-skills pack — creates ~/claude-business layout, copies hub and skills, writes CLAUDE.md, creates deliverables folders. Does not configure MCP, RAG, or dashboard unless user opts in. Use when setting up the heavy OS for the first time.
---

# Business OS install

## Preconditions

- User has the **`claude-skills`** folder (from repo clone or copy).
- Claude Code can write to `~/.claude/skills/` and user-chosen business root (default `~/claude-business`).

## Install steps (execute in order)

1. **Confirm paths** with user:
   - `BUSINESS_ROOT` (default `~/claude-business`)
   - `SKILL_PACK` path to `claude-skills/`
2. **Create directories:**
   - `$BUSINESS_ROOT/hub/` — copy entire `SKILL_PACK/hub/` tree
   - `$BUSINESS_ROOT/deliverables/{ad-packs,pwa-specs,pricing-memos,hub-init,hub-audits}`
   - `$BUSINESS_ROOT/memory/session-logs`
   - `$BUSINESS_ROOT/projects` (empty)
   - Optional: `$BUSINESS_ROOT/cadence` copy `rituals.md`; `$BUSINESS_ROOT/docs` symlink or copy HEAVY-OS + MVP docs
3. **Install skills** — copy each folder to `~/.claude/skills/`:
   - ad-pack-from-offer, business-hub-init, business-hub-audit, pwa-idea-to-spec, pricing-positioning-memo, business-os-install
4. **Write** `$BUSINESS_ROOT/.claude/CLAUDE.md` from `templates/claude-business-CLAUDE.md` with absolute HUB_PATH.
5. **Initialize git** in `$BUSINESS_ROOT` if user wants (`.gitignore`: secrets, `.env*).
6. **Do NOT** by default: edit `settings.json` MCP, install Redis/RAG, build dashboard.
7. **Verify:** list hub sections 01–08, list 6 skills, show CLAUDE.md head.
8. **Offer** immediate **`/business-hub-init`** (greenfield) in `$BUSINESS_ROOT`.

## Report

Print install summary markdown: paths, next commands, pointer to `docs/MVP-REQUIRED.md`.
