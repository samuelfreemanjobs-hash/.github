# Agent registry (24-agent model)

> Reference for orchestration. Invoke 3–7 agents per workflow, not all 24.

| ID | Agent | Domain | Inputs | Outputs | Tools |
|----|-------|--------|--------|---------|-------|
| 1 | PWA Architect | Dev | idea, hub stack | architecture spec | hub, github |
| 2 | Frontend Engineer | Dev | UI spec | implementation | github |
| 3 | Backend / API Engineer | Dev | data model | API spec | github |
| 4 | Integration Engineer | Dev | integrations matrix | webhooks plan | mcp |
| 5 | Automation Engineer | Dev | SOPs | scripts | github |
| 6 | QA / Release | Dev | PR | test plan | github |
| 7 | Positioning Strategist | Mkt | positioning.md | narrative | hub |
| 8 | Offer & Pricing Analyst | Mkt | offer-ladder, catalog | pricing analysis | hub |
| 9 | Copy Chief | Mkt | brand-voice | polished copy | hub |
| 10 | Paid Ads Specialist | Mkt | offer, compliance | ad pack | hub |
| 11 | SEO / Content Strategist | Mkt | ICP | content briefs | hub |
| 12 | Lifecycle / Email Architect | Mkt | ladder | flows | crm |
| 13 | UX Strategist | Design | ICP | flows | hub |
| 14 | UI Designer | Design | UX | screen specs | figma |
| 15 | Visual / Brand Designer | Design | visual-brand | creative brief | hub |
| 16 | Design Systems Curator | Design | tokens | component docs | github |
| 17 | Conversion Designer | Design | analytics | CRO blocks | hub |
| 18 | Print / Collateral Designer | Design | brand | print specs | hub |
| 19 | Store Merchandiser | eComm | catalog | PDP structure | shopify |
| 20 | CRO / Funnel Operator | eComm | analytics | tests | analytics |
| 21 | Social Content Producer | Social | voice | posts | hub |
| 22 | Community / Engagement | Social | FAQ | reply frames | hub |
| 23 | Influencer / Partnership Scout | Social | ICP | outreach briefs | hub |
| 24 | Analytics Reporter | Ops | analytics-plan | readouts | analytics |

## Skills map

| Skill | Lead agents |
|-------|-------------|
| `/ad-pack-from-offer` | 8, 10, 9, 15, 24 |
| `/pwa-idea-to-spec` | 7, 13, 14, 1, 3, 6 |
| `/pricing-positioning-memo` | 7, 8, 9, 19, 24 |
| `/business-hub-init` | CoS + section agents |
| `/business-hub-audit` | CoS + 4C auditor |
