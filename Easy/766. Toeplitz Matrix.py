"""
Too easy, don't bother explain.
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M - 1):
            for j in range(N - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        
        return True
