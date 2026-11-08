#!/usr/bin/env python3
"""Energy and completion stats from BudgeBit task rows.

Input: JSON (file path or stdin) with a list of task objects, as you would
copy them from `Budgebit:list_tasks` results:

  [{"title": "...", "list": "...", "status": "done|todo|in_progress",
    "due_date": "YYYY-MM-DD", "start_time": "HH:MM", "due_time": "HH:MM",
    "overdue": false}, ...]

Fields other than title/status/due_date are optional.

Output: Markdown tables with completion rate by list, by hour of day (from
start_time, else due_time), and by weekday, plus planned minutes per day.
No data leaves the machine. Run:  python3 energy_stats.py tasks.json
"""
import json
import sys
from collections import defaultdict
from datetime import date

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def minutes(hhmm):
    try:
        h, m = hhmm.split(":")
        return int(h) * 60 + int(m)
    except (AttributeError, ValueError):
        return None


def table(title, rows):
    out = [f"### {title}", "", "| key | done | total | rate |", "|---|---|---|---|"]
    for key, (done, total) in rows:
        rate = f"{done / total:.0%}" if total else "-"
        out.append(f"| {key} | {done} | {total} | {rate} |")
    return "\n".join(out) + "\n"


def main():
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    tasks = json.load(src)
    by_list = defaultdict(lambda: [0, 0])
    by_hour = defaultdict(lambda: [0, 0])
    by_day = defaultdict(lambda: [0, 0])
    planned = defaultdict(int)

    for t in tasks:
        done = 1 if t.get("status") == "done" else 0
        by_list[t.get("list", "(no list)")][0] += done
        by_list[t.get("list", "(no list)")][1] += 1
        start = minutes(t.get("start_time"))
        end = minutes(t.get("due_time"))
        anchor = start if start is not None else end
        if anchor is not None:
            by_hour[f"{anchor // 60:02d}:00"][0] += done
            by_hour[f"{anchor // 60:02d}:00"][1] += 1
        if t.get("due_date"):
            try:
                d = date.fromisoformat(t["due_date"])
            except ValueError:
                continue
            by_day[WEEKDAYS[d.weekday()]][0] += done
            by_day[WEEKDAYS[d.weekday()]][1] += 1
            if start is not None and end is not None and end > start:
                planned[t["due_date"]] += end - start

    print(table("By list", sorted(by_list.items(), key=lambda kv: -kv[1][1])))
    print(table("By hour (start)", sorted(by_hour.items())))
    print(table("By weekday", [(d, by_day[d]) for d in WEEKDAYS if d in by_day]))
    if planned:
        print("### Planned minutes per day\n\n| date | minutes |\n|---|---|")
        for d in sorted(planned):
            print(f"| {d} | {planned[d]} |")


if __name__ == "__main__":
    main()
