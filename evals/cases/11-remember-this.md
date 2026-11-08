# 11 · Remember this
skill: hachibu-memory
prompt: "Remember that I never want calls before 10:00"
setup: Coach Memory exists.

## Expected tool calls
- Budgebit:list_tasks search "Coach Memory" → open; Budgebit:propose_task_update with full description

## Rubric
Must:
- [ ] Added under Rules with today's date and a why
- [ ] No duplicate if a similar rule exists (it is replaced)
- [ ] One-line confirmation naming where to confirm in BudgeBit
