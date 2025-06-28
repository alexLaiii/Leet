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
