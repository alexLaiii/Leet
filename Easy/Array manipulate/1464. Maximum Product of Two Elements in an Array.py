"""
Too easy, just find the two largest element
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num, second_max = 0, 0
        
        for n in nums:
            second_max = max(second_max, n)
            if second_max > max_num:
                max_num, second_max = second_max, max_num
        
        return (max_num - 1) * (second_max - 1)
        
