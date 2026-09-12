# MOCKUP-SPEC.md — Revenue Pipeline System (HUNTER CRM)

**Product:** Revenue Pipeline System (HUNTER CRM) · Consultant edition · $97  
**Channels:** Etsy (primary visuals) · Gumroad (reuse same 5 assets)  
**Copy source (Architect v4):** `ETSY-COPY-ARCHITECT-V4.md` · `ARCHITECT-BRIEF-RPS.md`  
**Canva execution:** `CANVA-DESIGN-PROMPTS.md` (AI prompts duplicate below for one-file handoff)

**Designer role:** Senior product / Etsy listing designer — flat B2B, no stock handshake, no income claims, no fake reviews.

---

## 1. Deliverables checklist

| Asset | Size | Format | Filename |
|-------|------|--------|----------|
| Listing image 1 (hero) | 2000 × 2000 | PNG | `rps-etsy-01-hero.png` |
| Listing image 2 (HOT view) | 2000 × 2000 | PNG | `rps-etsy-02-hot-view.png` |
| Listing image 3 (rubric) | 2000 × 2000 | PNG | `rps-etsy-03-rubric.png` |
| Listing image 4 (Claude) | 2000 × 2000 | PNG | `rps-etsy-04-claude.png` |
| Listing image 5 (included) | 2000 × 2000 | PNG | `rps-etsy-05-included.png` |
| Shop banner (optional) | 3360 × 840 | PNG | `rps-etsy-shop-banner.png` |
| Gumroad cover (optional crop) | 1280 × 720 | PNG | `rps-gumroad-cover.png` (crop from hero) |

**Etsy upload order:** 1 → 2 → 3 → 4 → 5 (image 1 = search thumbnail).

---

## 2. Brand kit (lock before layout)

| Token | Hex | Usage |
|-------|-----|--------|
| Navy | `#0F172A` | Hero bg, callout boxes, headlines on light slides |
| White | `#FFFFFF` | Type on navy, card surfaces |
| Amber | `#D97706` | HOT tier, accent bars, checkmarks, primary CTA strip |
| Slate | `#64748B` | Subheads, secondary type |
| Light | `#F8FAFC` | Screenshot slide backgrounds |
| Grid border | `#E2E8F0` | UI mock frames |

**Typography**

| Role | Font | Weight | Size guide (2000px canvas) |
|------|------|--------|----------------------------|
| Headline | Inter or DM Sans | Bold | 72–96 px (hero); 56–72 px (inner slides) |
| Subhead | Inter or DM Sans | Medium | 32–40 px |
| Body / bullets | Inter or DM Sans | Regular | 24–28 px |
| Footer / legal | Inter or DM Sans | Regular | 18–22 px |

**Logo:** Freeman Intelligence wordmark if available; else text footer only.

**Forbidden:** 3D coins, rockets, “10X”, star ratings, testimonial quotes without `[PROOF NEEDED]`, handshake stock.

---

## 3. Safe zones & legibility

- **Etsy thumbnail:** Assume **~300 × 300** preview — headline must read at that size (test export scaled down).
- **Margins:** 120 px minimum inset on 2000 × 2000.
- **Contrast:** White on navy ≥ WCAG AA; amber pills use **white** label text.

---

## 4. Frame-by-frame spec

### Image 1 — Hero (thumbnail)

**Purpose:** Search click-through; 8-word spine + product name (readable at ~300px).

**Layout**

- Background: solid navy `#0F172A`.
- Right 40%: abstract pipeline — 4 thin horizontal lines (opacity 30%), amber dots on line ends (HOT metaphor).
- Left 55%: type stack.

**Copy (Architect v4 — use this set)**

| Zone | Text |
|------|------|
| Headline | Know who's HOT before Monday. |
| Product line | Revenue Pipeline System |
| Subline | (HUNTER CRM) · Airtable + Claude |
| Bullets | 100-pt score · 7 dimensions · ~45 min setup |
| Footer | Consultant edition · Instant digital download |
| Accent | 4 px amber bar under headline |

**Canva AI prompt**

```
Minimal professional B2B digital product cover, square 2000x2000, dark navy background #0F172A, abstract subtle pipeline funnel made of thin horizontal lines, small amber highlight dots, no people, no 3D coins, clean corporate tech aesthetic, lots of negative space for typography, flat design
```

---

### Image 2 — HOT view (product proof)

**Purpose:** Show the actual workflow (grid + tier).

**Layout**

- Light bg `#F8FAFC`.
- Center: browser-style frame (12 px radius, shadow 8% black).
- Inside: table mock **or** real screenshot from sanitized Airtable duplicate.

**Table columns (visible)**  
Company · Total Score · Tier · Stage

**Sample rows (fictional only)**

| Company | Score | Tier |
|---------|-------|------|
| Northline Ops Group | 90 | HOT |
| Meridian Brand Studio | 76 | HIGH |
| Harborview Legal Tech | 48 | WATCH |

