# Freeman PM Agent — commands (Claude / Cloud Agent)

**Base:** Freeman Intelligence — PM (`appUuhVQHAOv31wJ1`) · **Projects:** `tblRGiHqxz0K8Q0qi` · **Artifacts:** `tblUaFGrktRDqFyur`

Use these phrases in chat so any agent with Airtable (Zapier MCP or Airtable MCP) knows what to do.

## Read

| Command | Action |
|---------|--------|
| **PM BRIEFING** | List all **ACTIVE** projects: name, urgency, health, % complete, next action. Flag CRITICAL/HIGH first; note ON HOLD. Summarize blocked crawls (missing git URLs). |
| **PM STATUS:** *Project Name* | One project: scope, notes, stack, artifacts links, blockers. |
| **PM ARTIFACTS:** *Project Name* | All **Artifacts** rows linked to that project. |

## Write (confirm with Sam for urgency/health changes unless he asked for the update)

| Command | Action |
|---------|--------|
| **PM UPDATE:** *Project Name* — *field* = *value* | Update Projects row (Next Action, Notes, % Complete, etc.). |
| **PM ADD:** *Project Name* | Create project if missing (rare). |
| **PM ARTIFACT ADD:** *name* → *project* | New Artifacts row + link to project. |

## Latest briefing snapshot

**Generated:** 2026-09-12 (cloud agent sync)

| Urgency | Project | Health | % | Next action |
|---------|---------|--------|---|-------------|
| CRITICAL | Clinical Revenue Systems Engineering | RED | 20 | 5 secret-shopper calls (after 5pm) |
| HIGH | OIS — OpExcel (Automotive AI) | YELLOW | 25 | LinkedIn + 50-target prospect list |
| HIGH | Agent Ecosystem + Agents Explained Book | GREEN | 50 | Ch.6 + Linear in Cursor MCP |
| HIGH | Etsy Digital Agents Store | YELLOW | 40 | First 5 Etsy listings |
| HIGH | Freeman Copy Studio | GREEN | 65 | Dripify 20 connections/day |
| HIGH | PM Agent — Proactive Project Intelligence | YELLOW | 30 | PHASE 3: pm-agent-system-prompt |
| MEDIUM | Agent IP Registry | GREEN | 70 | Paste TheFreemanFix + Clinical git URLs |
| MEDIUM | HUNTER — Revenue Pipeline CRM | GREEN | 90 | List $97 product on Gumroad/Etsy |

**Portfolio:** 15 active-ish rows · **Revenue unlock (human):** Clinical calls > Copy outreach > Etsy listings > HUNTER $97 listing.

**Agent can advance without Sam:** hub/artifact docs, public repo crawl, Airtable Artifacts rows, PR on `claude-skills/`.

**Sam-only:** private repo URLs, sales calls, Etsy publish, legal/HIPAA sign-off, Dripify/Stripe live tweaks.

See also [AIRTABLE-ARTIFACTS.md](./AIRTABLE-ARTIFACTS.md) and [FREEMAN-WORKING-ARTIFACTS-AND-PRODUCTS.md](./FREEMAN-WORKING-ARTIFACTS-AND-PRODUCTS.md).
