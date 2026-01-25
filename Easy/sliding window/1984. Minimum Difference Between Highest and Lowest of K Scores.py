  """
  Return the minimum possible difference between the highest and lowest scores
  among any group of `k` scores from `nums`.

  Approach:
  - Sort `nums` so any optimal group of size `k` corresponds to a contiguous
    window in the sorted array.
  - Slide a window of length `k` across the sorted list and track the minimum
    difference `nums[r] - nums[l]` for each window.

  Edge cases:
  - If `k == 1` (or there is only one element), the difference is 0 because
    the highest and lowest in a single-element group are the same.

  Time Complexity:
  - O(n log n) for sorting, plus O(n) for scanning windows.

  Space Complexity:
  - O(1) extra space (ignoring the space used by Python's sort implementation).

  Args:
      nums: List of integer scores.
      k: Size of the group to choose.

  Returns:
      The minimum difference between max and min within any size-`k` subset.
  """

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        res = float("inf")
        l = 0
        for r in range(k - 1, len(nums)):
            res = min(res, nums[r] - nums[l])
            l += 1
        return res
            
            
