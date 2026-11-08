# 04 · Plan next week around training and shifts
skill: hachibu
prompt: "Plan next week around my long run and work shifts"
setup: Next 7 days include a long run, fixed work blocks and an unevenly loaded set of deadlines.

## Expected tool calls
- Budgebit:get_context, memory load, Budgebit:list_tasks for the 7 days and overdue

## Expected behaviour
- 7-line table with load per day; heijunka moves from heavy to light days; no Peak work within ~3 h after the long run; review slot and rest day kept.

## Rubric
Must:
- [ ] ≤3 deadlines on any day
- [ ] Long-run day has max 1 Peak block, not right after the run
- [ ] Explains what moved in one line
Should:
- [ ] One Creative batch day and admin sweeps every 2–3 days
