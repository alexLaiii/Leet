"""
Count the number of subarrays consisting only of zeros.

We scan the array and keep a running count of consecutive zeros.
- If nums[i] == 0, extend the current zero-run: consectiveZero += 1,
  and add it to the result because every new zero creates that many
  new zero-only subarrays ending at i.
- If nums[i] != 0, reset consectiveZero to 0.

Intuition: a run of length k contributes k + (k-1) + ... + 1 = k*(k+1)/2
zero-filled subarrays, and we accumulate this on the fly.

Time: O(n), Space: O(1).
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        consectiveZero = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                consectiveZero += 1
                res += consectiveZero
            else:
                consectiveZero = 0
        return res
                
