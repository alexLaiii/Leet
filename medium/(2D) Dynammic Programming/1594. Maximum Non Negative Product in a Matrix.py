"""
Compute the maximum non-negative product from the top-left to the bottom-right
of a grid, moving only right or down.

Approach:
- Use Dynamic Programming where each cell stores a pair:
    (max_product, min_product) reachable at that cell.
- Tracking both is necessary because negative values can flip signs:
    a large negative * negative → large positive.

DP Definition:
- dp[i][j] = (largest product, smallest product) ending at (i, j)

Transition:
- From top (i-1, j) and left (i, j-1), compute all possible products:
    grid[i][j] * previous max and min
- Take:
    max(...) → new largest
    min(...) → new smallest

Initialization:
- dp[0][0] = (grid[0][0], grid[0][0])
- First row/column only have one possible path

Result:
- If the final maximum product is negative → return -1
- Otherwise return result modulo 10^9 + 7

Time Complexity: O(M * N)
Space Complexity: O(M * N)

Key Insight:
- Must track both max and min at each step due to sign changes.
"""

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        M,N = len(grid), len(grid[0])
        dp = [[(0,0) for _ in range(N)] for _ in range(M)]
        # precompute to prevent index out of range
        # (largest, smallest) pair
        dp[0][0] = (grid[0][0], grid[0][0])
        for i in range(1, M):
            val = dp[i - 1][0][0] * grid[i][0]
            dp[i][0] = (val, val)
        for j in range(1, N):
            val = dp[0][j - 1][0] * grid[0][j]
            dp[0][j] = (val,val)
       
        for i in range(1, M):
            for j in range(1, N):
                curr_val = grid[i][j]
                left_pair = dp[i][j-1]
                top_pair = dp[i-1][j]
                all_vals = [curr_val * left_pair[0], curr_val * left_pair[1], curr_val * top_pair[0], curr_val * top_pair[1]]
                dp[i][j] = (max(all_vals), min(all_vals))
  
        
        return dp[-1][-1][0] % MOD if dp[-1][-1][0] >= 0 else -1
            
