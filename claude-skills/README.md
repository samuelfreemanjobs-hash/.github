# Claude business OS — skills & hub

Copy this folder into your machine:

```text
~/.claude/skills/          ← each skill subfolder (SKILL.md inside)
~/claude-hub/hub/          ← or ./hub/ in a business repo (templates)
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| `ad-pack-from-offer/` | `/ad-pack-from-offer` | Multi-agent ad pack from one offer |
| `business-hub-init/` | `/business-hub-init` | Fill hub sections 1–8 via interview |
| `business-hub-audit/` | `/business-hub-audit` | 4 Cs score + backlog |

## Hub layout

| Section | Folder |
|---------|--------|
| 1 Identity & strategy | `hub/01-identity-strategy/` |
| 2 Legal, finance, trust | `hub/02-legal-finance-trust/` |
| 3 Product & delivery | `hub/03-product-delivery/` |
| 4 Technical platform | `hub/04-technical-platform/` |
| 5 Marketing & growth | `hub/05-marketing-growth/` |
| 6 Connections | `hub/06-connections/` |
| 7 Operating rules | `hub/07-operating-rules/` |
| 8 Human roles | `hub/08-human-roles/` |
| Agents | `hub/agents/REGISTRY.md` |

## Recommended order

1. Copy `hub/` → your `HUB_PATH`
2. Add `CLAUDE-snippet.md` to your user `CLAUDE.md`
3. Run **`/business-hub-init`** (greenfield)
4. Run **`/business-hub-audit`**
5. Run **`/ad-pack-from-offer`** on a real offer

## Deliverables (created by skills)

- `deliverables/ad-packs/`
- `deliverables/hub-init/`
- `deliverables/hub-audits/`
