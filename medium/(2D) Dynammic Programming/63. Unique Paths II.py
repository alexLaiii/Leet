  """
  Compute the number of unique paths from the top-left to the bottom-right
  of a grid with obstacles, where the robot can only move right or down.

  Uses dynamic programming: dp[i][j] stores the number of ways to reach
  cell (i, j). For non-obstacle cells, dp[i][j] = dp[i-1][j] + dp[i][j-1].
  The first row and first column are initialized carefully so that once an
  obstacle appears, all cells after it in that row/column remain unreachable.

  Returns 0 if the start cell is blocked or if the destination is unreachable.
  """

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(N)] for i in range(M)]
        for i in range(M):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(N):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]
        return dp[M-1][N-1]
