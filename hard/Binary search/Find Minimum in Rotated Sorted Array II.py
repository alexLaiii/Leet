"""
Finds the minimum element in a rotated sorted array that may contain duplicates.

Main Idea:
We use a modified binary search. Normally, we compare nums[mid] and nums[r] to 
determine whether mid is in the left or right sorted portion. However, due to 
duplicates, this comparison can become ambiguous.

For example:
nums = [3, 3, 3, 3, 3, 1, 3]
        l        m        r
nums[m] > nums[r] -> False
nums[m] <= nums[r] -> True, but "r + m" will take you to the wrong sorted portion, and the minimum would never be correctly found
=> Unable to determine the sorted portion

In such ambiguous cases where nums[l] == nums[m] == nums[r], we can't conclude
anything about which half contains the minimum. Therefore, we shrink the search 
space by doing r -= 1 (or l += 1) — either is safe.

This is safe because:
- Even if nums[l] or nums[r] is the minimum, nums[m] has the same value and is still retained.
- We are not discarding a unique occurrence of the minimum; only duplicates.

The rest of the binary search proceeds as in the standard rotated-array problem:
- If nums[m] > nums[r], the minimum is in the right half (l = m + 1)
- If nums[m] < nums[r], the minimum is in the left half or at m (r = m)
- If nums[l] == nums[m] == nums[r], ambiguity — shrink search space (r -= 1)

Time Complexity:
- Worst Case: O(n), e.g., nums = [3, 3, 3, 3, 3, 3, 3]
  (must discard duplicates one by one)
- Average Case: O(log n), when duplicates are minimal and binary search is decisive

This strategy ensures correctness even in fully duplicate or degenerate inputs.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[l] == nums[r]:
                r -= 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[r]
