"""
Search for target in an M x N matrix where each row is sorted left to
right and the first element of each row is greater than the last
element of the previous row.

Treats the matrix as a flattened, sorted 1D array of length M*N and
binary searches over the flat index space, mapping each mid index
back to (row, col) via divmod by N.

Args:
    matrix: 2D list of integers, sorted as described above.
    target: Integer value to search for.

Returns:
    True if target is found in matrix, False otherwise.

Time complexity: O(log(M*N))
Space complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        M, N = len(matrix), len(matrix[0])
        l, r = 0, (M * N) - 1 
        while l <= r:
            mid = (l + r) // 2 
            row  = mid // N    
            col = mid % N      
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
