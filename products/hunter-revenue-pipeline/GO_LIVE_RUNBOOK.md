# HUNTER — Revenue Pipeline System · Go-Live Runbook

**Product:** HUNTER Intelligence OS (aka **Revenue Pipeline System**)  
**Repo branch:** `cursor/autonomous-hunter-os-54da` (launch prep: `cursor/hunter-launch-prep-c763`)  
**Last verified:** 2026-09-12 — `npm run health` passes on local JSON storage with 10 seeded leads.

---

## What “launched” means

| Criterion | Target |
|-----------|--------|
| Public API + landing | `PUBLIC_URL` serves `/` and `/api/health` returns 200 |
| Pipeline loaded | ≥10 scored leads in CRM (seed or n8n) |
| Booking | `BOOKING_URL` set on landing + outreach |
| First outreach | ≥5 emails sent (manual or Resend batch) |
| Automation | n8n discovery workflow **active** OR daily manual discovery |
| Revenue signal | ≥1 diagnostic call booked **or** ≥1 proposal sent |

Code-complete alone is not launch. Track outcomes in `frontend/operator.html`.

---

## Phase 0 — Local smoke (15 min, no keys)

```bash
npm ci
cp .env.example .env   # keys optional for smoke test
npm start              # or: npm run setup
npm run seed
npm run health
```

Open:

| Screen | URL |
|--------|-----|
| Landing | http://localhost:3001/ |
| Operator | http://localhost:3001/operator.html |
| CRM | http://localhost:3001/hunter_crm.html |

---

## Phase 1 — Production database (Supabase)

1. Create a Supabase project.
2. In **SQL Editor**, run in order:
   - `supabase/migration-full.sql`
   - `supabase/migration-v3-outreach.sql` (Resend webhook / engagement columns)
3. Copy **Project URL** + **anon public** key (starts with `eyJ…`) into `.env`:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
4. Restart the app. `/api/health` should show Supabase storage.

> **Note:** Local `data/*.json` does not auto-sync to Supabase. After switching, run `npm run seed` once against production or import via n8n.

---

## Phase 2 — Deploy backend (Railway / Render / Docker)

### Railway (recommended)

1. New project → deploy from GitHub branch `cursor/hunter-launch-prep-c763` (or merge to `main`).
2. Set all variables from `.env.example`.
3. `railway.json` configures Docker build + `/api/health` healthcheck.

### Docker

```bash
docker compose up -d --build
```

Required env vars at minimum for production pipeline:

| Variable | Purpose |
|----------|---------|
| `SUPABASE_URL`, `SUPABASE_ANON_KEY` | Persistent CRM |
| `GEMINI_API_KEY` | Live scoring, proposals, diagnostics |
| `RESEND_API_KEY`, `RESEND_FROM` | Outreach |
| `BOOKING_URL` | Diagnostic booking CTA |
| `PUBLIC_URL` | Links in emails and webhooks |
| `SLACK_WEBHOOK` | HOT lead alerts (optional) |
| `SPARK_WEBHOOK_SECRET` | Gemini Spark import (optional) |

---

## Phase 3 — Email & domain (Resend)

1. Verify sending domain in Resend.
2. Set `RESEND_FROM=HUNTER Intelligence <you@yourdomain.com>`.
3. Configure Resend webhook → `POST {PUBLIC_URL}/api/webhooks/resend`  
   See `docs/RESEND_WEBHOOK.md`.

---

## Phase 4 — Automation (n8n)

1. Import `n8n/hunter-lead-discovery.json` and `n8n/hunter-follow-up-sequence.json`.
2. Set `hunterApiUrl` to `{PUBLIC_URL}/api`.
3. Add Apify token + Slack webhook in the Config node.
4. Activate daily schedule (6 AM) or run manual test.

Details: `n8n/README.md`.

---

## Phase 5 — GTM (day 1 revenue actions)

1. **LinkedIn** — post `content/linkedin-post-001.md` (Tue 7 AM ET suggested).
2. **Outreach** — send HOT lead first (Great Lakes Aerospace) from `content/outreach-batch-001.md`.
3. **CRM** — move stages as replies arrive; use `/api/outreach/batch` with `dryRun: true` before live batch.
4. **Operator** — daily briefing at `GET /api/operator/daily`.

30-day checklist: `business/LAUNCH_CHECKLIST.md`.

---

## Phase 6 — Optional: Gemini Spark feed

Webhook: `POST {PUBLIC_URL}/api/webhooks/spark` with `SPARK_WEBHOOK_SECRET`.  
See `docs/SPARK_WEBHOOK.md`. Nightly JSON drops in `data/gemini-spark-import-*.json` can be replayed with `npm run import-spark`.

---

## Verification commands

```bash
npm run health                    # API + core routes
npm run verify-launch             # Static assets, n8n JSON, migrations documented
curl -s $PUBLIC_URL/api/health | jq .
```

---

## Rollback

- **App:** Redeploy previous Railway release or `docker compose` previous image.
- **Data:** Supabase point-in-time recovery (if enabled) or export leads via `GET /api/leads`.
- **Automation:** Deactivate n8n workflows (discovery stops; CRM data remains).

---

## Support files

| Doc | Use |
|-----|-----|
| `LAUNCH_STATUS.md` | Checklist snapshot |
| `business/PRICING.md` | Service catalog alignment |
| `business/OPERATOR_PLAYBOOK.md` | Daily operator rhythm |
| `README.md` | Architecture + API index |
