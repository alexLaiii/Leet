  """
  Fill an n×n matrix in spiral order using DFS that keeps moving straight
  and rotates right when blocked.

  Strategy:
    - Write current value, then try to continue in the same direction.
    - If the next cell is out of bounds or already filled, rotate clockwise
      (right → down → left → up) and try again, up to four times.

  Correctness:
    Each cell is written exactly once; rotation guarantees we always find the
    next valid step until all n^2 cells are filled.

  Complexity:
    Time O(n^2) — each cell written once.
    Space O(n^2) for the result; O(1) extra auxiliary space.
  """

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]

   
        hash_map = {
            (0, 1) : (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0), 
            (-1, 0):(0 , 1)
        }
        def dfs(r,c, prevDir, val):
            if r >= n or c >= n or r < 0 or c < 0 or res[r][c] != 0:
                return 
            res[r][c] = val
            i = 0
            newDir = prevDir
            while i < 4 and not dfs(r + newDir[0], c + newDir[1], newDir, val + 1):
                newDir = hash_map[newDir]
                i += 1
          


        
        dfs(0,0, (0, 1), 1)
        return res
