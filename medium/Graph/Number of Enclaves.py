"""
This problem is essentially the same as **"130. Surrounded Regions"**.

---

### 💡 Idea:

Similar to *Surrounded Regions*, we use **DFS from the border** and mark all land cells that are **not enclaves** (i.e., land cells that can reach the border). These are stored in a `visited` set.

This time, however, the goal is to **count the land cells that are enclaves** — meaning they **cannot** reach any border.

So in the final loop, we simply count every land cell (`1`) that is **not in the `visited` set**.

---

### ✅ Summary:
- Use DFS from the borders to find land cells that are *not* enclaves.
- Traverse the entire grid and count all remaining land cells that aren't visited.

Time Complexity:
- **O(m × n)**  
  Each cell is visited at most once by DFS, and the final counting loop is also O(m × n).

Space Complexity:
- **O(m × n)** worst case  
  If the entire grid is land, the `visited` set and DFS recursion stack can grow to O(m × n).
"""


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




"""
To save space for visited, I update each traveled cell to 0 (flood), so I dont need to maintain a visited set.
Now, in the final loop, if anything is 1, it must be an enclaves.
"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        directions = [[1,0], [0,-1],[-1,0],[0,1]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == 0:
                return
            grid[r][c] = 0
            for dr,dc in directions:
                dfs(r+dr, c+dc)
            
      
        for i in range(M):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][N-1] == 1:
                dfs(i, N-1)
        
        for j in range(N):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[M-1][j] == 1:
                dfs(M-1, j)
        
        enclaves = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    enclaves += 1
        return enclaves
                
            
        
