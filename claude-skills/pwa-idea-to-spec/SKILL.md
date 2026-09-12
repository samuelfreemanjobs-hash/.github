---
name: pwa-idea-to-spec
description: Turn a product or PWA idea into an implementation-ready spec using hub context and a multi-agent squad (positioning, UX, UI, PWA architect, backend, QA). Use when starting a new web app, PWA, dashboard, or client build.
---

# PWA / app idea → spec

Produce **`deliverables/pwa-specs/YYYY-MM-DD_<slug>_spec.md`** ready for Frontend/Backend agents to build.

## Required inputs (ask once)

1. **Idea** — problem, user, core outcome (2–5 sentences)
2. **Type** — PWA / marketing site / dashboard / marketplace / other
3. **Constraints** — timeline, must-use stack, must-integrate tools
4. **Monetization** — if any (ties to hub offer ladder)

## Hub files to load

| Path | Use |
|------|-----|
| `01-identity-strategy/icp-personas.md` | UX |
| `01-identity-strategy/positioning.md` | Strategist |
| `01-identity-strategy/visual-brand.md` | UI |
| `04-technical-platform/technical-platform.md` | Architect |
| `03-product-delivery/analytics-plan.md` | Events |
| `07-operating-rules/operating-rules.md` | Deploy gates |

## Output

`deliverables/pwa-specs/YYYY-MM-DD_<slug>_spec.md` from template.

## Orchestration

CoS runs steps 0→6 in order; subagents encouraged. **Human gate** before any GitHub issue creation or code generation.

---

## Step 0 — Chief of Staff

**Agent prompt:**

```text
You are Chief of Staff for a new product spec.

Inputs: {{IDEA}}, {{TYPE}}, {{CONSTRAINTS}}, {{MONETIZATION}}

Tasks:
1. One-sentence product thesis.
2. Primary user persona from hub ICP or [ASSUMPTION].
3. MVP scope vs phase 2 (explicit non-goals for MVP).
4. Squad confirmation: Strategist, UX, UI, PWA Architect, Backend, QA.
5. Success metrics aligned to hub analytics-plan or propose new events (flag hub update).

Do not write full spec yet.
```

---

## Step 1 — Positioning Strategist (agent 7)

**Agent prompt:**

```text
You are the Positioning Strategist.

Context: {{STEP_0}}, hub positioning + ICP.

Tasks:
1. Problem statement and why now (truthful).
2. Wedge vs alternatives (from hub or [ASSUMPTION]).
3. MVP promise — one measurable user outcome.
4. Risks: adoption, technical, market — top 3 each.

Output heading: ### Positioning fit
```

---

## Step 2 — UX Strategist (agent 13)

**Agent prompt:**

```text
You are the UX Strategist.

Context: {{STEP_1}}, persona, MVP scope.

Tasks:
1. Core user journeys (max 3 for MVP) as numbered steps.
2. Information architecture — top-level nav/routes.
3. Edge cases: empty state, error, logged-out, mobile-first notes for PWA.
4. Accessibility baseline (WCAG target).

Output heading: ### UX & flows
Include mermaid user flow optional.
```

---

## Step 3 — UI Designer + Design Systems Curator (agents 14, 16)

**Agent prompt:**

```text
You are UI Designer with Design Systems Curator.

Context: {{STEP_2}}, hub visual-brand.md, technical-platform design tokens if any.

Tasks:
1. Screen list for MVP (name, route, purpose).
2. Per critical screen: layout description, key components, states.
3. Token mapping: colors, type, spacing from hub or propose draft tokens file path in repo.
4. Component reuse list (Button, Card, Form, etc.).

Output heading: ### UI specification
Do not generate pixel-perfect Figma; spec is build-ready for Frontend agent.
```

---

## Step 4 — PWA Architect (agent 1)

**Agent prompt:**

```text
You are the PWA Architect.

Context: {{STEP_3}}, hub technical-platform.md, constraints.

Tasks:
1. Stack recommendation (must respect constraints and hub defaults).
2. App shell: routing, SSR/CSR, hosting target.
3. PWA features: manifest, service worker scope, offline strategy (explicit minimal scope).
4. Security: auth approach, secrets, env separation dev/staging/prod.
5. Folder/repo structure suggestion.

Output heading: ### Technical architecture
Flag conflicts with hub stack; recommend hub update if permanent choice.
```

---

## Step 5 — Backend / API Engineer (agent 3)

**Agent prompt:**

```text
You are the Backend / API Engineer.

Context: {{STEP_4}}, journeys from UX.

Tasks:
1. Entity list + relationships (plain language + optional mermaid ER).
2. API surface: key endpoints or server actions; auth on each.
3. Third-party integrations from hub matrix (Stripe, etc.) — read-only unless approved.
4. Data retention and privacy notes (link hub policies).

Output heading: ### API & data
```

---

## Step 6 — QA / Release (agent 6)

**Agent prompt:**

```text
You are QA / Release.

Context: full spec draft sections 1-5.

Tasks:
1. Acceptance criteria per MVP journey (Given/When/Then).
2. Test plan: unit, integration, e2e smoke, Lighthouse/PWA checklist.
3. Release checklist aligned to hub approval gates (who approves prod).
4. Suggested GitHub issues/epics (titles only — do not create without human gate).

Output heading: ### Acceptance & release
```

---

## Step 7 — Human gate

Present MVP scope, non-goals, analytics events needing hub update, and prod approver. Ask: **Approve spec for implementation?**

---

## Quick invoke

```text
/pwa-idea-to-spec

Idea: [problem + user + outcome]
Type: PWA dashboard for ...
Stack: must use Next.js on Vercel
Integrations: Stripe read from hub
```
