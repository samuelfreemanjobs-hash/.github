# AI Proposals Agent™

**Last updated:** 2026-09-12  
**Completion:** 45% (9/20 tasks)

## Overview

B2B single-agent SaaS for logistics BD teams in the Detroit corridor: ingest RFPs, extract requirements, deterministic pricing/compliance, agent-generated narrative, export proposal bundles. "Done" = paying pilot on Professional tier with full golden fixture runs green and staging deploy.

## Audience & success

- **For:** Logistics BD, sales, and solutions teams responding to RFPs (Metro Detroit corridor).
- **Success metric:** 1 paying customer or 3 signed pilots with LOI within 90 days of launch.
- **Urgency:** High — lead SKU for Freeman agent suite.

## Stack & constraints

- **Stack:** Python deterministic core, agent + skills, frontend/UI, deploy docs; factory spec in `saas-factory/products/ai-proposals-agent.yaml`.
- **Constraints:** No model-generated numerics in binding fields; compliance fail-closed; schema violation HALT.

## Tasks

- [x] Factory product spec validated
- [x] Scaffold tree (agent, skills, backend, scripts)
- [x] Golden test runner — component logic green
- [x] Frontend + UI present
- [x] Deployment guide drafted
- [x] Pricing tiers defined in spec
- [x] Skills pack (5 skills) present
- [x] Deterministic modules stubbed/implementing
- [x] README + verify command documented
- [ ] Knowledge base configured for full golden fixtures
- [ ] Full golden fixture run green end-to-end
- [ ] Staging deploy (Railway/cloud) with secrets
- [ ] Pilot customer workflow (intake → export) dogfooded once
- [ ] Production deploy + monitoring
- [ ] Sales one-pager + demo Loom
- [ ] Billing (Stripe) wired to tiers
- [ ] First external pilot signed
- [ ] First paying customer
- [ ] Onboarding checklist for Professional tier
- [ ] Support/runbook for HALT cases

## Decisions

| Date | Decision |
|------|----------|
| 2026-09-12 | Portfolio registry: launch rank #1 B2B lane |

## Blockers & open questions

- KB content/source for golden fixtures not configured in audit environment.
- [TBD] Primary pilot account name and RFP sample for demo.

## Portfolio cross-ref

- **Registry id:** `ai-proposals-agent`
- **Repo / path:** https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude — `ai-proposals-agent/`
- **Branch:** `main`

## Gaps [TBD]

- Live deploy URL
- Pilot customer identity
