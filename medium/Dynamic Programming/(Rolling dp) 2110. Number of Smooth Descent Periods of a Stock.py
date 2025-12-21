"""
Count the total number of "smooth descent periods" in a stock price array.

A smooth descent period is any contiguous subarray (length >= 1) where each
consecutive pair decreases by exactly 1:
    prices[k] - prices[k+1] == 1  for all k in the subarray.

Key idea (rolling DP / streak DP):
- Let dp[i] be the number of valid descent periods that end at index i.
- If prices[i] == prices[i-1] - 1, we can extend every period ending at i-1
  by one day, so dp[i] = dp[i-1] + 1.
- Otherwise, dp[i] = 1 (the single element [prices[i]] is always valid).
- The answer is sum(dp[i]) over all i.

Implementation details:
- `curr` stores dp[i] for the current index i (length of the current
  consecutive "-1" streak ending at i).
- `res` accumulates the total number of periods by adding `curr` at each step.

Args:
    prices: List of daily stock prices (non-empty per problem constraints).

Returns:
    Total number of smooth descent periods.

Time Complexity:
    O(n), one pass through the array.

Space Complexity:
    O(1), constant extra space.
"""


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 1
        curr = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            res += curr
        return res
        
        
