  """
  Return the number of odd integers in the inclusive range [low, high].

  Approach:
  - Let diff = high - low, the length of the interval minus one.
  - Handle small intervals explicitly:
      * If diff == 0, there is only one number (low == high):
          - Return 1 if that number is odd, otherwise 0.
      * If diff == 1, there are exactly two consecutive integers:
          - One of them must be odd, so return 1.
  - For larger intervals (diff >= 2), use parity of the endpoints:
      * If both low and high are odd:
          - The interior (excluding endpoints) contributes (diff - 1) // 2 odds,
            and both endpoints are odd, so total is ((diff - 1) // 2) + 2.
      * Otherwise (at least one endpoint is even):
          - The interior still contributes (diff - 1) // 2 odds,
            but only one odd endpoint at most, so total is ((diff - 1) // 2) + 1.

  Time Complexity: O(1) — only arithmetic and a few condition checks.
  Space Complexity: O(1) — no extra data structures used.
  """


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff == 0:
            return 0 if high % 2 == 0 else 1
        elif diff == 1:
            return 1
        elif low % 2 != 0 and high % 2 != 0:
            return ((diff - 1) // 2) + 2
        else:
            return ((diff - 1) // 2) + 1
