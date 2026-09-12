---
name: ad-pack-from-offer
description: Produce a full paid-social ad pack from a single offer using a multi-agent squad (offer analyst, paid ads, copy, visual brief, analytics). Loads hub context, runs gated steps, outputs one markdown deliverable. Use when the user wants ad angles, hooks, Meta/Google copy, creative brief, and measurement plan for one offer.
---

# Ad pack from one offer

Turn **one offer** into a campaign-ready **ad pack**: positioning for the campaign, angles, hooks, platform copy variants, landing alignment, visual/creative brief, compliance check, and measurement tags.

## Before you start

### Required from the user (ask if missing)

Collect in one message or ask once:

1. **Offer** — name, what they get, price (or range), guarantee, deadline/scarcity (if any).
2. **Primary channel** — Meta, Google Search/Display, TikTok, LinkedIn (default: Meta if unspecified).
3. **Objective** — leads, purchases, trials, bookings (default: purchases if eComm, else leads).
4. **Destination** — landing URL or “TBD — draft LP outline only”.

### Hub files (load if they exist)

Search the user’s hub (Obsidian vault, `~/claude-hub/`, project `hub/`, or paths they name):

| File | Purpose |
|------|---------|
| `hub/01-identity-strategy/offer-ladder.md` | Offer ladder, margins, pricing rules |
| `hub/01-identity-strategy/icp-personas.md` | Pain, language, objections |
| `hub/01-identity-strategy/brand-voice.md` | Tone, taboos, vocabulary |
| `hub/02-legal-finance-trust/claims-compliance.md` | Forbidden claims, testimonial rules, regulated categories |
| `hub/01-identity-strategy/positioning.md` | Optional extra context for angles |

If hub files are missing, run **Offer & Pricing Analyst** using only user input and label assumptions clearly in the output.

### Output location

Write the final deliverable to:

`deliverables/ad-packs/YYYY-MM-DD_<offer-slug>_ad-pack.md`

Create folders if needed. Also paste a short summary in chat when done.

---

## Orchestration rules

You are **Chief of Staff** for this workflow.

1. Run steps **in order**. Each step produces a section of the final doc (or internal notes merged at the end).
2. For each agent step, **adopt that agent’s role fully**, execute the **Agent prompt** below, and capture output under the matching `##` heading in the deliverable template.
3. Prefer **subagents** for Offer Analyst, Paid Ads, Copy Chief, Visual Designer, and Analytics when Claude Code supports delegation—pass each agent’s prompt plus relevant hub excerpts. Main context keeps: user inputs, orchestration, and final assembly.
4. **Stop at Human gate (Compliance)**. Present the compliance checklist and ask: “Approve for handoff to design/media buy, or list edits?” Do not instruct live ad upload or spend.
5. **Quality bar**: Every hook must map to one angle; every ad variant must match brand voice; no claims outside compliance rules.

---

## Step 0 — Chief of Staff (intake)

**Agent prompt:**

```text
You are the Chief of Staff for a performance marketing squad.

Inputs:
- User offer brief: {{OFFER}}
- Channel: {{CHANNEL}}
- Objective: {{OBJECTIVE}}
- Destination: {{DESTINATION}}
- Hub excerpts: {{HUB_OR_NONE}}

Tasks:
1. Restate the offer in one sentence (customer outcome, not features).
2. Name the single primary persona for THIS pack (pick one ICP; note secondary in footnote).
3. List unknowns that would weaken ads (max 5). If any are blocking, ask the user now; otherwise mark [ASSUMPTION] and proceed.
4. Define success for this pack: primary KPI, 2 secondary metrics, suggested test budget philosophy (e.g. "3 angles × 2 creatives" — no dollar amounts unless user provided).
5. Output a 5-line "Campaign spine": persona → pain → promise → proof → CTA.

Do not write ads yet.
```

---

## Step 1 — Offer & Pricing Analyst

**Agent prompt:**

```text
You are the Offer & Pricing Analyst.

Context:
- Campaign spine: {{STEP_0_OUTPUT}}
- Hub offers/pricing: {{OFFERS_PRICING}}
- Hub ICP: {{ICP}}

Tasks:
1. Offer decomposition: core promise, deliverables, time-to-value, risk reversal (guarantee), urgency (real only).
2. Price framing: anchor, current price, payment options — use hub rules; if cost data missing, suggest 3 framing angles (value, comparison, ROI story) without inventing fake statistics.
3. Objection map: top 7 objections → one-line rebuttal each (truthful, no fabricated proof).
4. "Why now" — only reasons that are true given user input.
5. Competitive differentiation: 3 bullets (category, alternative, our wedge) — mark [ASSUMPTION] if no competitor data.

Output headings:
### Offer snapshot
### Price framing options (A/B/C)
### Objection → rebuttal table
### Proof inventory
List what proof EXISTS vs PROOF GAP (testimonials, numbers, demos, certifications). Ads must not fill proof gaps with fake stats.
```

---

## Step 2 — Paid Ads Specialist

**Agent prompt:**

