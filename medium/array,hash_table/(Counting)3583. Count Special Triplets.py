"""
Count the number of special triplets (i, j, k) such that
0 <= i < j < k < len(nums), nums[i] == 2 * nums[j], and
nums[k] == 2 * nums[j].

Uses prefix/suffix frequency counts:
- `left[v]`  = count of value v to the left of current index j.
- `right[v]` = count of value v to the right of current index j.

For each middle index j with value nums[j] = x, let need = 2 * x.
Then:
    #choices for i  = left[need]
    #choices for k  = right[need]
    contribution    = left[need] * right[need]

Sum contributions for all j and return modulo 1e9+7.

Time  : O(n)
Space : O(u) where u is the number of distinct values in nums.
"""

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        MOD = (10 ** 9) + 7
        left = defaultdict(int)
        right = defaultdict(int)
        res = 0
        for n in nums:
            right[n] += 1
        
        for n in nums:
            right[n] -= 1
            need = n * 2
            if need in right and need in left:
                res += left[need] * right[need]
            
            left[n] += 1
        return res % MOD
        
