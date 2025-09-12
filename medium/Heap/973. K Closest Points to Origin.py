"""
LeetCode 973 — K Closest Points to Origin
Review Docstring (matches the provided min-heap solution)

Idea
-----
Use a priority key = squared Euclidean distance (x^2 + y^2). Since sqrt is
monotonic, sorting/ordering by squared distance yields the same order as by the
actual distance. This avoids floating point work and precision issues.

Algorithm (Min-Heap of all points)
-----------------------------------
1) For each point (p1, p2), compute dist2 = p1*p1 + p2*p2.
2) Push (dist2, p1, p2) into a min-heap.
3) Pop k times; the popped points are the k closest.

Correctness Sketch
-------------------
Each heap pop returns the currently smallest dist2 among all remaining points.
After k pops, we have extracted exactly the k points with the smallest keys,
i.e., the k closest (ties are allowed to be in any order per problem).

Complexity
-----------
Let n = len(points).
- Time: O(n log n) to push n items + O(k log n) to pop k items ⇒ O(n log n).
- Space: O(n) for the heap.

Why squared distance (no sqrt)?
-------------------------------
- sqrt is unnecessary for comparison (monotone).
- Avoids floats and rounding.
- Slightly faster.

Edge Cases
-----------
- k == 0 → return [] after zero pops.
- k == n → you’ll effectively return all points (order by distance).
- Negative coordinates and duplicate points are handled naturally.
- Ties in distance can be returned in any order.

Implementation Notes
---------------------
- Store the key (dist2) first in the heap tuple so the heap orders by it.
- Variable names in your code:
  - `distance_sq` is accurate (it’s a squared distance).
  - `minHeap` contains tuples (distance_sq, p1, p2).
- Marking order stability is not required by the problem.

Alternatives (when n is large and k is small)
----------------------------------------------
1) Size-k Max-Heap: Keep a heap of at most k items keyed by −dist2.
   - Time: O(n log k), Space: O(k).
   - Push first k points; for each new point, pushpop if closer than the current worst.
2) Quickselect (nth_element style):
   - Average O(n), worst O(n^2) without good pivots.
   - Partition points by dist2 until the first k are the closest; then slice.

Tiny Dry Run
-------------
points = [(1,3),(−2,2),(2,−2)], k=2
dist2: (1,3)->10, (−2,2)->8, (2,−2)->8
Heap: [(8,−2,2),(10,1,3),(8,2,−2)]  # order internal to heap may vary
Pop1 -> (−2,2), Pop2 -> (2,−2)  => k closest returned.

Related Problems
-----------------
- 215. Kth Largest Element in an Array (selection/heap patterns)
- 347. Top K Frequent Elements (heap / bucket)
- 973 variants using quickselect or size-k heap
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for p1, p2 in points:
            distance_sq = (p1 ** 2) + (p2 ** 2)
            heapq.heappush(minHeap, (distance_sq, p1, p2))
    
        res = []
        for i in range(k):
            dis, p1, p2 = heapq.heappop(minHeap)
            res.append([p1,p2])
        return res
        
