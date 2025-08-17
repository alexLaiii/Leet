"""
Compute the product of all elements in the array except self, 
without using division.

Why it works:
- For any index i, the desired product is:
      nums[0] * nums[1] * ... * nums[i-1] * nums[i+1] * ... * nums[n-1]
- This can be broken into two independent parts:
      (product of all elements before i) * (product of all elements after i)
- By precomputing:
      prefix_prod[i] = product of nums[0..i]
      suffix_prod[i] = product of nums[i..n-1]
  we can quickly retrieve these two parts:
      prefix_prod[i-1] gives product before i
      suffix_prod[i+1] gives product after i
- Multiplying them yields the correct result for index i.

Steps:
1. Build prefix_prod from left to right.
2. Build suffix_prod from right to left.
3. For each index i, multiply prefix_prod[i-1] and suffix_prod[i+1],
   with edge cases handled at array boundaries.

Complexity:
- Time: O(n) (one pass for prefix, one for suffix, one for result).
- Space: O(n) for prefix_prod and suffix_prod arrays.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = []
        suffix_prod = [0] * n
        prefix, suffix = 1,1
        for i in range(n):
            prefix *= nums[i]
            prefix_prod.append(prefix)
        for j in range(n - 1, -1, -1):
            suffix *= nums[j]
            suffix_prod[j] = suffix
        
        res = [1] * n
        for i in range(n):
         
            if i - 1 >= 0:
                res[i] *= prefix_prod[i - 1]
            if i + 1 < n:
                res[i] *= suffix_prod[i + 1]
        return res
     
        

        
        
