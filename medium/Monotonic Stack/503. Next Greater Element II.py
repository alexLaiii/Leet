    """
    LeetCode 503 — Next Greater Element II (circular array)

    Computes, for each element in a circular array, the first element to its right
    (wrapping around) that is strictly greater. If no such element exists, returns -1
    for that position.

    Approach:
        - Use a **monotonic decreasing stack** of tuples (value, index).
        - Iterate 2 * n times to simulate circularity; map i -> idx = i % n.
        - For each idx, while the current number nums[idx] is greater than the value
          at the top of the stack, pop and set that popped index's answer to nums[idx].
        - Push the current (value, index). (This version intentionally pushes in both
          passes; it remains correct because any “duplicate” index will be assigned the
          same next-greater value when it reappears.)

    Why it works:
        - The stack maintains indices whose next greater element hasn't been found yet,
          in strictly decreasing order of their values. When a larger value arrives,
          it resolves all smaller values on top of the stack.
        - Doubling the pass supplies wrap-around candidates so elements near the end
          can see greater elements near the beginning.

    Edge cases:
        - Equal elements do not pop (strictly greater required), so positions whose
          next greater does not exist remain -1.
        - Works for all-decreasing arrays (answers all -1) and mixed patterns.

    Complexity:
        - Time: O(n). Each index is pushed at most twice and popped at most once; the
          constant factor is higher due to pushing in both passes but remains linear.
        - Space: O(n) for the stack and output array.

    Args:
        nums: List[int] — the input circular array.

    Returns:
        List[int]: res where res[i] is the first strictly greater element to the right
        of nums[i] in the circular traversal, or -1 if none exists.
    """

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums) * 2):
            idx = i % len(nums)
            while stack and nums[idx] > stack[-1][0]:
                prev_n, prev_i = stack.pop()
                res[prev_i] = nums[idx]
            stack.append((nums[idx], idx))
        return res

