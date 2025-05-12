"""
💡 Intuition
To solve this problem, we consider the constraint that the first and last houses are adjacent in a circular arrangement — meaning we cannot rob both.

So, we divide the problem into two linear subproblems:

Include the first house, which means we exclude the last house. So we rob houses from index 0 to n-2.

Exclude the first house, which means we can include the last house. So we rob houses from index 1 to n-1.

We solve both cases using the original House Robber logic, and return the maximum of the two results.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        r1_prev, r1_max, r2_prev, r2_max = 0,0,0,0
        for i in range(len(nums) - 1):
            r1_max,r1_prev = max(nums[i] + r1_prev, r1_max), r1_max
            r2_max,r2_prev = max(nums[i+1] + r2_prev, r2_max), r2_max
        return max(r1_max,r2_max)
