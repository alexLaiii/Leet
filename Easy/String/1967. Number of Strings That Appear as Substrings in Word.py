"""
Very easy problem
"""
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for w in patterns:
            if w in word:
                res += 1
        return res
