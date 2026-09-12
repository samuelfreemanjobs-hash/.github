# Phase 0 — Revenue Intel Agent v5.0 (product foundation)

**Goal:** Make v5.0 **reviewable**, **version-pinned**, and **ready to package** for paying customers — without publishing listings yet.

**Exit gate:** Sam signs Phase 0 review in `review/index.html` checklist (or replies “Phase 0 approved”) → unlock Phase 1 (ZIP + Gumroad).

---

## 0.1 Source of truth & version pin

| Task | Owner | Status |
|------|-------|--------|
| Gem v5.0 exported to repo (`REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md`) | Agent (draft) + Sam (delta) | **In progress** — draft port from catalog + HUNTER industrial context |
| Version string `v5.0` in prompt header + README | Agent | **Done** |
| Changelog stub `CHANGELOG.md` | Agent | **Done** |
| Skill wrapper `revenue-intel-agent/SKILL.md` | Agent | **Done** |

## 0.2 Product definition

| Task | Owner | Status |
|------|-------|--------|
| ICP + anti-personas (`NICHE-POSITIONING.md`) | Agent | **Done** (draft) |
| Output contract (`OPPORTUNITY-BRIEF-SCHEMA.md`) | Agent | **Done** |
| HUNTER handoff rules (internal base only) | Agent | **Done** (see schema + HUNTER launch checklist) |
| Compliance disclaimers in prompt + setup guide | Agent | **Done** (draft — legal review Sam) |

## 0.3 Review surface

| Task | Owner | Status |
|------|-------|--------|
| Review portal HTML | Agent | **Done** |
| Example run: 1 sample opportunity brief (`examples/sample-opportunity-brief.md`) | Agent | **Done** |
| Dogfood: Sam runs 3 real Metro Detroit targets | Sam | **Not started** |

## 0.4 Commercial prep (no public listing yet)

| Task | Owner | Status |
|------|-------|--------|
| Price band decision ($47 / $97 / $197 prompt SKU — see `LISTING-GUMROAD.md`) | Sam | **Not started** |
| License line (`LICENSE.txt`) | Agent | **Done** |
| Support email placeholder `{SUPPORT_EMAIL}` | Agent | **Done** |
| SKU row in `hub/03-product-delivery/product-catalog.md` | Agent | **Done** (draft) |

## 0.5 Integrations & ops

| Task | Owner | Status |
|------|-------|--------|
| PM Artifacts row path updated in hub docs | Agent | **Done** |
| Zapier/Airtable PM sync (Next Action = Phase 0 review) | Agent | **Blocked** — Zapier task limit (same as HUNTER build) |
| Revenue Intel → HUNTER note in **internal** HUNTER base only | Sam | **Not started** |

---

## Phase 1 preview (locked until Phase 0 exit)

- Export SETUP-GUIDE + QUICK-START to PDF  
- Build `Revenue-Intel-Agent-v5.0.zip`  
- Gumroad live + receipt email  
- Loom: paste prompt → one opportunity brief → optional HUNTER row  

---

## Sam — Phase 0 review questions

1. Does the system prompt match your live Gem v5.0 voice and research steps?
2. Is Metro Detroit + compliance/cost-recovery scope correct, or should we widen/narrow?
3. Preferred SKU price and channel (Gumroad vs Etsy vs bundle with HUNTER $97)?
4. Any forbidden opportunity types (legal, HIPAA, government incentives) to hard-block?
