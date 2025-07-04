"""
This problem could be solved by using the prefixSum approach in Sum array sum equals K, but its a overkill imo, and take O(n) space.
Instead, we can solve it in O(1) space using sliding window.

Goal:
Count the number of subarrays with sum exactly equal to goal.

Trick:
Use the identity:
count(sum == k) = count(sum <= k) - count(sum <= k - 1)

We define helper(x) to return number of subarrays with sum ≤ x
and compute:
helper(goal) - helper(goal - 1)

Time: O(n)
Space: O(1)
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0:
                return 0
            res, currSum,l = 0, 0, 0
            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > x:
                    currSum -= nums[l]
                    l += 1
                res += r - l + 1
            return res
        
        return helper(goal) - helper(goal - 1)

        
        
        
