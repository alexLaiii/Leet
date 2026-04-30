"""
Key idea:
For each row, we only need to check whether the row remains unchanged
after a cyclic shift of k positions.

Although the problem describes odd/even rows shifting in opposite directions,
this distinction does not matter for checking similarity. A row that stays
the same after a right cyclic shift by k also stays the same after a left
cyclic shift by k, because both conditions mean the row is periodic with
period k mod N.

So for every cell mat[i][j], compare it with the element k positions away
in the same row:
    mat[i][j] == mat[i][(j + k) % N]

If all rows satisfy this, the matrix is similar after the cyclic shifts.
"""
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        M, N = len(mat), len(mat[0])
        for i in range(M):
            for j in range(N):
                if mat[i][j] != mat[i][(j + (k % N)) % N]:
                    return False
        
        return True
        
