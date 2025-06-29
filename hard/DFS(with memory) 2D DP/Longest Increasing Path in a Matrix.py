"""
Brute force is too inefficient to pass LeetCode large test cases, so we need to cache the previously computed values in this problem.

Idea:
The main idea here is to store the longest path that can start from each cell. Since loops are impossible in this problem 
(it must always be an increasing path), the longest increasing path (LIP) will be a combination of subpaths, and we want 
to find the maximum path that can be built by chaining them.

Example:
Input matrix:
[9, 9, 4]
[6, 6, 8]
[2, 1, 1]

Corresponding longest increasing path starting from each cell:
[1, 1, 2]
[2, 2, 1]
[3, 4, 2]

Notice that [1, 2, 6, 9] is the LIP in this case, so the answer is 4.

Consider the value `1` at position (2,1):
To determine that this has a LIP of 4:
- It can move to two neighbors: 2 (left) and 6 (up).
- We check both subpaths. The LIP from cell 2 is 3, and from cell 6 is 2.
- So for cell (2,1), the LIP = max(3, 2) + 1 = 4.

So the key idea is:
When we compute the LIP from any cell, it equals: 1 + max(LIP from its increasing neighbors).
This avoids recomputation if we cache each result.

Why DFS + memo works:
Since every increasing path is acyclic, any DFS call from a cell will **only call subcells once**, 
and their results will be stored in a dictionary `memo`. Once a cell’s LIP is computed, future DFS calls
that land on it return immediately in O(1).

Implementation notes:
Instead of using a 2D DP grid, I use a dictionary `memo` with key = (row, col), value = longest path length from that cell.

The `dfs(r, c, prevVal)` function:
- Computes the LIP from position (r, c), given previous value `prevVal`.
- If it's out of bounds or not strictly increasing, return 0.
- If already computed (in `memo`), return memo value.
- Else, explore 4 directions and store the result: 1 + max of neighbor DFS results.

Then we loop through all (i, j) in the matrix, and call `dfs(i, j, -1)` from each cell.
Since each cell’s value is cached after first visit, it’s very efficient.

Time Complexity: O(m * n)
- Each cell is visited once and stored.

Space Complexity: O(m * n)
- Memoization + call stack for DFS.

"""



class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        # The memo will store the Longest Increasing Path in the key=(r,c) cell indicate that the path start at that position
        # This approach cache the result of the previous work, so we can reuse it to avoid repeated work
        memo = {}
        def dfs(r,c, prevNum):
            if r < 0 or c < 0 or r >= M or c >= N or matrix[r][c] <= prevNum:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = 1 + max(dfs(r+1, c, matrix[r][c]), dfs(r-1, c, matrix[r][c]), dfs(r, c+1, matrix[r][c]), dfs(r,c-1, matrix[r][c]))
            return memo[(r,c)]

        result = 0
        for i in range(M):
            for j in range(N):
                result = max(result, dfs(i,j,-1))
   
        return result

                    

            
