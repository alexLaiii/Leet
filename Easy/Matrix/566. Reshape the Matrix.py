"""
Reshape mat (M x N) into an r x c matrix, preserving row-major order.

Args:
    mat: Source matrix of size M x N.
    r: Desired number of rows.
    c: Desired number of columns.

Returns:
    The reshaped r x c matrix, or the original mat unchanged if
    r * c != M * N (reshape not possible).

Time: O(M * N) - each element visited once.
Space: O(r * c) - for the output matrix.
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if r * c != M * N:
            return mat
        res = [[None for i in range(c)] for j in range(r)]
        k = 0
        for i in range(M):
            for j in range(N):
                res[k // c][k % c] = mat[i][j]
                k += 1
        return res
                
        
