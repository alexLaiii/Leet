"""
Use prefix sums to check every possible square efficiently.

Build four prefix structures:
1. Row prefix sums for O(1) row-sum queries.
2. Column prefix sums for O(1) column-sum queries.
3. Main diagonal prefix sums for O(1) top-left to bottom-right diagonal queries.
4. Anti-diagonal prefix sums for O(1) top-right to bottom-left diagonal queries.

For each possible top-left corner and square size:
- Check that all row sums are equal.
- Check that all column sums are equal.
- Check that both diagonal sums equal the same value.
- If all match, update the maximum magic square size.

The important indexing detail is that the loops use 1-based prefix indices,
so grid cell (r, c) corresponds to prefix position (r + 1, c + 1).
"""

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        max_possible = min(M, N)
        if M == N == 1:
            return 1
        
        PrefixSumRow = [[0 for j in range(N + 1)] for i in range(M + 1)]
        PrefixSumCol = [[0 for j in range(N + 1)] for i in range(M + 1)]
        PrefixToptoBottom = [[0 for j in range(N + 1)] for i in range(M + 1)]
        PrefixBottomtoTop = [[0 for j in range(N + 2)] for i in range(M + 1)]
        
        for i in range(M ):
            rowSum = 0
            for j in range(N):
                rowSum += grid[i][j]
                PrefixSumRow[i + 1][j + 1] = rowSum
        for j in range(N):
            colSum = 0
            for i in range(M):
                colSum += grid[i][j]
                PrefixSumCol[i + 1][j + 1] = colSum
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and j - 1 >= 0:
                    PrefixToptoBottom[i + 1][j + 1] = grid[i][j] + PrefixToptoBottom[i][j]
                else:
                    PrefixToptoBottom[i + 1][j + 1] = grid[i][j]
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and j + 1 < N:
                    PrefixBottomtoTop[i + 1][j + 1] = grid[i][j] + PrefixBottomtoTop[i][j + 2]
                else:
                    PrefixBottomtoTop[i + 1][j + 1] = grid[i][j]

        max_size = 1

        # i,j here is the correct index for the prefixSum
        for i in range(1,M):
            for j in range(1,N):
                size = min(M - i + 1, N - j + 1)
                for k in range(size):
                    not_magic = False
                    # row
                    rowSum = PrefixSumRow[i][j + k] - PrefixSumRow[i][j - 1]
                    for ith in range(k + 1):
                        val = PrefixSumRow[i + ith][j + k] - PrefixSumRow[i + ith][j - 1]
                        if rowSum != val:
                            not_magic = True
                            break
                    if not_magic:
                        continue
              
                    # col
                    colSum = PrefixSumCol[i + k][j] - PrefixSumCol[i - 1][j]
                    for jth in range(k + 1):
                        val = PrefixSumCol[i + k][j + jth] - PrefixSumCol[i - 1][j + jth]
                        if colSum != val:
                            not_magic = True
                            break
                    if not_magic:
                        continue
           
                    # diaginal top to bottom
                    topBotSum =  PrefixToptoBottom[i + k][j + k] - PrefixToptoBottom[i - 1][j - 1]
                    # diagonal bot to top
                    botTopSum = PrefixBottomtoTop[i + k][j] - PrefixBottomtoTop[i - 1][j + k + 1]
                    if rowSum == colSum == topBotSum == botTopSum:
                        max_size = max(max_size, k + 1)
                        if max_size == max_possible:
                            return max_size
                        

                    
        return max_size

        
