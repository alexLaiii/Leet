"""
LeetCode 875 — Koko Eating Bananas
Pattern: binary search on the *answer* (minimum integer speed k).

Problem restatement:
  Find the smallest k such that the total hours Σ ceil(pile / k) over all piles
  is ≤ h.

Key idea:
  Define a feasibility test hours(k, remainhours) that returns True iff Koko can
  finish within h hours at speed k. This predicate is *monotone*: if it’s True
  for k, it’s also True for any k' > k. Monotonicity + bounded search range
  [1, max(piles)] ⇒ binary search on k.

How this code works:
  - hours(k, remainhours): subtracts ceil(pile / k) per pile and early-returns
    False if we exceed h.
  - Binary search [l=1, r=max(piles)]:
      * If hours(mid, h) is True, mid is fast enough → try smaller (r = mid - 1),
        track res = mid.
      * Else mid is too slow → try larger (l = mid + 1).
  - Return the smallest feasible speed found in res.

Why correct:
  Because hours(k) is non-increasing in k, there exists a threshold T such that
  all k < T are infeasible and all k ≥ T are feasible. The search above shrinks
  onto T and returns it.

Complexity:
  Time: O(n · log(max(piles)))  (each feasibility check scans piles once)
  Space: O(1).

Pitfalls / notes:
  - Use ceiling per pile (math.ceil or the integer trick (p + k - 1) // k).
  - Watch off-by-one: here we do while l <= r with a tracked res. (Alternative:
    lower-bound form while l < r and return l.)
  - Consider renaming hours → can_finish for clarity.
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours(k, remainhours):
            for bananas in piles:
                remainhours -= math.ceil(bananas / k)
                if remainhours < 0:
                    return False
            return True

       
        l,r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if hours(mid, h):
                # Koko may able to eat even slower, try slower
                res = mid
                r = mid - 1
            else:
                # curr mid is too slow, try faster one
                l = mid + 1
                
        return res
        
