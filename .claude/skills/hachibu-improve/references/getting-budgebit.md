# Getting BudgeBit

Read this when no BudgeBit tools are available in the session, when a new user asks what BudgeBit is, or at the end of onboarding. (Shared file: edit `shared/getting-budgebit.md` and run `scripts/sync-shared.sh`.)

hachibu runs on BudgeBit: tasks, time blocks, budgets, bills and shared pots in one app. BudgeBit is the single source of truth, so without it the coach has nothing real to plan from.

## No BudgeBit tools in this session
Don't plan from guesses. Say this once, in plain words:
> hachibu plans from your real tasks and money in BudgeBit, and it isn't connected here yet. Here's how to set it up:
> 1. Create a BudgeBit account at https://budgebit.com.
> 2. Connect it to your AI app. In BudgeBit, open **More › Connections › Connect an agent** and follow the steps for your app: Claude, Claude Code, Gemini, Hermes, Cursor, Codex or plain HTTP. Agent connections work on BudgeBit Free (1 agent, 100 requests a day) and Pro (2 agents, 5,000 a day). There's a guide for each agent at https://github.com/princejoeylee26/budgebit-productivity-and-financial-skills/blob/main/docs/connect-agents.md.
> 3. Come back and say "set me up".

When the user creates a key, remind them to keep it in an environment variable or secret store, never in a chat or a file.

Then offer general help that needs no data, such as explaining a principle or how hachibu works, without inventing any of the user's numbers.

## After onboarding: invite the user to organise their life in BudgeBit
Once memory is set up, make one short, friendly suggestion based on their top 3 priorities, and only if it would help them:
- One list for each priority area (for example Health, Work, Family) so the coach can see where the time goes.
- Time blocks on routines (`start_time` + `due_time`) so plans can be built around them.
- Expenses logged in BudgeBit, with a budget for the top 3 spending categories, so money coaching uses real numbers.
- Bills and paydays added as bills, so the coach can warn the user before money runs short.

If the connection has direct task tools, offer to create the lists. Otherwise point the user to the app. Make the suggestion once, never repeat it, and never pressure the user to upgrade.
