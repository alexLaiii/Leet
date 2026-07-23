"""
Observation:
- When n <= 2, the unique XOR results are simply the elements themselves,
  so the answer is n.
- For n >= 3, using numbers from 1 to n allows us to construct every XOR
  value in the range [0, 2^k - 1], where k is the number of bits needed to
  represent n.
- Hence, the number of distinct XOR triplets is exactly 2^k.

Complexity:
- Time: O(1)
- Space: O(1)
"""
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        return 2 ** n.bit_length()
        

        
        
