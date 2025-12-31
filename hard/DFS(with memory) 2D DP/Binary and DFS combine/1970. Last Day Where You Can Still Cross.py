"""
Return the latest day (0-indexed count of flooded cells) on which it is still possible
to cross from the top row to the bottom row in a `row x col` grid.

Problem setup:
- The grid is initially all land.
- Each day, one cell in `cells` becomes flooded (water) in the given order.
- You can move 4-directionally (up/down/left/right) through land cells.
- Crossing is possible if there exists a path from any cell in the top row (r=1)
  to any cell in the bottom row (r=row).

Key idea (monotonicity + binary search):
- If you can cross on day `d`, then you can also cross on any earlier day `< d`
  (fewer flooded cells).
- If you cannot cross on day `d`, then you cannot cross on any later day `> d`
  (more flooded cells).
- This monotonic property allows binary search for the last day that is still feasible.

Feasibility check for a given `mid` (day):
- Build a `flooded` set containing the first `mid` flooded cells: `cells[:mid]`.
- Run a DFS from each top-row column (r=1, c=1..col) to see if any reaches r=row.
- Use a shared `visited` set across all DFS starts for this `mid` to avoid
  re-exploring the same connected land region multiple times.

DFS details:
- Coordinates are treated as 1-indexed to match `cells` input.
- Base cases:
    * Out of bounds -> False
    * Flooded or already visited -> False
    * Reached bottom row (r == row) -> True
- Otherwise mark visited and recurse in 4 directions.

Complexity:
- Let N = row * col.
- Binary search performs O(log N) checks.
- Each check explores each cell at most once across all DFS calls due to shared `visited`,
  so O(N) time per check in the worst case.
- Total time: O(N log N), space: O(N) for `flooded` + `visited`.
- Note: recursive DFS may hit Python recursion depth on large grids; an iterative
  stack/BFS can be used if recursion errors occur.

Returns:
- `l`, the maximum `mid` such that crossing is still possible when the first `mid`
  cells are flooded.
"""

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def dfs(r,c, visited):
            if r > row or r < 1 or c > col or c < 1 or (r,c) in flooded or (r,c) in visited:
                return False
            if r == row:
                return True
            visited.add((r,c))
            return dfs(r, c + 1, visited) or dfs(r, c - 1, visited) or dfs(r + 1, c, visited) or dfs(r - 1, c, visited)
        l,r  = 0, len(cells)
        while l < r:
            flooded = set()
            mid = (l + r + 1) // 2

            for rr,cc in cells[:mid]:
                flooded.add((rr,cc))
            havePath = False
            visited = set()
            for i in range(1, col + 1):
                if dfs(1, i, visited):
                    havePath = True
                    break
            if havePath:
                l = mid
            else:
                r = mid - 1
        
        return l
                    
