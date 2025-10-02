"""
Return the single duplicated value in an array of length n+1 containing
integers in the range [1..n].

Approach — Binary Search on VALUE (Pigeonhole Principle):
  - Maintain a value range [l, r] where the duplicate must lie. Start with
    l = 1 and r = len(nums) - 1 (i.e., n).
  - Let mid = (l + r) // 2 be a value threshold (NOT an index).
  - Count how many elements in nums are <= mid.
      * If count > mid, there are “too many” numbers in [1..mid], so the
        duplicate must be in [l, mid]  → set r = mid.
      * Otherwise, the duplicate is in [mid+1, r]  → set l = mid + 1.
  - Loop ends when l == r; that value is the duplicate.

Why it works:
  - If values were all unique in [1..n], exactly mid elements would be <= mid.
    Any excess (count > mid) proves a collision within [1..mid].

Invariants:
  - The true duplicate always lies in the current closed interval [l, r].
  - The interval size strictly shrinks each iteration (since r = mid or l = mid+1).

Complexity:
  - Time: O(n log n) — each step scans nums to compute the count, with O(log n)
    steps from binary search over the value space.
  - Space: O(1) extra.

Pitfalls to avoid:
  - Do NOT treat mid as an array index; it is a value threshold.
  - Use the strict check `count > mid` to decide the left half.

Assumptions:
  - Input satisfies the problem constraints: exactly one duplicated value
    (possibly repeated more than twice), values in [1..n], and len(nums) = n+1.

Returns:
  The duplicated integer.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        
        return l
