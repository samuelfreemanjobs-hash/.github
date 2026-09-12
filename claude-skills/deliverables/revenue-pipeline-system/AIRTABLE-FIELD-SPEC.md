# Airtable field spec — Opportunities (Path B)

Add these fields to **Opportunities** after CSV import (CSV covers text/number columns that import cleanly).

## Select fields

**Industry:** Professional Services / Consulting · Marketing or Creative Agency · Dev or IT Services · B2B SaaS · Fractional / Executive Services · Other  

**Company Size:** 20-50 · 50-100 · 100-250 · 250-500 · 500+  

**Stage:** New Opportunity · Diagnostic Ready · Outreach Sent · Meeting Booked · Proposal Active · Closed Won / Client  

**Outreach Strategy:** A — Diagnostic · B — Opportunity · C — Competitive · D — Build · E — Audit · F — Intelligence  

## Number fields (0 decimals)

Problem Severity · Buying Signal · Ability to Pay · Service Fit · Accessibility · Urgency · Competitive Pressure  

## Other

- **Estimated Value** — Currency USD  
- **Last Activity** — Date  
- **Matched Service** — Link to Service Catalog (allow multiple off)  
- **Outreach Log** — Link to Outreach Log (inverse on Outreach)  

## Formula — Total Score

```text
IF(
  OR({Problem Severity},{Buying Signal},{Ability to Pay},{Service Fit},{Accessibility},{Urgency},{Competitive Pressure}),
  IF({Problem Severity},{Problem Severity},0) +
  IF({Buying Signal},{Buying Signal},0) +
  IF({Ability to Pay},{Ability to Pay},0) +
  IF({Service Fit},{Service Fit},0) +
  IF({Accessibility},{Accessibility},0) +
  IF({Urgency},{Urgency},0) +
  IF({Competitive Pressure},{Competitive Pressure},0),
  BLANK()
)
```

## Formula — Tier

```text
IF(
  {Total Score} >= 90, "🔥 HOT",
  IF({Total Score} >= 75, "🟠 HIGH",
    IF({Total Score} >= 60, "🟡 MEDIUM",
      IF({Total Score} > 0, "⚪ WATCH", "")
    )
  )
)
```

## Outreach Log fields

**Channel:** Email · LinkedIn DM · Phone · Loom / Video  

**Response Status:** Awaiting · Positive · Neutral · Negative · No Response  

**Opportunity** — Link to Opportunities  
