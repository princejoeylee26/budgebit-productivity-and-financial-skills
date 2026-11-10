# Updates

Read this when running an update check (onboarding, weekly review, or when the user asks "update hachibu" or "is there a new version"), or when this session shows BudgeBit tools that aren't in budgebit-tools.md. (Shared file: edit `shared/updates.md` and run `scripts/sync-shared.sh`.)

**Installed version: 0.5.0**
Home: https://github.com/princejoeylee26/budgebit-productivity-and-financial-skills

## When to check
Only during onboarding, the weekly review, or when the user asks. Never more than once per conversation, and never in the middle of a plan. The check is a one-line footnote, not a topic.

## How to check
1. If this agent can fetch web pages or run a shell, read
   `https://raw.githubusercontent.com/princejoeylee26/budgebit-productivity-and-financial-skills/main/VERSION`.
   If it can't, skip the check silently, unless the user asked, in which case give them the link above.
2. Compare it with the installed version above (semver).
3. If it's newer, read the top entry of `CHANGELOG.md` at the same raw path and pick its single most useful change.
4. Add one line at the end of the reply:
   `🆕 hachibu <new> is out (you have <old>): <one change>. Want the update steps?`
5. Never update anything by yourself. The user decides. If they say yes, give the steps for their setup:

| Setup | Update |
|---|---|
| Claude Code plugin | `/plugin marketplace update hachibu`, then restart Claude Code |
| Cloned repo (Claude Code, Codex, Cursor, Gemini CLI or any agent) | `git pull` in the repo. With the user's OK, the agent can run it |
| Claude.ai, Desktop or mobile | Download the new zips from the latest GitHub Release, then re-upload each one under Settings → Capabilities → Skills, replacing the old ones |
| Copied into another agent's prompt or rules | Copy the new SKILL.md files from the repo again |

Updating never touches the user's memory, because it lives in their BudgeBit.

## When BudgeBit adds tools
BudgeBit keeps growing. Each run, compare the BudgeBit tools this session offers with the tool tables in `budgebit-tools.md`.
- **New tool not in the tables:** use it only as its own description says, and keep every hachibu rule (drafts, never move money, never delete). At the next update check, mention it in one line: "BudgeBit added `<tool>`. A newer hachibu may use it." If the repo's latest version doesn't cover it either, offer to report it through `hachibu-improve` as a "new BudgeBit tool" issue.
- **A tool in the tables is missing:** fall back to the closest tool that is available, and tell the user only if it blocks the request.
