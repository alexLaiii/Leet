"""
Since XOR is both commutative and associative, any XOR triplet can be rewritten as:

```
(a ^ b) ^ c
```

Therefore, instead of enumerating all O(n^3) triplets, we can first precompute all possible XOR values of two numbers and then XOR those results with every number in the array.

The first pass computes every distinct value of nums[i] ^ nums[j] (including i == j, which produces 0 and accounts for repeated indices). Because XOR is commutative, iterating j from i to n - 1 is sufficient to cover all unique pair XOR values.

The second pass combines each precomputed pair XOR with every element in nums to generate all possible triplet XOR values. A set is used to ensure that each distinct XOR result is counted only once.

Time Complexity:
O(n^2 + n * 2^k), where k = max(nums).bit_length().

Space Complexity:
O(2^k), since there are at most 2^k distinct XOR values for k-bit integers.
"""

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                seen.add(nums[i] ^ nums[j])

        visited = set()
        res = 0
        for i in range(len(nums)):
            for val in seen:
                triplet = val ^ nums[i]

                if triplet not in visited:
                    res += 1
                    visited.add(triplet)
        
        return res
                
            
            
