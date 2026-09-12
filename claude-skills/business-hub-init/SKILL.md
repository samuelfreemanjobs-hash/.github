---
name: business-hub-init
description: Initialize or refresh the business hub (sections 1–8) through an interviewed multi-agent workflow. Creates or updates hub markdown files for identity, legal/finance, product, tech stack, marketing, integrations, operating rules, and human accountability. Use when starting a Claude OS, onboarding a new business, or rebuilding context after offer/stack changes.
---

# Business hub init (sections 1–8)

Build or refresh **`hub/`** so ad pack, PWA spec, pricing memo, and agent workflows share one source of truth.

## Paths

- **Hub root:** `hub/` relative to project, or user-provided `HUB_PATH`.
- **Templates:** copy from skill pack `hub/` if files missing.
- **Deliverable summary:** `deliverables/hub-init/YYYY-MM-DD_hub-init-summary.md`

## Before you start

Ask once if not provided:

1. Business name and one-line description  
2. Hub location path (default `./hub/`)  
3. Mode: **greenfield** (empty templates) vs **refresh** (merge with existing)  
4. Sensitive data rule: **no secrets in git** — use placeholders  

## Orchestration

You are **Chief of Staff**. Run steps **1 → 8 in order**. Each step:

1. Run the **agent prompt** (subagent OK).  
2. **Write/update** the listed hub files with merged content.  
3. Append a short status to the init summary deliverable.  

In **refresh** mode: read existing files first; preserve user edits; mark AI-added blocks with `<!-- hub-init {{date}} -->`.

**Not legal or tax advice** — steps 2 flags items for professional review.

---

## Step 0 — Chief of Staff (scope)

**Agent prompt:**

```text
You are Chief of Staff bootstrapping a Claude business hub.

Inputs:
- Business: {{BUSINESS}}
- Mode: {{greenfield|refresh}}
- Hub path: {{HUB_PATH}}

Tasks:
1. List which hub files exist vs missing (use template list from skill).
2. Identify the top 5 unknowns that block accurate hub content — ask the user ONLY these if blocking; else proceed with [ASSUMPTION] tags.
3. Publish a file write plan: which files this session will touch.
4. Set review cadence recommendation (weekly metrics, monthly hub review).

Do not fill section content yet.
```

---

## Step 1 — Identity & strategy architect

**Files:**  
`01-identity-strategy/business-model.md`  
`01-identity-strategy/icp-personas.md`  
`01-identity-strategy/offer-ladder.md`  
`01-identity-strategy/positioning.md`  
`01-identity-strategy/brand-voice.md`  
`01-identity-strategy/visual-brand.md`

**Agent prompt:**

```text
You are the Identity & Strategy Architect.

Interview the user (batch questions, max 12) OR use provided brief:

Required topics:
- Who pays, for what, how delivered (business model)
- One primary ICP + optional secondary; pains, objections, their language
- Offer ladder: lead magnet → core → upsell; prices if known
- Category, differentiation, why us; 3 messaging pillars
- Brand voice adjectives, always/never, taboo claims
- Visual brand: colors, type, photo style; Figma/link if any

Output:
1. Full markdown content for EACH of the six files (use template headings).
2. Cross-check: positioning must match ICP; offer ladder must match business model.
3. List contradictions to resolve with user.

Write files to hub. No fake testimonials or revenue numbers.
```

---

## Step 2 — Legal, finance & trust advisor

**Files:**  
`02-legal-finance-trust/entity-banking-payments.md`  
`02-legal-finance-trust/tax-accounting.md`  
`02-legal-finance-trust/policies-terms-privacy-refund.md`  
`02-legal-finance-trust/claims-compliance.md`  
`02-legal-finance-trust/contract-templates.md`

**Agent prompt:**

```text
You are the Legal, Finance & Trust Advisor (operations documentation only, NOT a lawyer or CPA).

Gather:
- Entity type, payment processors, invoicing tool (names only, no account numbers)
- Accounting tool + high-level chart of accounts categories
- Whether terms/privacy/refund URLs exist or need drafting
- Sensitive categories (health, income claims, testimonials rules)
- Contract template locations (client, contractor)

Output:
1. Fill all five hub files with placeholders where user lacks docs.
2. Section "Professional review required" checklist per file.
3. claims-compliance.md must align with brand-voice taboos from step 1.

Never invent policy text as final legal copy — mark as DRAFT for attorney review.
Do not store EIN, bank numbers, or API keys in hub files.
```

---

## Step 3 — Product & delivery operator

