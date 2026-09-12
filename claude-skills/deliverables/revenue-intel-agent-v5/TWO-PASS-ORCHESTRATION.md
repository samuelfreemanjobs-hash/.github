# Two-pass orchestration (optional)

Single-pass is the default. Use two passes when **search cost** or **format drift** hurts quality.

## When to use

| Signal | Action |
|--------|--------|
| Brief cites facts not in `source_ledger` | Enable two-pass |
| JSON omitted when only MD requested | Pass 1 always JSON |
| Runs exceed `search_budget` often | Pass 1 higher budget, Pass 2 zero search |

## Pass 1 — Research

**System:** Full Revenue Intel v5.1 prompt.

**Runtime overrides:**

```yaml
output_modes:
  - JSON
search_budget: 28
allow_hypothesis_in_brief: true   # internal only
brief_profile: internal_lab
```

**User suffix:**

```
RESEARCH_PASS: Maximize source_ledger and gate_results. Opportunities may be
Hypothesis. Do not emit ExecutiveBriefMD.
```

**Orchestrator:** Run `validate_run.py` on output. Store JSON. Abort if parse fails.

## Pass 2 — Write (no new research)

**System:** Short writer prompt (or same agent with research disabled):

```
You are the Revenue Intel brief writer. You may NOT search the web.
Use ONLY the JSON from Pass 1. Emit ExecutiveBriefMD per output_contract.
Respect status_model: Pick of the week = Validated only.
Apply brief_profile from runtime_context.
```

**Runtime:**

```yaml
output_modes:
  - ExecutiveBriefMD
search_budget: 0
allow_hypothesis_in_brief: false
brief_profile: client_facing
```

**User message:** Attach Pass 1 JSON (or file path content).

**Orchestrator:** Optionally validate that brief headlines match JSON ids.

## Same model vs two models

| Approach | Pros | Cons |
|----------|------|------|
| Same model, two chats | Simple | Pass 2 may still hallucinate if not strict |
| Cheaper model Pass 2 | Cost | Needs strong “no search” enforcement |
| Pass 2 human | Highest trust | Not automated |

**Default recommendation:** Same model, two chats, Pass 2 `search_budget: 0` and explicit JSON-only input.

## CLI sketch

```bash
# After Pass 1
python3 scripts/validate_run.py runs/$RUN_ID.json
# Merge profile for Pass 2
python3 scripts/apply_presets.py --brief client_facing --in runs/context.yaml
```
