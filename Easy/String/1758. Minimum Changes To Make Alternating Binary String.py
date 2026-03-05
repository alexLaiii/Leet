"""
Return the minimum number of character changes needed to make the
binary string `s` alternating.

An alternating binary string must follow one of two patterns:
1. Starting with '0': "010101..."
2. Starting with '1': "101010..."

The algorithm counts the number of mismatches with each pattern and
returns the minimum.

Approach:
- Simulate the alternating pattern starting with '0' and count the
  number of mismatches (res1).
- Simulate the alternating pattern starting with '1' and count the
  number of mismatches (res2).
- The result is the minimum of the two counts.

Time Complexity:
    O(n), where n is the length of the string.

Space Complexity:
    O(1), only constant extra variables are used.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        prev = "0"
        res1 = 0
        res2 = 0

        for i in range(len(s)):
            if s[i] != prev:
                res1 += 1
            prev = "0" if prev == "1" else "1"
        
        prev = "1"

        for i in range(len(s)):
            if s[i] != prev:
                res2 += 1
            prev = "0" if prev == "1" else "1"
        
        return min(res1, res2)

            
