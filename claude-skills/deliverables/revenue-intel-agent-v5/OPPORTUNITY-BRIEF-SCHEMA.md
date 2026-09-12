# Opportunity brief schema — Revenue Intel → HUNTER

Use this when pasting intel into **HUNTER — Revenue Intelligence OS** (internal operator base).

## HUNTER field mapping (suggested)

| Intel field | HUNTER / Opportunities column |
|-------------|-------------------------------|
| `company` | Company Name |
| `site` | Notes (lead with “Site: …”) |
| `vertical` | Industry |
| `title` | Opportunity Title or Notes headline |
| `pain_summary` + evidence | Evidence / Notes |
| `hunter_tier` | Tier |
| `outreach_strategy` | Outreach Strategy (A–F) |
| `suggested_service_name` | Match row in Service Catalog |
| `confidence` | Notes tag `[confidence: medium]` |

## JSON object (canonical)

See `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` for the full `opportunities[]` shape.

## Internal-only rule

**Do not** ship Freeman prospect names, live intel rows, or Metro Detroit target lists inside the **customer** HUNTER template ZIP. Buyers start from fictional examples (`EXAMPLE-OPPORTUNITIES.md` in HUNTER kit).

Operator workflow:

1. Run Revenue Intel Agent on a target.  
2. Human-verify `seller_action` items.  
3. Create/update row in **internal** HUNTER base.  
4. Run HUNTER Claude scoring prompt on the row before outreach.
