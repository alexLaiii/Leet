"""
Find the smallest positive multiple of k missing from nums, in O(n)
time and O(1) auxiliary space, using in-place index marking (no hash
set, no sorting).

NOTE: This is more than the problem requires. It's rated Easy and
the intended solution is a simple hash set in O(n) time / O(n) space.
This in-place approach borrows the "First Missing Positive" (LC41)
technique, which is overkill for these constraints (n, nums[i], k
all <= 100) but demonstrates the O(1)-space pattern.

Key idea:
    By pigeonhole, among the first N+1 multiples of k (k, 2k, ...,
    (N+1)*k), at least one must be missing from nums, since nums has
    only N elements. So we only need to track presence of multiples
    k*1..k*N using the array itself, then check index N+1 as the
    fallback.

Marking scheme:
    For each nums[i], if it's a multiple of k with multiplier
    t = nums[i] // k in [1, N], negate nums[t-1] to record that the
    t-th multiple of k is present. abs() is used on read since a
    value may have already been negated by an earlier marking.
    A guard (nums[multiplier-1] < 0) prevents duplicates from
    flipping an already-negative marker back to positive.

Second pass finds the first un-marked (still non-negative) index i,
meaning k*(i+1) is missing; if none found, the answer is k*(N+1).

Time:  O(n)  - two linear passes
Space: O(1)  - in-place sign marking, no extra data structures
"""


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        """
        Since the first missing mutiple can only happen between k and len(nums) * k
        nums[i] should be k * (i + 1)
        """
        N = len(nums)
        for i in range(N):
            if abs(nums[i]) % k != 0:
                continue
            multiplier = abs(nums[i]) // k
            if multiplier > N or nums[multiplier - 1] < 0:
                continue
            nums[multiplier - 1] = -nums[multiplier - 1]
        
        for i in range(N):
            if nums[i] >= 0:
                return k * (i + 1)
        return k * (N + 1)
