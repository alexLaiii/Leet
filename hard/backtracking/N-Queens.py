"""
Solves the N-Queens problem: place N queens on an N×N board such that no two queens can attack each other.
Queens can attack vertically, horizontally, and diagonally.

### Concept:
We use backtracking to explore all possible queen placements row by row. Since only one queen can be placed per row, 
we fix the row and try placing a queen in each column. For each position (r, c), we check if it's valid:
    - No other queen in the same column → `col not in cols`
    - No other queen on the same '/' diagonal → `(r + c) not in posDiag`
    - No other queen on the same '\' diagonal → `(r - c) not in negDiag`

If a position is valid:
    - Place the queen at (r, c)
    - Mark the column and diagonals as attacked
    - Recurse to the next row
    - After recursion, backtrack: remove the queen and unmark its attack zones

If `r == n`, that means N queens are successfully placed → we build and store the current board configuration.

### Data Structures:
- `cols`: set of columns already occupied by queens
- `posDiag`: set of '/' diagonals (row + col) under attack
- `negDiag`: set of '\' diagonals (row - col) under attack
- `queens`: list of tuples storing (row, col) positions of current queens
- `res`: list of valid board configurations (each as List[str])

### Functions:
- `buildBoard(queens_pos)`: builds a visual board from queen positions and appends it to the result

### Flow:
1. Call `backtrack(0)` to start placing from row 0
2. In each row, try placing a queen in every column
3. Skip invalid columns based on `cols`, `posDiag`, and `negDiag`
4. If row == n: build board and store the solution
5. Use backtracking to explore all valid configurations

### Time Complexity:
O(N!) in the worst case — backtracking prunes many invalid paths early.

Returns:
List of all valid board configurations where N queens are placed without conflict.
"""



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiag, negaDiag = set(), set(), set()
        queens, res = [], []
        
        def buildBoard(queens_pos):
            board = [["."] * n for i in range(n)]
            for r,c in queens_pos:
                board[r][c] = "Q"
            res.append(["".join(row) for row in board])
            
                
        def backtrack(r):
            if r == n:
                return
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negaDiag:
                    continue
                queens.append((r,c))
                if len(queens) == n:
                    buildBoard(queens)
                cols.add(c)
                posDiag.add(r+c)
                negaDiag.add(r-c)

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negaDiag.remove(r-c)
                queens.pop()

        backtrack(0)
        return res
