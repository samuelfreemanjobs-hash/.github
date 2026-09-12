---
name: revenue-intel-agent
description: Run Revenue Intel Agent — v5.1 weekly monetization briefs with gated evidence, ROI modeling, and optional JSON/CSV. Use when the user asks for revenue intel, market opportunities, weekly revenue brief, or monetization analysis for a niche and ICP.
---

# Revenue Intel Agent — v5.1

Invoke the official **Revenue Intel Agent — v5.0** system prompt with a filled **runtime context** every run.

## Before you start

| File | Purpose |
|------|---------|
| `deliverables/revenue-intel-agent-v5/REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` | Full system prompt (paste into system role) |
| `deliverables/revenue-intel-agent-v5/RUNTIME-CONTEXT.example.yaml` | Template for `<runtime_context>` |
| `deliverables/revenue-intel-agent-v5/OPPORTUNITY-BRIEF-SCHEMA.md` | v5 JSON + optional HUNTER mapping |
| `hub/02-legal-finance-trust/claims-compliance.md` | Claims guardrails |

## Workflow

1. **Stop if missing context** — Require `today`, `niche`, and `icp`. Do not guess dates or market.
2. **Inject `<runtime_context>`** — Copy from `RUNTIME-CONTEXT.example.yaml` (or orchestrator supply). Set `output_modes` (default `ExecutiveBriefMD` only).
3. **Adopt system prompt** — Use the full v5.0 prompt from the `.md` file (all sections `<role>` through changelog).
4. **User message** — Use the run template at the bottom of the system prompt file (`Niche/Market`, `ICP`).
5. **Research** — Web search + fetch per `<research_protocol>`; respect `search_budget`.
6. **Deliver** — Only the requested `output_modes`, in contract order. Never pad opportunity count.
7. **Human gate** — Hypothesis items need `validation_plan`; no outreach automation without user approval.

## HUNTER handoff (optional)

When `hunter_handoff: true` in runtime context, map validated opportunities per `OPPORTUNITY-BRIEF-SCHEMA.md`. Internal operator base only — not the customer HUNTER template.

## Quality bar

- Zero opportunities with populated `rejected` is a valid successful run
- No fabricated hashes, undated sources, or memory-as-current-fact
- Mandatory "What I rejected and why" in ExecutiveBriefMD
