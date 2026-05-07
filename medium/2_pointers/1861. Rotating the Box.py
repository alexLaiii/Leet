"""
Idea:
Simulate gravity first, then rotate the matrix 90 degrees clockwise.

Step 1 — Simulate gravity inside each row:
Because the final rotation turns "right movement" into "downward gravity",
we first process every row from right to left and let stones '#' slide
toward the right side until blocked by:
    1. an obstacle '*'
    2. another stone '#'

Pointer meaning:
    r = current valid position where a stone can fall.

Process:
- If we see '*':
    reset r to this obstacle position because stones cannot cross it.
- If we see '.':
    update r if needed.
- If we see '#':
    and the target position is empty '.',
    swap the stone into the rightmost available position.

The while-loop after swapping moves r leftward until the next empty
space is found.

Step 2 — Rotate the matrix:
After gravity simulation, rotate the box 90 degrees clockwise.

Rotation mapping:
    res[i][j] = boxGrid[M - 1 - j][i]

This corresponds to:
    original (row, col)
        ->
    rotated (col, M - 1 - row)

Time Complexity:
    O(M * N)

Space Complexity:
    O(M * N)
"""

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        M, N = len(boxGrid), len(boxGrid[0])
        res = [['.' for j in range(M)] for i in range(N)]

        for i in range(M):
            r = N - 1
            for l in range(N - 1, -1, -1):
                if boxGrid[i][l] == '*':
                    r = l
                elif boxGrid[i][l] == '.' and boxGrid[i][r] != '.':
                    r = l
                elif boxGrid[i][l] == '#' and boxGrid[i][r] == '*':
                    r = l
                elif boxGrid[i][l] == '#' and boxGrid[i][r] == '.':
                    boxGrid[i][l], boxGrid[i][r] = boxGrid[i][r], boxGrid[i][l]
                    while r > l and boxGrid[i][r] != '.':
                        r -= 1

        
        for i in range(N):
            for j in range(M):
                res[i][j] = boxGrid[M - 1 - j][i]
        return res
                    
