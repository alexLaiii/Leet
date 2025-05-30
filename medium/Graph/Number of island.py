class Solution(object):
    def numIslands(self, grid):
        rows, cols, islands = len(grid), len(grid[0]), 0
        def dfs(r,c):
            if  r >= rows or  c >= cols or r < 0 or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    dfs(i,j)
                    islands += 1
        return islands
        

            
                


        
