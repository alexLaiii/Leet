"""
Modify the matrix in-place so that any row or column containing a zero
is set entirely to zero.

Strategy (two-pass with sets):
1) First pass: scan the matrix to collect the indices of rows and columns
   that contain at least one zero. We store them in two sets `row` and `col`.
   Importantly, we do NOT write zeros yet—this prevents zeros introduced
   during processing from cascading to other rows/columns.
2) Second pass: zero out all flagged rows.
3) Third pass: zero out all flagged columns.

Correctness:
- Because we only act on rows/columns discovered in the first pass, newly
  written zeros in step (2) or (3) do not cause additional propagation.

Args:
    matrix: M x N list of lists of integers. Modified in-place.

Time Complexity:
    O(M*N + |row|*N + |col|*M), which is O(M*N) in the worst case.

Space Complexity:
    O(M + N) for the `row` and `col` sets.

Edge Cases:
    - Single row or single column matrices.
    - All zeros or no zeros.
    - Multiple zeros in the same row/column (handled naturally by sets).
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
    
        for r in row:
            for i in range(N):
                matrix[r][i] = 0
        
        for c in col:
            for j in range(M):
                matrix[j][c] = 0
                
        
        
