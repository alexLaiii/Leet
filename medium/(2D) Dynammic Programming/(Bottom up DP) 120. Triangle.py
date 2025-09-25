  """
  LeetCode 120 – Triangle (Bottom-up 1D DP with sentinel)

  Core idea:
  Compute the min path sum from bottom to top using a rolling 1D DP array.
  Let dp[j] and dp[j+1] represent the best costs from the two children of
  triangle[i][j] on the row below. Then:
      best(i, j) = triangle[i][j] + min(dp[j], dp[j+1])

  Implementation details:
  - Initialize dp with length n+1 filled with 0 (sentinel on the right).
    This avoids bounds checks at the last column because dp[j+1] always exists.
  - For each row i from bottom to top, build nextDp of length len(dp)-1 where:
        nextDp[j] = triangle[i][j] + min(dp[j], dp[j+1]).
    Then set dp = nextDp. After processing all rows, dp has length 1 and dp[0]
    is the global minimum path sum.

  Complexity:
  - Time: O(n^2) over ~n(n+1)/2 entries of the triangle.
  - Space: O(n) auxiliary (the rolling dp array), shrinking each row.

  Pitfalls:
  - Iterate rows from bottom → top; within each row compute from left → right
    into a fresh nextDp to avoid overwriting needed values.
  """

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        for i in range(len(triangle) - 1, -1, -1):
            nextDp = []
            for j in range(len(dp) - 1):
                nextDp.append(min(triangle[i][j] + dp[j], triangle[i][j] + dp[j + 1]))
            dp = nextDp

        return dp[0]
            
        
