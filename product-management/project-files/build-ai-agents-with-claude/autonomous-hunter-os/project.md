# HUNTER Intelligence OS (Revenue Pipeline System)

**Date:** 2026-09-12  |  **Urgency:** HIGH  |  **Progress:** 85%

---

## Scope

End-to-end revenue pipeline for solo operators selling operational intelligence to mid-market manufacturers: lead discovery (n8n + Apify), AI scoring, CRM, outreach (Resend), proposals/diagnostics (Gemini), operator dashboard, and business metrics. Node/Express monolith with Supabase persistence and static operator UIs.

---

## Proposed Outcome

Production deployment with live pipeline (10+ leads), booking link on landing, first outreach batch sent, and n8n discovery running daily. **Launched** = ≥1 diagnostic booked or ≥1 proposal sent.

**For:** Samuel Freeman / HUNTER Intelligence GTM

---

## Opportunity Value

Catalog services $18K–$45K per engagement; retainer $4.5K/mo. Target $25K collected in first 30 days (`business/LAUNCH_CHECKLIST.md` in repo).

---

## ✅ Done

- [x] Full API: leads, scoring, outreach, proposals, diagnostics, business metrics
- [x] CRM + operator + landing frontends
- [x] n8n discovery + follow-up workflows
- [x] Seed data + outreach/LinkedIn content
- [x] Docker/Railway deploy config
- [x] Go-live runbook, CI, verify-launch script (2026-09-12)

---

## ☐ To Do

- [ ] Apply launch patch to monorepo (see `product-management/patches/hunter-launch-prep-c763.patch`)
- [ ] Push branch `cursor/hunter-launch-prep-c763` and deploy Railway
- [ ] Supabase migrations + production env vars
- [ ] Resend domain + `BOOKING_URL`
- [ ] Activate n8n + first 5 outreach emails

---

## Stack

Node 20 · Express · Supabase · Gemini · Resend · n8n · Apify

---

## Artifacts

| Artifact | Location |
|----------|----------|
| Go-live runbook | `GO_LIVE_RUNBOOK.md` in monorepo |
| Launch hub (this org) | `products/hunter-revenue-pipeline/README.md` |
| Launch patch | `product-management/patches/hunter-launch-prep-c763.patch` |

---

## Repo

`github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude`  
Base: `cursor/autonomous-hunter-os-54da` → Launch prep: `cursor/hunter-launch-prep-c763`
