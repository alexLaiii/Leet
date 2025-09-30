"""
Spiral Matrix (DFS + turn-right simulation)

Core idea:
- Walk the matrix as if you were a robot: keep moving in the current direction; when
  blocked (out of bounds or revisiting a cell), rotate direction 90° clockwise and try again.
- Use DFS to *continue the path* from each cell until the entire spiral is traced.
- A `visited` set guarantees each cell is appended exactly once.

How it works:
- `hash_map` encodes the clockwise rotation: (0,1)→(1,0)→(0,-1)→(-1,0)→(0,1).
- `dfs(r, c, prevDir)`:
    1) If (r,c) is invalid or already seen → return False (can't proceed).
    2) Otherwise record matrix[r][c], mark visited, and try to continue in `prevDir`.
    3) If continuing fails, rotate right and try up to 3 more directions.
    4) If *none* of the 4 directions works from this cell, return True to signal
       “we finished the entire spiral path” and stop further rotation up the stack.
       (This True result short-circuits the `while ... and not dfs(...)` in callers.)

Why returning True at the end makes sense:
- The only time a valid cell sees all 4 neighbors fail is when there is no unvisited
  neighbor left anywhere along the spiral path — i.e., traversal is complete.
- Bubbling up True prevents callers from exploring other directions, ending the run cleanly.

Complexity:
- Time: O(M·N) — each cell is visited once.
- Space: O(M·N) for `visited` (+ recursion stack up to path length).

Caveats:
- Python recursion depth: for large matrices, recursion may hit the default limit (~1000).
  Use an iterative version (boundary pointers or iterative direction cycling) if needed.
- Add an empty-matrix guard (`if not matrix or not matrix[0]: return []`) in production.

Alternative (canonical) approach:
- Maintain four bounds (top, bottom, left, right) and peel the matrix layer by layer.
  It’s iterative, O(M·N), and avoids recursion and a visited set.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        M, N = len(matrix), len(matrix[0])
        hash_map = {
            (0, 1) : (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0), 
            (-1, 0):(0 , 1)
        }
        visited = set()
        res = []
        def dfs(r,c, prevDir):
            if r >= M or c >= N or r < 0 or c < 0 or (r,c) in visited:
                return False
            res.append(matrix[r][c])
            visited.add((r,c))
            i = 0
            newDir = prevDir
            while i < 4 and not dfs(r + newDir[0], c + newDir[1], newDir):
                newDir = hash_map[newDir]
                i += 1
            return True


        
        dfs(0,0, (0, 1))
        return res
