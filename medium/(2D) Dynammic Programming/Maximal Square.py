"""
Remember that each cell store the maximal square of that position included that cell.
"""



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for j in range(N + 1)] for i in range(M+1)]
        max_size = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if int(matrix[i-1][j-1]) == 0:
                    continue
                if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

                max_size = max(max_size, dp[i][j])
    
        return max_size ** 2

        
