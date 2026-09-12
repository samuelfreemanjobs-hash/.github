# What should be PDF for Etsy buyers?

Etsy customers often **never open `.md`** or run Node on day one. Ship **read-first PDFs** plus the **full app ZIP** for implementation.

## Included in buyer ZIP (`00-PDF-Guides/`)

| PDF | Source | Why PDF |
|-----|--------|--------|
| `01-Quick-Start.pdf` | `START_HERE.md` | First file to open; no Markdown required |
| `02-Buyer-FAQ-and-License.pdf` | `BUYER-FAQ.md` + `DIGITAL-LICENSE.txt` | Policy + support in one printable doc |
| `03-Outreach-Batch-1.pdf` | `content/outreach-batch-001.md` | Copy/paste emails without CRM |
| `04-Give-Before-Ask-True-Industries.pdf` | HTML framework | Attach to email #1 |
| `05-Give-Before-Ask-Auto-Metal-Craft.pdf` | HTML | Email #2 |
| `06-Give-Before-Ask-Barron-Industries.pdf` | HTML | Email #3 |
| `07-Give-Before-Ask-Fitzpatrick.pdf` | HTML | Email #4 |
| `08-LinkedIn-Post-1.pdf` | `content/linkedin-post-001.md` | Optional paste-ready social |

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
