# Dynamic Programming - Salary Work Schedule
A salaryman has worked most of the time during his days. However, the salaryman may receive offer to do part time jobs which sometimes may make more money from his daily jobs.

We want to maximise the amount of money that can be earn by combining the daily job as a salaryman while doing part time jobs.

## Input
**weekly_income** is a list of non-negative integers, where weekly_income[i] is the amount of
money you will earn working as a personal trainer in week i.

**part_time** is a list of tuples, each representing a part time job. Each tuple contains
3 non-negative integers, (start_time, end_time, winnings).

**start_time** is the is the week that you will need to begin preparing for this part time job.

**end_time** is the last week that you will need to spend recovering from the part time job.

**winnings** is the amount of money you will win if you compete in this part time job.

## Output
**best_schedule** returns an integer which is the maximum amount of money that can be earned.

## Example
```
weekly_income = [3,7,2,1,8,4,5]
part_time_job = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
print(best_schedule(weekly_income, part_time_job))
>>> 42
```

In the above example, the optimal schedule is to work as a trainer in weeks 0 and 1 (earning
3+7), then compete in the (2,2,8) event in week 2 (earning 8), then compete in the (3,5,19)
event from weeks 3 to 5 (earning 19), then work as a trainer in week 6 (earning 5).

## Complexity
best_schedule should run in O(Nlog(N)) time and O(N) space, where N is the total number
of elements in weekly_income and part_time put together.

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

