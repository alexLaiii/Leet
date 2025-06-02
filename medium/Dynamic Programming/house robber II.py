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
        # two route solution, compare which route gets more at the end
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # if rob house 1
        r1 = [nums[0], max(nums[0], nums[1])]
        # if rob house 2
        r2= [nums[1], max(nums[1], nums[2])]

        for i in range(2, len(nums) - 1):
            r1[0], r1[1] = r1[1], max(r1[1], r1[0] + nums[i])
        for i in range(3, len(nums)):
            r2[0], r2[1] = r2[1], max(r2[1], r2[0] + nums[i])
        return max(r1[1], r2[1])
