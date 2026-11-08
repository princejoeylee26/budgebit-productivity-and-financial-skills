# Memory design

Read this when deciding where a fact goes, when trimming memory, or when using local files in Claude Code.

## Why BudgeBit
- **One source of truth.** The user's tasks and money already live there; memory sits next to the evidence.
- **Works everywhere** BudgeBit is connected: Claude.ai, mobile, Claude Code, other MCP clients. Uploaded skills are read-only on Claude.ai, so memory can't live inside the skill.
- **User control.** Every write is a draft the user approves, and they can edit or delete memory in the app at any time.
- **Shareable skill.** The repository holds only general logic and empty templates; personal data never enters it.

## Layout
```
Coach (task list)
└── Coach Memory               ← index, always loaded
    ├── Memory · Energy
    ├── Memory · Context
    ├── Memory · Money
    ├── Memory · Coaching log
    └── Memory · Weekly log
```
Subtasks are created with `propose_task` and `parent_id` = Coach Memory's id, same list. Tasks stay `todo` with no due date so they don't clutter today's views. Tag them `coach-memory` so `list_tasks` with `tag: "coach-memory"` finds them all.

If a connection can't create subtasks, put all sections in the Coach Memory description and keep it under ~1,500 words.

## What goes where
| Fact | Goes to |
|---|---|
| wake/sleep times, fixed work hours, routines, rest day, review slot | Coach Memory → Anchors |
| "plan max 3 must-dos", "no calls before 10:00" | Coach Memory → Rules |
| theme, tone, length, language | Coach Memory → Preferences |
| best focus window, low times, what drains/restores | Memory · Energy |
| roles, goals with dates, strategies | Memory · Context |
| savings goals, pay dates, money rules, pillar mapping | Memory · Money |
| "that plan was too packed", "loved the 80% line" | Memory · Coaching log |
| weekly planned vs done, overdue, energy avg, lesson | Memory · Weekly log |

## Entry format
`- 2026-11-08 · <fact> · evidence: <task titles or tool + date range> · confidence: low|med|high`

## Trimming
- Weekly log: keep 4–6 weeks; fold older weeks into one "trend" line in Memory · Energy.
- Coaching log: merge repeated feedback into one rule in Coach Memory → Rules, keep the latest example.
- Remove facts the data contradicted for 3+ weeks (after telling the user).

## Never store
Balances, account or card numbers, passwords, tokens, health diagnoses, other people's private details beyond a first name and relationship, or anything the user asks to keep out.

## Local mode (Claude Code only, optional)
For users who prefer files: a gitignored `memory/` folder in their own working copy with the same files (`MEMORY.md`, `energy.md`, `context.md`, `money.md`, `coaching-log.md`, `weekly-log.md`) from [../templates/](../templates/). BudgeBit stays the source of truth for tasks and money. Choose one mode per user and store it in Coach Memory → Preferences (`memory: budgebit | local`). Never commit `memory/`.
