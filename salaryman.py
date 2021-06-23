"""
Author: Ng Wei Han
"""

#%% 
def turn_into_part_time(lst):
    """
    Helper function to turn weekly_income (list) into part_time (tuple) in the format of (start_time,end_time,winnings)
    
    :params lst: List of non-negative integers which represent income at each week
    :return: List containing tuples in the format of (start_time,end_time,winnings) where start_time = end_time

    ---Time Complexity---
    Best/Worst: O(n) 
    n - number of elements in the list

    ---Space Complexity---
    Total Space: O(n)
    Auxiliary Space: O(1) 
    n - number of elements in the input list
    """
    for i in range(len(lst)):
        tup = (i,i,lst[i])
        lst[i] = tup

    return lst
# %%
def best_schedule(weekly_income,part_time):
    
    """
    Function which maximise the amount of money earned while working as a trainer and joining part_time using dynamic programming
    
    :params weekly_income: List of non-negative integers in which weekly_income[i] represents the amount of money earned in week i
    :params part_time: List of tuples where each tuple represents a part_time in the form of (start_time,end_time,winnings)
    start_time: First week begin for part_time
    end_time: Last week to recover from part_time
    winnings: Amount of money win for the part_time
    :return: Maximum money that can be earned

    ---Time Complexity---
    Best: O(N)
    Worst: O(N Log N)
    N - Total number of elements in the weekly_income and part_time
    Time complexity is determined by Python's built in sorting algorithm which is Timsort. 

    ---Space Complexity---
    Total Space: O(N)
    Auxiliary Space: O(N) 
    N - Total number of elements in the weekly_income and part_time
    Only 1 memoization array is created which has the length of weekly_income+1.
    """
    memo_length = len(weekly_income)
    empty_weekly_income = False

    # Work for all weeks
    if len(part_time) == 0: 
        return sum(weekly_income)
    
    if len(weekly_income) == 0:
        empty_weekly_income = True 
        # Find the maximum end_time in part_time
        for i in range(len(part_time)):
            if part_time[i][1] > memo_length: 
                memo_length = part_time[i][1]

    # Initialize memo 
    memo = [-1 for _ in range(memo_length+1)]
    memo[0] = 0

    # Convert income into part_time
    turn_into_part_time(weekly_income)
    
    # Combine both list
    part_time = part_time + weekly_income

    # Combination of weekly_income and part_time is empty
    if len(part_time) == 0: 
        return 0

    # Sort part_time based on end_time
    part_time.sort(key=lambda x:x[1])

    pointer = 0
    curr_item = part_time[pointer] 
    for i in range(1,len(memo)): # Iterate over memo
        while curr_item[1] < i: # Iterate over each item once only
            include = 0
            if curr_item[0]-1 >= 0: 
                include = memo[curr_item[0]]
            memo[i] = max(memo[i],include+curr_item[2])

            pointer += 1
            if pointer == len(part_time):
                break

            curr_item = part_time[pointer]
    
    if empty_weekly_income: 
        return max(memo)

    return memo[memo_length]