"""
Simple counting problem
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = {
            "b" : 0,
            "a" : 0,
            "l" : 0,
            "o" : 0,
            "n" : 0,
    
        }
        for c in text:
            if c in charCount:
                charCount[c] += 1
        
        charCount["l"] //= 2
        charCount["o"] //= 2
        res = float("inf")
        for key in charCount:
            res = min(res, charCount[key])
        return res
        
