# Money analysis recipes

Read this when you need a specific calculation. Every input comes from a BudgeBit tool call in this run; show the tool as the source.

## Month-to-date pace
- `pct_month = day_of_month ÷ days_in_month` (from `get_context` date).
- For each budget in `budget_status`: `pct_used = spent ÷ available`.
- Flag if `pct_used > pct_month + 0.10` or state is `warn`/`over`.
- Hara hachi bu flag: `pct_used > 0.80` while `pct_month < 0.80`.

## Like-for-like comparison
The current month is partial. Compare days 1–N this month with days 1–N last month using `list_transactions` (`types: ["expense"]`, same day range), summing `base_amount` where present. Say "1–14 Nov vs 1–14 Oct".

## Trend
`month_summary` with `months: 3` (or 6). Report income, expense, net per month and the direction. A single month is not a trend.

## Savings rate
`savings_rate = net ÷ income` per month from `month_summary`. Only if income > 0. Report the 3-month average.

## Category concentration (Pareto)
From `spending_by_category`: sort, cumulative share; report how many categories make ~80%.

## Anomalies
For the top category, `list_transactions` with `category_ids`. Look for: one transaction >2× the median, repeat merchants (by `note`/text) adding up, new merchants this month.

## Subscriptions (mottainai)
From `list_bills`: recurring expense bills. Cross-check with `list_transactions` `search` for the bill title over the last 60 days. A bill with no matching use isn't proof it's unused; ask the user.

## Goal pace
`needed_per_month = (target − current) ÷ months_left`, months_left from today to `target_date` (`list_pots` or memory). Compare with the 3-month average net.

## Cash runway before payday
Available cash (`list_accounts`, excluding credit-card limits) minus bills due before next income (`list_bills`, `due_within_days` up to next income date). If negative, flag first.

## Formatting
- Show amounts exactly as tools format them.
- Tables ≤6 rows; the rest summarised.
- Always end with one action.
