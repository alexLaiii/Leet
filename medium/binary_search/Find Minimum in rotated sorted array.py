"""
Initialize two pointers, left and right.
Use binary search to narrow down the region containing the minimum.
If nums[mid] > nums[right], the minimum lies to the right. (Because it is rotated, a normal sorted array will never satisfy this condition)
Otherwise, it lies to the left or could be the mid itself. (Might rotated, might not, but the rotation didnt cause minimum value lies in the right, tho there might be larger value lies in the left)
The loop ends when left == right, pointing to the minimum.
This is a clean and optimal binary search pattern that's highly valuable in technical interviews.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (right + left) // 2
            # if mid > right, then the array must be rotated, the minimum lies in the right direction
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[left]

