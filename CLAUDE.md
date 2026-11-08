# CLAUDE.md

All shared instructions live in AGENTS.md, so every AI agent follows the same rules:

@AGENTS.md

## Claude-specific notes
- Claude Code loads the skills in `.claude/skills/` as project skills automatically. The plugin install is described in `docs/connect-agents.md`.
- BudgeBit tools appear as `mcp__Budgebit__<tool>` in Claude Code and as `Budgebit:<tool>` on Claude.ai.
- At session start, run the version check from AGENTS.md ("Keeping up to date") and tell the user in one line if they're behind.
