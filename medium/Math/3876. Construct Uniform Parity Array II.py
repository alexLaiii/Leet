"""
Determine if nums1 can be transformed into a uniform-parity array.

For each index i, nums2[i] must be either nums1[i] itself, or
nums1[i] - nums1[j] for some j != i with nums1[i] - nums1[j] >= 1.
Returns True if some choice makes every element of nums2 the same
parity (all odd or all even).

Key facts:
    - Subtracting an odd value always flips parity; subtracting an
      even value always preserves it.
    - Therefore flipping odd -> even requires subtracting a smaller
      odd value, and flipping even -> odd requires subtracting a
      smaller odd value.
    - The smallest odd number in nums1 has no smaller odd number
      available, so it can never be flipped to even. This means
      target-even is only achievable if nums1 contains no odd
      numbers at all.
    - Consequently, if nums1 is mixed parity, all-odd is the only
      viable target, and it succeeds iff no even number is smaller
      than the smallest odd number (since that even number would
      have no smaller odd number to subtract).

Args:
    nums1: List of n distinct integers.

Returns:
    True if nums1 can be transformed into a uniform-parity array,
    False otherwise.

Time complexity:
    O(n), where n = len(nums1); two linear passes over the array.
Space complexity:
    O(1), only a constant number of tracking variables are used.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallestOdd, smallestEven = float("inf"), float("inf")
        for n in nums1:
            if n % 2 == 0:
                smallestEven = min(smallestEven, n)
            else:
                smallestOdd = min(smallestOdd, n)

        # All-even only possible if no odd number exists at all.
        if smallestOdd == float("inf") or smallestEven == float("inf"):
            return True

        # Mixed parity: only fixing everything to odd is possible.
        # Any even number smaller than smallestOdd has no smaller odd
        # number to subtract, so it can never be flipped to odd.
        for n in nums1:
            if n % 2 != 1 and n - smallestOdd <= 0:
                return False

        return True
