"""
This is a graph traversal problem.

Example:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Result: 3 islands

Idea:
Since all adjacent "1"s represent the same island, they form a connected group — a graph.
So, each island is essentially a connected component in the grid.

We use DFS (Depth-First Search) to explore each component (island).
When we visit a cell with "1", we recursively visit all its adjacent land cells (up, down, left, right),
and mark them as "0" (flooded/visited) to avoid revisiting.

This guarantees correctness: every "1" in the same island is visited once,
and "1"s that are not connected (i.e., different islands) will be counted separately.

Implementation:
- Loop through every cell in the grid.
- If a cell contains "1", we start a DFS from that cell.
- In the DFS:
    - Base case: return if the cell is out of bounds or already "0".
    - Mark the cell as visited by setting grid[r][c] = "0".
    - Recursively call DFS in 4 directions:
        - dfs(r+1, c)  # South
        - dfs(r-1, c)  # North
        - dfs(r, c+1)  # East
        - dfs(r, c-1)  # West

After the DFS, all the nodes representing the island will be marked as "0", 
so when the outer loop continues, those nodes are already visited and won't trigger another DFS.

Increment the island count by 1 since an island has just been fully visited and marked.

Keep looping through the grid to find another "1" that is not connected to the previous island.
If found, perform the same DFS logic again.

Repeat this process until all islands (connected components of "1"s) are found and counted.

Note:
The order of traversal does not matter since we always mark visited cells as "0".
Each DFS guarantees full traversal of one island.

Time Complexity:
O(m * n), where m = number of rows, n = number of columns.
Each cell is visited once.

Space Complexity:
O(m * n) worst-case due to recursion stack (if all land).
No extra space used for tracking visited — we modify the grid in-place.
"""


class Solution(object):
    def numIslands(self, grid):
        islands, rows, cols = 0, len(grid), len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
        

            
                


        
