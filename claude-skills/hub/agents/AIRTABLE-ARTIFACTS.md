# Airtable — Artifacts table

**Base:** Freeman Intelligence — PM (`appUuhVQHAOv31wJ1`)

| Table | ID |
|-------|-----|
| Projects | `tblRGiHqxz0K8Q0qi` |
| **Artifacts** | `tblUaFGrktRDqFyur` |

## Schema

| Field | Purpose |
|-------|---------|
| Artifact Name | Primary |
| Project | Link → Projects (inverse on Projects: **Artifacts**) |
| Artifact Type | Web app, Agent SaaS, HTML, Prompt pack, CRM, Framework, Manuscript, Repo, Spec |
| Artifact Status | SHIP / WORKING / PROTOTYPE / SPEC / DESIGN / WIP / ON HOLD |
| Productizable | Yes / Partial / Internal |
| Path or URL | GitHub or live URL |
| Repo path | In-repo path + crawl notes |
| Notes | |

## Repo crawl log (2026-09-12)

| Remote | Result |
|--------|--------|
| `-build-ai-agents-with-claude` | **Crawled** — 6 product dirs; 20 artifact rows seeded |
| `TheFreemanFix` | **Not found** on `samuelfreemanjobs-hash` (404) — placeholder rows from PM |
| Clinical / `rev-systems-os.html` | **Not found** on public GitHub — rows from PM stack |

Re-crawl when Sam provides clone URLs (private repo or org).

## Maintenance

- New shippable file → **Artifacts** row + link **Project**
- Quarterly sync with `FREEMAN-WORKING-ARTIFACTS-AND-PRODUCTS.md`
