    """
    Count the number of submatrices that start at the top-left corner (0, 0)
    and have sum less than or equal to k.

    Core Idea:
    This problem reduces to computing 2D prefix sums, since every valid
    submatrix must begin at (0, 0). Thus, each cell (i, j) represents the
    sum of the submatrix from (0, 0) to (i, j).

    The prefix sum is computed using the inclusion-exclusion principle:
        prefix[i][j] =
            prefix[i-1][j]      (top region)
          + prefix[i][j-1]      (left region)
          - prefix[i-1][j-1]    (overlap, subtracted once)
          + current cell value

    The subtraction avoids double-counting the overlapping top-left region.

    Implementation:
    - The grid is updated in-place to store prefix sums.
    - For each cell (i, j), after computing its prefix sum,
      we check if it is <= k and increment the count.

    Time Complexity:
        O(M * N)

    Space Complexity:
        O(1) extra space (in-place modification of grid)
    """

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        count = 0
        for i in range(M):
            for j in range(N):
                if i - 1 < 0:
                    if j > 0:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j - 1 < 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += (grid[i-1][j] + grid[i][j - 1] - grid[i-1][j-1])
                if grid[i][j] <= k:
                    count += 1
        return count
