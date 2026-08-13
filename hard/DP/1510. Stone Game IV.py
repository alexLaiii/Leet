"""
Determines whether the first player wins Stone Game IV.

Two players alternate removing a non-zero perfect square number of
stones from a pile of n stones; whoever cannot move (pile is empty
on their turn) loses. Both players play optimally. This uses bottom-
up DP where dp[i] is True if the player about to move, facing i
stones, wins.

Args:
    n: Number of stones in the pile initially.

Returns:
    True if the first player can force a win, False otherwise.

Time Complexity:
    O(n * sqrt(n)) - for each of the n states, we try up to sqrt(i)
    square moves.

Space Complexity:
    O(n) - dp array storing one boolean per pile size.
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False, True]
        for i in range(2, n + 1):
            root = math.isqrt(i)
            dp.append(False)
            for j in range(1, root + 1):
                if not dp[i - (j * j)]:
                    dp[-1] = True
                    break
        return dp[-1]
