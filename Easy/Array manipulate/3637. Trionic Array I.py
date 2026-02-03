class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        i = 1
        iB4 = i
        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1
        if i == iB4:
            return False
        iB4 = i
        while i < len(nums) and nums[i] < nums[i - 1]:
            i += 1
        if i == iB4:
            return False
        iB4 = i
        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1
        if i == iB4:
            return False
        if i == len(nums):
            return True
        return False
