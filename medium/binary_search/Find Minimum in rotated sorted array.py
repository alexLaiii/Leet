##
Initialize two pointers, left and right.
Use binary search to narrow down the region containing the minimum.
If nums[mid] > nums[right], the minimum lies to the right.
Otherwise, it lies to the left or could be the mid itself.
The loop ends when left == right, pointing to the minimum.
This is a clean and optimal binary search pattern that's highly valuable in technical interviews.
##

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
