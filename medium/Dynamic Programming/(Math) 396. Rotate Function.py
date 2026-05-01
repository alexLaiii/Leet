"""
Compute the maximum value of the rotation function F(k) for all rotations.

Key Insight:
Instead of recomputing F(k) from scratch for each rotation (which would be O(n^2)),
we observe how the value changes between consecutive rotations.

Let:
    F(k) = sum(i * nums[i] after k rotations)

When we rotate the array by 1 step:
- Every element except the last one effectively shifts right by 1 index,
  so each of those elements contributes +1 extra to the total.
- The last element (the "abandoned" element) moves from index (n-1) to index 0:
    → Previously contributed: nums[last] * (n - 1)
    → Now contributes: nums[last] * 0
    → So we must REMOVE its previous full contribution.

Therefore:
    F(k) = F(k-1)
           - nums[last] * (n - 1)      # remove old contribution
           + (sum(nums) - nums[last]) # all other elements gain +1

Implementation Details:
- First compute F(0) directly.
- Then iteratively compute F(k) using the recurrence above.
- Track the maximum value across all rotations.

Time Complexity: O(n)
Space Complexity: O(n) (can be optimized to O(1))
"""

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        numSums = sum(nums)
        N = len(nums)
        dp = [0] * N
        for i in range(N):
            dp[0] += nums[i] * i
        
        delete_idx = N - 1
        for i in range(1, N):
            dp[i] = (dp[i - 1] - nums[delete_idx] * (N - 1)) + (numSums - nums[delete_idx])
            delete_idx -= 1

        return max(dp)
        
        

        
