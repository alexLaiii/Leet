"""
Count the number of homogenous substrings in a string.

A homogenous substring is a contiguous substring where all characters
are the same. For example:
    - "aaa" has homogenous substrings: "a", "a", "a", "aa", "aa", "aaa"
      → total = 6

Idea:
    - Traverse the string from left to right.
    - Maintain `consecutiveC`, the length of the current run of
      identical characters ending at index i.
        * If s[i] == s[i-1], we extend the run: consecutiveC += 1
        * Otherwise, we start a new run: consecutiveC = 1
    - Every time we update `consecutiveC`, we add it to the result,
      because there are exactly `consecutiveC` homogenous substrings
      ending at position i (all suffixes of this run).

We take the result modulo 10^9 + 7 to avoid overflow.

Args:
    s: Input string.

Returns:
    The total number of homogenous substrings of s, modulo 10^9 + 7.

Time Complexity:
    O(n), where n = len(s), since we scan the string once.

Space Complexity:
    O(1), using only a couple of integer variables.
"""

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        consectiveC = 0
        for i in range(len(s)):
            if i > 0 and s[i-1] == s[i]:
                consectiveC += 1
            else:
                consectiveC = 1
            res = (res + consectiveC) % (10**9 + 7)
        return res
