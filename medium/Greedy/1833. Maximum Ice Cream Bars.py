"""
This problem is really easy as no docstring is required.
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0

        for cost in costs:
            if cost > coins:
                return res
            coins -= cost
            res += 1
        return res
            
        
