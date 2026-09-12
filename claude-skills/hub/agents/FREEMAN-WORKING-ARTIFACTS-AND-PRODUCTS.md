# Freeman Intelligence — Working Artifacts & Product IP

> **Inventory of shippable creations:** apps, sites, prompts, frameworks, CRMs, agents, and bundles.  
> **Sources:** Airtable PM **Projects** (2026-09-12), public GitHub (`samuelfreemanjobs-hash/*`), `claude-skills/` in `.github`.  
> **Legend — status:** **SHIP** = verified working · **WORKING** = usable · **PROTOTYPE** = demo · **SPEC** = documented, not built · **DESIGN** = spec only · **WIP** · **ON HOLD**

**Related:** [FREEMAN-AGENT-IP-CATALOG.md](./FREEMAN-AGENT-IP-CATALOG.md) (agent personas only)

---

## A. Web apps, sites & “prompt UIs”

| Artifact | Status | Product? | What it is | Where / pointer |
|----------|--------|----------|------------|-----------------|
| **AI Proposals Agent™ — customer frontend** | WORKING | Y ($ B2B logistics RFP) | Vite/React app (`frontend/`) for proposal workflow UI | [ `-build-ai-agents-with-claude/ai-proposals-agent/frontend`](https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude/tree/main/ai-proposals-agent/frontend) |
| **AI Proposals Agent™ — operator console** | WORKING | Y (internal ops) | Static operator UI for pipeline control | `ai-proposals-agent/ui/operator-console/index.html` (same repo) |
| **Prompt / agent architecture docs (web-ready)** | WORKING | Y (lead magnet) | `docs/prompt-architecture.md`, GTM, brand system | `ai-proposals-agent/docs/` |
| **Freeman Copy Studio — landing + checkout** | WORKING | Y (service) | Vercel LP, Stripe, Tally brief, Make automation | PM: Freeman Copy Studio (live stack in Airtable **Stack**) |
| **Clinical Revenue — ROI dashboard** | WORKING | Y (sales tool) | `rev-systems-os.html` — 7-tab ROI calculator | PM notes; path in Clinical project repo (not in public `.github`) |
| **Freeman Industrial Intelligence** | PROTOTYPE | Y (subscription) | React app, 7 queues, MIA-X scoring | ON HOLD · Claude prototype → Gemini prod target |
| **God Of Prompt (GOP) skill** | WORKING | Y (fork/skill product) | Six-part XML system prompt generator + execute | Fork: [God-Of-Prompt](https://github.com/samuelfreemanjobs-hash/God-Of-Prompt) — `$gop` Codex skill, not a standalone hosted site |
| **Marketing swipe + XML writing prompts** | WIP | Y | DK/FK master swipe, God-of-Prompt corpus analysis, XML Claude prompts | PM: Marketing AI Agent — Swipe File |
| **CONTENT FORGE article output** | SHIP | Y | Production HTML articles (PAS default) | AGENT FORGE / Notion host |
| **Etsy digital agents (40+ HTML SKUs)** | SHIP | Y | Flat-file agents, web apps, tools ($17–47+) | TheFreemanFix builder output · PM: Etsy store |
| **Freeman Intel (plant inbound SaaS)** | DESIGN | Y | Multi-agent inbound readiness; approval UI planned | Spec: `-build-ai-agents-with-claude/saas-factory/products/freeman-intel.yaml` · **no `freeman-intel/` tree in repo yet** |
| **Claude Business OS pack** | SHIP | Y ($97–297 template) | Hub + 6 workflow skills + install prompt | `claude-skills/` · [`.github` PR branch](https://github.com/samuelfreemanjobs-hash/.github) |
| **claude-os repo** | WIP | Y | Public “Heavy OS for Claude” (README stage) | [claude-os](https://github.com/samuelfreemanjobs-hash/claude-os) |

**Note on “prompt website”:** Closest **working web surfaces** in public repos are **AI Proposals Agent frontend + operator console** (prompt-driven B2B SaaS UI) and **Copy Studio / rev-systems-os.html** (PM-documented). GOP is a **prompt generator skill**, not a hosted site. If you mean a different URL, add it to this table once located.

---

## B. Agent SaaS products (monorepo factory)

**Repo:** [ `-build-ai-agents-with-claude`](https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude) · **Factory:** `saas-factory/`

| Product | Status | Sell as | Backend + tests | Prompts / skills |
|---------|--------|---------|-----------------|------------------|
| **AI Proposals Agent™** | WORKING (not prod-ready per README) | B2B SaaS / white-label | FastAPI, golden tests, pricing/compliance scripts | `prompts/` + 5× `skills/` |
| **Engineering Manager Agent** | WORKING scaffold | SaaS / internal | Python API + golden tests | 7 skills |
| **Principal Software Engineer** | WORKING scaffold | SaaS / internal | Python API + golden tests | 7 skills |
| **Software Architect** | WORKING scaffold | SaaS / internal | Python API + golden tests | 7 skills |
| **Software Developer Agent** | WORKING scaffold | SaaS / internal | Python API + golden tests | 6 skills |
| **Freeman Intel** | DESIGN | $499–1999/mo tiers in YAML | Not scaffolded | Pipeline S0–S5 in spec |
| **SaaS Factory itself** | SHIP | Y (meta-product) | `saas-factory` CLI scaffold + product registry | Template `agent-saas/` |

Each agent product includes: `agent/SOUL.md`, `DUTIES.md`, `core-config.xml`, `system-prompt.md`, JSON schemas, deterministic `scripts/`, optional `deploy/` (Docker).

---

## C. Services & funnels (human-in-loop)

| Offering | Status | Price (from PM) | Artifacts |
|----------|--------|-----------------|-----------|
| **Freeman Copy Studio** | WORKING | $197–597 packages | Stripe, Tally, Make, Airtable orders, Dripify |
| **Clinical Revenue SKUs** | SPEC/WIP | $1,500–4,500/mo + setup | Architecture spec, 4-agent LangGraph plan, legal templates |
| **OIS / OpExcel** | WORKING (tools) | High-ticket B2B | 60+ tools, AIT Command Center, diagnostics |
| **Freeman Intelligence services** | WORKING | HUNTER catalog (7 services) | Service Catalog in HUNTER base |

---

## D. CRM, pipeline & ops artifacts

| Artifact | Status | Product? | Contents |
|----------|--------|----------|----------|
| **HUNTER — Revenue Pipeline CRM** | SHIP | Y **$97** **Revenue Pipeline System (HUNTER CRM)** | Airtable base (Opportunities, Outreach, Service Catalog), 7-dim scoring, Setup Guide PDF, paste-ready Claude scoring prompt · Launch kit: `deliverables/revenue-pipeline-system/` |
| **Freeman Intelligence — PM base** | WORKING | Y (internal / white-label) | Projects table, PM Agent triggers, health rules |
| **Freeman Copy Studio — order Airtable** | WORKING | Internal | Order tracking |

---

## E. Frameworks, methodology & education

| Artifact | Status | Product? | Notes |
|----------|--------|----------|-------|
| **DPCS Lightweight** | SHIP | Y (license / course) | TheFreemanFix: 5 entry points, Cursor rules, CLAUDE.md, AGENTS.md |
| **Autonomous Etsy Product Designer & Builder** | SHIP | Y (proof + Etsy) | Complete + verify script (TheFreemanFix) |
| **AGENT FORGE (Notion)** | SHIP | Y | Modular multi-agent framework; CONTENT FORGE child |
| **Agents Explained (book)** | WIP | Y | 18 ch planned, 5 written |
| **The Autonomous Builder (manuscript)** | WIP | Y | ~155 pages, publication TBD |
| **TRON — autonomous agent system** | ON HOLD | Y (future) | Walking skeleton rebuild |
| **Cleo agent packages (13+)** | SHIP | Y | See agent catalog |
| **24-role Business OS + skills** | SHIP | Y | This pack |

---

## F. Intelligence & research engines

| Artifact | Status | Product? | Notes |
|----------|--------|----------|-------|
| **Revenue Intel Agent v5.0** | WORKING | Y | Compliance/cost-recovery intel; Gem port |
| **Freeman Industrial Intelligence** | PROTOTYPE | Y | 7 queue types, weekly deliverables |
| **OIS diagnostics** | WORKING | Y | Inventory, JIT, inbound variability, etc. |

---

## G. Bundles & catalogs (product lines)

| Line | Status | Channel | PM project |
|------|--------|---------|------------|
| Etsy marketing agents | SHIP (files) | Etsy $17–47 | Etsy Digital Agents Store |
| Etsy business bundles | SHIP | $67–97 | Same |
| Logistics agents | SHIP | Gumroad/own $97–297 | Same |
| **Starter Business Kit** / **Complete Business in a Box** | SHIP (planned bundles) | Etsy | Etsy notes |
| HUNTER digital product | SHIP | Gumroad/Etsy $97 | **Revenue Pipeline System (HUNTER CRM)** · see `deliverables/revenue-pipeline-system/` |
| Claude Business OS install pack | SHIP | Gumroad/Etsy/repo | claude-skills |

---

## H. Supporting repos (public GitHub)

| Repo | Original IP? | Product relevance |
|------|--------------|-------------------|
| `-build-ai-agents-with-claude` | **Yes** | Agent SaaS factory + 5 agent products |
| `push` / `ai-agent-team` | **Yes** | Gemini + Supabase agent API (early) |
| `.github` / `claude-skills` | **Yes** | Business OS |
| `claude-os` | **Yes** | Heavy OS branding |
| `God-Of-Prompt` | Fork | Prompt skill; informs Marketing swipe work |
| `openclaw-framework` | **Yes** (empty remote) | Placeholder |
| Many forks (OpenClaw, LangChain, etc.) | No | Reference only — **exclude from product IP** |

---

## I. Legal & compliance artifacts (Clinical + ops)

| Artifact | Status | Product? |
|----------|--------|----------|
| BAA, MSA, Disclaimer, Telecom templates | SHIP | Y (with Clinical SKU) |
| HIPAA-oriented architecture spec | SPEC | Y |

---

## J. Not yet located in public git (PM-only — add path when found)

| Artifact | PM reference | Action |
|----------|--------------|--------|
| **TheFreemanFix** full tree | Primary DPCS + Etsy builder | Add repo URL or sync to GitHub |
| **rev-systems-os.html** | Clinical stack | Confirm path in Clinical repo |
| **Notion AGENT FORGE** | Notion host | Export or link |
| **OIS 60+ tool names** | OpExcel stack | Export catalog from OIS repo |
| **Individual Etsy SKU list** | 40+ products | Run Etsy builder manifest / folder listing |
| **Specific “prompt website” URL** | Your mention | **PM UPDATE** with URL → add to §A |

---

## Maintenance

1. When an artifact **ships**, set status **SHIP** and add repo path.  
2. When listing for sale, add price + channel to §G.  
3. Run quarterly: diff this file vs **PM BRIEFING** project list.  
4. **Airtable:** `Artifacts` table `tblUaFGrktRDqFyur` linked to Projects — see [AIRTABLE-ARTIFACTS.md](./AIRTABLE-ARTIFACTS.md).

**Last sync:** 2026-09-12 (PM Agent IP Registry 70%; +claude-os, AI Proposals docs in Airtable)
