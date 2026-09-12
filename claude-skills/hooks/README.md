# Session hooks — setup

Claude Code hooks live in `.claude/settings.json` (see official docs for your version).

## Recommended hooks

### session-start

- Verify `HUB_PATH` exists
- Warn if any `hub/01-identity-strategy/*.md` older than 30 days (parse `Last updated`)

### session-end

- Append to `memory/session-logs/YYYY-MM-DD.md`:
  - Timestamp
  - User goal (one line if known)
  - Files changed
  - Decisions to promote to hub (bullet list, unchecked)

## Allowlist (optional)

Restrict tool writes to:

- `hub/`
- `deliverables/`
- `projects/`
- `memory/session-logs/`

## Post-deliverable git (optional)

After skill writes deliverable:

```bash
git add deliverables/ && git commit -m "deliverable: ${TYPE} ${SLUG}"
```

Run manually or via hook when you trust automation.

## Files

Add executable scripts under `hooks/` in your business repo and reference paths in settings.
