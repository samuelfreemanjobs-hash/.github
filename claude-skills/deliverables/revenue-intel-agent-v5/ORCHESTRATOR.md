# Orchestrator guide — Revenue Intel Agent — v5.1

Humans or automation that **inject runtime context**, **store runs**, and **publish briefs**.

## Minimum loop

1. Generate `run_id` (UUID).
2. Load `prior_run_opportunities` from last N stored JSON payloads (headlines or `O*` ids).
3. Build runtime YAML:
   ```bash
   python3 scripts/apply_presets.py --brief client_facing --sector automotive_supplier
   ```
   Or edit `RUNTIME-CONTEXT.example.yaml` manually.
4. Prepend filled YAML as `<runtime_context>` to the user message.
5. Set system prompt from `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md`.
6. Enable web search + fetch in the host (Claude, etc.).
7. Parse delimited outputs (`===JSON_START===`, `===BRIEF_MD_START===`, …).
8. **Validate before publish:**
   ```bash
   python3 scripts/validate_run.py runs/$RUN_ID.json
   ```
9. SHA-256 hash the JSON payload in orchestrator code (not in the model).

## Brief profile (confidence tension)

| Profile | Use |
|---------|-----|
| `client_facing` | **Default** — external briefs; confidence gate only, not ranking |
| `internal_lab` | Your Monday stack; Hypothesis in brief; confidence in score |
| `balanced` | Unsure — see `DESIGN-TENSION-CONFIDENCE.md` |

## Two-pass mode (optional)

When briefs drift from evidence or JSON is skipped: `TWO-PASS-ORCHESTRATION.md`.

## CI / regression

```bash
bash scripts/run_validation_tests.sh
```

GitHub Actions: `.github/workflows/revenue-intel-validate.yml`.

## Storage schema (suggested)

```
runs/{run_id}.json
runs/{run_id}.md
runs/index.jsonl
```

## HUNTER handoff

When `hunter_handoff: true`, map only `Validated` rows per `OPPORTUNITY-BRIEF-SCHEMA.md` into the **internal** HUNTER base.

## Cost control

- Default `output_modes: [ExecutiveBriefMD]` only; always validate with JSON in Pass 1 or add JSON to modes when testing.
- Lower `search_budget` for ad hoc; raise for new niches.
