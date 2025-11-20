"""
Greedy intuition for 757. Set Intersection Size At Least Two

We need to choose a set S of integers such that:
    - For every interval [li, ri], there are at least TWO numbers from S inside it.
    - We want |S| to be as small as possible.

Key ideas:

1. Sort intervals by their right endpoint (end) in ascending order.
   If two intervals have the same end, sort the one with the LARGER start first:
       intervals.sort(key=lambda x: (x[1], -x[0]))
   Why?
     - Once an interval ends at 'end', any numbers > end are useless for that interval.
     - By processing smallest 'end' first, when we choose new points, placing them near 'end'
       gives them the best chance to be reused by future intervals (which end later).

2. Only track the two largest points we have chosen so far.
   Let:
       a = second largest chosen point
       b = largest chosen point
   (We maintain a <= b.)
   We don't need the full set S for the greedy decision:
     - When considering a new interval [L, R], only the largest points matter, because
       intervals are processed in order of increasing R.
     - If some older, smaller point < a didn't help the current interval, it also
       won't help future intervals (whose R are >= current R), so it doesn't affect our choices.

3. For each interval [L, R], count how many of a and b fall inside it:
       cnt = (L <= a <= R) + (L <= b <= R)
   - If cnt == 2:
       This interval already has at least two points from S. Do nothing.
   - If cnt == 1:
       This interval has exactly one useful point so far. We must add ONE more point.
       Greedy choice: add R.
       Then update: a = b, b = R.
       (We push our new point to the right, at R, so it has maximum chance to help later intervals.)
   - If cnt == 0:
       This interval has no useful point yet. We must add TWO points.
       Greedy choice: add R - 1 and R.
       Then update: a = R - 1, b = R.
       Again, both are as far to the right as possible to help future intervals.

4. Why is this optimal?
   - Suppose we need to add k new points (k is 1 or 2) for [L, R].
   - Any valid solution must choose at least k points inside [L, R].
   - Among all such choices, putting them as far right as possible (R-1, R) cannot be worse,
     because future intervals will end at R' >= R, so these rightmost points are
     "most likely" to lie inside them.
   - There exists an optimal solution that follows exactly this "put new points at the right end"
     rule, so our greedy is safe.

5. Complexity:
   - Sorting intervals: O(n log n)
   - One pass through the intervals, O(n) time.
   - Overall: O(n log n) time, O(1) extra space (besides the input).

This method avoids tracking all chosen points explicitly; instead we only keep
the two largest points, which is enough due to the sorted-by-end processing order.
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1] )
        greedyPick = set()
        
        for start, end in intervals:
            count = 0
            for n in greedyPick:
                if start <= n and n <= end:
                    count += 1
                    if count == 2:
                        break
    
            if count == 0:
                greedyPick.add(end - 1)
                greedyPick.add(end)
            elif count == 1:
                if end not in greedyPick:
                    greedyPick.add(end)
                else:
                    greedyPick.add(end - 1)

        return len(greedyPick)
                
