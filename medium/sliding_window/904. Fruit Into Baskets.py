  """
  LeetCode 904 — Fruit Into Baskets
  Sliding window with counts (at most 2 distinct).

  Idea
  ----
  Maintain a window [l..r] and a counter `basket` for fruit types inside it.
  For each r, include fruits[r]. If the window now has > 2 distinct types,
  move l right, decrementing counts and deleting zero-count types, until the
  constraint (≤ 2 types) is restored. Track the largest window length seen.

  Why this works
  --------------
  We want the longest subarray with ≤ 2 distinct values. Expanding greedily
  and shrinking only when the constraint is violated explores exactly all
  maximal valid windows without missing any better candidate.

  Complexity
  ----------
  Time: O(n) — each index enters/leaves the window at most once.
  Space: O(1) — counter holds ≤ 2 keys.
  """


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        result = 0
        l = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            result = max(result, r - l + 1)
        
        return result
