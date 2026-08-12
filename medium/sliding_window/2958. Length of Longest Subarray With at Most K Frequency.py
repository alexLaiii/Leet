"""
Return the length of the longest subarray in which every value
appears at most k times.

Sliding window with a frequency map. The right pointer extends the
window one element at a time; whenever the incoming value's count
exceeds k, the left pointer advances until that value is back within
the limit. Only the value just added can violate the constraint, since
every other count is unchanged or decreasing, so the check inspects a
single key rather than scanning the whole map.

Args:
    nums: List of integers.
    k: Maximum allowed frequency of any single value within a subarray.

Returns:
    Length of the longest valid subarray, or 0 if nums is empty.

Time:  O(n), each pointer moves forward at most n times.
Space: O(n), for the frequency map of distinct values in the window.
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        nums_count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            curr = nums[r]
            nums_count[curr] += 1
            while nums_count[curr] > k:
                nums_count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
            
