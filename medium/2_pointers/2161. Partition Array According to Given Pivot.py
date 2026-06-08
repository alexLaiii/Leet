"""
Super easy problem
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        exact = []
        larger = []
        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                larger.append(n)
            else:
                exact.append(n)
        return smaller + exact + larger
        
        
