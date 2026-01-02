"""
Return the element that is repeated N times in an array of length 2N.

Approach:
- Use a hash set `seen` to track elements we've already encountered.
- Scan left-to-right:
  - If the current number is already in `seen`, it must be the N-repeated element,
    so return it immediately.
  - Otherwise, add it to `seen`.

Why this works:
- The problem guarantees exactly one value appears N times, while all others appear once.
- The first time we see any duplicate during the scan, it can only be that N-repeated value.

Complexity:
- Time: O(n), where n = len(nums), single pass.
- Space: O(n) in the worst case for the `seen` set.

Notes:
- This solution returns as soon as it finds the duplicate, so it can finish early in practice.
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

                

        
