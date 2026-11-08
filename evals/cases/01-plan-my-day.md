# 01 · Plan my day
skill: hachibu
prompt: "Plan my day"
setup: Coach Memory exists with anchors and a Peak window; 6+ tasks due today, 3+ overdue.

## Expected tool calls
- Budgebit:get_context (first)
- Budgebit:list_tasks search "Coach Memory" → open by task_id; Budgebit:recall_memories
- Budgebit:task_summary
- Budgebit:list_tasks due today; Budgebit:list_tasks overdue_only

## Expected behaviour
- Energy forecast line, top 3, time-blocked plan with zone labels, load % and free time, one "why" line, one next step, offer of drafts.

## Rubric
Must:
- [ ] Planned controllable load ≤ ~80% and shown
- [ ] Anchors from memory untouched
- [ ] Every block has start and end
- [ ] Max 3 must-dos; hardest Peak task in the Peak window
- [ ] No invented tasks or times
Should:
- [ ] Names at most one law or principle
- [ ] ≤ ~12 lines
