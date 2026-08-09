"""
Alex plays optimally against Bob for piles of stones, where each turn
a player takes the first X piles (1 <= X <= 2*M) and M updates to
max(M, X) afterward. Returns the max stones the first player (Alex)
can collect.

State: dp[i][m] = best score the current player can get from the
remaining piles[i:], given current bound m.

Transition: for each legal X, the current player's payoff is the
total stones left (suffixSum[i]) minus whatever the opponent
optimally scores afterward (dp[i+X][max(m,X)]) — a zero-sum split
of the remaining pile. Take the best X.

Base case: if 2*m >= remaining piles, take everything (dp[i][m] =
suffixSum[i]).

Build order: i descending (dp[i] depends on dp[i+X], X>=1, so
larger i must be computed first); m in any order within a fixed i.

Time: O(N^3) - O(N^2) states, O(N) transition each (X ranges up
to 2*m).
Space: O(N^2) for the dp table.
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        suffixSum = [0] * N
        suffixSum[-1] = piles[N - 1]
        for i in range(N - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + piles[i]

        dp = [[0 for j in range(N + 1)]for i in range(N)]

        for i in range(N - 1, -1, -1):
            for m in range(1, N + 1):
                if  2 * m >= N - i:
                    dp[i][m] = suffixSum[i]
                else:
                    maxGain = 0
                    for x in range(1, 2 * m + 1):
                        if i + x > N - 1:
                            break
                        maxGain = max(maxGain, suffixSum[i] - dp[i + x][max(m, x)])
                    dp[i][m] = maxGain
   
        return dp[0][1]
        
