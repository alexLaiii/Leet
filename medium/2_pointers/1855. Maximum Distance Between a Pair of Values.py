"""
Two-pointer approach for Maximum Distance Between a Pair of Values.

Idea:
Since both nums1 and nums2 are non-increasing arrays, we can use
two pointers i and j to efficiently find the maximum valid distance.

A valid pair satisfies:
    i <= j
    nums1[i] <= nums2[j]

Algorithm:
1. Start with i = 0 and j = 0.
2. If nums2[j] >= nums1[i], then (i, j) is a valid pair:
   - update maxDiff = max(maxDiff, j - i)
   - move j forward to try getting a larger distance
3. If nums2[j] < nums1[i], the pair is invalid:
   - move i forward to make nums1[i] smaller/easier to satisfy
4. Special case:
   - if i == j and still invalid, move j forward first to maintain
     the required condition i <= j
5. Continue until j reaches the end of nums2.

Why this works:
Because both arrays are sorted in non-increasing order, moving i
forward makes nums1[i] smaller, and moving j forward explores larger
possible distances. Each pointer moves only once.

Time Complexity:
O(len(nums1) + len(nums2))

Space Complexity:
O(1)
"""
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        maxDiff = 0
        
        while j < len(nums2):
            if i >= len(nums1):
                return maxDiff
            if nums2[j] >= nums1[i]:
                maxDiff = max(maxDiff, j - i)
                j += 1
            elif i == j:
                j += 1
            else:
                i += 1
        
        return maxDiff
                
        
