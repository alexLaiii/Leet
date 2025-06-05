"""
This problem is a fking hell
"""


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while r >= l:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                # must land on right portion, 
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                   l = m + 1
        return -1

            
     

            
