"""
Return True if the first player can win the Nim Game.

Main concept:
Every multiple of 4 is a losing position. If the number of
stones is not a multiple of 4, the first player can remove
1, 2, or 3 stones to leave a multiple of 4 to the opponent.

After that, whatever the opponent removes, take enough stones
to make the total removed by both players equal to 4, keeping
the opponent on a multiple of 4.

Time: O(1)
Space: O(1)
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
