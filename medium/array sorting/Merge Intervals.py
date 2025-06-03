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
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]]

        for start, end in intervals:
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            # Note: The first condition covers all overlapping cases — including full containment.
            # For example, if res = [1, 10] and the current interval = [5, 9], since 10 >= 5, it triggers the merge.
            # Any interval that doesn't satisfy the first condition must be completely separate.
            # For example, res = [1, 10] and interval = [11, 13] — no overlap, so it's added as a new interval.
            else:
                res.append([start, end])
        return res

            
            


   

            
            
                
                
            
        
        
            


   

            
            
                
                
            
        
        
