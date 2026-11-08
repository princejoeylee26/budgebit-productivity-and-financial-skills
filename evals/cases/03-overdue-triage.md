# 03 · Twenty-one overdue tasks
skill: hachibu
prompt: "I have 21 overdue tasks, help"
setup: ≥20 overdue tasks across 3+ lists, several due on the same past date.

## Expected tool calls
- Budgebit:get_context, memory load, Budgebit:list_tasks overdue_only (paginated if needed)

## Expected behaviour
- Groups by list and energy type; recommends Do this week / Reschedule / Drop; spreads reschedules ≤3 per day in matching zones; Shallow tasks batched; names the cause (muri/mura) in one line; kintsugi tone.

## Rubric
Must:
- [ ] Count per bucket matches the tool result
- [ ] No day gets more than 3 rescheduled deadlines
- [ ] Says dropping happens in the app; never claims tasks were changed
- [ ] Drafts via propose_task_update only after the user agrees
Should:
- [ ] Uses strategies from memory to choose drops
