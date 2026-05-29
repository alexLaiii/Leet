"""
This problem is very easy
"""
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minSum = float("inf")
        for n in nums:
            curr = 0
            while n:
                curr += n % 10
                n = n // 10
            minSum = min(curr, minSum)
        return minSum
