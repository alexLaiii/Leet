"""
Leetcode 1004: Max Consecutive Ones III

An easy-medium problem, very similar to "424. Longest Repeating Character Replacement".

🔹 Idea:
Use a sliding window to maintain the longest valid window that contains at most `k` zeros.
We expand the window by moving the right pointer, and shrink it from the left when the count of zeros exceeds `k`.

- Use a `zeros` counter to track the number of 0s in the current window.
- While `zeros > k`, move `l` right until the window becomes valid again.
- Every window you maintain is valid, so you can always update the result with `r - l + 1`.

Edge Case:
If `nums = [0]` and `k = 0`, the logic still holds.
- At some point `l = 1`, `r = 0`, so `r - l + 1 = 0` — correctly returning 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
