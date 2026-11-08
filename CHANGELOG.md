# Changelog

All notable changes to hachibu. Versions follow [semver](https://semver.org): patch = wording, minor = new playbook/principle/workflow/eval, major = memory layout or behaviour users rely on (with a migration note).

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
