# Contributing to hachibu

Thank you for helping the coach get wiser. Every change must keep three promises: **BudgeBit is the source of truth**, **everything is a draft**, and **no personal data in the repo**.

## Ways to help
- **Open an issue**: *Coach got it wrong*, *New principle*, or *New playbook* (templates in `.github/ISSUE_TEMPLATE/`).
- **Open a pull request**: use the `hachibu-improve` skill in Claude Code, or follow the steps below by hand.

## Pull request steps
1. Describe the problem in one sentence and who it helps. It must generalise beyond one person's job, schedule or currency.
2. Add or update an eval case in `evals/cases/` first (see `evals/README.md`).
3. Make the smallest change that fixes it. SKILL.md stays under 500 lines; detail goes in `references/`.
4. If you edit `shared/`, run `scripts/sync-shared.sh`.
5. Run `python3 scripts/check_skills.py`. It must pass.
6. Bump `VERSION` and `.claude-plugin/marketplace.json`, run `scripts/sync-shared.sh`, and add a `CHANGELOG.md` entry (what and why).
7. Open the PR with the eval case and, if you ran it, an anonymised result in `evals/results/`.

## Writing style
- Coach voice: warm, calm, short, practical. Decision first.
- Name a principle or law in a few words; never lecture.
- Cite origins in references and keep claims modest where evidence is mixed.
- Placeholders in examples: `<Peak task>`, `Alex`, `1,500.00`, `Mon 3 Mar`.

## Privacy check
Add your own private words (your name, employer, project names, city) to `scripts/blocklist.local.txt`. It's gitignored, and the check uses it to stop you leaking them.
