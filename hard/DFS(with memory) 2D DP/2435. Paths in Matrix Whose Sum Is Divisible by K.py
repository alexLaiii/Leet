  """
  Count the number of paths from (0,0) to (M-1,N-1) (moving only right or down)
  such that the path sum is divisible by k.

  Core idea (DP over remainders):
  - For each cell, we only care about the path sum modulo k, not the full sum.
  - Let dp[c][r] = number of ways to reach the current row's column c with
    (path_sum % k) == r.
  - Transition: coming into (i,j) from top or left shifts remainders by grid[i][j]:
      new_r = (old_r + grid[i][j]) % k

  Rolling row optimization:
  - prev_dp stores dp for the previous row (size N x k).
  - curr_dp stores dp for the current row (size N x k).
  - This reduces space from O(M*N*k) to O(N*k).

  Initialization:
  - Start at (0,0): prev_dp[0][grid[0][0] % k] = 1
  - Fill the first row using only left transitions.

  Row processing:
  - For each new row i:
    * Fill first column using only top transitions.
    * Fill remaining columns using both top (prev_dp[j]) and left (curr_dp[j-1]).

  Result:
  - Answer is the number of ways to reach the bottom-right cell with remainder 0:
    prev_dp[N-1][0].

  Complexity:
  - Time:  O(M * N * k)  (each cell processes k remainders)
  - Space: O(N * k)      (two rows of DP)

  Important implementation note:
  - For performance, DP values should be kept modulo MODULO at the point of update
    (i.e., mod the *accumulated bucket*), otherwise numbers can grow huge and slow
    down Python big-int arithmetic.
  """


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MODULO = 10 ** 9 + 7
        M, N = len(grid), len(grid[0])
        prev_dp = [[0] * k for i in range(N)]
        remainder = grid[0][0] % k
        prev_dp[0][remainder] += 1
        for i in range(1, N):
            for j in range(k):
                remainder = (j + grid[0][i]) % k
                prev_dp[i][remainder] += prev_dp[i - 1][j] % MODULO
        
        for i in range(1, M):
            curr_dp = [[0] * k for i in range(N)]
            for z in range(k):
                remainder = (z + grid[i][0]) % k
                curr_dp[0][remainder] += prev_dp[0][z] % MODULO
            for j in range(1, N):
                for z in range(k):
                    remainder = (z + grid[i][j]) % k
                    curr_dp[j][remainder] += (prev_dp[j][z] + curr_dp[j - 1][z]) % MODULO
        
            prev_dp = curr_dp
        
        return prev_dp[-1][0]
