"""
Dynamic programming solution.

dp[i] represents the maximum number of jumps needed to reach index i.
If index i is unreachable, dp[i] remains -1.

We initialize dp[0] = 0 because we start at index 0 with 0 jumps.

For each index i, we check every previous index j.
If index j is reachable and the jump from j to i is valid, meaning
abs(nums[i] - nums[j]) <= target, then we can update dp[i] using:

    dp[i] = max(dp[i], dp[j] + 1)

This ensures that we keep the maximum possible number of jumps to reach i,
instead of stopping at the first valid previous index.

Finally, dp[-1] gives the maximum number of jumps to reach the last index,
or -1 if the last index is unreachable.

Time Complexity: O(n^2), because every pair (j, i) with j < i may be checked.
Space Complexity: O(n), for the dp array.
"""

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [-1] * N
        dp[0] = 0
        for i in range(N):
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)
                 
   
        return dp[-1]
