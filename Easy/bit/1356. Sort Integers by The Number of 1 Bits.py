"""
Sort integers by the number of 1-bits in their binary representation.

Approach:
- Use bucket sorting by popcount (number of set bits).
- Create 65 buckets (0..64) since Python ints can be large, and LeetCode's
  constraints for this problem fit comfortably within that range.
- For each number, compute its popcount using bit operations and append it
  to the corresponding bucket.
- For each non-empty bucket, sort it numerically (tie-breaker rule) and
  concatenate into the final result.

Helper:
- checkBit(num): counts 1-bits by repeatedly checking the least significant
  bit and shifting right until the number becomes 0.

Time Complexity:
- Let n = len(arr), and let B be the maximum number of bits needed to
  represent the largest number.
- Popcount for each number costs O(B), so bucketing is O(n * B).
- Sorting within buckets totals O(n log n) in the worst case.
- Overall: O(n * B + n log n).

Space Complexity:
- O(n) for the buckets and the output list.

Note:
- In checkBit, writing `(num & 1) == 1` is clearer than `num & 1 == 1`
  because `==` has higher precedence than `&` in Python.
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        store = [[] for i in range(65)]
       
        def checkBit(num):
            count = 0
            while num != 0:
                if (num & 1) == 1:
                    count += 1
                num >>= 1
            return count
        
        for n in arr:
            bits = checkBit(n)
   
            store[bits].append(n)

        res = []
        for bucket in store:
            if bucket:
                bucket.sort()
                res += bucket
        
        return res
                
        
                
        
