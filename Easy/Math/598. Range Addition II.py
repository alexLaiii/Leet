"""
Return the number of cells with the maximum value after all operations.

Each operation [r, c] increments every cell in the rectangle from
(0, 0) to (r - 1, c - 1).

The cells with the maximum value are the cells included in every
operation. Therefore, we only need to find the overlapping rectangle
of all operations.

The overlap has:
    minimum row limit = min r from all ops
    minimum col limit = min c from all ops

So the number of maximum cells is:

    min_row * min_col

If ops is empty, no cells are incremented, so every cell has the same
value 0. In that case, the answer is m * n.

Time Complexity: O(len(ops))
Space Complexity: O(1)
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_col = m, n
        for r,c in ops:
            min_row = min(min_row, r)
            min_col = min(min_col, c)

        return min_row * min_col
