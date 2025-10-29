"""
Return the smallest integer ≥ n whose binary representation is all 1s.
Builds numbers of the form 1, 3, 7, 15, ... by repeatedly doing x = 2*x + 1
(which appends a '1' bit), stopping at the first x ≥ n.
Time: O(log n)  |  Space: O(1).
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        # build bit 1111...
        x = 1
        while  x < n:
            x = x * 2 + 1
        return x
