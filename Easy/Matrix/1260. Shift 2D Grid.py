"""
Flatten the 2D grid into a 1D array, rotate it to the right by k positions,
and then reconstruct the original grid dimensions.

Since shifting the grid M*N times returns it to its original state, reduce
k using modulo (M * N) to avoid unnecessary work.

Time Complexity:
    O(M * N)

Space Complexity:
    O(M * N)
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        k = k % (M * N)
        flatten_arr = []
        for i in range(M):
            flatten_arr += grid[i]
        flatten_arr = flatten_arr[M * N - k:] + flatten_arr[:M * N - k]
        l = 0
        for i in range(M):
            for j in range(N):
                grid[i][j] = flatten_arr[l]
                l += 1
        return grid
                
        
        
