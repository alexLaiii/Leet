"""
Find the smallest integer >= the longest sequential prefix sum that is
absent from nums.

A sequential prefix is a run nums[0..i] where each element is exactly one
more than the previous. Only the longest such prefix counts, so the scan
stops at the first break and the sum up to that point is the starting
candidate. From there, linearly probe upward past any value already in
nums.

The probe is bounded: each step requires the candidate to be present in
nums, so it advances at most len(nums) times before hitting a gap.

Args:
    nums: List of positive integers.

Returns:
    The smallest integer >= the longest sequential prefix sum that does
    not appear in nums.

Time:  O(n) for the scan, set build, and bounded probe.
Space: O(n) for the set of seen values.
"""
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sums = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                break
            sums += nums[i]
        
        nums_set = set(nums)
        while sums in nums_set:
            sums += 1
        return sums
        
