"""
Beginner DP problem
"""
class Solution:
    def fib(self, n: int) -> int:
        dp = [1, 0]
        if n == 0:
            return dp[1]
        if n == 1:
            return dp[0]
        for i in range(1, n):
            dp[0], dp[1] = dp[0] + dp[1], dp[0]
        return dp[0]
