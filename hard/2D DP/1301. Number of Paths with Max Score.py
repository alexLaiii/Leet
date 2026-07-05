"""
Dynamic Programming.

The algorithm is divided into two phases.

1. Compute the maximum score obtainable for every cell.
   Starting from the top-left, each reachable cell stores the
   largest score that can be collected when arriving there using
   only moves from the left, top, or top-left. Blocked cells are
   marked as unreachable.

2. Count the number of paths that achieve the maximum score.
   Using the previously computed score table, each cell sums the
   number of ways from predecessor cells whose score plus the
   current cell's value equals the optimal score for that cell.
   The number of paths is taken modulo 10^9 + 7.

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD =  10 ** 9 + 7
        M, N = len(board), len(board[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        for i in range(1, N):
            num = board[0][i]
            if dp[0][i - 1] == -1:
                dp[0][i] = -1
            elif num == "X":
                dp[0][i] = -1
            elif num == "S":
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = int(board[0][i]) + dp[0][i - 1]
        for j in range(1, M):
            num = board[j][0]
            if dp[j - 1][0] == -1:
                dp[j][0] = -1
            elif num == "X":
                dp[j][0] = -1
            elif num == "S":
                dp[j][0] = dp[j-1][0]
            else:
                dp[j][0] = int(board[j][0]) + dp[j - 1][0]
        
        for i in range(1, M):
            for j in range(1, N):
                val = board[i][j]
                if val == "X":
                    dp[i][j] = -1
                    continue
                if val == "S":
                    val = "0"
                left = topLeft = top = -1
                if board[i][j - 1] != "X":
                    left = dp[i][j - 1]
                if board[i-1][j-1] != "X":
                    topLeft = dp[i-1][j-1]
                if board[i-1][j] != "X":
                    top = dp[i-1][j]
                maximum = max(left, topLeft, top)
                if maximum == -1:
                    dp[i][j] = -1
                else:
                    dp[i][j] = maximum + int(val)
            
       
        if dp[-1][-1] == -1:
            return [0,0]
        path_dp = [[[0,0] for _ in range(N)] for _ in range(M)]
        path_dp[0][0] = [1, 0]
        
        for i in range(1, N):
            if board[0][i] == "X":
                path_dp[0][i] = (-1, -1)
            else:
                path_dp[0][i] = (path_dp[0][i-1][0], dp[0][i])
        for j in range(1, M):
            if board[j][0] == "X":
                path_dp[j][0] = (-1, -1)
            else:
                path_dp[j][0] = (path_dp[j - 1][0][0], dp[j][0])
        # dp mark the max
        
        for i in range(1, M):
            for j in range(1, N):
                maximum = dp[i][j]
                if dp[i][j] == -1:
                    path_dp[i][j] = (-1, -1)
                    continue
                val = board[i][j]
                if val == "S":
                    val = 0
                else:
                    val = int(val)
                path_dp[i][j][1] = dp[i][j]
                # left
                if dp[i][j - 1] != -1 and val + dp[i][j - 1] == dp[i][j]:
                    path_dp[i][j][0] += path_dp[i][j - 1][0]
                # top left
                if dp[i - 1][j - 1] != -1 and val + dp[i - 1][j - 1] == dp[i][j]:
                    path_dp[i][j][0] += path_dp[i - 1][j - 1][0]
                # top
                if dp[i - 1][j] != -1 and val + dp[i - 1][j] == dp[i][j]:
                    path_dp[i][j][0] += path_dp[i - 1][j][0]
                path_dp[i][j][0] = path_dp[i][j][0] % MOD
        return [path_dp[-1][-1][1], path_dp[-1][-1][0]]
        
