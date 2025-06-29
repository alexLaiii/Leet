"""
This problem shares a similar idea with "62. Unique Paths".

Important Constraint:
- You can only move either **down** or **right** at any point in time.  
  This constraint simplifies the DP logic significantly.

Idea:
We use dynamic programming to store the **minimum path sum** from the top-left corner to each cell in the grid.  
For any cell `(i, j)`, the **minimum path sum** is:
  → `min(from top, from left) + current cell value`

- First row and first column are base cases (can only come from one direction)
- By the time we reach the bottom-right cell, we have the **minimum sum path** calculated.

Time Complexity:
- `O(m * n)` → Every cell is visited once.

Space Complexity:
- `O(1)` → if modifying `grid` in-place (as in your code)
- `O(m * n)` → if using a separate DP grid.
"""
# Inplace DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and j - 1 >= 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j - 1]) + grid[i][j]
                elif j - 1 >= 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i - 1 >= 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]

        return grid[-1][-1]
                

# 2D DP grid
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])


        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]
      

        for j in range(1, N + 1):
            dp[1][j] = dp[1][j-1] + grid[0][j - 1]

        for i in range(1, M + 1):
            dp[i][1]  = dp[i-1][1] + grid[i-1][0]

        for i in range(2, M + 1):
            for j in range(2, N + 1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]
