"""
Count unguarded cells in an m x n grid.

Idea:
- Build a grid: 0=empty, 1=wall, 2=seen-by-guard, 3=guard.
- For each guard, shoot rays in 4 orthogonal directions until blocked by a wall/guard.
  Mark cells as seen (2) the first time we hit them and count only the first mark.
- Answer = total cells - #guards - #walls - #seen.

Correctness:
- A guard's line of sight passes over empty cells and stops at a wall/guard.
- A cell might be traversed by multiple guards, but we only count it once (state 2).

Complexity:
- Time: O(G * (m + n)) worst-case (each guard can scan up to a full row and column).
  There are tighter O(mn) sweep solutions, but this passes constraints.
- Space: O(mn) for the grid.
"""

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 -> empty, 1 -> wall, 2-> seen, gurad = 3
        grid = [[0 for j in range(n)] for i in range(m)]
        for r,c in guards:
            grid[r][c] = 3
        for r,c in walls:
            grid[r][c] = 1

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        res = 0

        for r,c in guards:
            for dr, dc in directions:
                curr_r,curr_c = r + dr,c + dc
                while curr_r >= 0 and curr_r < m and curr_c >= 0 and curr_c < n:
                    if grid[curr_r][curr_c] == 1 or grid[curr_r][curr_c] == 3:
                        break
                    if grid[curr_r][curr_c] == 2:
                        curr_r += dr
                        curr_c += dc
                    else:
                        grid[curr_r][curr_c] = 2
                        curr_r += dr
                        curr_c += dc
                        res += 1
        
        return m*n - len(guards) - len(walls) - res

                
