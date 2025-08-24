  """
  ***
  Key point:
  The first Binary Search find the Leftmost index that nums[index] == target
  The Second Binary Search find the Rightmost index that nums[index] == target
  ***

  Key idea: two *biased* binary searches.
    1) Find the **leftmost** occurrence:
       - While searching, if nums[mid] == target, record it as a candidate left index.
       - Then bias the search to the **left** by doing `r = mid - 1` whenever
         `nums[mid] >= target`. This ensures we keep shrinking toward the earliest index.
    2) Find the **rightmost** occurrence:
       - Start from the found left index to save work.
       - While searching, if nums[mid] == target, record it as a candidate right index.
       - Then bias the search to the **right** by doing `l = mid + 1` whenever
         `nums[mid] <= target`. This pushes the window toward the latest index.

  Why it works:
    - The first pass effectively finds the smallest index i with nums[i] >= target,
      and records hits along the way; because we always move left on equality, we
      converge to the first equality position if it exists.
    - The second pass does the symmetric thing for the largest index j with
      nums[j] <= target, converging to the last equality position.

  Edge handling:
    - If the first pass never records an equality, target is absent → return [-1, -1].
    - Works for empty arrays and all-duplicate ranges.

  Complexity:
    - Time: O(log n) for each pass → O(log n) total.
    - Space: O(1).

  Pitfalls avoided:
    - We **update the answer when equality is seen** *before* continuing the biased move,
      so we don’t lose a valid mid.
    - Using `>=` in pass 1 and `<=` in pass 2 is the crucial bias that drives the window
      toward the boundaries rather than stopping at an arbitrary middle occurrence.
  """


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid] >= target:
                r = mid - 1
            else:   
                l = mid + 1
        if res[0] == -1:
            return [-1,-1]
        l,r = res[0], len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            
        return res