**Tier pills:** HOT = amber fill `#D97706` white text; HIGH = navy outline; WATCH = slate gray.

**Overlay copy (below or above frame)**

| Zone | Text |
|------|------|
| Headline | See who's HOT before you outreach |
| Subhead | Opportunities · auto-scored 0–100 |
| Micro | Demo data · not a guarantee |

**Canva AI prompt**

```
Clean UI mockup of a spreadsheet CRM dashboard on light gray background, columns for company name lead score and tier badges, professional SaaS screenshot style, fictional company names, navy and amber accent colors, no real logos, flat browser window frame
```

**Preferred:** Replace AI mock with **real screenshot** from template after Sam duplicates base.

---

### Image 3 — Seven dimensions (differentiation)

**Purpose:** Explain rubric vs generic “CRM template”.

**Layout:** White canvas; navy header band full width; 7 rows with label left, max points right, thin amber tick (decorative).

**Copy**

| Zone | Text |
|------|------|
| Headline | 7-dimension scoring rubric |
| Subhead | Evidence only — no invented facts |
| Rows | Problem Severity 25 · Buying Signal 20 · Ability to Pay 15 · Service Fit 15 · Accessibility 10 · Urgency 10 · Competitive Pressure 5 |
| Footer | HOT ≥90 · HIGH ≥75 · MEDIUM ≥60 |

**Canva AI prompt**

```
Infographic slide seven horizontal rows scoring criteria for B2B sales leads, minimal corporate style, navy headers white background amber accent lines, no photographs, typography focused layout
```

---

### Image 4 — Claude workflow

**Purpose:** AI-search buyers; show paste-in → scores-out.

**Layout:** 50/50 split; left “Research in” gray box with bullets; right score mini-table; amber badge **HIGH 78**.

**Copy**

| Zone | Text |
|------|------|
| Headline | Paste research → get tier + scores |
| Subhead | CLAUDE-SCORING-PROMPT included (.md + .txt) |
| Badge | Example output — not a guarantee |

**Canva AI prompt**

```
Split screen before and after layout for AI business workflow, left side messy bullet research notes right side clean score table, professional B2B presentation slide, navy and white color scheme amber tier badge HIGH 78
```

---

### Image 5 — What's included (purchase confidence)

**Purpose:** Reduce “what am I buying?” messages.

**Layout:** Soft gray bg; stacked doc icons (PDF, TXT, MD); navy callout box bottom or top.

**Copy**

| Zone | Text |
|------|------|
| Headline | What's in your download |
| Checklist | Setup Guide PDF · Quick Start PDF · Scoring prompt · Outreach templates · FAQ · Example catalog & leads |
| Callout (navy box, white type) | Airtable copy link inside Setup Guide (page 1) |

**Canva AI prompt**

```
Flat lay digital product bundle icons PDF documents and text files on soft gray background, checklist aesthetic, professional Etsy digital download product image, navy typography space at top
```

---

### Shop banner (3360 × 840)

**Copy:** Freeman Intelligence digital tools · B2B pipelines · Airtable templates · Claude prompts  
**Visual:** Navy bg, subtle grid, amber hairline rule; leave center clear for Etsy shop name if overlaid in UI.

**Canva AI prompt**

```
Wide Etsy shop banner, navy background, subtle grid pattern, professional B2B consulting aesthetic, amber thin line accent, empty center for shop name overlay
```

---

## 5. Gumroad reuse

- **Cover:** Crop hero (Image 1) to 16:9; keep headline in upper third.
- **Gallery:** Same 5 PNGs as Etsy.

---

## 6. QA before ship

- [ ] Thumbnail readable at 300 px width  
- [ ] No typos in HOT/HIGH/MEDIUM/WATCH  
- [ ] No income or results guarantees  
- [ ] Fictional company names only on Image 2  
- [ ] File size each &lt; 5 MB (Etsy limit per image)  
- [ ] sRGB color profile  

---

## 7. Handoff to listing ops

| Step | Owner |
|------|--------|
| Upload PNGs to Etsy in order 1–5 | Sam |
| Paste copy from `ETSY-COPY-ARCHITECT-V4.md` or `ETSY-PRODUCT-COPY.md` | Sam |
| Attach ZIP `Revenue-Pipeline-System-HUNTER-CRM-v1-consultant.zip` | Sam |
| Airtable URL **only** in Setup PDF + buyer message | Sam |

---

## 8. Revision log

| Date | Change |
|------|--------|
| 2026-09-12 | v1 — Architect hero headline; 5-frame Etsy set + banner |
| 2026-09-12 | v1.1 — Hero = 8-word spine; bullets = spec facts |

**Rule for all Freeman digital SKUs:** Create **`MOCKUP-SPEC.md`** alongside copy whenever listing visuals are in scope.
