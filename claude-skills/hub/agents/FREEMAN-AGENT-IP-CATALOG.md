# Freeman Intelligence — AI Agent IP Catalog

> **Sources:** `claude-skills/` (this repo), Airtable PM **Projects** table (Freeman Intelligence — PM), portfolio notes as of 2026-09-12.  
> **Purpose:** Single inventory of agent IP — named agents, squads, frameworks, and productized agents.  
> **Not exhaustive:** OIS (60+ tools) and Etsy (40+ SKUs) are summarized by system; enumerate in product repos when listing for sale.

---

## Summary counts

| Category | Count | Maturity |
|----------|------:|----------|
| Named production agents (Cleo ecosystem) | 13+ | Delivered packages |
| Clinical Revenue squad | 4 | Spec + legal; build pending |
| CONTENT FORGE (AGENT FORGE child) | 7 | V1 complete |
| Claude Business OS role model | 24 | Template / skills |
| Workflow orchestrators & skills | 6 skills + CoS | In repo |
| Intelligence / revenue agents | 3 | Revenue Intel, HUNTER, Marketing Swipe |
| Autonomous build systems | 2 | TRON (rebuild), Etsy Builder (complete) |
| OpExcel / OIS tool surface | 60+ tools, 12 modes | Built; pre-revenue |
| Etsy digital agent products | 40+ | Built; listings pending |
| PM / ops | 1 | PM Agent (Phase 3) |

---

## 1. Cleo multi-department ecosystem

**Parent project:** Agent Ecosystem + Agents Explained Book  
**Orchestrator:** Cleo  

| Agent | Role (from portfolio notes) |
|-------|-----------------------------|
| **Cleo** | Orchestrator |
| **Devon / Kelvin** | Development specialist |
| **Quinn** | Specialist (dept TBD in notes) |
| **Ana** | Specialist |
| **Nova** | Specialist (Taskade integration noted) |
| **Code Reviewer** | Code quality |
| **PM Agent** | Project intelligence (see §8) |
| **Financial Analyst** | Finance |
| **Data Scientist** | Data / analytics |
| **SEO Intel** | SEO intelligence |
| **ARIA** | (Named package) |
| **Revenue Intel** | Compliance / cost-recovery intel (see §5) |
| **FlipReseller** | Reseller / flip vertical |
| **Korg** | (Named package) |
| **Ultimate Frame** | (Named package) |

**Convention:** `.claude/agents/` · Skills framework · Book: *Agents Explained* (18 ch, 5 written)

---

## 2. AGENT FORGE + CONTENT FORGE V1

**Parent project:** AGENT FORGE — Multi-Agent Framework  
**Host:** Notion modular framework  

| # | Agent | Function |
|---|--------|----------|
| 1 | Strategic Director | Content strategy |
| 2 | Brand Architect | Brand alignment |
| 3 | Copywriter | Draft copy |
| 4 | SEO Optimizer | SEO pass |
| 5 | Critic Swarm | Multi-critic QA (SMB-calibrated) |
| 6 | Memory Core | Context / memory |
| 7 | Evolution Engine | Iteration / improvement |

**Output:** Production HTML articles · Default structure PAS

---

## 3. Clinical Revenue Systems Engineering squad

**Product:** Chair-Guard OS, Flow-Capture, Revenue-Vault 360  
**Architecture:** LangGraph + FastAPI (pending build)

| Agent | Role |
|--------|------|
| **Scout** | Prospecting / signal |
| **Closer** | Conversion |
| **Dispatcher** | Routing / ops |
| **Auditor** | Compliance / QA |

**Adjacent IP:** ROI calculator (`rev-systems-os.html`), legal templates (BAA, MSA, Disclaimer, Telecom)

---

## 4. Claude Business OS — 24 role model

**Location:** `claude-skills/hub/agents/REGISTRY.md`  
**Type:** Reusable role definitions (not 24 separate codebases) — invoked 3–7 at a time via skills.

**Dev (1–6):** PWA Architect, Frontend Engineer, Backend/API Engineer, Integration Engineer, Automation Engineer, QA/Release  

**Marketing (7–12):** Positioning Strategist, Offer & Pricing Analyst, Copy Chief, Paid Ads Specialist, SEO/Content Strategist, Lifecycle/Email Architect  

**Design (13–18):** UX Strategist, UI Designer, Visual/Brand Designer, Design Systems Curator, Conversion Designer, Print/Collateral Designer  

**eComm / Social (19–24):** Store Merchandiser, CRO/Funnel Operator, Social Content Producer, Community/Engagement, Influencer/Partnership Scout, Analytics Reporter  

**Meta:** Chief of Staff (every workflow skill)

---

## 5. Revenue, pipeline & marketing intelligence

