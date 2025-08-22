  """
  IMPORTANT:
  This problem is bascially coin change but you have to compute your own "COINS", If failed to solve it, think of coin change
  
  Return the minimum number of perfect squares whose sum is n.  (LeetCode 279)

  Core idea (DP = unbounded coin change):
    Treat every perfect square ≤ n as a “coin” you can use unlimited times.
    Let dp[i] be the fewest squares needed to sum to i. Then the optimal way
    to make i is to choose one square `sq` (as the last pick) and add 1 to
    the optimal solution for the remainder i - sq:
        dp[i] = 1 + min(dp[i - sq]) over all squares sq ≤ i

  What this code does:
    1) Precompute all perfect squares up to n into sqr_list.
    2) Initialize dp[0..n] with a large sentinel (n+1), and set dp[0] = 0
       (zero squares to make sum 0).
    3) For each target sum i from 1..n, try subtracting every square sq in
       sqr_list that does not exceed i, and keep the best (minimum) count.

  Why it works:
    - Optimal substructure: the best way to build i uses a last square sq,
      plus the best way to build i - sq. Because squares can be reused,
      this is the unbounded variant of coin change.
    - Bottom-up order (i increasing) guarantees dp[i - sq] is already
      computed when we compute dp[i].

  Complexity:
    - Time: O(n * √n)  (about √n squares, n states)
    - Space: O(n)      (the dp array)

  Notes:
    - A tiny speedup is to break the inner loop once sq > i, or iterate
      squares outside and i inside (classic unbounded knapsack order).
  """


class Solution:
    def numSquares(self, n: int) -> int:
        sqr_list = []
        i = 1
        while i * i <= n:
            sqr_list.append(i * i)
            i += 1
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for sqr in sqr_list:
                if i - sqr >= 0:
                    dp[i] = min(dp[i], dp[i - sqr] + 1)
        
        return dp[-1]
        
        
