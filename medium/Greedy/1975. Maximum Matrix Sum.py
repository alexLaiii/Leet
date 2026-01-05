"""
Return the maximum possible sum of all elements in `matrix` after performing any number
of allowed operations (each operation flips the signs of two adjacent cells).

Key insight:
- Flipping two cells changes the number of negative entries by an even amount, so the
  parity (even/odd) of the negative count is invariant.
- The best we can do is make every entry contribute its absolute value to the sum.
  This is always achievable when the number of negatives is even.
- If the number of negatives is odd, then after maximizing all other signs, exactly one
  entry must remain negative. To minimize the penalty, that entry should be the one with
  the smallest absolute value. Compared to summing all absolute values, keeping one value
  negative reduces the total by 2 * (smallest absolute value).

Approach:
1) Iterate through all cells:
   - Add abs(value) to `absSum`.
   - Track `smallestAbs` = min abs(value) over the matrix.
   - Count how many values are negative (parity matters).
2) If negative count is even: answer is `absSum`.
   Else: answer is `absSum - 2 * smallestAbs`.

Correctness reasoning:
- `absSum` is the theoretical upper bound if all entries can be made non-negative.
- Parity constraint determines whether that bound is reachable.
- When odd parity, the smallest absolute value is the optimal one to "sacrifice" as negative.

Complexity:
- Time: O(m * n)
- Space: O(1)
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negativeCount = 0
        absSum = 0
        smallestInPositive = float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] <= 0:
                    negativeCount += 1
                smallestInPositive = min(smallestInPositive, abs(matrix[i][j]))
                absSum += abs(matrix[i][j])
        if negativeCount % 2 == 0:
            return absSum

        return absSum - (smallestInPositive * 2)
        
