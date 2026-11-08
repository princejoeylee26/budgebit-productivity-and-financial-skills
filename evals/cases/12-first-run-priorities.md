# 12 · First run asks top 3 priorities
skill: hachibu-memory
prompt: "I just installed hachibu"
setup: BudgeBit connected; no Coach Memory.

## Expected behaviour
- 2-line welcome, then the top 3 life priorities question before any analysis output.
- After answers: analysis, ≤3 more questions, drafts with `## Top 3 priorities` filled in the user's words.
- One BudgeBit organising suggestion tied to the priorities; never repeated.

## Rubric
Must:
- [ ] Priorities question is first
- [ ] Priorities stored dated, in the user's words
- [ ] BudgeBit suggestion appears once and isn't pushy
