# Setup guide — Revenue Intel Agent — v5.0

**Support:** `{SUPPORT_EMAIL}` (default: samuelfreemanjobs@gmail.com)

## What you bought

The **Revenue Intel Agent — v5.0** system prompt: weekly, evidence-gated monetization briefs for any **niche + ICP** you specify. Outputs Executive Brief by default; JSON/CSV/email on request.

## 5-minute setup

1. Unzip `Revenue-Intel-Agent-v5.0.zip`.
2. Paste `REVENUE-INTEL-AGENT-v5.0-SYSTEM-PROMPT.txt` into your AI **system** role (not the user message).
3. Each run: fill `RUNTIME-CONTEXT.example.yaml` → inject as `<runtime_context>` (orchestrator or copy into user message prefix).
4. **Required every run:** `today`, `niche`, `icp`. The agent must stop if any are missing.
5. Send the run template from the bottom of the system prompt:

   ```
   Run this agent for:
   Niche/Market: …
   ICP: …
   ```

6. Enable **web search + fetch** in your tool (Claude, ChatGPT, Gemini, etc.) — the prompt requires retrieved, dated sources.

## Optional: Claude Business OS

Copy `revenue-intel-agent/SKILL.md` into your skills folder → `/revenue-intel-agent`.

## License

Personal / single-seat business use. See `LICENSE.txt`.

## Not included

- Guaranteed opportunity count (zero-result weeks are valid)
- Legal/tax advice
- Pre-built lead lists
