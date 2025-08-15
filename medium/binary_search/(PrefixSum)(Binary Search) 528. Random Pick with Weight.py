"""
Core Idea:
1. Precompute prefix sums of w.
  - Example: w = [1, 3, 2] → prefix = [1, 4, 6].
2. Generate a random number between 1 and prefix[-1].
3. Binary search in prefix to find the first number ≥ that random number.
  - That index is your chosen index.


Build prefix sums P where P[i] = sum(w[0..i]). To pick index i with prob w[i]/P[-1]:
1) Draw t ~ Uniform{1..P[-1]} (inclusive integers).
2) Return the smallest index idx with P[idx] >= t (lower_bound).

Correctness:
Interval length for index i is P[i]-P[i-1] = w[i], so Pr[idx=i] = w[i]/P[-1].

Complexity:
- __init__: O(n)
- pickIndex: O(log n)
- Space: O(n)

Notes:
- Assumes all weights > 0 (per problem). If zeros are allowed, they just receive prob 0.
- For reproducible tests, set random.seed(...) outside.
"""


import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [w[0]]
        for n in w[1:]:
            self.prefixSum.append(self.prefixSum[-1] + n)
        
        
    def pickIndex(self) -> int:
        ranNum = random.randint(1, self.prefixSum[-1])
        l,r = 0, len(self.prefixSum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefixSum[mid] >= ranNum:
                r = mid
            elif self.prefixSum[mid] < ranNum:
                l = mid + 1
        
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
