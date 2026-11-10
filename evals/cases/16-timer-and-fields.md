# 16 · Timer and custom fields
skill: hachibu
prompt: "Start a timer on my writing task and set its Stage to Draft"
setup: Connection has the `tasks` scope. One open task "Write chapter" in a list whose fields are `Stage (select: Idea, Draft, Done)`. Case A: BudgeBit Pro. Case B: BudgeBit Free, where `start_timer` returns "The task timer is a Pro feature."

## Expected behaviour
- Finds the task with `list_tasks` first; doesn't create a new one.
- Sets the field with `update_task` `custom_fields: { "Stage": "Draft" }`, using the option label from `list_task_lists`.
- Case A: calls `start_timer` once and says which timer it replaced, if any.
- Case B: says in one sentence that the timer needs Pro; the field change still goes through; no retry.

## Rubric
Must:
- [ ] Uses the field and option names shown by BudgeBit, never invented ones
- [ ] Says exactly what changed
- [ ] On Free: no retry, upgrade mentioned at most once
- [ ] Doesn't claim time was tracked when the timer didn't start
