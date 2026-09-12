# HUNTER — Revenue Pipeline System (launch hub)

**HUNTER Intelligence OS** is the autonomous revenue pipeline for mid-market manufacturing outreach: discovery → scoring → CRM → proposals → delivery metrics.

| Item | Location |
|------|----------|
| Portfolio `project.md` | [`product-management/project-files/build-ai-agents-with-claude/autonomous-hunter-os/project.md`](../product-management/project-files/build-ai-agents-with-claude/autonomous-hunter-os/project.md) |
| Registry entry | `autonomous-hunter-os` in [`product-management/REGISTRY.yaml`](../product-management/REGISTRY.yaml) |
| Go-live runbook (copy) | [`GO_LIVE_RUNBOOK.md`](GO_LIVE_RUNBOOK.md) |
| Monorepo launch patch | [`product-management/patches/hunter-launch-prep-c763.patch`](../product-management/patches/hunter-launch-prep-c763.patch) |

## Source repository

- **Repo:** [samuelfreemanjobs-hash/-build-ai-agents-with-claude](https://github.com/samuelfreemanjobs-hash/-build-ai-agents-with-claude)
- **Base branch:** `cursor/autonomous-hunter-os-54da`
- **Launch prep branch:** `cursor/hunter-launch-prep-c763`

## Apply launch prep to the monorepo

From a clone of `-build-ai-agents-with-claude` on `cursor/autonomous-hunter-os-54da`:

```bash
git checkout -b cursor/hunter-launch-prep-c763
git apply /path/to/product-management/patches/hunter-launch-prep-c763.patch
npm ci && npm run verify-launch
npm start & sleep 3 && npm run health && npm run seed
git add -A && git commit -m "Prepare HUNTER Revenue Pipeline System for launch"
git push -u origin cursor/hunter-launch-prep-c763
```

Or use the helper script in this repo:

```bash
./product-management/scripts/apply-hunter-launch-patch.sh /path/to/-build-ai-agents-with-claude
```

## Your launch blockers (cannot be automated here)

1. **Supabase** — run `migration-full.sql` + `migration-v3-outreach.sql`
2. **Railway/Render** — deploy with env from `.env.example`
3. **Resend** — verified domain + webhook to `/api/webhooks/resend`
4. **`BOOKING_URL`** — Cal.com / Calendly 15-min diagnostic
5. **n8n** — import workflows under `n8n/` and activate discovery

## Verified 2026-09-12

- `npm run health` — 6/6 API checks pass (local JSON storage)
- `npm run seed` — 10 scored manufacturing leads
- `npm run verify-launch` — static pre-flight passes

Follow **[GO_LIVE_RUNBOOK.md](GO_LIVE_RUNBOOK.md)** for phased production rollout.
