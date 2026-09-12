# Product Matrix (CRO / PM view)

**As of:** 2026-09-12  
**Portfolio:** 4 GitHub root repos · **50+ branch-hosted products** (see [`PORTFOLIO_DEEP_MAP.md`](PORTFOLIO_DEEP_MAP.md)) · 6 factory agents on monorepo `main` · ~136 forks

> **Correction:** An earlier pass used only the non-fork list and missed your **`push` branch warehouse** (Etsy kits, MedFlow, Manuscript Master, ChiroBook, etc.) and **monorepo branch companies** (Autoborder, Freeman Intelligence, Hunter OS, prompt library platform).

## Executive summary

Your **near-term revenue** is concentrated in one monorepo: [`-build-ai-agents-with-claude`](https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude). **AI Proposals Agent™** is the most launch-ready SKU (frontend + UI + deterministic core + golden tests). **Freeman Intel** is the highest strategic heat but still **design-only** (spec + factory entry, no scaffolded tree). **SaaS Factory** is the platform moat—ship it as the “how we build agents” story alongside the first paid agent.

---

## Parallel revenue lanes (pick one primary per quarter)

| Lane | Anchor location | SKUs | Notes |
|------|-----------------|------|-------|
| **B2B agents** | monorepo `main` | Proposals + factory + engineering agents | Highest ACV |
| **Digital / Etsy** | `push` @ `cursor/etsy-store-automation-f219` | 29 kits + bundles | Fastest to cash if storefront live |
| **Prompt platform** | monorepo @ `gh-pages` / `cursor/*-prompt-library-*` | 1,352+ prompts scraped | SEO + lead gen |
| **Vertical MVPs** | monorepo branches | Autoborder, Freeman Intelligence, Hunter OS, Luxury Outlet | Need merge or release tag |
| **Creator tools** | `push` branches | Manuscript Master, book manuscript, MedFlow docs | IP + authority |

## Launch order (ranked) — B2B lane (unchanged priority)

| Rank | Product | Where (repo / path) | % complete | Heat | Status | Why this order |
|------|---------|---------------------|------------|------|--------|----------------|
| 1 | **AI Proposals Agent™** | `-build-ai-agents-with-claude` / `ai-proposals-agent/` | **52%** | 🔥 Hot | scaffold | Clear Detroit logistics ICP, pricing tiers defined, only SKU with UI+deploy docs |
| 2 | **SaaS Factory** | `-build-ai-agents-with-claude` / `saas-factory/` | **65%** | 🔥 Hot | mvp | Validates specs, scaffolds products—sell “agent SaaS in a box” |
| 3 | **Freeman Intel** | `-build-ai-agents-with-claude` / `freeman-intel/` *(spec only)* | **18%** | 🔥 Hot | design | Strong wedge (email-first ASN); needs scaffold + deterministic modules |
| 4 | **Software Developer Agent™** | `software-developer-agent/` | **42%** | Warm | scaffold | Golden tests green; upsell to proposals customers |
| 5 | **Principal Software Engineer Agent™** | `principal-software-engineer/` | **42%** | Warm | scaffold | Decision-trace positioning; bundle with architect |
| 6 | **Software Architect Agent™** | `software-architect/` | **42%** | Warm | scaffold | C4/governance; enterprise tier |
| 7 | **Engineering Manager Agent™** | `engineering-manager-agent/` | **42%** | Warm | scaffold | Delivery planning; sell last in suite |
| 8 | **VST Sampling Factory** | `VSTSampling` / root | **78%** | Warm | mvp | Niche desktop tool; blocked on Reaper/MPC hardware validation |
| 9 | **AI Agent Team** | `push` / `ai-agent-team/` | **35%** | Cold | scaffold | Generic Gemini+Supabase API—rebrand or merge into factory demo |
| — | **OpenClaw Framework** | `openclaw-framework` | **0%** | Cold | concept | Empty repo—archive or populate from `openclaw` fork |

### Fast-cash lane (if B2B pilot slips)

| Rank | Product | Where | % | Heat |
|------|---------|-------|---|------|
| FC-1 | **Top-10 / Top-20 AI Agents Bundle** | `push` @ `cursor/etsy-store-automation-f219` / `ai-agent-team/products/` | ~70% | Hot |
| FC-2 | **Prompt library (live)** | monorepo @ `gh-pages` | ~75% | Warm |
| FC-3 | **Product Creation SOP + templates** | `push` @ `claude/product-creation-template-ogygnk` | ~55% | Warm |

---

## Branch-only products (high value — not on `main`)

