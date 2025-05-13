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
                    
            
