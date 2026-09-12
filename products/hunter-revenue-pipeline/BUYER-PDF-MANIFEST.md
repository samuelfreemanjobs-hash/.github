# What should be PDF for Etsy buyers?

Etsy customers often **never open `.md`** or run Node on day one. Ship **read-first PDFs** plus the **full app ZIP** for implementation.

## Included in buyer ZIP (`00-PDF-Guides/`)

| PDF | Source | Why PDF |
|-----|--------|--------|
| `00-PDF-Only-Path.pdf` | `buyer-guides/PDF-ONLY-PATH.md` | **No install** — outreach today |
| `01-Quick-Start.pdf` | `START_HERE.md` + video link | Install path; links to walkthrough |
| `02-Install-Node-Mac-Windows.pdf` | `buyer-guides/INSTALL-NODE-*.md` | Mac/Windows Node with screenshots |
| `03-Buyer-FAQ-and-License.pdf` | FAQ + license | Policy + support |
| `04-Outreach-Batch-1.pdf` | `content/outreach-batch-001.md` | Copy/paste emails without CRM |
| `05`–`08` Give-Before-Ask | HTML frameworks | Email attachments ranks 1–4 |
| `09-LinkedIn-Post-1.pdf` | `content/linkedin-post-001.md` | Optional social |

Walkthrough video: seller uploads `buyer-guides/WALKTHROUGH-SOURCE.mp4` unlisted, sets `VIDEO_URL` in `WALKTHROUGH-VIDEO.txt`, rebuilds ZIP (link in `01-Quick-Start.pdf` + `WALKTHROUGH-VIDEO.txt` in ZIP root). **Do not** bundle the `.mp4` in the Etsy ZIP.

## Stays **not** PDF (editable / runnable)

| Format | Items |
|--------|--------|
| **Code** | `server.js`, `lib/`, `frontend/`, `n8n/` |
| **Data** | `data/seed-leads.json` (CRM import) |
| **Legal templates** | `templates/*.md` (buyers edit in Word/Google Docs) |
| **Deep technical** | `GO_LIVE_RUNBOOK.md`, Supabase SQL |

## Regenerate PDFs

```bash
npm run build-buyer-pdfs    # writes etsy-digital-product/pdf-exports/
npm run build-etsy          # bundles pdf-exports → ZIP folder 00-PDF-Guides/
```

Seller Canva art is separate: `listing-creative/` (shop photos only).
