"""
DFS solution for LeetCode 1391 - Check if There is a Valid Path in a Grid.

Idea:
Each cell represents a street type (1 to 6), and each street type
allows movement only in specific directions.

A valid path exists if we can start from the top-left cell (0, 0)
and reach the bottom-right cell (M - 1, N - 1) while following
street connection rules.

Key observation:
Moving from one cell to a neighbor is only valid if:
1. The current street allows movement in that direction
2. The neighbor street allows connection back from the opposite side

So movement must be valid in BOTH directions.

Approach:
- Create a dictionary `directions` that maps each street type
  to its allowed movement directions.
- Create a dictionary `valid` that checks whether the neighboring
  street type can properly connect back based on the chosen direction.
- Use DFS starting from (0, 0)
- Track visited cells to avoid infinite loops
- If DFS reaches the bottom-right cell, return True

Why visited is needed:
Without visited, DFS may revisit cells and loop forever since
the grid behaves like an undirected graph.

Time Complexity:
O(M * N)
Each cell is visited at most once.

Space Complexity:
O(M * N)
For the visited set and recursion stack in the worst case.
"""

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        if M == N == 1:
            return True
        directions = {
            1: [(0, -1), (0, 1)],  # Street 1: Horizontal (left, right)
            2: [(1, 0), (-1, 0)],  # Street 2: Vertical (down, up)
            3: [(0, -1), (1, 0)],  # Street 3: Left-Down (left, down)
            4: [(0, 1), (1, 0)],   # Street 4: Right-Down (right, down)
            5: [(0, -1), (-1, 0)], # Street 5: Left-Up (left, up)
            6: [(0, 1), (-1, 0)]   # Street 6: Right-Up (right, up)
        }

        valid = {
            1: [(1, 4, 6), (1, 3, 5)],  # Street 1: Valid connections for right and left
            2: [(2, 5, 6), (2, 3, 4)],  # Street 2: Valid connections for down and up
            3: [(1, 4, 6), (2, 5, 6)],  # Street 3: Valid connections for left and down
            4: [(1, 3, 5), (2, 5, 6)],  # Street 4: Valid connections for right and down
            5: [(1, 4, 6), (2, 3, 4)],  # Street 5: Valid connections for left and up
            6: [(1, 3, 5), (2, 3, 4)]   # Street 6: Valid connections for right and up
        }
        visited = set()
        def dfs(r,c):
            
            visited.add((r,c))
            street = grid[r][c]
            direct = directions[street]

            for i in range(len(direct)):
                new_r, new_c = r + direct[i][0], c + direct[i][1]
                if (new_r,new_c) in visited or new_r < 0 or new_r >= M or new_c < 0 or new_c >= N:
                    continue
                if grid[new_r][new_c] not in valid[street][i]:
                    continue
                if new_r == M-1 and new_c == N - 1:
                    return True
                if dfs(new_r, new_c):
                    return True
            return False
        return dfs(0,0)
         

            
