# 06 · When should I film videos?
skill: hachibu
prompt: "When should I film videos?"
setup: Coach Memory has energy windows; a filming task exists without a time.

## Expected tool calls
- Budgebit:get_context, memory load (Energy), Budgebit:list_tasks for the next 7 days

## Expected behaviour
- Classifies filming as Creative; proposes the next rested Creative window (not after hard training), batched; one reason; one draft offered.

## Rubric
Must:
- [ ] Specific date and time range in local time
- [ ] Day stays ≤ ~80% after adding it
- [ ] Not in a post-training or low window
Should:
- [ ] Mentions batching (Carlson) in a few words
