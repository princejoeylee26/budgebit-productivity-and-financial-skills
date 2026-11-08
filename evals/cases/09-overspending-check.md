# 09 · Am I overspending this week?
skill: hachibu-money
prompt: "Am I overspending this week?"
setup: Budgets set this month; some categories in warn/over.

## Expected tool calls
- Budgebit:get_context, Budgebit:budget_status (this month), Budgebit:list_transactions (week to date, expense)

## Expected behaviour
- One-line verdict with % of budgets used vs % of month passed, up to 3 flagged categories, one action, source line.

## Rubric
Must:
- [ ] Every amount matches tool output formatting
- [ ] Transfers excluded from spending
- [ ] Labels figures as month or week to date
- [ ] ≤8 lines
Should:
- [ ] Hara hachi bu flag for categories >80% early in the month
