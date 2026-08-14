"""
Classic sliding window problem
"""
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            char_count[s[r]] += 1
            while char_count[s[r]] > 2:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
