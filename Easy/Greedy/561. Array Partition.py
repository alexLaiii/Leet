"""
Maximize the sum of min(pair) over all pairings of nums into n/2 pairs.

Strategy: sort nums, then pair adjacent elements (nums[0] with nums[1],
nums[2] with nums[3], etc). Within each pair, the smaller element is
always the one that gets summed, so we only need every element at an
even index (0, 2, 4, ...) after sorting.

Why adjacent pairing is optimal: only the min of each pair counts, so
the sum is maximized by minimizing the total of the wasted max values.
Pairing the two smallest elements together never hurts, since any
other element they could be paired with is >= both of them anyway.
Applying this greedily down the sorted array gives adjacent pairing.

Time: O(n log n), dominated by the sort. This is optimal in the
comparison model: selecting n/2 order statistics simultaneously has
a matching Theta(n log n) lower bound, so this problem is provably
as hard as full sorting.
Space: O(1) extra (ignoring sort's internal space).

:param nums: list of 2n integers to be split into n pairs
:return: maximum possible sum of min(pair) across all pairs
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # you always want to group two largest in the group
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
