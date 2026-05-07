"""
rolling DP space optimize version

Idea:
Optimize the full 3D DP solution by noticing that each row only
depends on:
    1. the previous row
    2. the current row being built

Instead of storing the entire:

    dp[M][N][k]

table, keep only:
    prev_row
    next_row

State Definition:
    prev_row[j][c]

represents the maximum score reaching column j in the previous row
using exactly c non-zero cells.

Transition:
For each cell:
    top  = prev_row[j][kp]
    left = next_row[j-1][kp]

Then transition into:

    next_row[j][kp + cost]

where:

    cost = 0 if grid[i][j] == 0 else 1

Transition formula:

    next_row[j][kp + cost] =
        max(top, left) + grid[i][j]

Special Handling:
- First row only comes from the left.
- First column only comes from the top.

Rolling DP Observation:
Since row i only depends on row i-1, older rows are unnecessary.

After finishing a row:

    prev_row = next_row

This is a classic rolling-array DP optimization.

Final Answer:
Return:

    max(prev_row[N - 1])

because the final cell may be reached using any valid cost
from 0 to k.

Time Complexity:
    O(M * N * k)

Space Complexity:
    O(N * k)
"""

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        prev_row = [[-1 for _ in range(k + 1)] for j in range(N)]
        if grid[0][0] == 0:
            prev_row[0][0] = 0
        else:
            prev_row[0][1] = grid[0][0]
        
        for j in range(1, N):
            cost = 0 if grid[0][j] == 0 else 1
            for kp in range(k + 1):
                if prev_row[j-1][kp] != -1 and kp + cost < k + 1:
                    prev_row[j][kp + cost] = prev_row[j - 1][kp] + grid[0][j]
        
        for i in range(1, M):
            next_row = [[-1 for _ in range(k + 1)] for j in range(N)]
            for j in range(N):
                cost = 0 if grid[i][j] == 0 else 1
                if j == 0:
                    for kp in range(k + 1):
                        top = prev_row[0][kp]
                        if kp + cost < k + 1:
                            if top != -1:
                                next_row[0][kp + cost] = top + grid[i][0]
                else:
                    for kp in range(k + 1):
                        top = prev_row[j][kp]
                        left = next_row[j-1][kp]
                        if kp + cost < k + 1:
                            if top != -1 and left != -1:
                                next_row[j][kp + cost] = max(top,left) + grid[i][j]
                            elif top != -1:
                                next_row[j][kp + cost] = top + grid[i][j]
                            elif left !=  -1:
                                next_row[j][kp + cost] = left + grid[i][j]
            prev_row = next_row
             
      
        return max(prev_row[N - 1])       


"""
Full DP Version

Idea:
Use 3D dynamic programming where:

    dp[i][j][c]

represents the maximum path score obtainable when reaching cell
(i, j) using exactly c non-zero cells along the path.

A non-zero cell contributes:
    cost = 1
while:
    cost = 0
for a zero cell.

Transition:
Each cell can only be reached from:
    1. top  -> (i-1, j)
    2. left -> (i, j-1)

If the current cell has:
    cost = 0 or 1

then:
    previous cost usage = kp
maps to:
    new cost usage = kp + cost

Transition formula:

    dp[i][j][kp + cost] =
        max(
            dp[i-1][j][kp],
            dp[i][j-1][kp]
        ) + grid[i][j]

Important Observation:
There is no need to compare against the existing
dp[i][j][kp + cost] during the transition because:

    kp -> kp + cost

is a one-to-one mapping for a fixed cost value at the current cell.

Initialization:
Handle first row and first column separately since they only have
one possible incoming direction.

Final Answer:
The destination cell may be reached with different valid costs
from 0 to k, so return:

    max(dp[M-1][N-1])

Time Complexity:
    O(M * N * k)

Space Complexity:
    O(M * N * k)
"""
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[[-1 for _ in range(k + 1)] for j in range(N)] for i in range(M)]
        if grid[0][0] == 0:
            dp[0][0][0] = 0
        else:
            dp[0][0][1] = grid[0][0]
        for i in range(1, M):
            cost = 0 if grid[i][0] == 0 else 1
            for kp in range(k + 1):
                if dp[i - 1][0][kp] != -1 and kp + cost < k + 1:
                    dp[i][0][kp + cost] = dp[i - 1][0][kp] + grid[i][0]
        
        for j in range(1, N):
            cost = 0 if grid[0][j] == 0 else 1 
            for kp in range(k + 1):
                if dp[0][j - 1][kp] != -1 and kp + cost < k + 1:
                    dp[0][j][kp + cost] = dp[0][j-1][kp] + grid[0][j]

        for i in range(1, M):
            for j in range(1, N):
                cost = 0 if grid[i][j] == 0 else 1 
                for kp in range(k + 1):
                    top = dp[i-1][j][kp]
                    left = dp[i][j-1][kp]
                    if kp + cost < k + 1:
                        if top != -1 and left != -1:
                            # no need to include dp[i][j][kp + cost] in the maximum check since the "cost" is a fixed value for dp[i][j]
                            # so each mapping value "kp" between dp[i-1][j][kp] to dp[i][j][kp + cost] and dp[i][j-1][kp] to dp[i][j-1][kp + cost] is one to one
                            dp[i][j][kp + cost] = max(top, left) + grid[i][j]
                        elif top != -1:
                            dp[i][j][kp + cost] = top + grid[i][j]
                        elif left != -1:
                            dp[i][j][kp + cost] = left + grid[i][j]
                    
        for i in range(M):
            print(dp[i])
        return max(dp[M-1][N-1])
        
