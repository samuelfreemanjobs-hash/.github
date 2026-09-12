# Airtable views to create (customer template)

Create these in the **duplicated template** so buyers open a polished base. Takes ~15 minutes.

## Opportunities

| View name | Type | Config |
|-----------|------|--------|
| **All opportunities** | Grid | Default; show Company, Tier, Total Score, Stage, Last Activity |
| **HOT + HIGH** | Grid | Filter: Tier contains `HOT` OR `HIGH` · Sort: Total Score desc |
| **Needs score** | Grid | Filter: Total Score is empty |
| **By stage** | Kanban | Stack by **Stage** (if Kanban available) |
| **Stale — 14d+** | Grid | Filter: Last Activity is before 14 days ago (or empty) |

## Service Catalog

| View name | Type | Config |
|-----------|------|--------|
| **All services** | Grid | Service Name, Typical Price Range, Target Verticals |

## Outreach Log

| View name | Type | Config |
|-----------|------|--------|
| **All outreach** | Grid | Sent Date desc |
| **Awaiting response** | Grid | Filter: Response Status = Awaiting |
| **This week** | Grid | Filter: Sent Date is within past 7 days |

## Optional (nice)

- **Opportunities · Group by Tier** — group by Tier field  
- Hide wide text fields (Notes, Evidence) in HOT+HIGH view for scanability  

Document in Setup Guide: “If views are missing, recreate from `VIEWS-TO-CREATE.md`.”

**Sam:** Build these once in your template duplicate before generating the share link.
