  """
  Decide if `nums` can be split into two subsets with equal sum (LeetCode 416).

  Reframe:
    Let T = sum(nums). The task is equivalent to: “Is there a subset that sums to
    target = T/2?” If such a subset exists, the remaining elements also sum to T/2.
    If T is odd, this is impossible.

  DP intuition (subset-sum, 0/1 knapsack — set-based):
    Maintain a set `dp` of all reachable sums using the numbers seen so far.
    Initialize dp = {0}. For each number n:
      • Take a snapshot of current sums (we build a fresh `next_dp`).
      • Keep each existing sum e (meaning: skip n).
      • If e + n == target → early return True.
      • If e + n <  target → add (e + n) to next_dp (meaning: take n).
    Assign dp = next_dp and continue. Using a fresh set each step enforces the
    0/1 constraint (each element is used at most once) because we never let the
    newly formed sums in this step combine with `n` again.

  Why this is correct:
    After processing any prefix of nums, `dp` exactly equals the set of sums reachable
    by some subset of that prefix. Thus, if `target` ever appears, a valid partition exists.

  Complexity:
    At most `target + 1` distinct sums are tracked; each of the n numbers updates them once.
    Time ~ O(n * target) in practice; Space O(target).

  Notes / pitfalls:
    • Use integer math for the target to avoid floats: prefer `target = T // 2`.
    • This set DP is the same 0/1 knapsack recurrence as a boolean array/bitset;
      it
  """

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        target = sums / 2
        dp = set()
        dp.add(0)
        for n in nums:
            next_dp = set()
            for e in dp:
                next_dp.add(e)
                if e + n == target:
                    return True
                elif e + n < target:
                    next_dp.add(e + n)
            dp = next_dp
        
        return False
