"""
Find the leftmost pivot index where the sum of all elements to the
left equals the sum of all elements to the right.

Compute the total sum of the array once. As we iterate through the
array, maintain a running left sum. The right sum at index i can be
calculated in O(1) as:

  right_sum = total_sum - left_sum - nums[i]

If left_sum == right_sum, then i is the pivot index.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
                
        
"""
Solution that use O(n) space, with both prefix sum array and suffix sum array precomputed
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        N = len(nums)
        left_sum = [0] * (N + 1)
        right_sum = [0] * (N + 1)
        
        for i in range(1,N + 1):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
        for j in range(N - 1, -1, -1):
            right_sum[j] = right_sum[j + 1] + nums[j]

        for k in range(N):
            if left_sum[k] == right_sum[k + 1]:
                return k
        return -1
                
        
