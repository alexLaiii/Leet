"""
Return the maximum number of operations to move all '1's to the end.

Key idea:
- Each valid operation effectively moves a '1' rightward across a boundary where a block of '1's
  meets a '0' (i.e., a transition "10"). For maximizing operations, we can count contributions
  per such boundary rather than simulate swaps.
- Scan left to right while tracking `total_one` = number of '1's seen so far.
- Whenever we encounter the *first* '0' of a zero-block (pattern: s[i] == '0' and s[i-1] != '0'),
  that zero-block will eventually be crossed by every '1' that is currently to its left, yielding
  `total_one` operations contributed by that boundary. Add it to `res`.

Why the "start of zero-block" check matters:
- For consecutive zeros "00...0", we should only count the boundary once; counting every '0'
  would overcount because the operation-triggering boundary is the transition into the block.

Args:
    s: Binary string consisting of '0' and '1'.

Returns:
    The maximum number of operations possible.

Complexity:
    Time: O(n) for one pass through the string.
    Space: O(1) extra space.

Notes:
    This implementation assumes `s` is non-empty (accesses s[0]).
"""

class Solution:
    def maxOperations(self, s: str) -> int:
        total_one = 1 if s[0] == "1" else 0
        res = 0
        for i in range(1, len(s)):
            if s[i] == "1":
                total_one += 1
            elif s[i] == "0" and s[i - 1] != "0":
                res += total_one
        return res
