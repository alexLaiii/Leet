"""
Introduction to programming
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set()
        for j in jewels:
            jewel.add(j)
        res = 0
        for s in stones:
            if s in jewel:
                res += 1
        return res
        
