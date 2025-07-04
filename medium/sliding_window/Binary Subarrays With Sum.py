"""
This problem could be solved by using the prefixSum approach in Sum array sum equals K, but its a overkill imo, and take O(n) space.
Instead, we can solve it in O(1) space using sliding window.

This sliding window algorithm is an idea built up for Leetcode 992
Idea:
Instead of checking how many subarray == goal.
We check how many subarray <= goal.
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

        
        
        
