# Revenue Intel Agent — v5.0 — product launch kit

**Official product name:** **Revenue Intel Agent — v5.0**  
**Codename:** Revenue Intel (Cleo ecosystem)  
**Function:** Weekly, evidence-gated monetization briefs for a stated **niche + ICP** (runtime-injected each run)  
**Status:** Phase 0 in progress · **Sam review gate** before Phase 1 (buyer packaging)

## What you are reviewing

| Asset | Path |
|-------|------|
| **Agent system prompt (v5.0)** | `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` + `.txt` |
| **Claude skill (invoke in Business OS)** | `../../revenue-intel-agent/SKILL.md` |
| **Runtime template** | `RUNTIME-CONTEXT.example.yaml` |
| **Brief presets** | `BRIEF-PROFILES.yaml` + `DESIGN-TENSION-CONFIDENCE.md` |
| **Sector presets** | `SECTOR-PROFILES.yaml` |
| **Validator** | `scripts/validate_run.py` · `scripts/run_validation_tests.sh` |
| **Two-pass mode** | `TWO-PASS-ORCHESTRATION.md` |
| **Output schema (v5 + optional HUNTER)** | `OPPORTUNITY-BRIEF-SCHEMA.md` |
| **Phase 0 runbook** | `PHASE-0.md` |
| **Launch checklist** | `LAUNCH-CHECKLIST.md` |
| **Build status** | `PRODUCT-BUILD-STATUS.md` |
| **Review portal (browser)** | `review/index.html` |
| **Positioning & ICP** | `NICHE-POSITIONING.md` |
| **Buyer setup (draft)** | `SETUP-GUIDE.md` |
| **Listing copy (draft)** | `LISTING-GUMROAD.md` |

## Local review (this environment)

```bash
cd claude-skills/deliverables/revenue-intel-agent-v5/review
python3 -m http.server 8765
```

Open `http://localhost:8765` — tabs: Overview, System prompt, Phase 0, Launch prep.

## Build order (after Sam approves Phase 0)

1. Paste Gem deltas into `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.md` if your live Gem differs from this port.
2. Complete Phase 0 checklist in `PHASE-0.md`.
3. Phase 1: PDF exports, ZIP, Gumroad listing (`LISTING-GUMROAD.md`).
4. Phase 2: Optional bundle with HUNTER CRM (intel → pipeline); keep intel sources **internal** on customer template per HUNTER launch checklist.

## PM project

**Airtable:** Freeman Intelligence — PM · project **Revenue Intel Agent**  
**Artifact path (this repo):** `claude-skills/deliverables/revenue-intel-agent-v5/`
