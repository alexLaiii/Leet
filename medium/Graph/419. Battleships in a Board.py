"""
DFS erase-and-count approach.

Scan the board; when an 'X' is found, launch DFS that turns the
contiguous ship to '.' by exploring only DOWN and RIGHT. This works
because ships are straight and we encounter each ship at its top-left
segment in row-major order. Each DFS corresponds to exactly one ship.

Note: violates the typical problem constraint of not modifying the
board and O(1) space (uses recursion stack).

Time:  O(MN)
Space: O(L) recursion depth (L = ship length)
"""


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M, N = len(board), len(board[0])

        def dfs(r,c):
            if r >= M or c >= N or r < 0 or c < 0 or board[r][c] == ".":
                return 
            board[r][c] = "."
            dfs(r + 1, c)
            dfs(r, c + 1)
        ships = 0
        for i in range(M):
            for j in range(N):
                if board[i][j] == "X":
                    dfs(i,j)
                    ships += 1

        return ships
"""
Optimal head count only solution

Count battleships in O(MN) time and O(1) space without modifying the board.

Idea: Only count the 'head' of each ship—an 'X' whose top and left
neighbors are not 'X'. Because ships are straight (horizontal or vertical)
and non-adjacent diagonally, each ship has exactly one such head.

Returns:
    int: number of ships.
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M, N = len(board), len(board[0])
        ships = 0
        for r in range(M):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                if (r > 0 and board[r-1][c] == "X") or (c > 0 and board[r][c-1] == "X"):
                    continue
                ships += 1
        return ships
                
