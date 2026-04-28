"""
Flatten the 2D grid into a 1D array and sort it so the median can be found.

Since each operation only allows adding or subtracting x, all values must
belong to the same modulo class with respect to x. This means the difference
between every value and the target value must be divisible by x; otherwise,
it is impossible to make the grid uni-value, so return -1.

To minimize the total number of operations, the optimal target value is the
median of the sorted array. The median minimizes the sum of absolute
differences, which directly minimizes the number of required operations.

For each number:
1. Compute the absolute difference from the median.
2. Check if the difference is divisible by x.
3. Add diff // x to the total operation count.

Time Complexity:
O(m * n log(m * n)) due to sorting

Space Complexity:
O(m * n) for storing the flattened grid
"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr.append(grid[i][j])
        sort_arr = sorted(arr)
        median = sort_arr[len(sort_arr) // 2]
        minimum_operations = 0
        for n in sort_arr:
            diff = abs(n - median)
            if diff % x != 0:
                return -1
            minimum_operations += diff // x

        return minimum_operations

        
