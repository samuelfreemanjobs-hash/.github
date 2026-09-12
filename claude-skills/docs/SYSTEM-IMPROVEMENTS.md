# System improvements (changelog)

## Problems we fixed

| Before | After |
|--------|--------|
| Unclear if MCP/dashboard/RAG required | **`docs/MVP-REQUIRED.md`** — explicit skip list |
| Many docs, no entry point | **`START-HERE.md`** + install prompt |
| Manual copy steps | **`/business-os-install`** skill + **`INSTALL-PROMPT.md`** |
| Skills didn’t declare hub deps | **`hub/MANIFEST.md`** cross-reference |
| Thin CLAUDE snippet | **`templates/claude-business-CLAUDE.md`** full project rules |
| MCP fear of missing out | **`settings.json.example`** commented optional only |

## How to make the system better over time (habits)

1. **One hub location** — symlink projects to `~/claude-business/hub`, don’t fork.
2. **Git commit** on hub + deliverable changes with message `hub:` or `deliverable:`.
3. **Monthly audit skill** — never skip after offer/pricing changes.
4. **One workflow at a time** — master ad pack before adding MCP write tools.
5. **Promote session decisions** — weekly: 3 bullets from `memory/session-logs/` into hub (Phase B+).
6. **Winners/losers log** — after campaigns, update `05/marketing-growth-stack.md`.
7. **Trim hub** — if a section stays empty, delete placeholders or mark N/A (audit scores improve).

## Future pack upgrades (not built yet)

- `/email-launch-sequence`, `/social-week-batch` skills
- Hook scripts (executable) in `hooks/`
- Obsidian Dataview dashboard template
- CI check that hub `Last updated` is set

Contributions: edit hub templates and skills in repo; re-run install skill only for new skill folders.
