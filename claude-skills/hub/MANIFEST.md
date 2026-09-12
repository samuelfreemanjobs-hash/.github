# Hub manifest — which skill reads which file

Use this to avoid stale or missing context.

| Hub file | ad-pack | pwa-spec | pricing-memo | hub-init | hub-audit |
|----------|---------|----------|--------------|----------|-----------|
| 01/business-model.md | ○ | ○ | ● | ● | ● |
| 01/icp-personas.md | ● | ● | ○ | ● | ● |
| 01/offer-ladder.md | ● | ○ | ● | ● | ● |
| 01/positioning.md | ● | ● | ● | ● | ● |
| 01/brand-voice.md | ● | ○ | ● | ● | ● |
| 01/visual-brand.md | ● | ● | ○ | ● | ● |
| 02/claims-compliance.md | ● | ○ | ● | ● | ○ |
| 02/* (other legal) | ○ | ○ | ○ | ● | ○ |
| 03/product-catalog.md | ○ | ○ | ● | ● | ○ |
| 03/analytics-plan.md | ● | ● | ● | ● | ○ |
| 04/technical-platform.md | ○ | ● | ○ | ● | ○ |
| 05/marketing-growth-stack.md | ○ | ○ | ○ | ● | ○ |
| 06/integrations-matrix.md | ○ | ○ | ○ | ● | ● |
| 07/operating-rules.md | ○ | ● | ○ | ● | ● |
| 08/human-roles.md | ○ | ○ | ○ | ● | ○ |
| agents/REGISTRY.md | ○ | ○ | ○ | ● | ● |

● = load when running skill · ○ = optional / section agent only

**Rule:** After changing offers, pricing, or compliance, update hub then re-run affected skill (not the whole init).
