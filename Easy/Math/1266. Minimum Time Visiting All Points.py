"""
Problem:
Given a list of 2D points, return the minimum time required to visit all points
in order. In one second, you may move horizontally, vertically, or diagonally
by one unit.

Key Insight:
From point A to point B:
- Let dx = |x2 - x1| and dy = |y2 - y1|
- Diagonal moves reduce both dx and dy simultaneously
- Use diagonal moves for min(dx, dy) seconds
- Use straight moves for the remaining |dx - dy| seconds
- Total time = min(dx, dy) + |dx - dy| = max(dx, dy)

Algorithm:
- Iterate through consecutive point pairs
- For each pair, compute dx and dy
- Add max(dx, dy) to the total time

Correctness:
This greedy approach is optimal because diagonal movement maximizes distance
covered per second whenever possible.

Time Complexity:
O(n), where n is the number of points

Space Complexity:
O(1), constant extra space
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            distanceX, distanceY = abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])
            res += max(distanceX, distanceY)
        return res