| Agent / system | Version | Function | Parent project |
|----------------|---------|----------|----------------|
| **Revenue Intel Agent** | v5.0 | Metro Detroit compliance & cost-recovery opportunities; Gem port | Revenue Intel Agent |
| **HUNTER** | CRM v1 | 7-dimension lead scoring prompt + Airtable pipeline (not a chat persona) | HUNTER — Revenue Pipeline CRM |
| **Marketing AI Agent (Swipe File)** | WIP | DK/FK/God-of-Prompt corpora → email agent | Marketing AI Agent — Swipe File |

---

## 6. OpExcel / OIS (automotive operational AI)

**Project:** OIS — OpExcel (Automotive AI)  
**Scale:** 60+ AI tools · 12 modes · AIT Command Center  

**Named lead products / diagnostics (non-exhaustive):**

- Inventory Optimization Diagnostic (lead product)
- Inbound Variability Diagnostic
- JIT Risk Monitor
- (+ additional tools in stack — full catalog in OIS repo/product docs)

**Methodology encoded:** Lean, Six Sigma, JIT, TQM, Kaizen

---

## 7. TRON — autonomous agent system

**Status:** ON HOLD · PRE-PHASE-0 rebuild  
**Target architecture:** ~5 core agents, 10–20 skills, mission-state, memory, verification engine  
**Prime directive:** Missions → verified working artifacts  
**Planned core agents (not yet named in PM):** sandbox, verification, worker loop, persistence layers (sequential build order)

---

## 8. Operations & PM

| Agent | Function | Data |
|--------|----------|------|
| **Freeman Intelligence PM Agent** | Portfolio briefings, registry CRUD triggers | Airtable `Projects` |
| **Autonomous Etsy Product Designer & Builder** | End-to-end Etsy digital product generation | TheFreemanFix (COMPLETE) |

---

## 9. Service-embedded agents (human-in-loop)

| System | Agent behavior | Human gate |
|--------|----------------|------------|
| **Freeman Copy Studio** | Claude drafts DR packages (email, LP, ads, sales page) | Sam review 15–20 min |
| **Freeman Industrial Intelligence** | 7 queue types + MIA-X scoring (prototype) | ON HOLD |

---

## 10. Productized agents (Etsy / digital SKUs)

**Project:** Etsy Digital Agents Store  
**Volume:** 40+ HTML agent/app products built  

| Line | Audience | Price band |
|------|----------|------------|
| Marketing agents | Coaches, SMB, creators | $17–47 |
| Business agent bundles | SMB | $67–97 |
| Logistics agents | Gumroad / own site | $97–297 |

**Listing names:** In Etsy builder output / TheFreemanFix — not duplicated here.

---

## 11. Workflow skills (= packaged multi-agent IP)

| Skill | Agent steps inside |
|-------|-------------------|
| `/ad-pack-from-offer` | CoS, Offer Analyst, Paid Ads, Copy Chief, Visual Designer, Analytics |
| `/pwa-idea-to-spec` | CoS, Strategist, UX, UI+DS, PWA Architect, Backend, QA |
| `/pricing-positioning-memo` | CoS, Strategist, Pricing Analyst, Merchandiser, Copy Chief, Analytics |
| `/business-hub-init` | CoS + 8 section architects |
| `/business-hub-audit` | CoS + 4C auditors + synthesis |
| `/business-os-install` | Install orchestrator |

**Pack path:** `claude-skills/*/SKILL.md`

---

## 12. Cross-reference — agent IP → PM project

| PM project (Airtable) | Primary agent IP |
|-------------------------|------------------|
| Agent Ecosystem + Book | Cleo + 13 packages |
| AGENT FORGE | Framework + CONTENT FORGE ×7 |
| Clinical Revenue Systems Engineering | Scout, Closer, Dispatcher, Auditor |
| OIS — OpExcel | 60+ tools / diagnostics |
| TRON | Future ~5 core agents |
| Revenue Intel Agent | Revenue Intel v5.0 |
| HUNTER | Scoring agent + CRM |
| Marketing AI Agent — Swipe File | Email marketing agent |
| PM Agent | Freeman PM Agent |
| TheFreemanFix | DPCS + Etsy Builder |
| Etsy Digital Agents Store | 40+ productized agents |
| Freeman Copy Studio | Copy pipeline agent |
| Freeman Industrial Intelligence | Queue + MIA-X system |
| Claude Business OS (this pack) | 24 roles + 6 skills |

---

## Maintenance

- After shipping a **new named agent**, add a row to §1–§5 or §10 and link PM project via `PM ADD` / `PM UPDATE`.
- **Registry of record for ops:** Airtable Projects + this file.
- **Registry of record for Business OS workflows:** `REGISTRY.md` (24 roles).

**Last catalog sync:** 2026-09-12
