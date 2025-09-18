  """
  Why it works (key invariant):
      Let P[i] be the prefix sum nums[0] + ... + nums[i]. For any l ≤ r,
      sum(nums[l..r]) = P[r] - P[l-1]. This sum is divisible by k iff
      (P[r] - P[l-1]) ≡ 0 (mod k) ⇔ P[r] ≡ P[l-1] (mod k).
      Therefore, valid subarrays correspond exactly to pairs of indices whose
      prefix sums leave the same remainder modulo k.

  Main idea:
      Sweep once from left to right, and for each prefix sum P[i], consider its
      remainder r = P[i] mod k. Every earlier prefix with the same remainder r
      forms a distinct subarray ending at i that is divisible by k. So the total
      number of such subarrays is the sum, over all i, of “how many times we’ve
      already seen this remainder.” Seeding the count of remainder 0 with 1
      accounts for prefixes that are themselves divisible by k (choose l = 0).

  Notes:
      - Python’s modulo is non-negative; in languages where it isn’t, normalize.
      - This is a pure counting argument on congruent remainders—no window/DP needed.

  Complexity:
      Time O(n); auxiliary space O(min(n, k)) to store remainder frequencies.
  """

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums_count = {0:1}
        sums, count = 0,0

        for n in nums:
            sums += n
            if sums % k in sums_count:
                count += sums_count[sums % k]
            sums_count[sums % k] = 1 + sums_count.get(sums % k, 0)
        return count
