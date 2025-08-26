  """
  Return the number of combinations of coins that sum to `amount`.

  Idea:
  --------
  We use dynamic programming to count the number of unique *combinations*
  of coins (order does not matter). The key is to process coins one by one
  in the outer loop, which prevents counting the same set of coins in
  different orders.

  Definitions:
  ------------
  - dp[j]: number of ways to make amount j with the current coin and
    possibly previous coins.
  - prevDp[j]: number of ways to make amount j with only the previous
    set of coins (before adding the current one).

  Recurrence:
  -----------
  For each coin c:
      dp[j] = dp[j - c]        # include coin c at least once
           + prevDp[j]         # exclude coin c, rely on previous coins

  Base case:
  ----------
  dp[0] = 1 for every row, since there is exactly one way to make 0
  (use no coins at all).

  Why it avoids duplicates:
  -------------------------
  - Outer loop over coins enforces a *fixed order* of consideration:
    first coin 0, then coin 1, then coin 2, etc.
  - This means combinations like [1,2,2] and [2,1,2] cannot be counted
    separately. Once we finish processing coin 1, we never go back and
    reconsider it after coin 2, so all permutations collapse into a
    single combination.
  - In other words, every combination has a canonical construction path
    (based on the order coins are processed), which guarantees uniqueness.

  Complexity:
  -----------
  - Time:  O(n * amount), where n = number of coins
  - Space: O(amount), since we only keep two rows at a time
  """

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        prevDp = None
 
        for i in range(len(coins)):
            dp = [0] * (amount + 1)
            dp[0] = 1
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]
                if prevDp:
                    dp[j] += prevDp[j]
            prevDp = dp

        return prevDp[amount]
