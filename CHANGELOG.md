# Changelog

All notable changes to hachibu. Versions follow [semver](https://semver.org): patch = wording, minor = new playbook/principle/workflow/eval, major = memory layout or behaviour users rely on (with a migration note).

## [0.8.0] · 2026-11-14
- **Habits in Top 3:** a day's Top 3 can now hold habits. `list_top_priorities` lists them (`kind: habit`, goal, done) and `set_top_priorities` takes `habit_ids` for a day (after the tasks, 3 in all; left out = the day's habit picks stay).
- **Draft a habit check-in:** new tool `propose_habit_log` (`draft` scope) drafts a check-in the user confirms in BudgeBit, for connections without the `tasks` scope. Eval `18-habits` covers both.
- Pro's habit limit is now stated as up to 100.
- Why: some days the one thing that must happen is a habit, and read-and-draft connections can now log habits with the user's OK.

## [0.7.0] · 2026-11-14
- **Habits:** BudgeBit now has a Habit Tracker (Check, Yes/No and Number habits, streaks, strength). New tools `list_habits` and `habit_history` (any connection) and `log_habit` (`tasks` scope; logs today or a past day, never creates or deletes habits). Day planning places open habits as anchors; weekly reviews add a habit line (this week %, strength). New eval `18-habits`.
- Why: habits are the user's daily anchors, and logging "I drank 2 more glasses" by voice keeps the tracker honest without opening the app.

## [0.6.0] · 2026-11-11
- **Top 3 priorities:** BudgeBit now has a Top 3 for the day and for the week (on its Dashboard and Calendar). New tools `list_top_priorities` (any connection) and `set_top_priorities` (`tasks` scope; replaces a period's Top 3, never changes the tasks). Day and week planning read the user's Top 3 first and build around it; when it's empty the coach suggests 3 and, with the user's OK, saves them. Weekly reviews count how many Top 3 picks got done. New eval `17-top-3`.
- Why: the user's own picks are the best signal of what matters today, and a saved Top 3 stays visible in BudgeBit all day.

## [0.5.0] · 2026-11-10
- **Custom fields:** the tools reference covers BudgeBit's custom fields: `list_task_lists` shows each list's fields, `list_tasks` shows values and filters with `field` + `field_value`, and `create_tasks` / `update_task` take `custom_fields` by field name and option label.
- **Task timer:** new tools `start_timer` and `stop_timer` (Pro only, one timer at a time) and `time_tracked` (actual time by task and day). Weekly reviews use `time_tracked` for the priority balance when it has entries. New eval `16-timer-and-fields`.
- Why: the coach can compare planned time with real time, and keep a list's fields up to date without guessing.

## [0.4.0] · 2026-11-08
- **Works on BudgeBit Free:** agent connections are no longer Pro-only. Free connects 1 agent with 100 requests a day; Pro connects 2 with 5,000. Setup docs, the getting-BudgeBit steps and the tools reference say so.
- **Limit errors:** the tools reference explains BudgeBit's structured limit errors (`API_DAILY`, `API_RATE`, `API_DRAFTS`, `API_WRITES`, paused connections) and how the coach handles them: stop, say what was reached and when it resets in local time, mention the upgrade once. New eval `15-limit-reached`.
- Why: anyone can try hachibu for free, and the coach stays calm and honest when a daily budget runs out.

## [0.3.1] · 2026-11-08
- BudgeBit tools reference catches up with the server: `list_tasks` takes `assigned_to_me`; `create_tasks` takes `assignee_id` and `repeat` + `repeat_every`; `update_task` takes `assignee_id`; daily caps for drafts (~200) and direct task writes (~300) are listed.
- Why: the coach can filter to your own tasks, set up repeating tasks and plan around the real limits.

## [0.3.0] · 2026-11-08
- **Works with any AI agent:** setup steps for Claude, Claude Code, Gemini app and CLI, Hermes, Codex, Cursor, Windsurf, VS Code and plain HTTP are in `docs/connect-agents.md`. They match BudgeBit's own Connections page.
- `AGENTS.md` is now the single source of instructions. `CLAUDE.md` and `GEMINI.md` load it, and `.agents/skills` mirrors the skills for agents that look there.
- The BudgeBit tools reference now covers connection scopes (read, draft, tasks), the direct task tools (`create_task_list`, `create_tasks`, `update_task` with `append_description`), and rate limits. Drafts are confirmed in BudgeBit › Assistant.
- Onboarding can save Coach Memory directly when the connection has the tasks scope, after one OK from the user.
- Why: anyone can plug hachibu into the agent they already use, with the same rules everywhere.

## [0.2.0] · 2026-11-08
- **Update checks:** hachibu now tells you when a newer version is out, with one line on what's new and the update steps for your setup. It never updates by itself. It checks during onboarding, at the weekly review, or when you ask.
- **First-run priorities:** onboarding opens by asking your top 3 life priorities (health, money, relationships and so on). Plans, weekly reviews and money goals use them to pick what matters most and to flag a priority that got no time.
- **BudgeBit growth:** when BudgeBit adds tools, the coach notices and suggests an update. Maintainers have a documented path for adding new tools.
- **Getting BudgeBit:** if BudgeBit isn't connected, the coach explains how to connect it instead of guessing. After onboarding, it makes one friendly suggestion for organising life in BudgeBit.
- 3 new eval cases (first-run priorities, no BudgeBit, update check), `AGENTS.md` for any AI agent, a `VERSION` file, tagged releases with Claude.ai zips, and CI that checks the versions match.
- Why: installed copies stay current as hachibu and BudgeBit grow, and every new user starts from what matters to them.

## [0.1.0] · 2026-11-08
First release.
- **hachibu**: plan my day, plan my week, overdue triage, energy check-ins, "when should I do X", focus help. Energy model (Peak, Creative, Shallow, Recovery), 10 planning rules, kami and neutral zone themes, 9 playbooks, `energy_stats.py`.
- **hachibu-money**: kakeibo quick checks, spending analysis, next month's budget, afford-it checks, bills and subscriptions, savings goals, transaction logging, shared pots.
- **hachibu-review**: weekly and monthly hansei + kaizen reviews with a coach self-check that recalibrates capacity.
- **hachibu-memory**: onboarding from the user's own data, Coach Memory stored in BudgeBit (parent task + 5 subtasks), templates, optional local mode for Claude Code.
- **hachibu-improve**: the skill loop: anonymised changes, eval-first, versioned PRs.
- Evals (11 cases), CI checks (frontmatter, links, shared-file sync, personal-data scan), issue templates, plugin marketplace entry.
- Why: one coach that plans time, energy and money together, grounded only in BudgeBit data, and shareable with anyone.
