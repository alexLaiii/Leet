"""
Simple problem, not documentation needed
"""
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_n, max_n = min(nums), max(nums)
        set_nums = set(nums)
        res = []
        for n in range(min_n + 1, max_n):
            if n not in set_nums:
                res.append(n)

        return res
            
        
