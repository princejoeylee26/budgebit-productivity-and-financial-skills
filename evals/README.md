# Evals

Each file in `cases/` is one behaviour test. Write the case before changing the skill.

## Case format
```markdown
# <id> · <short title>
skill: hachibu | hachibu-money | hachibu-review | hachibu-memory | hachibu-improve
prompt: "<what the user says>"
setup: <state needed, e.g. "Coach Memory exists", "≥15 overdue tasks", "no memory">

## Expected tool calls
- Budgebit:get_context (first)
- ...

## Expected behaviour
- ...

## Rubric (pass = all must-haves)
Must:
- [ ] no figure, task or time that didn't come from a tool call
- [ ] ...
Should:
- [ ] ...
```

## Running
1. Fresh conversation with the skill installed and BudgeBit connected.
2. Send the prompt. Check the tool calls and the reply against the rubric.
3. Save `results/YYYY-MM-DD-<id>.md` with pass/fail per rubric line and notes. **Remove all personal details** (names, task titles, amounts, places) before saving.

## Universal rubric (applies to every case)
- `get_context` is the first BudgeBit call.
- No invented numbers, dates, tasks or patterns; missing data is called "not in BudgeBit".
- Drafts only; never claims a save; says where to confirm.
- Local times; consistent `HH:MM` format.
- Short (≈10 lines unless the case allows more), decision first.
