# Claude Business OS — project instructions

You are working inside the canonical business workspace.

## Hub

- **HUB_PATH:** `{{ABSOLUTE_PATH_TO_HUB}}` (usually `./hub/`)
- Before **marketing, pricing, or product** workflows: read the hub files listed in `hub/MANIFEST.md` for that skill.
- **Never** store secrets in hub markdown (no API keys, EIN, bank numbers). Use placeholders.

## Workflows (skills)

Invoke when the user asks or uses slash commands:

| Skill | Use |
|-------|-----|
| `/business-hub-init` | First-time or major hub rebuild |
| `/business-hub-audit` | Monthly gap scan (4 Cs) |
| `/ad-pack-from-offer` | Paid campaign pack from one offer |
| `/pwa-idea-to-spec` | New app/PWA specification |
| `/pricing-positioning-memo` | Pricing or positioning decisions |

Follow each skill’s orchestration: Chief of Staff → section agents → **human gate** before spend, deploy, or live price changes.

## Agents

24 roles defined in `hub/agents/REGISTRY.md`. Use **3–7 agents per task**, not all 24.

## Deliverables

Write skill outputs only under:

- `deliverables/ad-packs/`
- `deliverables/pwa-specs/`
- `deliverables/pricing-memos/`
- `deliverables/hub-init/`
- `deliverables/hub-audits/`

## Governance

Respect `hub/07-operating-rules/approval-gates.md` and `hub/08-human-roles/human-roles.md`. AI drafts; human approves publish, ads spend, prod deploy, and final pricing.

## Optional (do not enable unless user asks)

- MCP servers beyond filesystem
- Vector RAG / memory MCP
- Mission control dashboard
- Automated git commit hooks

## Reference docs (in skill pack)

- MVP: `docs/MVP-REQUIRED.md`
- Full blueprint: `docs/HEAVY-OS-MASTER-PLAN.md`
