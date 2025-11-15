"""
Find two numbers in a non-decreasing sorted array that add up to `target`.

This uses the classic two-pointer technique:
- Initialize one pointer at the start (l) and one at the end (r) of the array.
- Compute the current sum: curr = numbers[l] + numbers[r].
- If curr > target, move the right pointer left (r -= 1) to decrease the sum.
- If curr < target, move the left pointer right (l += 1) to increase the sum.
- If curr == target, we found the pair and return their 1-based indices.

The problem guarantees exactly one solution and does not allow using
the same element twice, which is naturally enforced since l < r.

Time Complexity:
    O(n), where n is the length of `numbers`, because each pointer
    moves at most n steps (they only move inward).

Space Complexity:
    O(1), since we only use a few variables regardless of input size.

Args:
    numbers: A list of integers sorted in non-decreasing order.
    target:  The integer sum we want to find using exactly two elements.

Returns:
    A list [i, j] where:
    - 1 <= i < j <= len(numbers)
    - numbers[i - 1] + numbers[j - 1] == target
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l + 1,r + 1]
        
