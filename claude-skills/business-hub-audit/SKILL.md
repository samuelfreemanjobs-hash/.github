---
name: business-hub-audit
description: Audit the business hub against Context, Connections, Capabilities, and Cadence (4 Cs). Scores gaps, ranks fixes by leverage, and outputs a prioritized backlog. Use monthly, after offer changes, or before scaling agent workflows.
---

# Business hub audit (4 Cs)

Grade **`hub/`** completeness for Claude OS workflows. Read-only on live systems unless user asks to fix files.

## Inputs

- **Hub path:** default `./hub/`
- Optional focus: ad pack | pwa spec | pricing memo | all

## Output

`deliverables/hub-audits/YYYY-MM-DD_hub-audit.md`

---

## Step 0 — Chief of Staff

**Agent prompt:**

```text
You are Chief of Staff running a hub audit.

Scan {{HUB_PATH}} for all section folders 01–08, agents/REGISTRY.md, and cross-links to skills.

List:
- Files missing
- Files stale (placeholder >50% or Last updated empty)
- Obvious contradictions between identity, offer ladder, catalog, compliance

Do not score yet.
```

---

## Step 1 — Context auditor

**Agent prompt:**

```text
You are the Context Auditor (4C: Context).

Evaluate section 01-identity-strategy:
- business-model, icp-personas, offer-ladder, positioning, brand-voice, visual-brand

Score /25:
- Completeness (0-10)
- Internal consistency (0-10)
- Actionability for copy/code agents (0-5)

List top 3 context gaps with exact file + section heading to fix.
```

---

## Step 2 — Connections auditor

**Agent prompt:**

```text
You are the Connections Auditor (4C: Connections).

Evaluate:
- 06-connections/integrations-matrix.md
- 04-technical-platform, 05-marketing-growth tool references

Score /25:
- Documented integrations vs workflows needed (0-10)
- MCP readiness (0-10)
- Read/write policy clarity (0-5)

Rank next 3 connections by leverage for user's focus workflow: {{FOCUS}}.
```

---

## Step 3 — Capabilities auditor

**Agent prompt:**

```text
You are the Capabilities Auditor (4C: Capabilities).

Evaluate:
- 07-operating-rules (approval gates, DoD, naming)
- agents/REGISTRY.md
- Skills available: ad-pack-from-offer, business-hub-init, (pwa, pricing if present)

Score /25:
- Approval gates cover spend/publish/deploy (0-10)
- DoD per deliverable type (0-8)
- Agent/skill coverage for user's work mix (0-7)

List missing skills or registry agents for their stated workflows.
```

---

## Step 4 — Cadence auditor

**Agent prompt:**

```text
You are the Cadence Auditor (4C: Cadence).

Evaluate:
- operating-rules cadence table
- analytics-plan review rhythm
- marketing winners/losers log usage
- Last updated dates across hub

Score /25:
- Defined rituals (0-10)
- Evidence of updates (0-10)
- Stale risk mitigation (0-5)

Recommend one weekly and one monthly ritual with owner.
```

---

## Step 5 — Synthesis lead

**Agent prompt:**

```text
You are the Synthesis Lead.

Combine scores:
- Context {{S1}}/25
- Connections {{S2}}/25
- Capabilities {{S3}}/25
- Cadence {{S4}}/25
Total /100

Produce:
1. Letter grade band: <40 critical, 40-69 build, 70-84 solid, 85+ maintain
2. Top 5 gaps ranked by leverage (tier 1 = blocks revenue/ship)
3. Top 5 strengths to preserve
4. 30-day plan: week 1-4 actions (max 3 tasks/week)

Also audit sections 02-legal-finance-trust and 03-08 for blocking gaps (one paragraph each).

Write deliverable hub-audit.md. Ask user if they want /business-hub-init refresh on tier-1 gaps only.
```

---

## Quick invoke

```text
/business-hub-audit

Hub path: ./hub/
Focus: all
```
