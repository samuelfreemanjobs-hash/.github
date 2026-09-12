# Portfolio deep map (where your work actually lives)

**Audit correction (2026-09-12):** Counting only non-fork repos listed **four** GitHub roots but **under-counted your creations**. Most SKUs live on **feature branches** inside `push` and `-build-ai-agents-with-claude`, not on `main`.

## How to read this document

| Location type | Meaning |
|---------------|---------|
| `repo / main` | Default branch |
| `repo @ branch` | Checkout branch to see the product |
| `repo / path` | Path inside that branch |

---

## A. `push` — automation repo, **multi-product branch warehouse**

Repo: https://github.com/samuelfreemanjobs-hash/push  
Default `main` ≈ minimal `ai-agent-team` API only. **Your catalog is on branches:**

| Branch | What you built | Path / notes |
|--------|----------------|--------------|
| `cursor/etsy-store-automation-f219` | **Etsy / digital product line** — Canva API, n8n, Supabase; **29 product folders** including agents 01–20, top-10/20 bundles, business-in-a-box | `ai-agent-team/products/*`, `ai-agent-team/src/etsy`, `scripts/canva` |
| `claude/product-creation-template-ogygnk` | **Product factory SOP** + sample apps **ChiroBook**, **LocalBook**, templates | `PRODUCT_CREATION_SOP.md`, `chirobook/`, `localbook/`, `templates/` |
| `claude/universal-prompt-framework-ewl26u` | **Prompt Architect v2** (5-tab workstation) | `prompt-framework/` |
| `claude/marketing-team-framework-w4sxpp` | Multi-agent **marketing team** + token budgeting | `ai-agent-team/src/agents` |
| `cursor/micro-saas-checklist-a24f` | **Micro SaaS Factory Starter** boilerplate | `micro-saas-factory-starter/` |
| `cursor/n8n-ea-runtime-3e82` | **MedFlow OS** playbook + n8n runtime docs | `ai-agent-team/docs/medflow`, `n8n/` |
| `cursor/manuscript-master-agent-ea28` | **Manuscript Master** KDP writing agent | `ai-agent-team/prompts/manuscript-master/` |
| `cursor/manuscript-master-aede` | Manuscript review PDF / build pipeline | `ai-agent-team/` (manuscript assets) |
| `cursor/back-office-chapters-667f` | **Book:** *Building AI Agents with Claude* — 11-chapter architecture | `ai-agent-team/manuscripts/building-ai-agents-with-claude/` |
| `cursor/mcp-multi-agent-revenue-chapters-b739` | Book Act III — guardrails, synthetic workforce, 30-day roadmap | same manuscript tree |
| `sandbox/b287b60e-ecbc-40c4-ac41--k5zj` | LINEAR integration experiment | `ai-agent-team/LINEAR` |

### Etsy / agent-kit SKUs (branch `cursor/etsy-store-automation-f219`)

Each folder under `ai-agent-team/products/` is a **shippable digital product** (playbook + workflows + implementation packs). Examples:

- `agent-01-etsy-listing-seo-agent-kit` … `agent-20-coach-consultant-professional-agent-kit`
- `top-10-ai-agents-bundle`, `top-20-ai-agents-bundle`
- `agent-17-business-in-a-box-orchestrator-agent-kit`
- `marketing-command-center-excel`, `copywriting-templates`, `postcard-direct-mail-pack`, etc.

**Count:** 29 top-level product directories on that branch (not 4 repos).

---

## B. `-build-ai-agents-with-claude` — B2B monorepo + **branch-only companies**

Repo: https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude  
**`main`:** agent SaaS suite (Proposals, Factory, 4 engineering agents).

**Additional businesses / platforms on branches** (not merged to `main`):

| Branch | Product / system | Top-level dirs |
|--------|------------------|----------------|
| `cursor/autoborder-comply-mvp-cc89` | **Autoborder Comply** — cross-border compliance MVP, Monterrey/Saltillo GTM | `autoborder/` |
| `cursor/autonomous-hunter-os-54da` | **Autonomous Hunter OS** — operator dashboard, launch readiness % | `frontend/`, `business/`, `n8n/`, `supabase/` |
| `cursor/freeman-intelligence-wris-64d3` | **Freeman Intelligence / WRIS** — site, calculators, deploy | `freeman-intelligence/` |
| `cursor/freeman-method-tools-c134` | **Freeman Method** — business applications | `freeman-method/` |
| `cursor/luxury-bedroom-outlet-46d5` | **Luxury Bedroom Outlet** (Maison Nocturne) | `luxury-bedroom-outlet/` |
| `cursor/the-architect-agent-0050` | **The Architect Agent** + God of Prompts integration | `the_architect/`, `website/` |
| `cursor/logistics-marketing-factory-c9f0` | **Logistics Marketing System Factory** | `src/` |
| `cursor/complete-monorepo-64d3` | Adds **freeman-intel** scaffold + **qa-engineer-agent** + CI | `freeman-intel/`, `qa-engineer-agent/` |
| `cursor/*-prompt-library-3a2e` (many) | **Unified prompt library platform** — scrapers + static site | `agents/`, `data/`, `public/`, `src/` |
| `gh-pages` | **Live prompt library** — ~1,352 scraped prompts deployed | GitHub Pages |

Prompt-library branches include: Anthropic, Gamma, Gemini API, PromptHero, Snack Prompt, Wharton GAIL, business generator (10k+), More Useful / God of Prompt, etc.

---

## C. Standalone repos (still valid, not the whole story)

| Repo | Role |
|------|------|
| `VSTSampling` | Desktop **VST Sampling Factory** (Python + Reaper pipeline) |
| `openclaw-framework` | Placeholder (empty) — intended OpenClaw agent files |
| `.github` | Profile + **this product-management KB** |

---

## D. Forks you may treat as **your GTM stack** (differentiated intent)

These are forks by GitHub metadata but align with your Etsy/agent-kit/automation work:

- `product-factory`, `ai-factory`, `etsy-digital-studio`, `etsy-products-hub`, `etsy-mcp-server`
- `openclaw-marketing-skills`, `marketing-ai-studio`, `God-Of-Prompt`
- `data-agent-kit` (empty description — verify before use)

**Rule:** classify as **yours** when branch history or unique folders exist; do not rely on `isFork` alone.

---

## E. Recommended portfolio consolidation (so agents stop missing products)

1. **Promote `push` branches to folders on `main`** — e.g. `push/products/etsy-agent-kits/`, `push/products/medflow/`, or split into repos.
2. **Merge or tag monorepo branch MVPs** — `freeman-intelligence`, `autoborder`, `autonomous-hunter-os` deserve `main` or release tags.
3. **Single registry source** — extend `REGISTRY.yaml` with `location_type: branch` and `branch:` fields (started in this update).
4. **Re-run elite prompt** with instruction: *scan all branches on `push` and `-build-ai-agents-with-claude` before scoring.*

---

## F. Quick commands (reproduce this audit)

```bash
# push branches
gh api repos/samuelfreemanjobs-hash/push/branches -q '.[].name'

# monorepo branches with extra roots
gh api repos/samuelfreemanjobs-hash/-build-ai-agents-with-claude/branches -q '.[].name'

# count Etsy kits
git clone https://github.com/samuelfreemanjobs-hash/push
cd push && git checkout cursor/etsy-store-automation-f219
ls -1 ai-agent-team/products | wc -l
```
