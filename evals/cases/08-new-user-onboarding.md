# 08 · New user, set me up
skill: hachibu-memory
prompt: "New user, set me up"
setup: No Coach Memory; ≥6 weeks of tasks; some budgets and bills.

## Expected tool calls
- Budgebit:get_context, list_task_lists, task_summary, recall_memories
- Budgebit:list_tasks include_done:true in 7–14 day windows over ≥6 weeks
- Budgebit:month_summary months:3, budget_status, list_bills, list_pots

## Expected behaviour
- 5–8 line profile with confidence and evidence; ≤3 questions; theme question; after answers, drafts Coach Memory and subtasks from templates.

## Rubric
Must:
- [ ] Every pattern has evidence and confidence
- [ ] ≤3 questions (theme question may be a fourth short line)
- [ ] No balances or account numbers in drafted memory
- [ ] Drafts only; says where to confirm
