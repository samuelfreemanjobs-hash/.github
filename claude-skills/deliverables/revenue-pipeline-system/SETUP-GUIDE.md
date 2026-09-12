# Revenue Pipeline System (HUNTER CRM) — Setup Guide

**Version 1.0 · Freeman Intelligence**

Turn scattered B2B leads into a **scored pipeline** you can prioritize every week — without a full CRM implementation.

---

## What you get

1. **Airtable template** — 3 tables: **Opportunities**, **Outreach Log**, **Service Catalog**
2. **100-point scoring model** — 7 dimensions, auto **Tier** (HOT / HIGH / MEDIUM / WATCH)
3. **Claude scoring prompt** — paste intel; get dimension scores + outreach angles
4. **This guide**

**Template link (replace before publish):** `{TEMPLATE_LINK}`

---

## 1. Copy the base (5 minutes)

1. Open the template link above while logged into Airtable.
2. Click **Copy base** (or **Add to workspace**).
3. Rename your copy: e.g. *My Company — Revenue Pipeline*.
4. Skim the three tabs: **Opportunities**, **Outreach Log**, **Service Catalog**.

You do **not** need Airtable paid tier for basic use; paid features are optional (extensions, sync).

---

## 2. Define your offers (15 minutes)

Open **Service Catalog**. Each row is a **productized service** you might sell.

- Edit the sample rows **or** replace them with your real packages.
- **Solves Problems** and **Ideal Buying Signals** help Claude (and you) match leads later.

Rule: if you change offer copy, you only touch **Service Catalog** — not old lead rows.

---

## 3. Add your first opportunities (10 minutes)

In **Opportunities**, create one row per prospect.

| Field | What to enter |
|-------|----------------|
| Company | Legal or trade name |
| URL | Website or LinkedIn company URL |
| Location | City, region |
| Industry | Pick closest type |
| Company Size | Employee band |
| Decision Maker | Name + title |
| Opportunity Title | One-line problem (e.g. “Manual QA logs → spreadsheet errors”) |
| Stage | Start at **New Opportunity** |
| Detected Problems | Bullet or comma list |
| Evidence Signals | Job posts, news, audits, hiring, etc. |

Leave **score fields blank** until step 4.

---

## 4. Score with Claude (10 minutes per batch)

1. Open `CLAUDE-SCORING-PROMPT.md` (included in your download).
2. Paste your **Service Catalog** (names + “Solves Problems” + “Ideal Buying Signals”) into the prompt where indicated.
3. Paste one or more opportunity records (Company, problems, evidence).
4. Run in Claude (claude.ai or Claude Code).
5. Copy returned **dimension scores** into Airtable:

| Dimension | Max points |
|-----------|------------|
| Problem Severity | 25 |
| Buying Signal | 20 |
| Ability to Pay | 15 |
| Service Fit | 15 |
| Accessibility | 10 |
| Urgency | 10 |
| Competitive Pressure | 5 |
| **Total** | **100** |

**Tier** (auto in Airtable):

- **HOT** ≥ 90  
- **HIGH** ≥ 75  
- **MEDIUM** ≥ 60  
- **WATCH** &lt; 60  

Link **Matched Service** to the best **Service Catalog** row.

Optional fields from Claude output: **Outreach Strategy** (A–F), **Diagnostic Angle**, **Give Before Ask**, **Estimated Value** / **Value Range**.

---

## 5. Outreach without duplication

When you send email/DM/call:

1. Add a row in **Outreach Log** (Subject, Body, Channel, Sent Date, Strategy Used).
2. Link **Opportunity** to the lead.
3. Set **Response Status** when they reply.

On the opportunity, set **Stage** (e.g. Outreach Sent → Meeting Booked).

---

## 6. Weekly rhythm (15 minutes)

1. Sort **Opportunities** by **Tier** → work HOT and HIGH first.  
2. Score any row with blank **Total Score**.  
3. Follow up **Outreach Log** where status = Awaiting.  
4. Add 3–5 new prospects.

---

## Outreach strategies (A–F)

| Code | Use when |
|------|----------|
| **A — Diagnostic** | Lead with a small audit or benchmark |
| **B — Opportunity** | Frame a clear ROI outcome |
| **C — Competitive** | They’re losing to a known alternative |
| **D — Build** | They need something built / implemented |
| **E — Audit** | Compliance, quality, or process audit hook |
| **F — Intelligence** | Share niche intel they don’t have |

Pick one per touch; log it on the outreach row and opportunity.

---

## Stage definitions

New Opportunity → Diagnostic Ready → Outreach Sent → Meeting Booked → Proposal Active → Closed Won / Client

Move stages only when the **event** happened (not when you *hope* it will).

---

## Support & license

- **Support:** `{SUPPORT_EMAIL}` (replace before launch)
- **License:** Single business use. Do not resell or redistribute the template as a competing product. Client work using the pipeline is allowed.

---

## Quick troubleshooting

| Issue | Fix |
|-------|-----|
| Tier blank | Enter at least one dimension score; Total Score is a formula |
| Claude scores feel off | Refresh Service Catalog in prompt; tighten Evidence Signals |
| Too many WATCH leads | Raise threshold; focus on HIGH+ only for outbound |

**You’re live.** Next: add 10 real prospects and score them this week.
