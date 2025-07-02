"""
The main Idea is shrink the array by one when you cant use mid to determine whether you are in the LEFT or RIGHT sorted portion
"""



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r > l:
            m = (l + r) // 2
            if nums[l] == nums[r]:
                r -= 1 
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[r]
