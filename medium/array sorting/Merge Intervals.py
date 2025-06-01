"""
Merge overlapping intervals.

This problem struggle me for some reasons at first.

Idea:
- First, sort the intervals based on their start point.
- Initialize the result with the first interval pairs in Intervals List
- Then, scan the sorted list linearly.
    - If the current interval overlaps with the last interval in the result 
      (i.e., current start <= previous end), merge them by updating the end to max(prev_end, curr_end).
    - If there's no overlap, append the current interval as a new entry in the result.

Time Complexity:
- O(n log n): sorting takes O(n log n), scanning takes O(n), total is O(n log n).

Space Complexity:
- O(n): in the worst case, no intervals overlap and all are stored in the result list.
- In practice, if many intervals overlap, fewer merged intervals are stored.
"""


class Solution(object):
    def merge(self, intervals):
        
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for interval in intervals:
            # means overlap
            if  res[-1][1] >= interval[0] and res[-1][1] < interval[1]:
                res[-1][1] = interval[1]
            # not overlap but new pair
            elif res[-1][1] < interval[1]:
                res.append(interval)
        return res
            
            


   

            
            
                
                
            
        
        
