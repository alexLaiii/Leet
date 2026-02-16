"""
Simulates the champagne flow through a triangular tower of glasses using
dynamic programming.

Each glass is represented as a tuple:
    (amount_filled, overflow)

where:
- amount_filled is capped at 1 (the glass capacity)
- overflow is the excess champagne that flows downward

The DP table is built row by row, where each glass receives half of the
overflow from the two glasses above it.

Algorithm:
- Initialize a 2D DP table of size (query_row + 2) × (query_row + 2)
  using 1-based indexing.
- Set the top glass based on the poured amount.
- For each subsequent row:
    • Compute incoming champagne from parent overflows
    • Cap the glass at 1 and store any excess as overflow
- Return the filled amount of the target glass.

Time Complexity: O(query_row²)
Space Complexity: O(query_row²)

Args:
    poured (int): Total units of champagne poured into the top glass.
    query_row (int): Row index of the target glass (0-indexed in problem statement).
    query_glass (int): Column index of the target glass (0-indexed in problem statement).

Returns:
    float: The amount of champagne in the specified glass, capped at 1.
"""

class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[(0, 0) for i in range(query_row + 2)] for i in range(query_row + 2)]
        tower[1][1] = (poured, 0) if poured <= 1 else (1, poured - 1)

        for i in range(2, query_row + 2):
            for j in range(1, i + 1):
                fall = tower[i-1][j][1] / 2 + tower[i-1][j-1][1] / 2
                tower[i][j] = (fall, 0) if fall <= 1 else (1, fall - 1)
                    
                
        return tower[query_row + 1][query_glass + 1][0]
