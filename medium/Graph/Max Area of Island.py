"""
This problem is a variation of "Leetcode 200: Number of islands"

Idea: 
When we find an island (grid[i][j] == 1), we use DFS to go through the entire island and count the the size of the island along the way.
Note that whenever we travel a cell, we flood that cell (mark it to 0), to indicate it as visited, So it wont visited again 
or for the later for loop, it will recognize it as the same island visited before.

Use a maxArea variable to keepTrack of the largest island, (maxArea = max(maxArea, dfs(i,j)))
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
