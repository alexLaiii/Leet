"""
Determine the winner of Stone Game III under optimal play.

  Two players alternate turns, each taking 1, 2, or 3 stones from the
  front of the row. Since stones are only ever removed from the front,
  every reachable position is a suffix of the original row, so a single
  index `i` (meaning "stones i..N-1 remain") fully describes the state.
  No turn dimension is needed: both players face identical rules from
  `i`, so the position is symmetric with respect to whose turn it is.

  State:
      dp[i] = the best achievable score difference (mover minus opponent)
              for whoever is about to move on the suffix starting at i.

  Recurrence:
      dp[i] = max over k in {1, 2, 3} of (sum(stoneValue[i:i+k]) - dp[i+k])

      The subtraction performs the turn flip. dp[i+k] is the opponent's
      advantage from the position we hand them, so it counts against us.

  Boundaries:
      dp[N-1] is seeded directly, and the guards on `N - i` suppress the
      dp[i+2] / dp[i+3] terms when fewer than 3 or 4 stones remain. Those
      cases consume the row exactly, leaving an empty suffix whose
      difference is 0, so omitting the subtraction is the correct
      behaviour rather than a special case.

  Evaluation order:
      dp[i] reads only larger indices, so the loop runs right to left.
      Play proceeds forward but dependencies point backward: a position's
      value is defined by the positions it can lead to.

  dp[0] is Alice's margin, since she moves first on the full row. Its
  sign gives the result; zero means neither player can force an edge.

  Time:  O(N), constant work per index (the window is capped at 3, so no
         prefix or suffix sum array is needed).
  Space: O(N) for dp, reducible to O(1) since only dp[i+1..i+3] are read.
  """
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [0] * N
        dp[-1] = stoneValue[-1]
        for i in range(N - 2, -1, -1):
            take_1 = stoneValue[i] - dp[i + 1]
            take_2 = stoneValue[i] + stoneValue[i + 1]
            take_3 = float("-inf")
            if N - i > 2:
                take_2 -=  dp[i + 2]
                # take 3
                take_3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2]
            if N - i > 3:
                take_3 -= dp[i + 3]
            dp[i] = max(take_1, take_2, take_3)
        
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"
