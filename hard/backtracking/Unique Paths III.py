"""
This function finds the number of unique paths from the starting square (value 1)
to the ending square (value 2) in a 2D grid, such that every non-obstacle square (value 0)
is visited exactly once.

The algorithm works in two main phases:

1. **Grid Preprocessing Phase**:
    - We iterate through the grid to:
        a) Count how many empty cells (value 0) we need to visit (`empty_cells`).
        b) Identify the coordinates of the starting square (`start`).
    - We do not count the start or end square as part of `empty_cells`, but we must still include them in the total path.

2. **Depth-First Search (DFS) with Backtracking**:
    - We recursively explore all 4 directions from the current cell.
    - If the cell is out of bounds, an obstacle, or already visited, we return immediately.
    - If we reach the end cell (value 2), we check if the number of visited squares is exactly
      equal to `empty_cells + 1` (since we also include the start cell but not the end).
      If it is, we count this as a valid path.
    - For other cells:
        a) We mark the cell as visited using a `visited` set.
        b) Recursively explore all 4 directions from this cell.
        c) After exploring, we backtrack by removing the cell from the `visited` set
           to allow other paths to try this cell again.

Key Notes:
- `visited_cells` counts how many total squares have been visited in the current path.
- We subtract 1 before comparing with `empty_cells` at the end cell, because the end cell is not counted in the walk.
- The result is stored in `self.res`, which accumulates the total number of valid paths.

Time Complexity: O(4^E), where E is the number of empty squares. Each step can try up to 4 directions.
Space Complexity: O(E) for the recursion stack and visited set.

Returns:
- int: The number of unique paths that visit every empty square exactly once and end at the target.
"""



class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        empty_cells = 0
        start = [0,0]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    empty_cells += 1
                if grid[i][j] == 1:
                    start = [i,j]
           
        self.res = 0
        visited = set()
        def dfs(r,c, visited_cells):
            if r < 0 or r >= M or c < 0 or c >= N or (r,c) in visited or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if visited_cells - 1 == empty_cells:
                    self.res += 1
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited_cells + 1)
            dfs(r - 1, c, visited_cells + 1)
            dfs(r, c + 1, visited_cells + 1)
            dfs(r, c - 1, visited_cells + 1)
            visited.remove((r,c))
        
        dfs(start[0], start[1], 0)
            
        return self.res
