"""
This problem is a variation of "Leetcode 200: Number of Islands".

Idea:
When we find an island (i.e., grid[i][j] == 1), we use DFS to traverse the entire island and count its size along the way.

Note: Whenever we visit a cell, we flood it (set it to 0) to mark it as visited. This prevents revisiting the same cell later or counting the same island again in future DFS calls.

We maintain a variable `maxArea` to keep track of the largest island seen so far:
    maxArea = max(maxArea, dfs(i, j))

If there are no islands in the grid, the condition `if grid[i][j] == 1` will never trigger, so `maxArea` stays at 0 and is safely returned.

Time Complexity: O(m * n)

- In the worst case, every cell is land (1), so:
  - The outer `for` loop checks every cell once → O(m * n)
  - The `dfs` visits each land cell exactly once → total O(m * n)
- So total time = O(m * n + m * n) = O(m * n)

Space Complexity: O(m * n)

- Due to recursion stack in DFS.
- In the worst case (grid full of land), the recursion can go as deep as all cells → O(m * n) stack space.
- If implemented with BFS and an explicit queue, it would also use up to O(m * n) space.

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count = 1
            count += dfs(r+1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            return count
            
        maxArea = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:         
                    maxArea = max(maxArea, dfs(i,j))
        return maxArea
