  """
  Removes all intervals that are covered by another interval.
  
  An interval [a, b] is considered covered by [c, d] if c <= a and b <= d.
  
  Approach:
  1. Sort the intervals by their start point in ascending order.
  2. Iterate through the sorted list while maintaining a 'previous' interval (prevStart, prevEnd).
  3. For each current interval (start, end), check:
     - If prevEnd >= end:
         → The current interval is fully covered by the previous interval, so reduce the count.
     - Else if prevStart == start:
         → The current interval starts at the same point but extends further.
         → It's considered as "replacing" the previous one, so update prevEnd and reduce count.
     - Else:
         → The current interval is not covered, so update prevStart and prevEnd.
  4. Return the number of remaining (non-covered) intervals.

  Notes:
  - The sort only uses x[0], so when intervals have the same start, their end values are not compared directly.


  Time Complexity:
      - Sorting takes O(n log n)
      - Scanning intervals takes O(n)
      - Overall: O(n log n)

  Example:
      Input: [[1,4],[3,6],[2,8]]
      After sort: [[1,4],[2,8],[3,6]]
      Logic removes [3,6] because it is covered by [2,8]
      Output: 2
  """

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        remain = len(intervals)
        prevStart, prevEnd =  intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd >= end:
                remain -= 1
            elif prevStart == start:
                remain -= 1
                prevEnd = end
            else:
                prevStart = start
                prevEnd = end
        return remain


        
        
