"""
LeetCode 1658 — Minimum Operations to Reduce X to Zero
Review Docstring (for future me)

Problem (reframed):
- You can remove elements from the left or right ends of `nums`.
- Let total = sum(nums). Removing ends that sum to x is equivalent to
  KEEPING a *middle* subarray whose sum is target = total - x.
- Answer = fewest removals = n - longest_length_of_subarray_with_sum(target).
- If no such subarray exists, return -1.

Key assumption (why sliding window works):
- nums[i] > 0 (strictly positive). With all positives:
  - Expanding the window increases sum monotonically.
  - Shrinking from the left decreases sum monotonically.
  - Thus a classic two-pointer window can find all subarrays with sum == target in O(n).
- If negatives were allowed, this approach would fail; use prefix-sum + hashmap instead.

Algorithm (current implementation):
1) Compute target = sum(nums) - x.
   - If target < 0 → impossible → return -1 (x > total).
2) Slide a window [l..r]:
   - Add nums[r] to windowSum.
   - While windowSum > target: move l right and subtract nums[l].
   - If windowSum == target: update maxArrLen with (r - l + 1).
3) If maxArrLen found: return n - maxArrLen else -1.

Correctness sketch:
- Any valid sequence of end removals leaves a contiguous middle block with sum target.
- Among all such middle blocks, leaving the *longest* keeps the most elements,
  hence minimizes removed elements: removals = n - longest_len.
- With positive nums, the sliding window enumerates exactly the candidate subarrays
  because windowSum moves monotonically as l/r change.

Edge cases:
- target == 0 → keep nothing → answer = n (remove all).
  (This implementation still finds a zero-length window; early-return is optional.)
- x > sum(nums) → target < 0 → return -1.
- No subarray hits target → return -1.

Complexity:
- Time: O(n)
- Space: O(1)

Common pitfalls:
- Using sliding window when nums can be negative (WRONG).
- Forgetting that target can be 0.
- Off-by-one when updating `best` length (use r - l + 1).

Variant (if nums may include non-positives):
- Use prefix-sum + hashmap to find the *longest* subarray with sum == target in O(n) time, O(n) space.

Quick dry run:
- nums = [1,1,4,2,3], x = 5 → total=11, target=6.
  Longest subarray with sum 6 is [4,2] (len=2) → answer = 5 - 2 = 3.

Takeaway:
- For LC1658 (positive nums), this sliding-window formulation is optimal and clean.
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        maxArrLen = -1
        windowSum = 0
        l = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            while   windowSum  > target:
                windowSum  -= nums[l]
                l += 1
            if  windowSum  == target:
                maxArrLen = max(maxArrLen, r - l + 1)
        return len(nums) - maxArrLen if maxArrLen != -1 else -1
