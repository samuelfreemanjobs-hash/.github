# HUNTER on Etsy — digital product

## Build upload file

In the monorepo (after applying `hunter-launch-prep-c763` patch):

```bash
npm run build-etsy
```

Upload **`dist/hunter-revenue-pipeline-etsy-digital.zip`** to the Etsy listing (auto digital delivery).

## Seller docs (keep in repo — not inside buyer ZIP)

| File | Purpose |
|------|---------|
| `etsy-digital-product/ETSY-LISTING.md` | Title, description, tags |
| `etsy-digital-product/ETSY-KEYWORD-PASS.md` | SEO pass |
| `etsy-digital-product/SELLER-CHECKLIST.md` | Pre-launch |
| `etsy-digital-product/SELLER-CHECKLIST.md` | Post-build QA |

## Buyer gets

- `START_HERE.md` (root of ZIP)
- `DIGITAL-LICENSE.txt` — no resale / no re-listing on Etsy
- Full pipeline app + unified GTM (`data/seed-leads.json`)

## Wholesale

Custom operator deals: `npm run build-operator-kit` + `operator-license-kit/` (separate from Etsy SKU).
