  """
  Return all intersections between two lists of closed, pairwise-disjoint, sorted intervals.

  Approach:
  - Maintain a rolling window `prevMerge` that represents the most recently
    seen interval boundary while scanning both lists in sorted order.
  - At each step, compare the next candidate interval (`nextCheck`) from
    either list (whichever starts earlier) with `prevMerge`.
    If they overlap (prevMerge.end >= nextCheck.start), emit their
    intersection [max(starts), min(ends)] and extend `prevMerge.end` to the
    larger end to keep the current window; otherwise reset `prevMerge` to
    `nextCheck`.
  - Continue until both lists are consumed or no future overlap is possible.

  Correctness:
  - Because both input lists are sorted and disjoint within themselves,
    the earliest-start-first scan never skips a potential overlap, and
    each overlap is computed exactly once using max/min of endpoints.

  Time:  O(m + n)
  Space: O(1) besides the output
  """
"""
Cleaner version
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersect = []
        i , j = 0,0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if end >= start:
                intersect.append([start,end])
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                
        return intersect


"""
My original solution
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i,j = 0, 0
        prevMerge = []
        intersect = []
        while i < len(firstList) or j < len(secondList):
            if i >= len(firstList):
                if prevMerge[1] >= secondList[j][0]:
                    intersect.append([max(prevMerge[0], secondList[j][0]), min(prevMerge[1], secondList[j][1])])
                    prevMerge[1] = max(prevMerge[1], secondList[j][1])
                    j += 1
                else:
                    break
            elif j >= len(secondList):
                if prevMerge[1] >= firstList[i][0]:
                    intersect.append([max(prevMerge[0], firstList[i][0]), min(prevMerge[1], firstList[i][1])])
                    prevMerge[1] = max(prevMerge[1], firstList[i][1])
                    i += 1
                else:
                    break
            elif not prevMerge:
                if firstList[0][0] <= secondList[0][0]:
                    prevMerge = firstList[0]
                    i += 1
                else:
                    prevMerge = secondList[0]
                    j += 1
            else:
                if firstList[i][0] <= secondList[j][0]:
                    nextCheck = firstList[i]
                    i += 1
                else:
                    nextCheck = secondList[j]
                    j += 1
                if prevMerge[1] >= nextCheck[0]:
                    intersect.append([max(prevMerge[0], nextCheck[0]), min(prevMerge[1], nextCheck[1])])
                    prevMerge[1] = max(prevMerge[1], nextCheck[1])
                else:
                    prevMerge = nextCheck
        return intersect



                
            
