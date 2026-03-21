"""
Vertically flips the k x k submatrix of grid whose top-left corner is at (x, y).

A vertical flip means reversing the order of the rows inside the selected square
while keeping the values within each row in the same left-to-right order.

Parameters:
    grid (List[List[int]]): The 2D matrix.
    x (int): Row index of the top-left corner of the square submatrix.
    y (int): Column index of the top-left corner of the square submatrix.
    k (int): Side length of the square submatrix.

Returns:
    List[List[int]]: The modified grid after flipping the selected square vertically.

Approach:
    Use two pointers:
    - topRow starts at the top of the square
    - bottomRow starts at the bottom of the square

    Swap the corresponding elements of these two rows only within the
    submatrix columns [y, y + k - 1], then move both pointers inward
    until all needed row pairs are swapped.

Time Complexity:
    O(k^2)

Space Complexity:
    O(1)
"""

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        topRow, bottomRow = x, x + (k - 1)
        while topRow < bottomRow:
            for i in range(y, y+k):
                grid[topRow][i], grid[bottomRow][i] = grid[bottomRow][i], grid[topRow][i]
            topRow += 1
            bottomRow -= 1
        
        return grid
        
