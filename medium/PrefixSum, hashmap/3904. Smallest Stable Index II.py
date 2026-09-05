"""
Finds the smallest stable index in nums.

An index i is "stable" if the maximum value in nums[0..i] minus the
minimum value in nums[i..N-1] is at most k. The suffix minimum for
every index is precomputed in one backward pass, then a forward pass
tracks the running prefix maximum and checks the stability condition
at each index in O(1).

Args:
    nums: List of integers to search.
    k: Maximum allowed difference between the prefix max ending at i
        and the suffix min starting at i for i to count as stable.

Returns:
    The smallest index i such that max(nums[:i+1]) - min(nums[i:]) <= k,
    or -1 if no such index exists.

Time Complexity: O(N), where N = len(nums) — one pass to build
    suffix_min, one pass to find the answer.
Space Complexity: O(N) for the suffix_min array.
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        suffix_min = [float("inf")] * (N + 1)
        for i in range(N - 1, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        curr_max = nums[0]
        for i in range(N):
            curr_max = max(curr_max, nums[i])
            if curr_max - suffix_min[i] <= k:
                return i
        return -1
            
        
