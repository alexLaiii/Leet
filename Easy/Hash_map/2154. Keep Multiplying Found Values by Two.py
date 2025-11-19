  """
  Repeatedly doubles the given `original` value as long as it appears
  in the array `nums`, and returns the final value when it no longer
  exists in the array.

  Idea:
  - Convert `nums` to a set for O(1)-average membership checks.
  - While `original` is in the set, multiply it by 2 and check again.
  - Stop when the current `original` is not found in the set.

  Correctness:
  - Each time `original` is found in `nums`, the problem requires us
    to double it and search again, which is exactly what the loop does.
  - Since `original` strictly increases and `nums` is finite, the loop
    must eventually terminate when the new `original` is not in `nums`.
  - The returned value is therefore the smallest value reachable by
    repeated doubling that does not appear in `nums`.

  Time Complexity:
  - Building the set from `nums` takes O(n).
  - The loop runs at most O(log M) times, where M is the final value,
    and each membership check is O(1) on average.
  - Overall: O(n) time, O(n) extra space for the set.
  """

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original
