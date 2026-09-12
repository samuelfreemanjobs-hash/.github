# Launch Status — HUNTER Intelligence OS (Revenue Pipeline System)

Last updated: **2026-09-12**  
Branch: `cursor/hunter-launch-prep-c763`  
Automated check: `npm run verify-launch` + `npm run health` (with server running)

## Executive summary

| Area | Status |
|------|--------|
| Application code | ✅ Ready — API, CRM, operator, scoring fallbacks verified |
| Docker / Railway | ✅ Ready — Dockerfile includes static `content/` + seed data |
| CI | ✅ GitHub Actions — install, verify-launch, health + seed |
| Supabase schema | ✅ SQL ready — run `migration-full.sql` + `migration-v3-outreach.sql` |
| n8n workflows | ✅ JSON validated — import + configure Apify |
| GTM content | ✅ Outreach batch + LinkedIn post + give-before-ask assets |
| **Your blockers** | ⚠️ Supabase keys, Resend domain, `BOOKING_URL`, production deploy URL |

Full procedure: **[GO_LIVE_RUNBOOK.md](GO_LIVE_RUNBOOK.md)**

## Launch Checklist Progress

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | Set up Supabase | ⚠️ **Your action** | `migration-full.sql` then `migration-v3-outreach.sql` |
| 2 | Add API keys | ⚠️ **Your action** | Gemini, Resend, Slack, `BOOKING_URL`, `PUBLIC_URL` |
| 3 | Deploy | ✅ **Ready** | Railway (`railway.json`) or `docker compose up` |
| 4 | Import n8n workflows | ✅ **Ready** | Discovery + follow-up sequences |
| 5 | Seed 10 leads | ✅ **Done** | `npm run seed` / `POST /api/seed` |
| 6 | Outreach ready | ✅ **Done** | `content/outreach-batch-001.md` |
| 7 | LinkedIn post ready | ✅ **Done** | `content/linkedin-post-001.md` |
| 8 | Booking link | ⚠️ **Your action** | Cal.com / Calendly → `BOOKING_URL` |

## Verified locally (2026-09-12)

- ✅ `npm run health` — all 6 endpoint checks pass
- ✅ `npm run seed` — 10 manufacturing leads (incl. Great Lakes Aerospace HIGH)
- ✅ Local JSON storage when Supabase not configured

## What Needs Your Keys

| Key | Enables | Get it at |
|-----|---------|-----------|
| `SUPABASE_URL` + `SUPABASE_ANON_KEY` | Production database, multi-device sync | supabase.com |
| `GEMINI_API_KEY` | Live AI scoring, proposals, diagnostics | aistudio.google.com |
| `RESEND_API_KEY` | Email outreach sending | resend.com |
| `SLACK_WEBHOOK` | HOT lead + daily alerts | api.slack.com/messaging/webhooks |
| `BOOKING_URL` | Diagnostic call booking on landing page | cal.com or calendly.com |
| `PUBLIC_URL` | Production links + webhooks | Your Railway/Render URL |

## Quick Commands

```bash
npm run setup          # Full setup + seed + health check
npm start              # Start server
npm run seed           # Seed 10 leads
npm run health         # Validate all endpoints
npm run verify-launch  # Static pre-flight (no server)
```

## Revenue Actions (Do Today)

1. **Deploy** — follow Phase 2 in `GO_LIVE_RUNBOOK.md`
2. **Post LinkedIn** → `content/linkedin-post-001.md`
3. **Send HOT outreach** → Great Lakes Aerospace in `content/outreach-batch-001.md`
4. **Set booking URL** → `BOOKING_URL` in production env
5. **Import n8n** → activate daily discovery workflow

## System URLs (Local)

| Screen | URL |
|--------|-----|
| Landing | http://localhost:3001/ |
| Operator | http://localhost:3001/operator.html |
| CRM | http://localhost:3001/hunter_crm.html |
