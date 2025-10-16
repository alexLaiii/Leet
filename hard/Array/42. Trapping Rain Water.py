"""
LeetCode 42 — Trapping Rain Water (Prefix/Suffix Maxima Approach)

Idea
-----
Water above index i is determined by the *shorter* of the tallest bars seen to its
left and right. If L[i] is the maximum height in height[0..i] and R[i] is the
maximum in height[i..n-1], then water at i equals:
    max(0, min(L[i], R[i]) - height[i])

What this code does
-------------------
1) Builds `maxLeft` so that maxLeft[i] = max(height[0..i]).
   - Starts with height[0], then extends by comparing to the previous prefix max.

2) Builds `maxRight` so that maxRight[i] = max(height[i..n-1]).
   - Initializes with the last element; fills right→left using a running suffix max.

3) Sums trapped water at each index:
   - traps += min(maxLeft[i], maxRight[i]) - height[i]
   - (In production code, clamp with max(0, …) for safety, though with correct
     prefix/suffix arrays this should already be non-negative.)

Complexity
----------
Time:  O(n) — three linear passes.
Space: O(n) — two auxiliary arrays (maxLeft, maxRight).

Correctness intuition
---------------------
Any water at position i must be bounded on both sides. The highest possible
water level is the lesser of the best left bound and the best right bound.
Subtracting the bar’s own height yields the water depth at i.

Edge cases & notes
------------------
- Empty input should return 0 (current code would index height[0] and error).
- Consider adding: `if not height: return 0`.
- Consider clamping: `max(0, min(maxLeft[i], maxRight[i]) - height[i])`.
- Naming: the loop variable `n` shadows the length `n`. Rename the loop
  variable to avoid confusion, e.g. `for h in height[1:]:`.

Alternatives
------------
- Two-Pointer O(1) space:
  Move the pointer on the side with smaller current height; accumulate water
  using a running leftMax/rightMax.
- Monotonic decreasing stack:
  Pop a “valley bottom” and compute the trapped area between the new stack top
  (left wall) and the current index (right wall).

Quick sanity checks
-------------------
[] → 0
[0,1,0,2,1,0,1,3,2,1,2,1] → 6
[4,2,0,3,2,5] → 9
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [height[0]]
        maxRight = [-1] *n
        maxRight[-1] = height[-1]
        for n in height[1:]:
            if n > maxLeft[-1]:
                maxLeft.append(n)
            else:
                maxLeft.append(maxLeft[-1])
        
        for i in range(len(height) - 2, -1, -1):
            if height[i] > maxRight[i + 1]:
                maxRight[i] = height[i]
            else:
                maxRight[i] = maxRight[i + 1]
        traps = 0
        for i in range(len(height)):
            traps += (min(maxLeft[i], maxRight[i]) - height[i])
        return traps
