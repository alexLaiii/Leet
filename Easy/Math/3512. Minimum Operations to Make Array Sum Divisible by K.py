"""
Too easy, not bother to explain.
"""
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sums = sum(nums)
        return sums % k
