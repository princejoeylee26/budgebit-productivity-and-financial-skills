# Use hachibu with any AI agent

Setting up takes two steps for any agent:
1. **Connect BudgeBit** so the agent can read your tasks and money. hachibu doesn't work without it.
2. **Give the agent the hachibu skills.**

BudgeBit's agent connections are a **Pro** feature. You'll find them in the BudgeBit app under **More › Connections › Connect an agent**. That page shows the exact address and steps for your agent, so always copy from there. The addresses below are placeholders.

## Step 1 · Connect BudgeBit

| Agent | How | Key needed? |
|---|---|---|
| **Claude** (claude.ai, Desktop, mobile) | Settings › Connectors › Add custom connector. Paste the **Claude** address from BudgeBit, tap Connect, sign in, then tap Allow. | No (sign-in) |
| **Claude Code** | `claude mcp add --transport http budgebit <MCP address> --header "Authorization: Bearer $BUDGEBIT_KEY"` | Yes |
| **Gemini app** | Settings › Connectors (or Apps) › Add custom connector. Paste the **Gemini** address (it ends in `/mcp`), leave the OAuth fields empty, then sign in and tap Allow. | No (sign-in) |
| **Gemini CLI** | In `~/.gemini/settings.json`: `{"mcpServers": {"budgebit": {"httpUrl": "<Gemini address>", "headers": {"Authorization": "Bearer <key>"}}}}` | Yes |
| **Hermes** | In `~/.hermes/config.yaml`: `mcp_servers: {budgebit: {url: "<MCP address>", headers: {Authorization: "Bearer <key>"}}}`, then restart Hermes | Yes |
| **Cursor, Windsurf, VS Code and other MCP clients** | `{"mcpServers": {"budgebit": {"type": "http", "url": "<MCP address>", "headers": {"Authorization": "Bearer <key>"}}}}` | Yes |
| **Codex and other agents with MCP over HTTP** | Add an HTTP MCP server named `budgebit` with the MCP address and an `Authorization: Bearer <key>` header, using your agent's MCP config | Yes |
| **No MCP** (scripts, n8n, GPT Actions) | Plain HTTP: `POST <MCP address>/tools/<tool name>` with the key. The OpenAPI spec is at `<MCP address>/openapi.json`. | Yes |

**About keys**
- You create a key in BudgeBit under More › Connections. It's shown **once**, and it starts with `bb_pat_`.
- Store it in an environment variable or your agent's secret store. **Never paste it into a repo, a prompt or a skill file.**
- Each key has scopes:
  - `read`: everything you can see in the app.
  - `draft`: the `propose_*` tools. Drafts wait for your tap in **BudgeBit › Assistant**.
  - `tasks` (optional): direct task tools such as `create_tasks` and `update_task`, which save immediately.
- For hachibu, turn on `read` and `draft`. Add `tasks` only if you want the coach to create lists and memory tasks without tapping each draft.
- Limits: about 60 weighted calls per minute per key and 5,000 per day. The agent gets a clear "slow down" message if it goes over.
- You can revoke a key anytime in More › Connections.

## Step 2 · Give the agent the skills

| Agent | Install |
|---|---|
| **Claude Code** | Plugin: `/plugin marketplace add princejoeylee26/budgebit-productivity-and-financial-skills`, then `/plugin install hachibu@hachibu`. Or clone the repo and open Claude Code inside it. |
| **Claude.ai, Desktop, mobile** | Download the zips from the latest Release. Upload each one under Settings › Capabilities › Skills. |
| **Codex** | Clone the repo. Codex reads `AGENTS.md`, and the skills are also at `.agents/skills/`. |
| **Gemini CLI** | Clone the repo and run `gemini` inside it. `GEMINI.md` loads `AGENTS.md`. |
| **Hermes** | Copy the folders in `.claude/skills/` into your Hermes skills folder. They use the standard `SKILL.md` format. Or point Hermes at `AGENTS.md`. |
| **Cursor, Windsurf, VS Code agents** | Clone the repo or add it to the workspace. These agents read `AGENTS.md`. |
| **Anything else** | Put `AGENTS.md` and the SKILL.md you need into the agent's instructions or system prompt, and let it open the `references/` files when needed. |

## Step 3 · Start
Say **"set me up"**. hachibu asks your top 3 priorities, learns from your BudgeBit data, and drafts your Coach Memory in BudgeBit.

## Staying up to date
Agents with web access check for a newer hachibu during onboarding and weekly reviews, and they ask before updating (see `AGENTS.md`). BudgeBit also adds tools over time. When the coach notices one it doesn't know yet, it suggests an update.
