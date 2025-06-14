"""
Note: This problem is Exactly Same as N-Queens
*** IF forget how to do this, visit N-Queens for a more detailed explnation. ***

Counts the total number of valid solutions to the N-Queens problem.

### Problem:
Place N queens on an N×N board such that no two queens can attack each other.
Queens can attack vertically, horizontally, and diagonally.

### Idea:
We use backtracking to place queens row by row. For each row `r`, we try every column `c` and check if the position
(r, c) is safe:
    - Not in the same column → `c not in cols`
    - Not in the same '/' diagonal → `(r + c) not in posDiag`
    - Not in the same '\' diagonal → `(r - c) not in negaDiag`

If the position is valid:
    - Simulate placing the queen by updating the sets
    - Recurse to the next row (`r + 1`)
    - Backtrack by removing the queen’s effects from the tracking sets

We increment the solution counter only when `r == n`, which means N queens have been placed successfully.

### Tracking Sets:
- `cols`: columns that already have queens
- `posDiag`: '/' diagonals under attack (`row + col`)
- `negaDiag`: '\' diagonals under attack (`row - col`)

### Time Complexity:
O(N!) in worst case due to backtracking, but pruning significantly reduces the search space.

### Returns:
An integer: the total number of valid N-Queens configurations.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, posDiag, negaDiag = set(), set(), set()
        self.res = 0
                   
        def backtrack(r):
            if r == n:
                return
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negaDiag:
                    continue
                # hit here means N queens is placed, since we can only get to r == n - 1 iff n - 1 queens is already placed on the board
                # Therefore, place one more queens now will have N queens on board
                if r == n - 1:
                    self.res += 1
                # simulate queens is on the board by adding new constraint because of that queens
                cols.add(c)
                posDiag.add(r+c)
                negaDiag.add(r-c)

                backtrack(r+1)
                # simulate removing that queens remove its constraints that cause by that queens
                cols.remove(c)
                posDiag.remove(r+c)
                negaDiag.remove(r-c)

        backtrack(0)
        return self.res
