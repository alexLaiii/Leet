"""
Return the length of the smallest positive integer consisting only of
digit '1' (a repunit) that is divisible by k, or -1 if none exists.

Uses the fact that if k has factors 2 or 5, no such repunit multiple
can exist. Otherwise, iteratively builds the remainder of the current
repunit modulo k using: remainder = (remainder * 10 + 1) % k, and
counts how many digits '1' are needed until the remainder becomes 0.
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        nums = 1
        length = 1
        while nums % k != 0:
            nums = (nums * 10 + 1) % k
            length += 1
        return length
