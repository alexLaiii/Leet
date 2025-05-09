class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if(nums[mid] > nums[right]):
                left = mid + 1
            if(nums[mid] < nums[right]):
                if(nums[mid] < nums[mid - 1]):
                    return nums[mid]
                right = mid - 1
        return nums[left]
