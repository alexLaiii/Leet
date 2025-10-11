"""
LeetCode 1208 — Get Equal Substrings Within Budget

Idea:
    Use a sliding window over the index range of s/t. The cost to change
    s[i] -> t[i] is abs(ord(s[i]) - ord(t[i])). Grow the window by moving
    the right pointer and accumulating cost. If the running cost exceeds
    maxCost, shrink from the left until the window cost is back within
    budget. Track the largest valid window length seen.

Why it works:
    The window cost is monotonic with respect to expanding/contracting:
    - Expanding by one index adds exactly that index’s cost.
    - Contracting from the left removes exactly that index’s cost.
    This lets us find the maximum-length contiguous segment whose total
    transform cost is ≤ maxCost in linear time without backtracking.

Steps:
    1) Precompute per-index costs: c[i] = |s[i] - t[i]|.
    2) Initialize left = 0, running_cost = 0, best = 0.
    3) For right in [0..n-1]:
         - running_cost += c[right]
         - while running_cost > maxCost:
               running_cost -= c[left]
               left += 1
         - best = max(best, right - left + 1)
    4) Return best.

Complexity:
    Time:  O(n) — each index enters and leaves the window at most once.
    Space: O(1) extra (O(n) if you store the cost array explicitly, but you
           can compute c[right] on the fly to keep it O(1)).

Edge cases:
    - maxCost == 0 → answer is the longest stretch where s[i] == t[i].
    - s == t → answer is len(s) (costs are all zero).
    - Empty strings → 0.

Returns:
    Length of the longest substring of s that can be transformed into the
    corresponding substring of t without exceeding maxCost.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l = 0
        for r in range(len(s)):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            while maxCost < 0:
                maxCost += abs((ord(s[l]) - ord(t[l])))
                l += 1
            res = max(res, r - l + 1)
        return res
                
        
