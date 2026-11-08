---
name: hachibu-improve
description: Improves the hachibu skills themselves. Turns patterns from a user's coaching log, or a reported issue, into a generalised change with no personal data, adds or updates an eval case, runs the checks, bumps the version, updates the changelog, and opens a pull request. Use when the user says "improve the skill", "the coach keeps getting X wrong", "add a playbook for…", "add this principle", "make hachibu better", "contribute this", or when hachibu-review flags a skill-level idea. Works best in Claude Code inside the hachibu repository.
---

# hachibu-improve · the skill learns too

Two loops make hachibu better:
1. **Personal loop** (in BudgeBit memory): the coach adapts to one person. Handled by `hachibu-memory` and `hachibu-review`.
2. **Skill loop** (in the repository): when a lesson would help everyone, it becomes a change to the skills, reviewed in a pull request. This skill runs that loop.

## Rules
1. **No personal data in the repository, ever.** No names, employers, task titles, list names, places, amounts, dates of the user's life, or account details. Rewrite every example with neutral placeholders (`<Peak task>`, `Alex`, `1,500.00`).
2. A change must generalise: it should help a user with a different job, schedule and currency.
3. Every behaviour change gets an eval case in `evals/cases/` (new or updated) **before** editing the skill text.
4. Keep SKILL.md files under ~500 lines; detail goes in `references/`, linked one level deep.
5. BudgeBit stays the source of truth; never add a rule that lets the coach guess figures or save without confirmation.
6. Never push to someone else's branch; open a PR for review. The maintainer decides what merges.

## Workflow
Copy and work through:
```
- [ ] Gather the signal: Memory · Coaching log "Skill-level ideas", or the issue text
- [ ] Write the problem in one sentence (Kidlin's law) and who it affects
- [ ] Check it's general: would it help 3 very different users? If not, keep it in personal memory
- [ ] Find the right file: SKILL.md workflow, a reference, a playbook, a template
- [ ] Write or update an eval case in evals/cases/ (format: evals/README.md)
- [ ] Make the smallest change that fixes it (Gall's law)
- [ ] Run checks: python3 scripts/check_skills.py (frontmatter, links, shared-file sync, personal-data scan)
- [ ] Bump the version (semver) in VERSION and .claude-plugin/marketplace.json, run scripts/sync-shared.sh, and add a CHANGELOG.md entry: what and why
- [ ] Branch, commit, open a PR with the eval and the reason
```

## Releasing (maintainers)
1. Bump `VERSION`, then run `scripts/sync-shared.sh`. It stamps the version into every skill's `references/updates.md`, so installed copies can tell when they're behind.
2. Set the same version in `.claude-plugin/marketplace.json`, and add a CHANGELOG entry whose first bullet is the change users will care about most. The update check shows that bullet.
3. Merge to main, then push a tag `v<version>`. CI builds the zips for Claude.ai and attaches them to a GitHub Release.
4. Installed copies see the new version at their next update check ([references/updates.md](references/updates.md)).

## New BudgeBit tools
When BudgeBit adds tools (the update check flags them), add them to `shared/budgebit-tools.md`. Then use them in the relevant workflow, keeping the draft-only and never-move-money rules, add an eval, and release a minor version.

## Versioning
- **patch**: wording, typo, clearer example.
- **minor**: new playbook, principle, workflow step, eval.
- **major**: changed memory layout or behaviour existing users rely on (include a migration note).

## Outside the repository
On Claude.ai or mobile (no repo access): write the proposal as a short GitHub issue text using the templates in `.github/ISSUE_TEMPLATE/` ("coach got it wrong", "new principle", "new playbook") and give it to the user to post. Never include personal data in the issue.

## Personal-data scan
`scripts/check_skills.py` blocks common leaks (emails, phone numbers, long digit runs, and terms listed in `scripts/blocklist.txt`). Users add their own private terms to a local, gitignored `scripts/blocklist.local.txt` so the scan protects them without publishing those terms.
