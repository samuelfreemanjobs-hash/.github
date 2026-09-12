# Critique — Revenue Intel Agent v5.0

**Verdict:** Strong product architecture (anti-padding, zero-result success, rejected ledger, no fake hashes). Weakest link is **enforceability** — many gates read as auditable but are still honor-system unless the JSON schema and orchestrator close the loop.

## What already works

| Design choice | Why it matters |
|---------------|----------------|
| Precision over recall + `min_opportunities: 0` | Stops the #1 agent failure mode (fabricated volume). |
| Absolute `RevenuePotential` bands | Weekly scores become comparable across runs (real v4.1 fix). |
| `<research_protocol>` + budget + stop rules | Gives models permission to stop — rare and valuable. |
| `rejected` + mandatory brief section | Negative knowledge is a feature, not an apology. |
| `claim_supported` + Bias gate intent | Right direction for mechanical review. |
| Removed SHA-256 | Honest about tool limits; pushes integrity to orchestrator. |
| Default `ExecutiveBriefMD` only | Cuts cost and format drift; JSON opt-in is correct. |

## Gaps (severity)

### Critical — logic holes

1. **Validated vs Hypothesis is undefined.** Gates say failure → Hypothesis, but Padding says shipped items must pass Evidence. When is `Validated` allowed? Models will label top picks Validated while failing Bias or Math.
2. **`priority_score` is not computable from the spec.** Components mix 0–1 scales and band weights; `score_breakdown.total` will be invented each run.
3. **SheetsSpec formula does not match CSV columns.** Column P / `J2-K2` refs are inconsistent with the declared CSV header — downstream automation will break silently.
4. **Math gate uses string `formula`.** LLMs verify arithmetic in prose; they do not reliably self-check. Need numeric fields + orchestrator-side recomputation.

### High — enforcement

5. **No `gate_results` object in JSON.** Gates are claimed in narrative only; orchestrator cannot block ship.
6. **Duplication gate (>50% shared evidence)** — no required `evidence_source_ids[]` per opportunity, so overlap is unmeasurable.
7. **`credibility_score` is self-assigned.** Expect systematic inflation on vendor PDFs; tie scores to `source_type` floors unless overridden with justification.
8. **`search_budget` undefined unit.** Search vs fetch vs “query reformulation” — models will miscount.

### Medium — product / ops

9. **ICP is a single string.** Real runs need geography, exclusions, price band, and **offer catalog** (what the owner actually sells).
10. **Weekly framing is hardcoded** but runs may be ad hoc — add `cadence` in runtime.
11. **No `run_id`** — series dedupe and storage are orchestrator problems but should be in contract.
12. **Confidence double-penalty** (gate + score) may be too harsh; document or make weights configurable.
13. **Compliance gate** is a long list with no sector shortcut — models either over-claim HIPAA or skip the field.

### Low — polish

14. Sample brief in buyer pack is pre-v5 shape (misleading).
15. No orchestrator doc for storage, hashing, PDF export, HUNTER handoff.

## Recommended direction (v5.1)

1. Formal **status model**: `Validated` = all gates pass + `confidence >= confidence_gate`; never Pick-of-the-week otherwise.
2. **Explicit `priority_score` formula** + optional `score_weights` in runtime.
3. **Structured `example_calc` inputs** for Math gate; keep `formula` as display only.
4. **`gate_results`** per opportunity + **`evidence_source_ids`** for duplication.
5. **Fix or drop** broken SheetsSpec formula; document column letters if kept.
6. **`offer_catalog`** + expanded ICP in runtime.
7. **`ORCHESTRATOR.md`** for humans/automation running the agent.
