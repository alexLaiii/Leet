"""
Find the largest area triangle that can be formed from any 3 points.

Brute-forces every combination of 3 points (C(n,3) triples) and computes
each triangle's area via the shoelace/cross-product formula:
  Area = (1/2) * |x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)|
which gives the area directly from coordinates with no need to find
an explicit base and height (works for any orientation of triangle).

Args:
  points: List of [x, y] integer coordinate pairs, len(points) >= 3.

Returns:
  The maximum triangle area achievable from any 3 of the points.

Time complexity: O(n^3) - three nested loops over point indices.
Space complexity: O(1) beyond the input.
"""
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2,y2 = points[j]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]
                    res = max(res, (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    
        return res

                    
        
