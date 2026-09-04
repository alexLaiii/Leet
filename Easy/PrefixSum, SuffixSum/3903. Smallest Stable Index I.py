"""Finds the smallest stable index in nums.

For each index i, the instability score is defined as
max(nums[0..i]) - min(nums[i..n-1]). An index is stable if its
instability score is <= k. Precomputes suffix minimums in one
pass, then scans left to right tracking the running prefix max
to evaluate each index's instability score in O(1).

Args:
    nums: List of non-negative integers.
    k: Maximum allowed instability score for a stable index.

Returns:
    The smallest stable index, or -1 if none exists.

Time Complexity:
    O(n), where n = len(nums) — one pass to build suffix minimums,
    one pass to find the answer.

Space Complexity:
    O(n) for the suffixMin array.
        """

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        suffixMin = [None] * N
        suffixMin[-1] = nums[-1]
        for i in range(N - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])
        currMax = 0
        for i in range(N):
            currMax = max(currMax, nums[i])
            if currMax - suffixMin[i] <= k:
                return i
        return -1
            
