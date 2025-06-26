class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Number of arrows == Number of overlap
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
        points.sort(key=lambda x: x[1])
        arrow, currEnd = 1, points[0][1]
        for start,end in points[1:]:
            if currEnd < start:
                # need new Arrow
                arrow += 1
                currEnd = end
   
        return arrow
            
