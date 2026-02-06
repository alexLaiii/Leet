"""
Returns the minimum number of elements to remove so that the remaining array
is balanced, meaning the maximum value is at most k times the minimum value.

The algorithm sorts the array and uses a sliding window (two pointers) to
maintain the largest valid subarray where:
    nums[r] <= k * nums[l]

For each right pointer r, the left pointer l is advanced until the condition
is satisfied. The size of the valid window is tracked to minimize removals.

Args:
    nums (List[int]): List of integers.
    k (int): Balance factor such that max <= k * min.

Returns:
    int: Minimum number of removals required to balance the array.

Time Complexity:
    O(n log n) due to sorting + O(n) sliding window

Space Complexity:
    O(1) extra space (ignoring sort cost)

Algorithm:
    1. Sort the array.
    2. Use two pointers to maintain the largest valid window.
    3. Update the minimum removals as n - window_size.

"""
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        l = 0
        res = float("inf")
        for r in range(N):
            while l < r and nums[l] * k < nums[r]:
                l += 1
            res = min(res, N - (r - l + 1))
            
        return res
        
