"""
Computes the total amount of money saved in the LeetCode bank after n days.

The saving pattern follows a weekly structure:
- On the first Monday, 1 dollar is saved, increasing by 1 each day.
- Each new week starts with 1 dollar more than the previous week’s Monday.
- A full week always consists of 7 days.

Approach:
- Split n into full weeks and remaining days.
- Each full week contributes an increasing fixed sum:
  Week 1 = 28, Week 2 = 35, Week 3 = 42, ...
- Remaining days are handled by continuing the daily increment
  starting from the next week's base value.

Parameters:
n (int): Total number of days money is saved.

Returns:
int: Total amount of money saved after n days.

Time Complexity:
O(n / 7), which is effectively O(1) since weeks are bounded.

Space Complexity:
O(1), using only a constant amount of extra space.
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        remain_days = n % 7
        weekSave = 28
        res = 0
        for w in range(1, week + 1):
            res += weekSave
            weekSave += 7
        start = week + 1
        for i in range(remain_days):
            res += start + i 
        return res
        
