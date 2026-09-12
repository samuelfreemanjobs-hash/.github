# Install prompt — paste into Claude Code

Copy everything inside the fenced block below into a **new Claude Code** session. Adjust `SKILL_PACK` if your folder lives somewhere else.

---

## Prompt (copy from here)

```markdown
You are installing my **Claude Business OS** from a local skill pack. Execute on my machine; do not just describe steps—run them and show what you created.

## Goal

A working MVP:

- Business workspace with hub (sections 1–8), deliverables folders, optional git
- Six skills in `~/.claude/skills/`
- Project `CLAUDE.md` with HUB_PATH and workflow rules
- **No** MCP setup, **no** RAG/Redis, **no** dashboard unless I opt in at the end

## Inputs (ask me if missing)

1. **SKILL_PACK** — absolute path to the `claude-skills` folder (contains `hub/`, `ad-pack-from-offer/`, etc.)
2. **BUSINESS_ROOT** — where the business workspace lives (default: `~/claude-business`)
3. **Use git?** — yes/no for initializing a repo at BUSINESS_ROOT

## Install procedure

Follow the skill logic in `business-os-install` if present; otherwise:

1. Create `BUSINESS_ROOT` and copy `SKILL_PACK/hub/` → `BUSINESS_ROOT/hub/`
2. Create deliverables subfolders: `ad-packs`, `pwa-specs`, `pricing-memos`, `hub-init`, `hub-audits`
3. Create `BUSINESS_ROOT/memory/session-logs/` and `BUSINESS_ROOT/projects/`
4. Copy `SKILL_PACK/cadence/rituals.md` → `BUSINESS_ROOT/cadence/rituals.md` (create cadence dir)
5. Copy `SKILL_PACK/docs/MVP-REQUIRED.md` and `START-HERE.md` → `BUSINESS_ROOT/docs/` (or tell me to read from SKILL_PACK)
6. Install skills to `~/.claude/skills/` by copying these folders from SKILL_PACK:
   - ad-pack-from-offer
   - business-hub-init
   - business-hub-audit
   - pwa-idea-to-spec
   - pricing-positioning-memo
   - business-os-install
7. Write `BUSINESS_ROOT/.claude/CLAUDE.md` using `SKILL_PACK/templates/claude-business-CLAUDE.md` — set HUB_PATH to `BUSINESS_ROOT/hub/` (absolute path)
8. If git yes: `git init`, add `.gitignore` for `.env`, `*.pem`, `secrets/`, commit "chore: init Claude Business OS layout"
9. Print a verification table: hub sections present, skill folders in ~/.claude/skills, CLAUDE.md exists

## After install

1. Tell me to open Claude Code with cwd = BUSINESS_ROOT
2. Start **`/business-hub-init`** in **greenfield** mode — interview me until hub sections 1–8 are filled (use placeholders for legal/tax; mark DRAFT)
3. Then run **`/business-hub-audit`** and list top 3 tier-1 fixes only

## Optional (ask me separately — default skip)

- Add MCP from `templates/settings.json.example`
- Obsidian vault = same hub folder
- Session hooks from `hooks/README.md`

## Constraints

- Never write API keys, passwords, EIN, or bank numbers into hub files
- Do not publish ads, deploy prod, or change live prices — hub setup only

When finished, give me a 5-line "how I use this daily" cheat sheet.
```

---

## Short version (if you already copied files)

```markdown
Install Claude Business OS MVP. SKILL_PACK=[path]. BUSINESS_ROOT=~/claude-business. Copy hub + 6 skills, write .claude/CLAUDE.md, create deliverables folders. No MCP. Then run /business-hub-init greenfield and /business-hub-audit. Execute, don't only instruct.
```

---

## Claude.ai (no Code / no filesystem)

Claude.ai cannot run this install. Use **Claude Code** on your computer, or clone the repo locally first:

`https://github.com/samuelfreemanjobs-hash/.github` (branch with `claude-skills/`)

Then point **SKILL_PACK** at the cloned `claude-skills` path in the prompt above.
