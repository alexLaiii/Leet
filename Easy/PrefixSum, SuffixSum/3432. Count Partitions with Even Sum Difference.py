  """
  Count the number of valid partitions of the array such that the difference
  between the sum of the left and right subarrays is even.

  A partition is an index i (0 <= i < n - 1) that splits nums into:
  - left subarray: nums[0..i]
  - right subarray: nums[i+1..n-1]

  This implementation maintains running sums of the left and right parts.
  For each partition, we update `left` and `right` in O(1) time and check
  whether the difference `left - right` has even parity.

  Time Complexity: O(n), where n is len(nums)
  Space Complexity: O(1)
  """

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        res = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if (abs(left - right) % 2 == 0):
                res += 1
        return res
        
