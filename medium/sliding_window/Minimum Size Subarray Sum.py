"""
While expanding the window, shrink it from the left as long as the sum is valid, and track the shortest valid window.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size, curr_sum, l = float("inf"),0,0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_size = min(min_size, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            
        return min_size if min_size != float("inf") else 0
