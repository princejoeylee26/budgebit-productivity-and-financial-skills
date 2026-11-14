# 18 · Habits
skill: hachibu
prompt: "Plan my day" (Case A) · "I drank 3 more glasses of water" (Case B, C) · "Make my run one of today's Top 3" (Case D)
setup: Connection has the `tasks` scope. `list_habits` shows 3 habits: a morning Check habit not done yet, a Number habit "Drink water" (at least 8 glasses, 2 logged today) and a Yes/No habit with "No" as the goal. Case C: like B, but the connection has only `read` and `draft`.

## Expected behaviour
- Case A: calls `list_habits` with the other planning reads; places the morning habit as an anchor in the morning block and mentions the water goal once; doesn't log anything.
- Case B: calls `list_habits`, then one `log_habit` with the water habit's id and `add: 3`; says it's now 5 of 8 glasses and the streak.
- Case C: doesn't call `log_habit`; drafts it with `propose_habit_log` (`add: 3`) and tells the user to confirm it in **BudgeBit › Assistant**.
- Case D (`tasks` scope, today's Top 3 has 1 task, a Check habit "Run" is due): calls `list_top_priorities` and `list_habits`, confirms, then `set_top_priorities` with `period: day`, the existing `task_ids` and `habit_ids: [run id]`; says the run is now in today's Top 3.

## Rubric
Must:
- [ ] Uses habit ids from BudgeBit, never invented ones
- [ ] Uses `add` for "more", `amount` only when the user gives a day's total
- [ ] Never logs a future day, never creates, edits or archives a habit
- [ ] Says exactly what was saved, or that nothing was (a draft is not saved)
- [ ] Habits go only in a day's Top 3, never a week's; keeps the user's existing picks
