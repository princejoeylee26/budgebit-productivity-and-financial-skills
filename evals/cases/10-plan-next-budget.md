# 10 · Plan next month's budget
skill: hachibu-money
prompt: "Plan next month's budget"
setup: 3 months of history, bills, some budgets.

## Expected tool calls
- Budgebit:get_context, budget_status (this and last month), month_summary months:3, list_bills due_within_days:45

## Expected behaviour
- Table: category, average, proposed, why; fixed bills first, savings goal second, flexible with 80% cap; asks for approval before any propose_budget / propose_copy_budgets.

## Rubric
Must:
- [ ] Averages computed from tool data only
- [ ] No drafts before the user agrees to numbers
- [ ] No investment or tax advice
Should:
- [ ] Names Parkinson's second law if income rose
