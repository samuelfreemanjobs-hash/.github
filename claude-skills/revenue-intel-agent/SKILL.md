---
name: revenue-intel-agent
description: Run Revenue Intel Agent v5.0 — Metro Detroit compliance and cost-recovery opportunity research with HUNTER-ready briefs. Use when the user asks for revenue intel, compliance intel, cost recovery leads, or industrial opportunity research in southeast Michigan.
---

# Revenue Intel Agent v5.0

Invoke the **Revenue Intel Agent v5.0** system prompt and produce opportunity briefs aligned with HUNTER CRM.

## Before you start

Read these files from this repo (paths relative to `claude-skills/`):

| File | Purpose |
|------|---------|
| `deliverables/revenue-intel-agent-v5/REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` | Full system instructions |
| `deliverables/revenue-intel-agent-v5/OPPORTUNITY-BRIEF-SCHEMA.md` | Field definitions |
| `deliverables/revenue-intel-agent-v5/NICHE-POSITIONING.md` | ICP and exclusions |
| `hub/02-legal-finance-trust/claims-compliance.md` | Claims guardrails |

## Workflow

1. **Intake** — Company name or prospecting criteria; optional service catalog from user.
2. **Load system prompt** — Adopt the v5.0 role, rules, and output format from the system prompt file (entire body under `## ROLE` through `## START`).
3. **Research** — Use web search when available; cite source classes per prompt rules.
4. **Deliver** — Markdown summary + JSON `opportunities` array per schema.
5. **Human gate** — Present `seller_action` and verification questions; do not instruct automated outreach without user approval.

## HUNTER handoff (optional)

If the user uses HUNTER / Revenue Pipeline System, map each opportunity to:

- Company, Industry, Evidence fields
- Tier from `hunter_tier`
- Outreach strategy letter from `outreach_strategy`

Remind: pre-built intel rows belong in the **operator’s internal** base, not the customer template (`deliverables/revenue-pipeline-system/LAUNCH-CHECKLIST.md`).

## Quality bar

- Max 3 opportunities per run
- No fabricated fines or savings
- Every brief includes `compliance_note` and at least one `evidence` item
