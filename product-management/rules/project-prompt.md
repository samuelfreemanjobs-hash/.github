# project.md Prompt

Two variants. Paste one at the start of any session.

---

## VARIANT 1 — New Project

Use when starting a fresh project or conversation.

```
PROJECT NEW

[One paragraph describing the project: what it is, what you're building or doing, who it's for, and roughly what "done" looks like. Include any known stack, urgency, or value context. Don't overthink it — even 2–3 sentences is enough to start.]

Generate a project.md for this using the standard template. Fill in everything you can from the description above and what you know about my work. Flag anything you don't have enough info to fill yet as [TBD] and list those gaps at the end.
```

**Example:**

```
PROJECT NEW

Building a lead capture landing page for Freeman Intelligence targeting Metro Detroit medical practices. It needs a headline, a short form (name, phone, practice type), and a CTA. Will be built as a single HTML file, no backend, form submits to a Zapier webhook. Goal is 5 booked calls in the first 30 days. Urgency is high — want to launch this week.

Generate a project.md for this using the standard template. Fill in everything you can from the description above and what you know about my work. Flag anything you don't have enough info to fill yet as [TBD] and list those gaps at the end.
```

---

## VARIANT 2 — Update Existing

Use when returning to a project mid-session or picking up where you left off.

```
PROJECT UPDATE

[Paste your current project.md here]

---

What changed this session:
- [What got done]
- [What was decided]
- [What's new in the todo list]

Update the project.md to reflect this. Recalculate % complete based on done vs total tasks. Keep everything else unless I specifically say to change it.
```

**Example:**

```
PROJECT UPDATE

[paste current project.md]

---

What changed this session:
- Finished the HTML skeleton and form fields
- Decided to use Tally instead of Zapier for the form — simpler
- Added task: write headline copy variants (3 options)
- Removed: "no backend" note — Tally handles it

Update the project.md to reflect this. Recalculate % complete based on done vs total tasks. Keep everything else unless I specifically say to change it.
```

---

## VARIANT 3 — Status Check (quick)

Use when you just want to see where things stand without a full update.

```
PROJECT STATUS

[Paste your current project.md here]

Give me a 3-line status summary: what's done, what's next, and any blockers or open questions I need to resolve.
```

---

## Tips

- Keep the description in Variant 1 honest and rough — Claude will ask clarifying questions for anything missing.
- In Variant 2, you only need to list what *changed*. Claude keeps everything else.
- Paste project.md at the top of any build session so Claude has full context, even if you're not updating it.
- The project.md lives in the repo root. Commit it alongside your code.

---

**Standard template:** [`../templates/project.md`](../templates/project.md)

**Progress %:** Update the header **Progress** field from ✅ Done vs ☐ To Do checkboxes (`done / (done + todo)`). Put `[TBD]` gaps in **Notes** (VARIANT 1).

**Monorepo / kits:** For products not at repo root, use the product folder root (e.g. `ai-proposals-agent/project.md`, `ai-agent-team/products/<kit>/project.md`). See [`PROJECT_MD_RULE.md`](PROJECT_MD_RULE.md).
