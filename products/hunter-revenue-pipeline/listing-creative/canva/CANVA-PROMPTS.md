# Canva prompts — Revenue Pipeline System (Etsy listing images)

**Seller only** — do **not** include this folder in `npm run build-etsy` (buyers get the ZIP, not your shop art).

## Where files live

| Purpose | Path (monorepo) | Path (.github launch hub) |
|---------|-------------------|---------------------------|
| Canva text prompts (this file) | `etsy-digital-product/listing-creative/canva/CANVA-PROMPTS.md` | `products/hunter-revenue-pipeline/listing-creative/canva/CANVA-PROMPTS.md` |
| Exported PNG/JPG (you create) | `etsy-digital-product/listing-creative/exports/` | same under `products/.../exports/` |
| Etsy copy | `etsy-digital-product/ETSY-LISTING.md` | `products/hunter-revenue-pipeline/` docs |

**Workflow:** Paste each prompt into **Canva → Magic Media / Text to Image** (or **Docs → Magic Write** for layout copy), export **2000×2000 px** (Etsy recommends square), save to `listing-creative/exports/`, upload to Etsy listing (5 images).

**Brand:** Revenue Pipeline System · colors: navy `#0a0e17`, blue accent `#3b82f6`, white text. No legacy codenames.

---

## Image 1 — Hero (thumbnail)

**Filename:** `01-hero-instant-download.png`

**Canva prompt:**

```
Square Etsy product thumbnail, modern dark navy tech aesthetic, bold headline text "Revenue Pipeline System", subline "Instant Digital Download", small icons for CRM pipeline, email, and dashboard, professional B2B consultant kit style, clean sans-serif typography, blue gradient accent, high contrast, no mockup laptop clutter, marketplace-ready
```

**Text overlay (if designing manually):**  
Revenue Pipeline System · CRM + Outreach · Instant Download

---

## Image 2 — What’s included

**Filename:** `02-whats-included-checklist.png`

**Canva prompt:**

```
Square infographic checklist on dark background, title "What's Inside the ZIP", six bullet items with checkmarks: CRM Dashboard, 10 Outreach Emails, Landing Page, 4 PDF Frameworks, n8n Automation JSON, START_HERE Guide, minimalist B2B SaaS marketing style, blue and white, readable at small size
```

---

## Image 3 — CRM screenshot style

**Filename:** `03-crm-pipeline-mockup.png`

**Canva prompt:**

```
UI mockup of a kanban sales CRM pipeline board, columns New Opportunity Outreach Sent Meeting Booked, dark mode interface, manufacturing B2B lead cards, professional software screenshot style, subtle browser frame, title banner "Pipeline CRM Included", not a real brand logo
```

*Tip:* For authenticity, screenshot `http://localhost:3001/hunter_crm.html` after `npm run seed` and drop into Canva as **Image 3** instead of AI-only.

---

## Image 4 — White-label

**Filename:** `04-white-label-your-brand.png`

**Canva prompt:**

```
Square marketing graphic, split before-after concept, left gray label "Generic", right vibrant "Your Brand", center arrow, headline "White-Label for Consultants", subtext "Set your name on emails, landing page, and templates", dark navy B2B style, trustworthy and simple
```

---

## Image 5 — Not physical / license

**Filename:** `05-digital-download-notice.png`

**Canva prompt:**

```
Square Etsy policy-style graphic, large icon digital download cloud with ZIP file, bold text "NOT A PHYSICAL ITEM", smaller text "Personal use license · No resale of files", clean navy and blue, reassuring professional design for digital product listing
```

---

## Optional — Shop banner (not a listing image)

**Canva prompt:**

```
Wide Etsy shop banner, Revenue Pipeline Systems for Consultants, digital download kits, dark tech aesthetic, blue accents, minimal text, 3360 x 840 px
```

---

## After export

1. Save PNGs to `listing-creative/exports/`
2. Etsy → Listing → Photos → upload images 1–5 in order above
3. Image 1 = thumbnail (most important for search scroll)

---

## Align with your other kits

Same pattern as **Agent 10 — Listing Mockup & Photo Brief** on `push` (`01-playbook` + optional Canva). This SKU keeps prompts next to `ETSY-LISTING.md` under `etsy-digital-product/listing-creative/` because the product ships from the monorepo, not `ai-agent-team/products/`.