**Files:**  
`03-product-delivery/product-catalog.md`  
`03-product-delivery/fulfillment-sop.md`  
`03-product-delivery/support-faq.md`  
`03-product-delivery/analytics-plan.md`

**Agent prompt:**

```text
You are the Product & Delivery Operator.

Gather:
- SKUs/services, prices, digital vs physical fulfillment
- SLAs, delivery mechanisms, onboarding steps
- Support channels, top FAQs, macros
- North star metric, conversion events, dashboard tools

Output:
1. Populate all four files.
2. Align catalog with offer-ladder from step 1.
3. analytics-plan conversion names must be concrete (event names, not vague "track sales").

Flag gaps: missing refund alignment with policies file — note cross-link to step 2.
```

---

## Step 4 — Platform engineer (documentation)

**Files:**  
`04-technical-platform/technical-platform.md`

**Agent prompt:**

```text
You are the Platform Engineer documenting the technical stack (not deploying).

Gather:
- Domains, DNS, hosting providers
- Git org/repos, branch rules
- dev/staging/prod URLs, secrets manager name (not secrets)
- CI/CD per repo
- Design system / Figma / token paths
- CMS, DB, Sentry or equivalent

Output:
1. Single technical-platform.md with tables filled or TBD rows.
2. Agent rules section: prod deploy gate, no secrets in git.
3. List minimum repos needed for next PWA spec workflow.
```

---

## Step 5 — Growth stack curator

**Files:**  
`05-marketing-growth/marketing-growth-stack.md`

**Agent prompt:**

```text
You are the Growth Stack Curator.

Gather:
- Ad platforms, pixel/CAPI status
- Email/CRM tool and live flows
- Social handles, posting tool, draft vs publish policy
- Landing hosts tied to analytics properties
- Creative library location, competitor notes doc path

Output:
1. Fill marketing-growth-stack.md including winners/losers log table (empty OK).
2. Tie ad accounts to claims-compliance and approval-gates (preview for step 7).
3. Recommend 3 connections to enable first in integrations matrix.
```

---

## Step 6 — Integrations architect (Connections)

**Files:**  
`06-connections/integrations-matrix.md`

**Agent prompt:**

```text
You are the Integrations Architect.

Context: workflows ad pack, PWA spec, pricing memo.

Tasks:
1. Fill integrations matrix: each connection, workflow checkmarks, MCP status, priority backlog.
2. List MCP servers to configure in Claude Code (GitHub, Figma, analytics, Shopify, tasks) — read vs write.
3. Rule: no write MCP until human enables in operating rules.

Cross-check step 4–5 tools appear in matrix.
```

---

## Step 7 — COO operating rules

**Files:**  
`07-operating-rules/operating-rules.md`  
`hub/agents/REGISTRY.md` (update if missing agents section)

**Agent prompt:**

```text
You are the COO defining human+AI operating rules.

Gather user preferences:
- What AI may draft vs execute (ads, deploy, email, social, pricing, refunds, contracts)
- DoD for ad pack, PWA spec, pricing memo
- Naming conventions for campaigns, branches, hub commits
- Cadence: weekly metrics, monthly offer review, quarterly compliance

Output:
1. operating-rules.md with approval gates table completed.
2. Confirm REGISTRY.md exists; add note if 24-agent registry not customized.

Align with human-roles step 8 — no contradictions on who approves spend/deploy.
```

---

## Step 8 — Human accountability lead

**Files:**  
`08-human-roles/human-roles.md`

**Agent prompt:**

```text
You are the Human Accountability Lead.

Tasks:
1. Fill non-delegable decisions table with named roles (user name or "founder").
2. Document team backups if any.
3. Define "good enough" for AI drafts before human review.
4. Emergency contacts (optional, no secrets).

Cross-check approval gates in operating-rules — every gate has a human approver.
```

---

## Step 9 — Human gate & handoff

Present:

1. **Contradiction list** from all steps  
2. **Professional review** items (legal, tax, policies)  
3. **Top 10 hub gaps** still `[TBD]`  
4. Ask: **"Approve hub v1 for use in ad pack / PWA / pricing skills?"**

Update init summary with file list and approval checkbox.

---

## Init summary template

Write `deliverables/hub-init/YYYY-MM-DD_hub-init-summary.md`:

```markdown
# Hub init summary — {{date}}

## Files written
- [ ] list each path

## Assumptions
-

## Professional review required
-

## Approved for workflow use
- [ ] User confirmed
```

---

## Quick invoke

```text
/business-hub-init

Business: [name + one line]
Hub path: ./hub/
Mode: greenfield
```

Run full workflow.
