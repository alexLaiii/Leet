"""
Explanation:

- Initialize two pointers: `left` and `right`.
- Use binary search to narrow down the region containing the minimum.

Key Logic:
- If `nums[mid] > nums[right]`, the minimum must lie **to the right of mid**. (Noted that this will never happen if the array is not rotated)
  - Because in a rotated array, this means the left half is still sorted but the pivot (smaller values) is on the right.
- Otherwise, the minimum lies **to the left (including mid)**.
  - This could mean the right half is sorted, or the array is not rotated at all.

- The loop continues until `left == right`, which points to the smallest element.

Why this works:
- This is a classic binary search variant used for rotated arrays.
- It guarantees O(log n) time and is a valuable pattern in interviews.

Time Complexity:
O(logn): binary search
Space Complexity:
O(1)
"""

class Solution(object):
    def findMin(self, nums):
        # find minimum value
        left, right = 0, len(nums) - 1
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


