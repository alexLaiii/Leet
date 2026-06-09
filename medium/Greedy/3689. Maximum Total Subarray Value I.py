"""
Return the maximum total value of k selected subarrays.

The value of a subarray is the difference between its maximum and
minimum element. The largest possible subarray value is therefore the
global maximum of nums minus the global minimum of nums. Since the same
maximum value can be achieved for each of the k choices, the answer is
that difference multiplied by k.

Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(1).
"""

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        return (max_val - min_val) * k
        
