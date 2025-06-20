class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= M or c >= N or (r,c) in visited or grid[r][c] == 0:
                return
            visited.add((r,c))
            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for dr,dc in directions:
                dfs(r+dr, c+dc)
                

        for i in range(M):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][N - 1] == 1:
                dfs(i, N - 1)
        
        for j in range(N):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[M - 1][j] == 1:
                dfs(M-1, j)
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count += 1
        return count
