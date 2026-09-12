# Build your Airtable template (10–15 minutes)

Use this if you do **not** yet have a share link. Two paths:

---

## Path A — Recommended: Duplicate full HUNTER base (formulas included)

You already have a complete base: **HUNTER — Revenue Intelligence OS** (`appfxMz1jb2MAO15G`).

1. Open https://airtable.com/appfxMz1jb2MAO15G  
2. Click **▼** next to base name → **Duplicate base**  
3. Rename duplicate: **Revenue Pipeline System (HUNTER CRM) — Template**  
4. In duplicate only:  
   - **Service Catalog:** replace rows using `airtable-import/service-catalog.csv` (import or paste)  
   - **Opportunities:** import `airtable-import/opportunities.csv`  
   - **Outreach Log:** clear or import `outreach-log.csv`  
   - Adjust **Industry** select options per `TEMPLATE-CUSTOMIZATION.md`  
   - Add views from `VIEWS-TO-CREATE.md`  
5. **Share** duplicate → **Allow copying** → copy link → paste into `SETUP-GUIDE` as `{TEMPLATE_LINK}`  

Keep your **original** HUNTER base for internal industrial work. If Service Catalog row 1 was edited during setup, restore from `INDUSTRIAL-SERVICE-CATALOG-BACKUP.md`.

---

## Path B — CSV import into a new empty base

1. Airtable → **Create** → **Start from scratch** → name **Revenue Pipeline System (Template)**  
2. Create table **Service Catalog** → **Import CSV** → `airtable-import/service-catalog.csv`  
3. Create table **Opportunities** → import `opportunities.csv`  
4. Add fields from `AIRTABLE-FIELD-SPEC.md` (numbers, selects, formulas)  
5. Paste formulas from `AIRTABLE-FORMULAS.md`  
6. Create **Outreach Log** + link fields (see field spec)  
7. Share → allow copying  

Path B takes longer; Path A is faster if HUNTER duplicate is available.

---

## Partial base already created (optional)

Tables were started in **Business Idea Tracker** (`appwaEPUOCXBoq8jB`): **Service Catalog**, **Opportunities**, **Outreach Log** (primary fields only). You can delete these tables or ignore them and use Path A instead.

---

## Buyer link format

After share is enabled:

```text
https://airtable.com/appXXXXXXXXXXXXXX
```

Buyers click **Copy base**. Put that URL in Gumroad receipt + Setup Guide page 1.
