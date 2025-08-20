"""
Extend each cell to a [3 * 3] cell to represent cut
Then use dfs() to flood out all the cell that it can traveled to, and thats one region, just like 200. Number of Islands
"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        myGrid = [[ 0 for i in range(N * 3)] for j in range(N * 3)]

        
        
        for i in range(N):
            for j in range(N):
                row = i * 3
                col = j * 3
                if grid[i][j] == "/":
                    myGrid[row][col+ 2] = 1
                    myGrid[row + 1][col + 1] = 1
                    myGrid[row + 2][col] = 1
                elif grid[i][j] == "\\":
                    myGrid[row][col] = 1
                    myGrid[row + 1][col + 1] = 1
                    myGrid[row + 2][col + 2] = 1

        def dfs(r,c):
            if r >= N * 3 or c >= N * 3 or r < 0 or c < 0 or myGrid[r][c] == 1:
                return
            myGrid[r][c] = 1
            direction = [(1,0),(-1,0), (0,1), (0,-1)]
            for dr, dc in direction:
                dfs(r + dr, c + dc)
            

        regions = 0
        for i in range(N * 3):
            for j in range(N * 3):
                if myGrid[i][j] == 0:
                    regions += 1
                    dfs(i,j)

        return regions
