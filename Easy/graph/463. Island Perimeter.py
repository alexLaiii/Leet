"""
Return the perimeter of the single island in a binary grid using DFS.

The idea:
- Find the first land cell (value 1) and start a DFS from there.
- Each DFS call:
- Contributes 1 to the perimeter when stepping out of bounds or onto water (0),
since that edge is a boundary of the island.
- Contributes 0 if the cell is already visited (marked as 2), since its edges
have already been counted.
- Marks the current land cell as visited (set to 2), then explores its 4 neighbors.
- The total perimeter is the sum of boundary contributions from all DFS calls.

Time Complexity: O(M * N), since each cell is visited at most once.
Space Complexity: O(M * N) in the worst case due to recursion depth.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= M or col < 0 or col >= N or grid[row][col] == 0:
                return 1
            if grid[row][col] == 2:
                return 0
            grid[row][col] = 2
            return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return dfs(i, j)
