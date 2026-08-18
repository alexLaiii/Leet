"""
Find the largest integer in nums that appears in exactly one
contiguous subarray (window) of size k.

Key insight: when 1 < k < n, only nums[0] and nums[-1] can possibly
be "almost missing" — every interior index is covered by more than
one window, so it's automatically disqualified. A boundary value
qualifies iff it doesn't reappear anywhere else in the array (any
second occurrence always falls in a different window, since k < n
guarantees window 0 and window n-k never coincide).

Args:
    nums: Array of integers to search.
    k: Size of the sliding window.

Returns:
    The largest almost missing integer, or -1 if none exists.

Time Complexity: O(n) — one pass to build the frequency map.
Space Complexity: O(n) — for the frequency map.
"""

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        if k == 1:
            res = -1
            for key, c in count.items():
                if c == 1:
                    res = max(res, key)
            return res
        elif k == n:
            return max(nums)
        else:
            if count[nums[0]] != 1 and count[nums[n - 1]] != 1:
                return -1
            elif count[nums[0]] == 1 and count[nums[n - 1]] == 1:
                return max(nums[0], nums[n - 1])
            else:
                return nums[0] if count[nums[0]] == 1 else nums[n - 1]
            