| Product | Branch | % (est.) |
|---------|--------|----------|
| Autoborder Comply | `cursor/autoborder-comply-mvp-cc89` | 45% |
| Autonomous Hunter OS | `cursor/autonomous-hunter-os-54da` | 50% |
| Freeman Intelligence (WRIS) | `cursor/freeman-intelligence-wris-64d3` | 55% |
| Freeman Method | `cursor/freeman-method-tools-c134` | 40% |
| Luxury Bedroom Outlet | `cursor/luxury-bedroom-outlet-46d5` | 45% |
| The Architect Agent | `cursor/the-architect-agent-0050` | 50% |
| Logistics Marketing Factory | `cursor/logistics-marketing-factory-c9f0` | 35% |
| QA Engineer Agent | `cursor/complete-monorepo-64d3` | 42% |

Full branch list: [`PORTFOLIO_DEEP_MAP.md`](PORTFOLIO_DEEP_MAP.md).

---

## Completion breakdown (owned products)

| Product | Spec | Scaffold | Deterministic + tests | Skills / agent | UI / API | Prod deploy | **Total %** |
|---------|------|----------|------------------------|----------------|----------|-------------|-------------|
| AI Proposals Agent | ✅ | ✅ | ✅ partial (KB needed for full golden) | ✅ | ✅ | ❌ | **52** |
| SaaS Factory | ✅ | ✅ | ✅ CLI tests | ✅ templates | N/A | ❌ | **65** |
| Freeman Intel | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | **18** |
| Dev / PSE / Arch / EM agents | ✅ | ✅ | ✅ 5/5 modules | ✅ | ❌ | ❌ | **42** each |
| VST Sampling Factory | N/A | ✅ | ✅ 43 tests | N/A | ✅ desktop | ❌ HW | **78** |
| AI Agent Team | ❌ | ✅ | ❌ | ❌ | ✅ minimal API | ❌ | **35** |

---

## Heat map (what to work on *this month*)

| Heat | Products | CRO action |
|------|----------|------------|
| 🔥 **Hot** | AI Proposals, SaaS Factory, Freeman Intel | Pick **one** external pilot for Proposals; scaffold Freeman Intel; publish factory `list` demo video |
| **Warm** | Agent suite (4), VSTSampling, fork: `marketing-ai-studio`, `openclaw-marketing-skills`, `God-Of-Prompt`, `ai-business-skills` | Do not launch forks until original SKU #1 has paying user |
| **Cold** | `push` demo API, empty `openclaw-framework`, reference forks | Park or delete to reduce cognitive load |

---

## Where each product lives (find & upgrade)

```
samuelfreemanjobs-hash/
├── -build-ai-agents-with-claude/     ← PRIMARY MONOREPO
│   ├── saas-factory/                 ← Platform / factory CLI
│   ├── ai-proposals-agent/           ← Launch SKU #1
│   ├── software-developer-agent/
│   ├── principal-software-engineer/
│   ├── software-architect/
│   ├── engineering-manager-agent/
│   └── freeman-intel/                ← NOT ON DISK YET — run scaffold
├── VSTSampling/                      ← Audio sampling desktop pipeline
├── push/
│   └── ai-agent-team/                ← Node Gemini + Supabase API
└── openclaw-framework/               ← Empty — placeholder
```

Pre-written `project.md` copies: [`project-files/`](project-files/README.md).

---

## Improvements to this program (recommended)

1. **Single dashboard repo** — Keep `product-management/` in `.github` (this repo) as the KB anchor; submodule or sync into Notion weekly.
2. **Automate scoring** — GitHub Action on `-build-ai-agents-with-claude` runs golden tests + updates `completion_pct` in `REGISTRY.yaml`.
3. **Kill empty SKUs** — Either scaffold `freeman-intel` or drop from README until folder exists (avoids agent confusion).
4. **Fork policy** — Tag forks `reference` vs `fork-product` in GitHub topics; only the latter get `project.md`.
5. **Revenue milestone** — Define “launched” = 1 paying customer OR 3 signed pilots with LOI—not “code complete.”

---

## Mandatory agent stack for next audit run

See [`prompts/ELITE_PORTFOLIO_CRO_AGENT.md`](prompts/ELITE_PORTFOLIO_CRO_AGENT.md).

| Role | Tooling |
|------|---------|
| Repo cartographer | `explore` subagent (very thorough) + `gh repo list` |
| Product scorer | Read `saas-factory/products/*.yaml` + run `verify` commands |
| CRO ranker | Update `REGISTRY.yaml` + this matrix |
| KB publisher | Write `project.md` per `rules/PROJECT_MD_RULE.md` |

**Skills to enable:** `tasks-plan`, `spec-to-implementation`, `knowledge-capture`, Zapier `inspect_zapier_actions` (if CRM sync), `env-setup` for test runners.
