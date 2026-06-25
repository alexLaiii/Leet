"""
Count how many subarrays have target as the majority element.

For every starting index i, expand the subarray one element at a time
using ending index j. Keep track of how many times target appears in
the current subarray nums[i:j+1].

A target is the majority element if it appears more than half of the
subarray length:

    target_count * 2 > subarray_length

If the condition is true, add 1 to the result.

Time Complexity: O(n^2), because we check every possible subarray.
Space Complexity: O(1), because we only use counters.
"""
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            target_count = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    target_count += 1
                if target_count * 2 > j - i + 1:
                    res += 1
        return res
