"""
This problem could be solved by using the prefixSum approach in Sum array sum equals K, but its a overkill imo, and take O(n) space.
Instead, we can solve it in O(1) space using sliding window.

Idea:
Instead of checking how many subarray == goal.
We check how many subarray <= goal.
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(target):
            if target < 0:
                return 0
            res = 0
            currSum = 0
            l = 0
            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > target:
                    currSum -= nums[l]
                    l += 1
                res += r - l + 1
            return res

        return helper(goal) - helper(goal-1)

        
        
        
