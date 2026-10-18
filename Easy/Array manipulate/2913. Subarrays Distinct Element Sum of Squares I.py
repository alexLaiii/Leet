"""
Just Brute force
"""

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            distinct = set()
            for j in range(i, len(nums)):
                distinct.add(nums[j])
                res += len(distinct) ** 2
        
        return res

        
