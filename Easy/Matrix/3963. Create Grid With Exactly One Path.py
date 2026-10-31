"""
Create a grid with exactly one path from the top-left to the bottom-right.

Start with all cells open ('.'), then block ('#') every cell outside
the first column and bottom row. From the starting cell, the only
possible move is down until reaching the bottom row, then right until
reaching the destination. Since there are no alternative routes, exactly
one valid path exists.

If there is only one row or column, the grid remains entirely open
and still has exactly one straight path.

Time complexity: O(m * n) to construct and convert the grid to strings.
Space complexity: O(m * n) for the grid and returned strings.
"""

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['.' for j in range(n)] for i in range(m)]
        for i in range(m - 1):
            for j in range(1, n):
                grid[i][j] = '#'
        for i in range(m):
            grid[i] = "".join(grid[i])
 
        return grid
