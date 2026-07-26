  """
  The maximum product can only come from one of two cases after sorting:

  1. The three largest numbers.
  2. The two smallest numbers and the largest number.

  The second case is necessary because two large-magnitude negative
  numbers produce a positive product when multiplied together, which
  may exceed the product of the three largest values.

  After sorting, we simply compute both candidates and return the
  larger one.

  Time Complexity: O(n log n)
  Space Complexity: O(1) (excluding Python's sorting implementation)
  """
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[1] * nums[0])
        
