"""
LeetCode 494 — Target Sum
Top-down DP (backtracking + memoization)

Idea
----
Each number gets either a '+' or a '−' sign. That means at index `depth`
we have exactly two choices: add nums[depth] or subtract nums[depth].
We explore this binary decision tree, but cache repeated states so we
don’t recompute the same subproblems.

State definition
----------------
f(depth, curr_sum) = number of ways to assign signs to indices
[depth .. len(nums) - 1] such that the final total equals `target`,
given that the running sum so far is `curr_sum`.

Recurrence
----------
For 0 <= depth < n:
    f(depth, curr_sum) =
        f(depth + 1, curr_sum + nums[depth])   # choose '+'
      + f(depth + 1, curr_sum - nums[depth])   # choose '−'

Base case
---------
When depth == len(nums):
    return 1 if curr_sum == target else 0
This contributes one valid assignment when we’ve assigned signs to all
numbers and landed exactly on `target`.

Why memoization makes it efficient
----------------------------------
Many different sign paths can lead to the same (depth, curr_sum) pair.
Without memoization, we would branch exponentially (O(2^n)).
Caching each (depth, curr_sum) result collapses all identical subtrees
to a single computation. If R = sum(nums), then curr_sum is bounded in
[-R, R], so the number of distinct states is O(n * R). Each state
combines two O(1) children once it’s cached.

Correctness (informal)
----------------------
- Base: At depth == n, the function returns 1 exactly when the built sum
  equals `target`, which is the definition of a valid assignment.
- Induction: Assume f(depth+1, ·) is correct. At `depth`, the only two
  legal moves are “+nums[depth]” or “−nums[depth]”. Every valid full
  assignment from this point must choose one of these two moves first,
  then proceed optimally. Summing the counts from both children gives
  the exact number of valid assignments from state (depth, curr_sum).

Complexity
----------
- Time:  O(n * R) in the typical analysis (R = sum(nums)), because we
         compute each reachable (depth, curr_sum) once and reuse it.
- Space: O(n * R) for the memo table; recursion depth is O(n).

Edge notes
----------
- If abs(target) > sum(nums), there are 0 ways (even all '+' can’t reach).
- Zeros: assigning '+' or '−' to 0 does not change curr_sum, but it
  doubles the number of sign assignments; the recurrence naturally
  counts both choices.
- Python integers are unbounded, so large intermediate sums are safe.

Alternative view (not required by this solution)
------------------------------------------------
Sign assignments implicitly partition nums into a '+' subset (sum P)
and a '−' subset (sum N), with P − N = target and P + N = total.
That implies 2P = total + target ⇒ P = (total + target)/2.
You can therefore convert the problem to counting subsets that sum to P.
This implementation solves it directly with top-down DP instead.

Returns
-------
Number of distinct expressions that achieving `target`.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(depth, curr_sum):
            if depth == len(nums):
                return 1 if curr_sum == target else 0
            if (depth, curr_sum) in memo:
                return memo[(depth, curr_sum)]
            memo[(depth, curr_sum)] = backtrack(depth + 1, curr_sum + nums[depth]) + backtrack(depth + 1, curr_sum - nums[depth])
            return memo[(depth, curr_sum)]

        return backtrack(0, 0)
