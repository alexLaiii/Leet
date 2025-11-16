"""
Count the number of substrings consisting only of '1's.

Idea:
- Scan the string once and track the current streak length of consecutive '1's.
- If s[i] == '1':
    - Increase consecutiveOne by 1.
    - The number of new all-'1' substrings ending at i is exactly consecutiveOne
      (the single '1', the last two '1's, ..., the whole streak).
    - Add consecutiveOne to the result.
- If s[i] == '0', reset consecutiveOne to 0 because any substring including this
  position can no longer be all '1's.

This achieves the same effect as summing k(k+1)/2 over each block of k consecutive '1's,
but in a single O(n) pass without extra storage.

Time Complexity: O(n), where n = len(s)
Space Complexity: O(1)
"""

class Solution:
    def numSub(self, s: str) -> int:
        consecutiveOne = 0
        res = 0
        for d in s:
            if d == "1":
                consecutiveOne += 1
                res = (res + consecutiveOne) % (10**9 + 7)
            else:
                consecutiveOne = 0
        return res
