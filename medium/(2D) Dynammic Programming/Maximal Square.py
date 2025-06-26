"""
Remember that each cell stores the maximal square length that it can make when including that cell,  and that cell has to be the bottom-right corner of the square.

Idea:  
Each cell stores the maximum square it can generate by including that cell when adding that cell to the grid.  
For example:  
[["1","0","1","0","0"],  
 ["1","0","1","1","1"],  
 ["1","1","1","1","1"],  
 ["1","0","0","1","0"]]

And the 2D Grid will be:  
[[0, 0, 0, 0, 0, 0],  
 [0, 1, 0, 1, 0, 0],  
 [0, 1, 0, 1, 1, 1],  
 [0, 1, 1, 1, 2, 2],  ← (2 here because when you look left, top, top-left, you will see a 2x2 square in the matrix. We are storing the largest square length that can be made with the current cell as the bottom-right corner.)  
 [0, 1, 0, 0, 1, 0]]

Notice that an extra row and extra column has been created in the grid (to handle out-of-bounds).

Implementation:  
Create a 2D DP grid with 1 extra row and column to deal with out-of-bounds. Since this row and column don’t exist in the original matrix, each cell is initialized to 0.

When filling out the grid, we are basically asking:  
"What is the maximum square that my left, top, and top-left neighbor can form so that I can extend that square using this cell?"

Case 1:  
If the current cell is "0" → This cell cannot be part of any square. We skip it.

Case 2:  
Assume this is our current grid, and we are filling out the last cell. If that position in the original matrix is "1":

[1, 1, 1, 0],  
[1, 2, 2, 1],  
[1, 2, 3, ?]

The maximum square that can be formed with the current cell is:  
min(left, top, top-left) + 1  
In code: `dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1`

Why min()?  
Because to expand the current square by 1, all three directions (left, top, top-left) must support at least that much size. If any one of them has less, we can only extend to that smaller size.

Example:  
[1, 1, 1],  
[1, 2, ?] → The answer for `?` is 2. You cannot extend the left square because the top and top-left is 1, so the max square ends up being only 2.
                                    (we can only extend the size-2 square when top and top-left support it, and vice versa)

If any one of the neighbors has a smaller square size, that limits the current square.

matrix =  
[1, 1, 1],  
[1, 0, 1]  
→ grid =  
[1, 1, 1],  
[1, 0, ?] → The answer for `?` is 1. You cannot extend the top-left or top square because the left is 0, so the max square ends up being only 1.

Finally, the largest value in the DP grid is the side length of the largest square → we return `side_length ** 2` as area.

Time Complexity: O(m * n)  
Space Complexity (2D): O(m * n)  
Space Complexity (1D): O(n) — by keeping only the last row
"""


# 2D solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M,N = len(matrix), len(matrix[0])
        dp = [[0 for j in range(N + 1)] for j in range(M+1)]
        max_area = 0
        for i in range(1, M + 1):
            for j in range(1, N+1):
                if matrix[i-1][j-1] == "0":
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                max_area = max(max_area, dp[i][j])

        return max_area ** 2

# 1D solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M,N = len(matrix), len(matrix[0])
        dp = [0 for i in range(N + 1)]
        max_side = 0
        for i in range(1, M + 1):
            new_row = [0 for i in range(N+1)]
            for j in range(1, N + 1):
                if matrix[i-1][j-1] == "0":
                    continue
                new_row[j] = min(dp[j], dp[j-1], new_row[j-1]) + 1
                max_side = max(max_side, new_row[j])
            dp = new_row
        
        return max_side ** 2

        
