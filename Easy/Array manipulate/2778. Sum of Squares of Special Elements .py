"""
So simple, so naive
"""
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            if N % (i + 1) == 0:
                res += nums[i] ** 2
        
        return res
        
