## Approach:
Find Pivot first
Find the index
##


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if(nums[mid] > nums[right]):
                left = mid + 1
            if(nums[mid] < nums[right]):
                if(nums[mid - 1] > nums[mid]):
                    left = mid
                    break
                right = mid - 1

        low = left
        high = low + len(nums) - 1
        while(low <= high):
            mid = (low + high) // 2 - len(nums)
            if(target == nums[mid]):
                if(mid < 0):
                    return mid + len(nums)
                else:
                    return mid 
            if(target > nums[mid]):
                low = mid + len(nums) + 1
            else:
                high = mid + len(nums) - 1
        return -1
