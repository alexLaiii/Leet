"""
Return the area of the rectangle that has the longest diagonal.
If multiple rectangles share the same (maximum) diagonal length, return the
largest area among them.

Approach:
- Iterate through each (l, w).
- Compute its diagonal length via the Pythagorean theorem: sqrt(l^2 + w^2).
- Track the largest diagonal seen so far and the best area tied to it.
* If a rectangle has a strictly longer diagonal, replace both best diagonal
  and best area.
* If it ties the best diagonal, update best area with max(area).

Time Complexity: O(n), where n = len(dimensions)
Space Complexity: O(1)
"""

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        largestD = 0
        largestA = 0

        for l,w in dimensions:
            diagLen = math.sqrt(l*l + w*w)
            if diagLen > largestD:
                largestD = diagLen
                largestA = l * w
            elif diagLen == largestD:
                largestA = max(largestA, l * w)
        
        return largestA 
                
            

        
