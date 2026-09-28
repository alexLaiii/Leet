"""
Very Simple problem
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        opens = res = 0
        for c in s:
            if c == "(":
                opens += 1
            if c == ")":
                opens -= 1
            res = max(opens, res)
        return res
        
