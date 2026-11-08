# 05 · Weekly review
skill: hachibu-review
prompt: "Weekly review"
setup: Coach Memory with Weekly log containing last week's line; this week has done and undone tasks.

## Expected tool calls
- Budgebit:get_context, memory (Coach Memory, Weekly log, Coaching log, Energy)
- Budgebit:list_tasks include_done:true this week and last week
- Budgebit:task_summary, Budgebit:budget_status

## Expected behaviour
- Done/planned with comparison, strong vs slipped, overdue trend, money line, coach self-check, next week's vital few, exactly one kaizen, the "most/least useful" question, memory drafts.

## Rubric
Must:
- [ ] All counts come from tool results
- [ ] Exactly one kaizen
- [ ] Coach self-check present (planned vs done Peak blocks)
- [ ] Memory updates are drafts with full descriptions
Should:
- [ ] ≤15 lines
