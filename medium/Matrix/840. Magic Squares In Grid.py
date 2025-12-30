  """
  Count how many 3x3 "magic squares" appear as contiguous subgrids.

  A valid 3x3 magic square here must:
    1) Contain each digit 1..9 exactly once (equivalently: all values are in [1, 9] and distinct).
    2) Have all 3 row sums, all 3 column sums, and both diagonal sums equal to the same value.

  Approach (sliding 3x3 window):
    - Slide a 3x3 window with top-left corner (i, j) over all possible positions.
    - First pass: validate digits and uniqueness using a `seen` set.
        * If any cell is <= 0, > 9, or repeated, mark `notMagic` and skip this window early.
    - Second pass: compute `curr_sum` as the first row sum of this 3x3 window.
    - Verify:
        * Each of the 3 rows sums to `curr_sum`
        * Each of the 3 columns sums to `curr_sum`
        * Both diagonals sum to `curr_sum`
    - If all checks pass, increment result.

  Notes:
    - `offSetM` and `offSetN` represent how many top-left positions exist for a 3x3 window.
    - `loop_time` counts windows visited; it's not needed for correctness.

  Time Complexity:
    O(M*N) windows overall (specifically (M-2)*(N-2)), with O(1) work per window
    (constant checks over 9 cells + constant number of sums).

  Space Complexity:
    O(1) extra space per window (the `seen` set holds at most 9 numbers).
  """

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        offSetM = (len(grid) - 3) + 1
        offSetN = (len(grid[0]) - 3) + 1
        res = 0
        loop_time = 0
        for i in range(offSetM):
            for j in range(offSetN):
                loop_time += 1
                seen = set()
                notMagic = False
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if grid[x][y] <= 0 or grid[x][y] > 9 or grid[x][y] in seen :
                            notMagic = True
                            break
                        seen.add(grid[x][y])
                if notMagic:
                    continue
                target_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                for r in range(i, i + 3):
                    if target_sum != grid[r][j] + grid[r][j + 1] + grid[r][j + 2]:
                        notMagic = True
                        break
                for c in range(j, j + 3):
                    if target_sum != grid[i][c] + grid[i + 1][c] + grid[i + 2][c]:
                        notMagic = True
                        break
                if target_sum != grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]:
                    notMagic = True
                if target_sum != grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]:
                    notMagic = True
                if not notMagic:
                    res += 1

        return res


        
