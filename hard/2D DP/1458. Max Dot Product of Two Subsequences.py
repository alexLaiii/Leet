"""
LeetCode 1458 — Max Dot Product of Two Subsequences

Goal:
    Choose a non-empty subsequence from nums1 and a non-empty subsequence from nums2
    (preserving relative order) with the same length, maximizing the dot product.

DP definition:
    dp[i][j] = the maximum dot product achievable using subsequences chosen from:
              nums1[i:] and nums2[j:], with the constraint that we must pick
              at least one pair overall (handled by -inf initialization).

Transition (iterate i, j from bottom-right to top-left):
    Let firstProduct = nums1[i] * nums2[j].

    We have 4 options:
      1) Start fresh with just this pair:
            firstProduct
         (This is crucial for cases where adding more pairs would hurt,
          and also for the "must be non-empty" requirement.)

      2) Take this pair and extend with best from the suffix:
            firstProduct + dp[i+1][j+1]
         (Continue picking more matched pairs after i and j.)

      3) Skip nums2[j]:
            dp[i][j+1]

      4) Skip nums1[i]:
            dp[i+1][j]

    So:
        dp[i][j] = max(firstProduct,
                       firstProduct + dp[i+1][j+1],
                       dp[i][j+1],
                       dp[i+1][j])

Base / boundaries:
    dp is sized (len(nums1)+1) x (len(nums2)+1), filled with -inf.
    The last row/col stay -inf, meaning "no valid non-empty selection possible"
    if one array is exhausted.

Why the -inf matters:
    If we used 0 as the base, the DP could incorrectly choose "pick nothing"
    and return 0, which is invalid when all possible products are negative.
    Using -inf forces at least one pair to be selected.

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
    where m = len(nums1), n = len(nums2).

Note:
    This is the standard correct DP for 1458.
"""

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1) + 1, len(nums2) + 1
        dp = [[float("-inf") for i in range(N)] for j in range(M)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                firstProduct = nums1[i] * nums2[j]
                dp[i][j] = max(firstProduct, firstProduct + dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
