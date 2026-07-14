"""
Computes the degree of each vertex in an undirected graph represented
by an adjacency matrix.

The algorithm iterates through each row of the matrix and sums its
entries. Since each row indicates which vertices are adjacent to the
corresponding vertex, the row sum equals that vertex's degree.

Time Complexity: O(n²), where n is the number of vertices, as every
entry in the adjacency matrix is visited once.

Space Complexity: O(n) for the output list storing the degree of each
vertex. Auxiliary space is O(1).
"""
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        M, N = len(matrix), len(matrix[0])
        res = []
        for i in range(M):
            i_degree = 0
            for j in range(N):
                i_degree += matrix[i][j]
            res.append(i_degree)
        return res        
