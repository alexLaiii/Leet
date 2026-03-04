"""
Count the number of special positions in a binary matrix.

A position (i, j) is considered special if:
1. mat[i][j] == 1
2. All other elements in row i are 0
3. All other elements in column j are 0

Approach
--------
1. First pass:
   Count how many 1s appear in each row and each column.
   - row[i] stores the number of 1s in row i
   - col[j] stores the number of 1s in column j

2. Second pass:
   For every cell (i, j), check if:
       mat[i][j] == 1
       row[i] == 1
       col[j] == 1
   If all conditions hold, the position is special.

Time Complexity
---------------
O(m * n)
Two full scans of the matrix.

Space Complexity
----------------
O(m + n)
For the row and column count arrays.

:param mat: Binary matrix of size m x n
:return: Number of special positions
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = [0] * len(mat)
        col = [0] * len(mat[0])
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        print(row, col)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    res += 1
        return res
        
