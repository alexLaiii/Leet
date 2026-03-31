"""
Determine whether a grid can be partitioned into two parts with equal sum
using a single horizontal or vertical cut.

Approach:
1. Compute the total sum of all elements in the grid.
2. If the total sum is odd, return False immediately since it cannot be split evenly.
3. Let half = totalSum // 2 be the target sum for one partition.
4. Attempt a horizontal partition:
   - Accumulate row sums from top to bottom.
   - Stop once the accumulated sum reaches or exceeds half.
   - If it equals half exactly, return True.
5. If horizontal partition fails, attempt a vertical partition:
   - Accumulate column sums from left to right.
   - Stop once the accumulated sum reaches or exceeds half.
   - If it equals half exactly, return True.
6. If neither partition works, return False.

Notes:
- The grid is partitioned using a full row cut or full column cut.
- Both resulting parts must be non-empty.
- The algorithm relies on prefix sums over rows and columns.

Time Complexity:
    O(M * N), where M is the number of rows and N is the number of columns.

Space Complexity:
    O(1), since only a few variables are used.

:param grid: 2D list of integers representing the grid
:return: True if a valid equal-sum partition exists, False otherwise
"""

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        totalSum = 0
        for i in range(M):
            for j in range(N):
                totalSum += grid[i][j]
        
        if totalSum % 2 == 1:
            return False
        half = totalSum // 2
        row_tol_sum = 0
        row = 0
        while row_tol_sum < half:
            for j in range(N):
                row_tol_sum += grid[row][j]
            
            row += 1
        if row_tol_sum == half:
            return True
        
        col_tol_sum = 0
        col = 0
        while col_tol_sum < half:
            for i in range(M):
                col_tol_sum += grid[i][col]
            col += 1
        if col_tol_sum == half:
            return True
        return False
