"""
Find the minimum number of prefix/suffix deletions needed to remove
both the minimum and maximum elements from the array.

Since deletions only happen from the front or back, the min and max
elements can always be removed via one of three strategies:
  1. Delete a prefix covering both (up through the later index).
  2. Delete a suffix covering both (from the earlier index onward).
  3. Delete a prefix up to the earlier index AND a suffix from the
     later index.

Args:
    nums: 0-indexed array of distinct integers.

Returns:
    The minimum number of deletions required.

Time complexity: O(N) — single pass to find min/max indices.
Space complexity: O(1) — only a constant number of index variables.
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = max_idx = 0
        N = len(nums)
        for i in range(N):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        min_idx, max_idx = min(min_idx, max_idx), max(min_idx, max_idx)
        return min(max_idx + 1, N - min_idx, min_idx + 1 + (N - max_idx))
