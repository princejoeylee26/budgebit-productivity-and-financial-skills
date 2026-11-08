# Onboarding analysis

Read this when onboarding a new person or refreshing memory. Use only the user's BudgeBit data; mark every pattern with evidence and confidence.

## 1 · Pull data
- `get_context`, `list_task_lists` (folders, counts), `task_summary`, `recall_memories`.
- `list_tasks` with `include_done: true`, `limit: 100`, in windows of 7–14 days (`due_after`/`due_before`) covering ≥6 weeks back and 2 weeks forward. If a window says "Showing 100 of N", split it.
- Open by `task_id` any task whose title suggests a plan, routine, schedule, strategy, training plan or launch.
- Money: `month_summary` (`months: 3`), `budget_status` (this month), `list_bills` (`due_within_days: 30`), `list_pots`.

## 2 · Find anchors
Recurring tasks at similar times on most days (morning routine, sleep, meals, work blocks, commute, training, faith, family dinners). Anchor = appears on ≥60% of days in the window at a similar time (±30 min). Record start–end and days.

## 3 · Energy windows
- Completion rate by start hour and by list (use `scripts/energy_stats.py` in the hachibu skill when available).
- Peak window = hours where Peak-type tasks (build, write, plan, study) actually get done most. If <10 data points, mark confidence low and ask.
- Low times = hours with lowest completion or right after training/commute.

## 4 · Load and failure patterns
- Days with >3 deadlines that went overdue (muri).
- Weekday vs weekend completion (mura).
- Which lists pile up overdue; which always get done.
- Training load: long or double sessions and what happens to work after them.

## 5 · Context and strategies
- Roles from list and folder names (job, businesses, training, family).
- Goals and strategies written in task descriptions (launch dates, races, content plans, review rituals). Record with the source task title and date.

## 6 · Money context (no balances stored)
- Income rhythm (pay dates from bills/planned income), top 3 categories, budgets set or not, savings goals in pots.

## 7 · Show and ask
Show a 5–8 line profile:
```
Day starts ~05:30 (routine, 90% of days) · high
Best focus: 13:30–16:30 on home days (14 of 18 build tasks done here) · med
Weekends slip: 40% routine completion Sat vs 92% weekdays · high
Overdue pile: marketing/admin, 8 due on Fri 6 Nov · high
```
The top 3 priorities question has already been asked at the start (see SKILL.md). Now ask at most 3 more questions from the bank, picking the ones with the lowest confidence:
- What time do you usually wake and sleep? Is the midday block a nap or night-shift sleep?
- What are your fixed work hours or shifts, and which days are office days?
- When do you feel sharpest for hard thinking?
- What are your top 1–3 goals for the next 3 months?
- Any day you keep light or off-limits (faith, family, rest)?
- Theme: kami names (☀ Amaterasu, 🏹 Hachiman…) or neutral?
- Do you have a monthly savings goal or a pay date I should plan around?

## 8 · Write memory
Fill the templates with confirmed facts and remaining open questions. Check `list_task_lists` for a Coach list. If it exists, use its `list_id`; if not, draft with `list_name: "Coach"` and, if the draft can't create the list, ask the user to create a "Coach" list in the app first. Draft the parent Coach Memory with `propose_task`, then each subtask with `parent_id` once the parent is confirmed (re-fetch its id with `list_tasks` `search: "Coach Memory"`). Tag all with `coach-memory`.
