"""
Note1: The first inituition of Greedy Algorithm won't work here, since always picking the largest coin will result in wrong solution or even cant sum to target amount sometimes.
Counter - Example: coins: [1,3,4,5], amount:7
Greedy will result
pick: 5 -> remain = 2
pick: 4 -> can't pick since 4 > 2
pick: 3 -> can't pick since 3 > 2
pick: 1 -> remain = 1
pick: 1 -> remain = 0
Thus, it pick 3 times.
But the optimal solution is 
pick 4: -> remain = 3
pick 3: -> remain = 0
Thus, it pick 2 times. So Greedy fails

Correct Solution, Dynamic Programming solution (divide to sub problem)
Idea:
Use an array to keep track of the minimum number of coins needed in every subamount, where 0 <= subamount < amount + 1
In every subamount, subamount - (the coin you select) will be the remain, and the remain will be another subamount, which is recorded in the array
Which is: If you pick this coin:
          New minimum amount = arr[subamount - (the coin you select)] + 1
So Traverse all the coint to found which (New minimum amount) is the smallest in current subamount
Set arr[current subamount] = new minimum amount
Loop this process until current subamount == amount
So in the end, arr[amount] will be the result, which is same as arr[-1],the last element of the array

Note**: We use the index of arr to represent the current tracking amount, such that 
for i in range(len(arr)):
  # i here represent the curr_amount

Time Complexity: O(n*m)  
                Outerloop = O(n) -> the amount
                Innerloop = O(m) -> the number of coins you can choose from
Space Complexity: O(n)
                an extra array with size = the amount

"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for curr_amount in range(len(dp)):
            for coin in coins:
                if curr_amount - coin >= 0:
                    if dp[curr_amount-coin]+ 1 < dp[curr_amount]:
                        dp[curr_amount] = dp[curr_amount-coin] + 1
        
        return -1 if dp[-1] == amount + 1 else dp[-1]



"""
Problem: Coin Change

Idea:
We want to find the minimum number of coins needed to sum up to a given `amount`, using the available denominations in `coins`.

This is a classic **1D Dynamic Programming** problem where we build up the solution from smaller subproblems.

Implementation:
- Define `dp[i]` as the minimum number of coins needed to make up amount `i`.
- Initialize `dp[0] = 0` (base case: 0 coins needed to make amount 0).
- Set all other values in `dp` to `float('inf')` initially, which represents that those amounts are currently unreachable.

For each amount `i` from 1 to `amount`, try every coin `c` in `coins`:
    - If `i - c >= 0`, that means we can use coin `c` to reach amount `i`.
    - So we take `dp[i - c] + 1` (the min coins to make `i - c`, plus 1 coin `c`) and update `dp[i]` if it’s smaller.

After filling the DP table, `dp[amount]` holds the answer.

Return:
- `dp[amount]` if it's not infinity.
- Otherwise, return -1 if there's no combination of coins to make the amount.

Time Complexity:
- O(amount * len(coins))

Space Complexity:
- O(amount)

Example:
coins = [1,2,5], amount = 11
=> Output: 3 (11 = 5 + 5 + 1)
"""


# same thing different style
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1

                    
            
