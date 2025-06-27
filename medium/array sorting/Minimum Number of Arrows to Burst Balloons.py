"""
This problem is easier if sorted by END time, but it can also be solved by sorting by START.

Problem:
Given balloons represented as intervals, one arrow can burst all balloons that overlap.
The goal is to minimize the number of arrows required.

Greedy Idea:
- If two balloons overlap, one arrow can burst them both.
- If they don't overlap, we need a new arrow.
- To minimize arrows, always shoot at the end of the current overlapping range.

Approach (Sort by END):
1. Sort all intervals by their end value.
2. Initialize `arrow = 1` since we need at least one arrow.
3. Set `prevEnd` as the end of the first balloon.
4. Iterate through remaining intervals:
   - If `start <= prevEnd`: current balloon overlaps with previous, one arrow suffices.
     - No new arrow is needed.
   - Else: no overlap, need a new arrow.
     - Increment `arrow`.
     - Update `prevEnd = end`.

🔎 Why Sorting by End Works:
- Sorting by end ensures we always deal with the balloon that ends earliest.
- If the next balloon starts after that, it must be non-overlapping. (Since the END is guranteen larger by sorting)
- This implicitly enables a greedy selection of the maximum number of balloons per arrow.

⚠️ Example Clarification:
You might ask: what if `[5,7]` comes after `[5,9]`? Won’t `[5,9]` miss `[5,7]`?
No — since we sorted by end, `[5,7]` comes **before** `[5,9]`, so no cases like this would occur.

Time Complexity: O(n log n) — sorting
Space Complexity: O(1)

---

Alternative (Sort by START):
1. Sort intervals by start.
2. Track the minimum `overlap = end` of overlapping intervals.
3. If next `start <= overlap`, update `overlap = min(overlap, end)` (shrink range).
4. If `start > overlap`, need a new arrow.

This method also works but requires explicit management of the overlap window.
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrow, currEnd = len(points), points[0][1]

        for start,end in points[1:]:
            if currEnd >= start:
                arrow -= 1
            else:
                # new arrow
                currEnd = end

        return arrow



# Solution 2, same idea:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prevEnd = points[0][1]
        arrow = 1

        for start, end in points[1:]:
            if prevEnd < start:
                arrow += 1
                prevEnd = end

        return arrow



# Solution 3, sort by start, with greedy picking the end
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        overLap = points[0][1]
        arrow = 1
        for start, end in points[1:]:
            if overLap >= start:
                # We can shoot the curret ballon with the previous arrow, so keep this arrow and mark overlap as the furthest it can reach
                overLap = min(overLap, end)
            else:
                # The previous arrow can't shoot the current ballon, we need to shot a new arrow and mark this overlap as the furthest it can reach
                arrow += 1
                overLap = end
        return arrow

        
