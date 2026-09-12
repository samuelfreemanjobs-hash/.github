# Operating rules

> Last updated: {{date}}

## Approval gates

| Action | AI may draft | AI may execute | Human approver |
|--------|--------------|----------------|----------------|
| Ad copy | ✓ | | |
| Ad spend / publish | | | |
| Deploy prod | | | |
| Pricing change | ✓ | | |
| Refunds | | | |
| Email send | ✓ | | |
| Social post | ✓ | | |
| GL / tax entries | ✓ | | |
| Contract send | ✓ | | |

## Definition of done

### Ad pack

- [ ] Angles map to one persona
- [ ] Compliance reviewed
- [ ] Tracking UTMs defined
- [ ] Creative brief attached

### PWA spec

- [ ] Acceptance criteria
- [ ] Auth/data model sketched
- [ ] Non-goals listed

### Pricing memo

- [ ] Margin logic stated
- [ ] Offer ladder updated in hub

## Naming conventions

| Asset | Pattern | Example |
|-------|---------|---------|
| Campaign | `{brand}_{offer}_{angle}_v##` | |
| Git branch | `feat/{ticket}-{slug}` | |
| Hub doc update | commit message `hub: {file} {change}` | |

## Agent registry

See `agents/REGISTRY.md` (or link).

## Cadence

| Ritual | Frequency | Owner | Output |
|--------|-----------|-------|--------|
| Metrics readout | weekly | | |
| Offer / hub review | monthly | | update `offer-ladder.md` |
| Hub audit skill | monthly | | `deliverables/hub-audits/` |
| Compliance refresh | quarterly | | |
