# Product Matrix (CRO / PM view)

**As of:** 2026-09-12  
**Portfolio:** 4 original repos · 6 factory-registered agent products · ~136 forks (see [`REPO_CATALOG.md`](REPO_CATALOG.md))

## Executive summary

Your **near-term revenue** is concentrated in one monorepo: [`-build-ai-agents-with-claude`](https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude). **AI Proposals Agent™** is the most launch-ready SKU (frontend + UI + deterministic core + golden tests). **Freeman Intel** is the highest strategic heat but still **design-only** (spec + factory entry, no scaffolded tree). **SaaS Factory** is the platform moat—ship it as the “how we build agents” story alongside the first paid agent.

---

## Launch order (ranked)

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
