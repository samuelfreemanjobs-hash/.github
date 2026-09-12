# AI Proposals Agent™

**Date:** 2026-09-12  |  **Urgency:** HIGH  |  **Progress:** 45%

---

## Scope

B2B single-agent SaaS for logistics BD teams: RFP intake, requirement extraction, deterministic pricing and compliance, narrative generation, exportable proposal bundles. Built in `-build-ai-agents-with-claude/ai-proposals-agent/` with factory spec and golden tests.

---

## Proposed Outcome

One paying pilot or three LOI pilots on Professional tier; full golden runs green; staging deploy live.

**For:** Logistics BD / solutions teams (Detroit corridor ICP).

---

## Opportunity Value

$497–$2,497/mo tiers in spec; anchor revenue SKU for Freeman agent suite.

---

## ✅ Done

- [x] Factory spec validated
- [x] Scaffold tree + skills + backend
- [x] Golden test runner — component logic green
- [x] Frontend + UI present
- [x] Deployment guide drafted
- [x] Pricing tiers in YAML spec
- [x] Skills pack (5 skills)
- [x] Deterministic modules in progress
- [x] README + verify command

---

## ☐ To Do

- [ ] Configure KB for full golden fixtures
- [ ] End-to-end golden run green
- [ ] Staging deploy
- [ ] Pilot customer dogfood (intake → export)
- [ ] Production deploy + monitoring
- [ ] Sales one-pager + demo Loom
- [ ] Stripe billing wired
- [ ] First paying customer
- [ ] Onboarding checklist for Professional tier
- [ ] HALT/runbook for support

---

## Stack

- Python deterministic core, agent + skills
- React/UI, Railway/deploy per docs
- `saas-factory/products/ai-proposals-agent.yaml`

---

## Artifacts

| Artifact | Path / Link | Status |
|----------|-------------|--------|
| Product spec | saas-factory/products/ai-proposals-agent.yaml | Complete |
| Golden tests | ai-proposals-agent/scripts/run_golden_tests.py | Partial |
| Deploy guide | ai-proposals-agent/docs/deployment-guide.md | Draft |

---

## AI Agents Created

- AI Proposals Agent™ — RFP → proposal with traced numerics

---

## Alternative Uses / Re-Niching

- Other vertical RFPs beyond logistics (new spec via SaaS Factory)
- Bundle with Software Developer / Architect agents

---

## API Keys Needed

- LLM provider keys for agent runtime
- Deploy host secrets (Railway/etc.)
- [TBD] Stripe

---

## Notes

- Registry: `ai-proposals-agent`
- Fail-closed pricing/compliance per factory hard_rules
- [TBD] Pilot account name

---

*Freeman · project.md — updated 2026-09-12*
