"""
Returns the minimum possible value of the maximum pair sum in the array.

The strategy is greedy:
- Sort the array.
- Pair the smallest remaining element with the largest remaining element.
- Track the maximum sum among all such pairs.

This pairing minimizes the worst-case pair sum because pairing large values
together would increase the maximum unnecessarily, while pairing each large
value with the smallest available balances the sums.

Args:
  nums (List[int]): An even-length list of integers.

Returns:
  int: The minimized maximum sum of all paired elements.

Time Complexity:
  O(n log n) due to sorting.

Space Complexity:
  O(1) extra space (excluding sorting overhead).
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        l,r = 0, len(nums) - 1
        maxSum = float("-inf")
        while l < r:
            maxSum = max(maxSum, nums[l] + nums[r])
            l += 1
            r -= 1
        return maxSum
