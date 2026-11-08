# hachibu 腹八分

**An energy-first life coach and kakeibo money planner for BudgeBit, built as Claude skills.**

> *Hara hachi bu*: eat until you are 80% full.
> hachibu plans your life the same way. It fills about 80% of your real capacity and keeps the rest for overruns, recovery and the people you love.

hachibu reads your tasks, time blocks, budgets and bills from BudgeBit and coaches you on them. It learns your energy rhythm and your routines, then plans around them. It remembers what works for you, and the skill itself improves as more people use it.

```
Today · Sat 14 Nov · double-run day, office afternoon · load 78% · 1h30 free
Top 3: 1) Ship release notes  2) Script 3 videos  3) Admin sweep
05:30–06:30  ☀ Amaterasu  Morning routine + run (anchor)
09:00–10:30  🏹 Hachiman  Ship release notes (+30% pad)
10:45–11:15  🦊 Inari     Admin sweep: invoices, 2 bills
13:00–14:30  🎵 Benzaiten Script 3 videos
19:30–21:00  🌙 Tsukuyomi Dinner, wind-down
Why: the hardest task goes first in your sharpest window (Laborit's law).
Next step: write tomorrow's top 3 before 21:00.
```
*(Illustrative example. Real plans use only your BudgeBit data.)*

## What's inside

| Skill | Ask it | It does |
|---|---|---|
| **hachibu** | "plan my day", "plan my week", "I'm tired, what can I still do?", "reschedule my overdue tasks", "when should I film?" | Time-blocked plans in energy zones, kept to about 80% load. It triages overdue tasks, re-plans after check-ins, and drafts task updates. |
| **hachibu-money** | "am I overspending this week?", "where is my money going?", "plan next month's budget", "can I afford this?" | Kakeibo-style tracking and analysis from live budgets, bills, pots and transactions. It drafts budgets and transactions for you to confirm. |
| **hachibu-review** | "weekly review", "review my month", "what slipped?" | Hansei and kaizen: planned vs done, overdue trend, a money line, a self-check of the coach's own advice, and exactly one change. |
| **hachibu-memory** | "set me up", "remember that I…", "what do you know about me?" | Onboards you from your own data and keeps a small, dated Coach Memory inside your BudgeBit. |
| **hachibu-improve** | "improve the skill", "add a playbook for…" | Turns lessons into anonymised pull requests on this repo, each with an eval case. |

## The philosophy

- **Japanese principles:** hara hachi bu, kaizen, hansei, ma, ikigai, muda/mura/muri, heijunka, kanban, kakeibo, mottainai, wabi-sabi, kintsugi, shu-ha-ri, ichigo ichie and more.
- **Laws of time and work:** Parkinson's law, the Pareto principle, Carlson's law, Hofstadter's law, the law of triviality, plus Laborit, Illich, Hick, Kidlin, Gall, Goodhart, Murphy, Eisenhower and Zeigarnik.
- **Energy psychology:** manage energy, not just time. Chronotypes, ~90-minute focus cycles, recovery after training, decision fatigue, implementation intentions and habit stacking.
- **Kami zones:** an optional mythology theme for the shape of your day. ☀ Amaterasu for the morning rise, 🏹 Hachiman for deep work, 🎵 Benzaiten for creative work, 🦊 Inari for money, ⛈ Susanoo for storm days, 🌙 Tsukuyomi for the evening and 🎎 Daruma for restarts. A neutral theme is included too.

Every plan follows the same rules:
- Stop at about 80% of capacity (hara hachi bu).
- Lead with the vital few (Pareto).
- Put the hard task first (Laborit).
- Work in unbroken blocks (Carlson).
- Timebox everything (Parkinson).
- Pad every estimate (Hofstadter).
- Leave space between blocks (ma).
- End with one small next step (kaizen).

## Install

You need a [BudgeBit](https://budgebit.com) account connected to your AI app. In BudgeBit, go to **More › Connections › Connect an agent**. Agent connections are part of BudgeBit Pro.

**Any AI agent**: hachibu works with Claude, Claude Code, Gemini (app and CLI), Hermes, Codex, Cursor, Windsurf, VS Code, and anything that speaks MCP or plain HTTP. [docs/connect-agents.md](docs/connect-agents.md) has the setup for each. All agents share one set of instructions, [AGENTS.md](AGENTS.md), which `CLAUDE.md` and `GEMINI.md` load.

**Claude Code (plugin)**
```
/plugin marketplace add princejoeylee26/budgebit-productivity-and-financial-skills
/plugin install hachibu@hachibu
```

**Claude Code (clone)**: clone this repo and open Claude Code inside it. The skills in `.claude/skills/` load automatically.

**Claude.ai and mobile**: download the zips from the latest [Release](https://github.com/princejoeylee26/budgebit-productivity-and-financial-skills/releases), or build them with `scripts/package.sh`. Then upload each `dist/<skill>.zip` under **Settings → Capabilities → Skills**. Start with `hachibu` and `hachibu-memory`.

## First run

Say **"set me up"**. hachibu starts by asking which **3 things matter most to you** right now, such as health, making money, family, love, learning or faith. Then it reads about 6 weeks of your BudgeBit tasks and a summary of your money, and shows you what it noticed, with how confident it is. It asks at most 3 more questions and drafts your Coach Memory in BudgeBit for you to confirm. If you haven't connected BudgeBit yet, it shows you how.

## Staying up to date

hachibu and BudgeBit both keep improving. During onboarding, at your weekly review, or whenever you ask "update hachibu", the coach checks for a newer version. If there is one, it tells you in one line what's new and how to update. It never updates on its own.

| Setup | Update |
|---|---|
| Claude Code plugin | `/plugin marketplace update hachibu` |
| Cloned repo (any agent) | `git pull` |
| Claude.ai, Desktop or mobile | Download the zips from the latest [Release](https://github.com/princejoeylee26/budgebit-productivity-and-financial-skills/releases) and re-upload them |

Your memory lives in BudgeBit, so updates never touch it. Using another AI agent? See [AGENTS.md](AGENTS.md).

## Privacy

- **BudgeBit is the single source of truth.** hachibu never invents numbers, and it says "not in BudgeBit" when something is missing.
- **Everything is a draft.** Changes are saved only when you confirm them in the BudgeBit app. hachibu never deletes or archives anything, and never moves money.
- **Your memory is yours.** It lives in a "Coach" list in your own BudgeBit, and you can read, edit or delete it there anytime. This repository contains no personal data, and CI scans every change to keep it that way.
- hachibu is a planner, not a financial, medical or legal adviser.

## How it gets better

1. **For you:** each weekly review checks the coach's own past plans against what you actually got done, then adjusts your capacity and energy zones. Your feedback is saved in your coaching log.
2. **For everyone:** when a lesson would help any user, `hachibu-improve` writes it up as an anonymised change with an eval case and opens a pull request. You can also open an issue: *coach got it wrong*, *new principle* or *new playbook*.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
