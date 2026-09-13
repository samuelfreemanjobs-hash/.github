# Setup guide — Revenue Intel Agent — v5.0

**Support:** `{SUPPORT_EMAIL}` (default: samuelfreemanjobs@gmail.com)

## What you bought

The **Revenue Intel Agent — v5.0** system prompt: weekly, evidence-gated monetization briefs for any **niche + ICP** you specify. Outputs Executive Brief by default; JSON/CSV/email on request.

## 5-minute setup

1. Unzip `Revenue-Intel-Agent-v5.0.zip`.
2. Paste `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.txt` into your AI **system** role (not the user message).
3. Each run: fill `RUNTIME-CONTEXT.example.yaml` (or `python3 scripts/apply_presets.py --brief client_facing`) → inject as `<runtime_context>`.
4. **Brief profile:** default `client_facing` — see `DESIGN-TENSION-CONFIDENCE.md` if unsure (`internal_lab` for your own research weeks).
5. **Required every run:** `today`, `niche`, `icp`. The agent must stop if any are missing.
6. Send the run template from the bottom of the system prompt:

   ```
   Run this agent for:
   Niche/Market: …
   ICP: …
   ```

7. Enable **web search + fetch** in your tool (Claude, ChatGPT, Gemini, etc.) — the prompt requires retrieved, dated sources.
8. Before sharing externally: `python3 scripts/validate_run.py your-run.json` (optional but recommended).

## Optional: Claude Business OS

Copy `revenue-intel-agent/SKILL.md` into your skills folder → `/revenue-intel-agent`.

## License

Personal / single-seat business use. See `LICENSE.txt`.

## Not included

- Guaranteed opportunity count (zero-result weeks are valid)
- Legal/tax advice
- Pre-built lead lists
