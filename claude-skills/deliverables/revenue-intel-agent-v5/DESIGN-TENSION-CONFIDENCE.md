# Design tension — confidence in gate vs score

## The problem

v5.0 uses **confidence** twice:

1. **Gate** — below `confidence_gate` → `Hypothesis` + validation plan  
2. **Score** — enters `priority_score` with weight `w_confidence`

That **double-penalizes** uncertain ideas: they drop out of Validated *and* sink in the ranking. Good for internal research sorting; harsh for **client-facing** briefs where you want “if it passed the bar, rank by money and urgency.”

## There is no universal “best” — pick a profile

| Profile | When to use | `confidence` in ranking | Hypothesis in brief |
|---------|-------------|-------------------------|---------------------|
| **`client_facing`** (default for product) | External briefs, Gumroad default | **Weight 0** — gate only | No |
| **`internal_lab`** | Your weekly Sam stack prioritization | **Weight 0.2** — gate + rank | Yes |
| **`balanced`** | Unsure / mixed audience | **Weight 0.1** | No |

**Recommendation:** Ship **`client_facing`** in setup docs and `RUNTIME-CONTEXT.example.yaml`. Use **`internal_lab`** in your own HUNTER/internal runs. Switch with one field:

```yaml
brief_profile: client_facing   # or internal_lab | balanced
```

Apply presets:

```bash
python3 scripts/apply_presets.py --brief client_facing --sector automotive_supplier
```

## What we did not do

Remove confidence from the gate — low-confidence ideas should never be labeled `Validated` for clients, regardless of ranking formula.

## How to A/B (3 runs)

1. Same `niche` / `icp` / `today`, two runs: `client_facing` vs `internal_lab`.  
2. Compare: count of `Validated`, top headline, and whether Hypothesis rows would have changed your Monday action.  
3. If internal_lab’s top pick differs only by confidence 0.55 vs 0.72 on the same deal size, **`client_facing` is working**.  
4. If internal_lab surfaces a Hypothesis you later validated manually, keep lab mode for **Monday research**, client_facing for **Friday client email**.
