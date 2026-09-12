# Output schema — Revenue Intel Agent — v5.0

Canonical contract is in `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` under `<output_contract>`.

## Modes

| Mode | Delimiters | When |
|------|------------|------|
| JSON | `===JSON_START===` … `===JSON_END===` | Required if CSV or SheetsSpec requested |
| ExecutiveBriefMD | `===BRIEF_MD_START===` … | Default |
| SummaryEmail | `===EMAIL_START===` … | Opt-in |
| CSV | `===CSV_START===` … | Opt-in |
| SheetsSpec | `===SHEETS_SPEC_START===` … | Opt-in |

## Core objects

- `run_meta` — `today`, `niche`, `icp`, `notes`
- `source_ledger` — dated sources with credibility scores
- `opportunities[]` — sorted by `priority_score`; `status` Validated | Hypothesis
- `rejected[]` — mandatory when ideas fail gates (zero-result runs still succeed)

## Optional HUNTER CRM mapping (Freeman internal)

When feeding **HUNTER — Revenue Intelligence OS** (operator base only):

| v5 field | HUNTER column (suggested) |
|----------|---------------------------|
| `headline` | Opportunity title / Notes headline |
| `why_now` | Evidence |
| `status` + `confidence` | Notes tags |
| `owner_role` | Notes / Next Action owner |
| `example_calc.gross_profit` | Notes (deal size signal) |
| `priority_score` | Inform Tier (manual — no auto-equate) |

Do not ship pre-researched intel rows in the **customer** HUNTER template ZIP.
