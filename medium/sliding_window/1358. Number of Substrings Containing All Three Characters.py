"""
Count the number of substrings that contain at least one 'a', one 'b',
and one 'c'.

Use a sliding window with two pointers. Expand the window by moving
the right pointer and counting each character. Once the current window
contains all three characters, every substring starting at left and
ending at right or any later index is valid, so add N - right.

Then shrink the window from the left while it still contains all three
characters, counting all valid starting positions.

Time Complexity:
    O(n), because each pointer moves through the string at most once.

Space Complexity:
    O(1), because only counts for 'a', 'b', and 'c' are stored.
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        left = 0
        res = 0
        substring = {'a': 0,
                     'b': 0,
                     'c': 0}
        for r in range(N):
            if s[r] in ["a", "b", "c"]:
                substring[s[r]] += 1
            while substring['a'] > 0 and substring['b'] > 0 and substring['c'] > 0:
                res += N - r
                substring[s[left]] -= 1
                left += 1

        return res 
            
