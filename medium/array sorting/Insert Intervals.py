  """
  Insert Interval — single-pass “place-by-start then sweep” strategy.

  Purpose
  -------
  Given sorted, non-overlapping intervals, insert `newInterval` and return a merged list.

  Core Intuition
  --------------
  1) **Place by start order**: Copy every interval whose **start** is strictly less than
     `newInterval.start` into the result. Because input intervals are sorted and disjoint,
     among those copied intervals, **at most the last one** can overlap with `newInterval`.
  2) **Insert/merge the new interval**: If the result is empty, append `newInterval`.
     Otherwise, compare `res[-1].end` with `newInterval.start`:
       - If `res[-1].end >= newInterval.start`, they overlap/touch → merge by extending
         `res[-1].end = max(res[-1].end, newInterval.end)`.
       - Else, append `newInterval` as a separate block.
     After this step, the tail of `res` is the **active merged interval** that will absorb
     any subsequent overlaps.
  3) **Sweep the remainder**: For each remaining interval:
       - If `interval.start <= res[-1].end`, merge into the active interval by extending
         its end.
       - Else, append it as a new disjoint block.

  Why This Works (Invariant)
  --------------------------
  - Input intervals are sorted by start and are pairwise disjoint.
  - After step (1), only `res[-1]` could possibly overlap with `newInterval`.
    Everything before `res[-1]` ends strictly before the next starts.
  - After placing/merging `newInterval`, the invariant is:
      **`res[-1]` is the unique “active” interval that can overlap with any subsequent interval.**
    Thus, a single linear sweep suffices to fold all necessary merges.

  Overlap Policy
  --------------
  - This implementation treats **touching** intervals as overlapping:
    `res[-1].end >= next.start` means `[1,2]` and `[2,3]` will merge to `[1,3]`.
    (Matches common LC57 interpretations.)

  Edge Cases Covered
  ------------------
  - `newInterval` comes **before all** intervals → result was empty, we append it first.
  - `newInterval` comes **after all** intervals → copied everything first, then append/merge.
  - `newInterval` fits **between two intervals without overlap** → appended between them.
  - `newInterval` **spans multiple** existing intervals → absorbed during the sweep.
  - Single-interval or empty input cases behave naturally.

  Complexity
  ----------
  - Time:  O(n) — single pass over the list.
  - Space: O(n) — output list (in-place merge into `res`).

  Notes vs. Canonical Pattern
  ---------------------------
  - Canonical LC57 often splits logic using `end < new.start` (strictly before),
    `start <= new.end` (overlap), and “rest”. This variant keys off **start order first**,
    then merges once, then sweeps — equivalent in correctness and complexity, often simpler
    to reason about indices.
  """

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            merged.append(intervals[i])
            i += 1
        
        if not merged:
            merged.append(newInterval)
        elif merged[-1][1] >= newInterval[0]:
            merged[-1][1] = max(merged[-1][1], newInterval[1])
        else:
            merged.append(newInterval)


        while i < len(intervals):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
            i += 1
        return merged

                
        

                
            
            
