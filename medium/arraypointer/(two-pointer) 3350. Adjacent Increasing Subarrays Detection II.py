  """
  Return the maximum k such that there exist two adjacent strictly increasing
  subarrays of length k each in `nums`.

  Idea:
  - First compress `nums` into maximal strictly-increasing runs [L, R].
    For example, nums = [1,2,3,  1,2,  5] -> runs: [0,2], [3,4], [5,5]
  - Two ways to obtain adjacent increasing subarrays of equal length k:
      1) Across a run boundary: take the suffix of the left run and the
         prefix of the right run. The best k across that boundary is
         min(len(left_run), len(right_run)).
      2) Within a single run: split one run into two adjacent parts;
         the best k there is floor(len(run) / 2).
  - The answer is the maximum k obtainable from any single run or any
    boundary of consecutive runs.

  Complexity:
  - Time: O(n) to build runs and scan them.
  - Space: O(r) to store the run endpoints, where r is the number of runs.

  """


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        increase_arr = []
        l = 0
        length = 1
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                length += 1
            else:
                increase_arr.append([l,r - 1])
                length = 1
                l = r
            if r == len(nums) - 1:
                increase_arr.append([l,r])
            
        longest = 0
        for i in range(len(increase_arr)):
            size = 0
            if i > 0:
                size = min((increase_arr[i - 1][1] -increase_arr[i - 1][0]) + 1, (increase_arr[i][1] - increase_arr[i][0]) + 1)
            longest = max(longest, size, ((increase_arr[i][1] - increase_arr[i][0]) + 1) // 2 )
        return longest
        