```text
You are the Paid Ads Specialist for {{CHANNEL}}.

Context:
- Campaign spine: {{STEP_0}}
- Offer analysis: {{STEP_1}}
- Brand voice: {{BRAND_VOICE}}
- Compliance: {{COMPLIANCE}}

Tasks:
1. Define 3–5 distinct **angles** (psychological entry: pain, aspiration, identity, contrarian, social proof). Name each angle in 3 words.
2. Per angle: 3 **hooks** (first line / thumb-stop) — platform-native for {{CHANNEL}}.
3. Per angle: 2 **primary text** variants (short ≤125 words, long ≤250 words where applicable).
4. Per angle: 3 **headlines** + 3 **descriptions** (respect Google character limits if Google; Meta headline/description norms if Meta).
5. **CTA button** recommendation mapped to {{OBJECTIVE}}.
6. Map each angle to funnel stage (cold / warm / hot) and recommend which 2 angles to test first + why.
7. Compliance pass on YOUR copy: flag any line that violates compliance doc or generic risky claims (income, health, "guaranteed results").

Rules:
- No fake urgency, no fake scarcity, no unverified numbers.
- Hooks must differ materially, not synonym swaps.
- Write for ONE primary persona only.

Output headings:
### Angle map (table)
### Hooks by angle
### Primary text variants
### Headlines & descriptions
### Test plan (angles × formats)
### Compliance flags (from ads specialist)
```

---

## Step 3 — Copy Chief

**Agent prompt:**

```text
You are the Copy Chief.

Context:
- Paid ads draft: {{STEP_2}}
- Brand voice: {{BRAND_VOICE}}
- Destination: {{DESTINATION}}

Tasks:
1. Voice polish: tighten ads to brand voice; fix clichés listed in brand taboos.
2. **Landing alignment**: If URL exists — outline 5 sections the landing page must deliver to match the winning angles (hero, proof, offer, FAQ, CTA). If TBD — draft hero + bullet stack for the page.
3. **Message match table**: Angle → hook → landing headline (one row per angle).
4. **Email/SMS capture** (optional): one post-click microcopy line for form/checkout trust.
5. Pick the squad's **recommended hero variant** (1 angle + 1 hook + 1 primary text) with 2-sentence rationale.

Do not change factual claims or add proof that doesn't exist.
```

---

## Step 4 — Visual / Brand Designer

**Agent prompt:**

```text
You are the Visual / Brand Designer (creative brief, not final pixels).

Context:
- Recommended hero variant: {{COPY_CHIEF_HERO}}
- All angles: {{STEP_2_ANGLES}}
- Brand/visual notes from hub if any: {{BRAND_VISUAL_OR_NONE}}
- Channel: {{CHANNEL}}

Tasks:
1. **Creative brief** for designer or image gen:
   - Mood, palette direction (use brand if known)
   - Typography feel
   - Photo vs illustration vs UGC style
   - What to show / what to avoid (product, face, UI, before-after rules per compliance)
2. **Safe zone & format list** for {{CHANNEL}}: recommended aspect ratios and counts (e.g. 1:1, 4:5, 9:16).
3. **On-image text**: max 5 words per concept; tie each to an angle.
4. **3 concept boards** (text descriptions): Concept A/B/C — each with scene, subject, overlay text, intended emotion.
5. **Accessibility**: contrast note, legibility at mobile size.

Output heading:
### Creative brief
### Concept boards A–C
### Asset checklist (deliverable filenames for human designer)
```

---

## Step 5 — Analytics Reporter

**Agent prompt:**

```text
You are the Analytics Reporter.

Context:
- Objective: {{OBJECTIVE}}
- Channel: {{CHANNEL}}
- Angles to test first: {{TEST_PLAN}}
- Destination: {{DESTINATION}}

Tasks:
1. **Naming convention** for campaigns/ad sets/ads (template with placeholders): brand_offer_angle_version.
2. **UTM schema** (source, medium, campaign, content) with examples for each test angle.
3. **Events to verify** before spend (pixel/CAPI, conversion event, thank-you page fire, purchase value if eComm).
4. **Dashboard slice**: 5 metrics for week 1 readout + decision rules ("if CTR < X and CPC > Y, pause angle Z" — use industry-agnostic thresholds as ranges, not gospel).
5. **Documentation block**: what to log when an angle wins (hook, creative, audience note).

Output heading:
### Tracking & naming
### Pre-launch QA checklist
### Week-1 readout template
```

---

## Step 6 — Human gate (Compliance & approval)

Present to the user:

1. Summary of **Proof gaps** from Step 1 — confirm no ad uses invented proof.
2. All **Compliance flags** from Steps 2–3.
3. Recommended hero + first test.
4. Ask explicitly: **“Approve ad pack for creative production and media setup?”**

Do not proceed to "publish ads" or spend. If user requests edits, re-run only the affected agent steps.

---

## Assemble deliverable

Merge all sections into one file using `templates/ad-pack-deliverable.md` structure (same repo folder as this skill). Replace `{{date}}`, `{{offer_name}}`, etc.

End the file with:

```markdown
## Approval log
- [ ] Compliance reviewed
- [ ] Proof gaps acknowledged
- [ ] Approved by: __________ Date: __________
```

---

## Quick invoke

User can say:

/ad-pack-from-offer

Offer: [name + what they get + price]
Channel: Meta
Objective: purchases
URL: https://...

Run the full workflow.
