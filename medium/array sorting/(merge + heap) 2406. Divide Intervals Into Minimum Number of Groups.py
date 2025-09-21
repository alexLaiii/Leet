  """
  Review docstring — Interval partitioning via min-heap (your version)

  What this does:
      - Sort intervals by start.
      - Keep a min-heap `minHeap` that stores the *current last end* of each group.
      - Initialize with the first interval’s end and `groups = 1`.
      - For each next [start, end]:
          * If the earliest group end (heap[0]) >= start, the new interval overlaps
            that group under inclusive endpoints ⇒ no existing group fits ⇒ open a new group
            (increment `groups`).
          * Else, the earliest group ended strictly before `start` ⇒ reuse it
            (pop its end from the heap).
          * Push the current interval’s end to update the used/new group’s last end.

  Why it works (intuition):
      - The heap tracks one end per active group. If even the smallest end overlaps the new
        start, then all groups overlap ⇒ we must add a group. Otherwise, greedily reuse the
        earliest-finishing group to keep options open for future intervals.

  Notes:
      - LeetCode 2406 treats touching intervals as overlapping (e.g., [1,2] and [2,3]).
      - `groups` equals the max number of concurrent active groups; in this pattern it’s tracked
        explicitly rather than via max heap size.

  Complexity:
      - Time: O(n log n) due to sorting and per-interval heap ops.
      - Space: O(n) in the worst case for the heap.

  (Optional hardening: if `intervals` could be empty, guard it before accessing intervals[0].)
  """

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        minHeap = [intervals[0][1]]
        groups = 1

        for start,end in intervals[1:]:
            if minHeap[0] >= start:
                groups += 1
            else:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return groups

