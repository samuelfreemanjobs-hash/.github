# Sample run — Revenue Intel Agent — v5.1 (fictional)

This example matches `fixtures/valid-sample-run.json` and passes `scripts/validate_run.py`.

## Executive brief excerpt

===BRIEF_MD_START===

# Weekly Revenue Brief — Automotive tier-2 stamping suppliers / Fractional ops consultant — 2026-09-12

## Bottom line

One **Validated** opportunity: OTIF reporting still lives in spreadsheets for many tier-2 stampers while OEM enforcement is documented in 2026 trade press. A single dashboard sprint is modeled at **$31,500** 90-day gross profit (conservative inputs). No other candidates cleared Evidence this week.

## Pick of the week

**OTIF reporting spreadsheet elimination for tier-2 stamper**

- Dated external pressure: 2026-03-15 trade coverage on OTIF enforcement into contract cycles.
- Fits catalog offer: KPI Command Center & Executive Dashboard Sprint.

## What I rejected and why

**Generic AI chatbot for plant floor** — vendor-only evidence; failed Evidence and Bias gates.

## Sources

- Sample OEM supplier quality manual excerpt • Fictional OEM • 2025-11-01 • primary
- Industry week — OTIF pressure on stampers • Fictional Trade Press • 2026-03-15 • secondary
- Michigan manufacturing employment report • Fictional State Agency • 2026-06-01 • primary

===BRIEF_MD_END===

## JSON

Full payload: `../fixtures/valid-sample-run.json`

Validate:

```bash
python3 ../scripts/validate_run.py ../fixtures/valid-sample-run.json
```
