
"""
LeetCode 152 — Maximum Product Subarray

Core idea (Kadane’s principle adapted to products):
At each index i, we only care about subarrays that **end at i**. With products,
a negative factor can flip signs, so yesterday’s worst product can become today’s
best. To capture this, we track two rolling extremes:
- max_till_i: largest product of any subarray until and including nums[i]
- min_till_i: smallest product of any subarray until and including nums[i]

Transition (why these formulas are enough):
Let x = nums[i], and let (prev_max, prev_min) be the extremes for subarrays
ending at i-1. Any subarray that ends at i is either:
  • just [x] (start fresh at i), or
  • an extension of a subarray that ended at i-1, multiplied by x.
Thus the only candidates for the new extremes are:
  x, x * prev_max, x * prev_min
We take:
  max_till_i = max(x, x * prev_max, x * prev_min)
  min_till_i = min(x, x * prev_max, x * prev_min)
Including x alone lets us restart after zeros or bad prefixes.

Invariant & correctness sketch:
After processing index i, (max_till_i, min_till_i) summarize **all**
products of subarrays that end exactly at i (we don’t need every product,
just the extremes). For index i+1 with value y, every subarray ending at i+1
is either [y] or (some subarray ending at i) * y, so knowing only the two
extremes from i is sufficient to compute the new extremes. The global answer
is the maximum over all max_till_i, tracked in `res`.

Complexity:
Time O(n) — one pass.
Space O(1) — constant extra variables.

Tiny trace (shows the “negative flip”):
nums = [2, 3, -2, 4]
i=0: x=2 → max=2,  min=2,   res=2
i=1: x=3 → max=6,  min=3,   res=6
i=2: x=-2 → candidates (-2, -12,  -6) → max=12, min=-12, res=12
i=3: x=4 → candidates (4,   48,  -48) → max=48, min=-48, res=48
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        min_till_i, max_till_i = nums[0], nums[0]
    
        for i in range(1, len(nums)):
            prev_min_till_i, prev_max_till_i = min_till_i, max_till_i
            min_till_i = min(nums[i], prev_min_till_i * nums[i], prev_max_till_i * nums[i])
            max_till_i = max(nums[i], prev_min_till_i * nums[i], prev_max_till_i * nums[i])
            res = max(res, max_till_i)
        return res
