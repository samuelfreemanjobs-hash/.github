# Orchestrator guide — Revenue Intel Agent — v5.1

Humans or automation that **inject runtime context**, **store runs**, and **publish briefs**.

## Minimum loop

1. Generate `run_id` (UUID).
2. Load `prior_run_opportunities` from last N stored JSON payloads (headlines or `O*` ids).
3. Fill `RUNTIME-CONTEXT.example.yaml` → prepend as `<runtime_context>` to user message.
4. Set system prompt from `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md`.
5. Enable web search + fetch in the host (Claude, etc.).
6. Parse delimited outputs (`===JSON_START===`, `===BRIEF_MD_START===`, …).
7. **Validate before publish:**
   - Recompute `example_calc.gross_profit` from `inputs`.
   - Recompute `priority_score` from `score_breakdown` + weights.
   - Reject publish if any `Validated` row has `gate_results` ≠ all pass.
   - SHA-256 hash the JSON payload here (not in the model).

## Storage schema (suggested)

```
runs/{run_id}.json     # parsed JSON mode
runs/{run_id}.md       # ExecutiveBriefMD
runs/index.jsonl       # run_id, today, niche, icp, opportunity_ids
```

## HUNTER handoff

When `hunter_handoff: true`, map only `Validated` rows per `OPPORTUNITY-BRIEF-SCHEMA.md` into the **internal** HUNTER base.

## Cost control

- Default `output_modes: [ExecutiveBriefMD]` only.
- Lower `search_budget` for ad hoc; raise for new niches.
- Set `max_opportunities: 3` for cheaper weekly cadence.
