# Operator license kit (summary)

Full kit lives in the monorepo at **`operator-license-kit/`** after you apply  
`product-management/patches/hunter-launch-prep-c763.patch`.

## Build the customer zip

```bash
npm run build-operator-kit
# → dist/hunter-operator-license-kit-YYYYMMDD.zip
```

## Zip contains (high level)

| Folder | Purpose |
|--------|---------|
| `server.js`, `lib/`, `frontend/` | Pipeline runtime |
| `data/seed-leads.json` | Unified 10-lead CRM seed |
| `content/gtm/manifest.yaml` | Send order + PDF map |
| `content/give-before-ask/` | Ranks 1–4 PDF sources |
| `n8n/` | Discovery + follow-up |
| `business/`, `templates/`, `prompts/` | Delivery + GTM |
| `operator-license-kit/` | White-label + handoff docs |

## White-label essentials

Set in `.env`: `OPERATOR_BRAND`, `RESEND_FROM`, `BOOKING_URL`, `PUBLIC_URL`.

Edit checklist: `operator-license-kit/WHITE_LABEL.md`.

## Unified marketing (no more split batches)

One list: **4 HOT leads with PDF attachments** + **6 HIGH/HOT email-only** — all in `data/seed-leads.json`.  
`content/outreach-batch-001.md` is the human-readable index.
