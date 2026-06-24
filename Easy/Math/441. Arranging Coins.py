import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Use the triangular number formula to find the number of complete rows.

        To build k complete rows, the total coins needed is:

            1 + 2 + 3 + ... + k = k * (k + 1) / 2

        We need the largest k where:

            k * (k + 1) / 2 <= n

        Rearranging gives:

            k^2 + k - 2n <= 0

        Solving with the quadratic formula gives:

            k = floor((sqrt(1 + 8n) - 1) / 2)

        The floor is needed because we only count fully completed rows.

        Time: O(1)
        Space: O(1)
        """
        return int((math.sqrt(1 + 8 * n) - 1) // 2)
