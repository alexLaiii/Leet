"""
Return all pairs [a, b] (with a < b) from arr such that b - a is the
minimum absolute difference among all pairs in the array.

Key idea:
- Sort arr. After sorting, the minimum absolute difference must occur
  between some pair of adjacent elements (any non-adjacent pair has
  a gap at least as large as the smallest adjacent gap in between).
- First pass: compute mindiff across adjacent differences.
- Second pass: collect every adjacent pair whose difference == mindiff.

Args:
    arr: List of integers.

Returns:
    A list of pairs [arr[i], arr[i+1]] (in increasing order) that achieve
    the minimum absolute difference. Pairs are naturally sorted by their
    first element due to the initial sort.

Time Complexity:
    O(n log n) for sorting + O(n) scans => O(n log n)

Space Complexity:
    O(1) extra space (excluding the output list), since sorting is in-place
    in typical Python implementations.
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float("inf")
        for r in range(1, len(arr)):
            mindiff = min(arr[r] - arr[r - 1], mindiff)
        res = []
  
        for r in range(1, len(arr)):
            if arr[r] - arr[r - 1] == mindiff:
                res.append([arr[r-1], arr[r]])
        return res
