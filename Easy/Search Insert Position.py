class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        top = len(nums) - 1
        low = 0
        while(low <= top):
            mid = (low + top) // 2
            if(nums[mid] == target):
                return mid
            if(nums[mid] > target):
                top = mid - 1
            if(nums[mid] < target):
                low = mid + 1
        return low
        
