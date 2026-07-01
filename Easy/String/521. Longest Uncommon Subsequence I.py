"""
Very stupid problem, just a complicated way to ask if two strings are the same.
"""
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
       
