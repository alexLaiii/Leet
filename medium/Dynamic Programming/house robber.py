"""
Classic dynamic programming problem
Idea:
-curr_rob always store the largest number you can rob at house[i]
-Tricky initialization, the first house profit is the first house, the second house profit has to be the max(first house, second house)
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1): return nums[0]
        else:
            prev_rob, curr_rob = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = curr_rob
                curr_rob = max(prev_rob + nums[i], curr_rob)
                prev_rob = temp
                
            return curr_rob


"""
Clean up version, same idea
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) <= 1): return nums[0]  
        else:          
            prev_rob, max_rob = 0,0
            for i in range(len(nums)):
                max_rob, prev_rob = max(nums[i] + prev_rob, max_rob), max_rob
        return max_rob
