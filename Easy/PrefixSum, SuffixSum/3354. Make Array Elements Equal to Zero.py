  """
  LeetCode 3354 — Make Array Elements Equal to Zero

  What this does:
    - Scans the array once while maintaining:
        prefix = sum of nums[0..i-1]
        suffix = sum of nums[i..n-1]
    - At each index i where nums[i] == 0, it treats i as a split point
      and compares left sum L = prefix with right sum R = suffix - nums[i].
      Since nums[i] is 0, R = suffix.
    - Adds:
        +2 if L == R,
        +1 if |L - R| == 1,
        +0 otherwise.
    - Updates prefix += nums[i], suffix -= nums[i] each step.

  Why it works:
    - For any zero position i, only the sums strictly left/right of i
      matter. 
        At a zero, only the total “work” (sum) on each side matters:
          • If prefix and suffix differ by exactly 1, you must start reducing from the
            bigger side; starting from the smaller leaves 1 unit stranded on
            the larger side → exactly 1 valid way.
          • If prefix == suffix, you can start from either side and perfectly balance
            to zero → 2 valid ways.
          • If |prefix - suffix| ≥ 2, no ordering can fix a gap that large → 0 ways.
      Using running prefix/suffix gives those sums in O(1) time.
      Because nums[i] = 0, excluding i from the right side is free
      (R = suffix), so the balance conditions map directly to the rules.

  Complexity:
    - Time:  O(n) single pass
    - Space: O(1) extra

  Edge notes:
    - No zeros ⇒ result 0
    - Handles negatives naturally (sum comparisons still valid)
  """


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        prefix, suffix = 0, sum(nums)

        for x in nums:
            if x == 0:
                # Here: left = prefix, right = suffix - x = suffix
                if abs(prefix - suffix) == 1:
                    count += 1
                elif prefix == suffix:
                    count += 2
            prefix += x
            suffix -= x

        return count
