"""
Finds the y-coordinate of a horizontal line that splits the total area of
axis-aligned squares into two equal halves.

Approach:
----------
Use binary search on the answer (y-coordinate), since the difference
between the upper area and lower area is a monotonic function of y.

For a candidate y = mid:
  - If a square lies completely below mid, its full area contributes
    to the lower half.
  - If a square lies completely above mid, its full area contributes
    to the upper half.
  - If mid cuts through a square, split its area proportionally by height.

Binary Search Logic:
--------------------
Let f(y) = upper_area(y) - lower_area(y)
- f(y) decreases monotonically as y increases.
- If upper_area > lower_area, the split line is too low → move up.
- Otherwise, the split line is high enough → move down.

Use floating-point binary search and terminate by precision, not equality.
The loop stops when (high - low) <= 1e-5, which satisfies the problem's
accepted error tolerance.

Complexity:
-----------
Time:  O(n log R), where n is the number of squares and R is the y-range.
Space: O(1) extra space.

Notes:
------
- Always use `while high - low > eps` (not >=) to avoid infinite loops
  due to floating-point precision.
- Return the midpoint of the final interval for best numerical stability.
"""
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high = 0, 10 ** 9
        while high - low > 10 ** -5:
            mid = (low + high) / 2
            lowerHalf, UpperHalf = 0.0, 0.0
            for x,y,l in squares:
                if y + l <= mid:
                    lowerHalf += l * l
                elif y >= mid:
                    UpperHalf += l * l
                else:
                    UpperHeight = (y + l) - mid
                    LowerHeight = mid - y
                    UpperHalf += l * UpperHeight
                    lowerHalf += l * LowerHeight
           
            if UpperHalf > lowerHalf:
                low = mid
            else:
                high = mid
        return low
