"""
Compute the maximum total happiness obtainable by selecting exactly k children.

Each time you select a child, the happiness contributed by any *later* selected child
is decreased by 1 per prior selection. If a child's adjusted happiness becomes negative,
it contributes 0 instead.

Greedy idea:
- To maximize the sum under a uniform increasing penalty (0, 1, 2, ...), always take the
  currently highest remaining base happiness first.
- Sort happiness in descending order, then for the i-th selected child (0-indexed),
  add max(0, happiness[i] - i).

Example:
happiness = [5, 3, 2], k = 2
sorted -> [5, 3, 2]
pick0: max(0, 5 - 0) = 5
pick1: max(0, 3 - 1) = 2
total = 7

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) extra space (aside from sorting implementation details)
"""

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            res += max(0, happiness[i] - i)
        
        return res
