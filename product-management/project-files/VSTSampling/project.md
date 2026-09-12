# VST Sampling Factory

> **Deploy target:** `https://github.com/samuelfreemanjobs-hash/VSTSampling` → `./project.md`

| Field | Value |
|-------|-------|
| **id** | `vst-sampling-factory` |
| **tagline** | Reaper → samples → MPC/SFZ/Kontakt. |
| **owner** | Sam Freeman |
| **status** | mvp |
| **completion %** | 78 |
| **heat** | warm |
| **launch rank** | 8 |
| **last verified** | 2026-09-12 |

## Location

- **Repo:** https://github.com/samuelfreemanjobs-hash/VSTSampling
- **Path:** `./`

## ICP & wedge

Producers and sound designers batching VST multisamples.

Automated multisample pipeline with MPC XPM export.

## Architecture

- **Type:** hybrid

## Hard rules

- Human approval on high-impact actions.
- Binding facts from deterministic code.
- Fail closed on schema violation.

## Evidence (why this %)

v1.0 README; 43 tests documented; full Python pipeline.

## Blockers

Reaper + MPC hardware validation on Windows.

## Next ship (one slice)

Run USAGE.md checklist on target machine; ship installer.

## Links

- Spec: `N/A`
- Verify: `pytest tests -q`
