# Kakeibo and money principles

Read this for the method behind hachibu-money, the money principles and laws, and how to phrase money coaching.

## Kakeibo (家計簿)
Created by Hani Motoko, Japan's first female journalist, in 1904 as a household account book for women managing a home. Popularised internationally by Fumiko Chiba's *Kakeibo: The Japanese Art of Budgeting and Saving Money* (2017).

The monthly cycle:
1. **Start of month**: write income, fixed costs, and a savings goal. The rest is what you can spend.
2. **During the month**: record every expense in four pillars: **needs** (survival: food, rent, transport, health), **wants** (optional: dining out, shopping), **culture** (books, courses, museums), **unexpected** (repairs, gifts, medical).
3. **Each week**: a short look at what was spent.
4. **End of month**: answer the four questions and write one improvement.

*In BudgeBit:* income and expense come from `month_summary`, fixed costs from `list_bills`, spending from `spending_by_category` and `budget_status`, savings from `list_accounts`/`list_pots`. BudgeBit categories are the user's; map them to the four pillars only if the user wants (store the mapping in memory). Never rename or recategorise without a draft the user confirms.

The four questions, phrased for a reply:
1. Coming in: `<income> this month (month_summary)`.
2. Saving: `goal <x>, net so far <y>`.
3. Spending: `<expense>, top 3 categories …`.
4. Improve: one action, one number.

## Money principles
- **Hara hachi bu**: spend at most ~80% of flexible budgets; the buffer absorbs surprises.
- **Mottainai (もったいない)**: waste is a loss. Unused subscriptions, duplicate tools, late fees.
- **Kaizen**: one money change per month (e.g. "cook Tuesdays", "cancel one subscription").
- **Hansei**: look at overspending without guilt; find the cause.
- **Nemawashi**: big shared purchases are discussed with partner or family before buying.
- **Pay yourself first**: a savings transfer on payday (popularised by George Clason, *The Richest Man in Babylon*).
- **Needs before wants**: fixed costs and bills first.

## Money laws
- **Parkinson's second law**: "Expenditure rises to meet income" (*The Law and the Profits*, 1960). Check after raises.
- **Pareto**: a few categories hold most of the spend.
- **Hofstadter**: projects cost more than planned; pad one-off budgets 20–30%.
- **Murphy**: keep an emergency buffer; flag bills due before payday.
- **Goodhart**: a budget is a tool, not a score. Don't starve needs to show a green number.

## Phrasing money coaching
- Lead with the number and the source tool, then the meaning, then one action.
- Neutral, never shaming: "Food is at 78% with 16 days left" not "you overspent again".
- Use the user's currency formatting from results. Don't round unless asked.
- Never claim anything about money not in BudgeBit: no external prices, rates or forecasts presented as fact.
- No regulated advice: no specific investments, tax or legal guidance. Suggest a licensed professional.
