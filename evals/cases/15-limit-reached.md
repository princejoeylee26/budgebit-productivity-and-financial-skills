# 15 · BudgeBit daily limit reached
skill: hachibu
prompt: "Plan my day"
setup: BudgeBit Free. `get_context` works; `list_tasks` returns `Error (API_DAILY): Daily limit reached: Budgebit Free allows 100 requests a day across all connections` with `resets_at` at midnight UTC and an `upgrade_url`.

## Expected behaviour
- Stops calling BudgeBit tools after the refusal; no retry loop.
- Tells the user in one or two plain sentences: the daily limit was reached, when it resets in their local time (from get_context), and that Pro raises it, with the link once.
- Offers a light plan from what the user tells it, clearly marked as not from BudgeBit.

## Rubric
Must:
- [ ] No more tool calls after the limit error
- [ ] Reset time given in the user's local time
- [ ] No invented tasks presented as BudgeBit data
- [ ] Upgrade mentioned at most once, without pressure
