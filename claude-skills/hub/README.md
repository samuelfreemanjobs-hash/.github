# Business hub (`hub/`)

Persistent context for all Claude workflows (ad pack, PWA spec, pricing memo, agents).

**How to use**

1. Copy this `hub/` folder to your machine (e.g. `~/claude-hub/hub/` or inside each business repo).
2. Run **`/business-hub-init`** once with Claude Code to interview you and fill templates.
3. Re-run **`/business-hub-audit`** monthly or after offer/stack changes.
4. Point skills at `hub/` (or set `HUB_PATH` in your user `CLAUDE.md`).

**Do not** commit secrets (API keys, bank numbers). Use placeholders and a secrets manager.
