# 02 · Slept 4 hours
skill: hachibu
prompt: "I slept 4 hours, what now?"
setup: Coach Memory exists; it's mid-morning local time; a Peak task is planned this afternoon.

## Expected tool calls
- Budgebit:get_context, memory load, Budgebit:list_tasks due today

## Expected behaviour
- Treats it as a Susanoo / low-energy day: 1 must-do, Peak task moved to a later good day (draft offered), Recovery protected (nap or early night if memory allows).

## Rubric
Must:
- [ ] Re-plans only from the current local time onward
- [ ] Peak work moved out or shrunk
- [ ] ≤5 lines
- [ ] No medical claims; no guilt language
Should:
- [ ] Offers to note the pattern in memory if it repeats
