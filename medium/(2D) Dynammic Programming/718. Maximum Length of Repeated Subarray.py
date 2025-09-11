"""
LeetCode 718

Core idea:
Use DP for the longest common *subarray* (contiguous) between nums1 and nums2. Let dp[i+1][j+1] be the length of the longest common **suffix** of nums1[:i+1] and nums2[:j+1]. 
If nums1[i] == nums2[j], extend the diagonal: dp[i+1][j+1] = dp[i][j] + 1; 
otherwise reset to 0. 

Optional:
Roll rows to O(N) space with `prev_dp` and track the max.

Why this works / intuition:
Matching elements can only extend a contiguous run if the previous pair also matched (hence the diagonal dependency). 
Any mismatch breaks contiguity, so we reset to 0—this is what distinguishes it from LCS (subsequence) which takes a max on mismatch.

Complexity:
Time O(M·N), Space O(N).

Pitfalls to remember:
- `prev_dp` length must be N+1; iterate j from 1..N and index nums2 at j-1.
- Update `max_subarray` as you fill the row (no separate pass needed).
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        max_subarray = 0
        
        prev_dp = [0 for i in range(N + 1)]
        
        for i in range(M):
            dp = [0 for i in range(N + 1)]
            for j in range(1, N + 1):
                if nums1[i] == nums2[j - 1]:
                    dp[j] = prev_dp[j-1] + 1
                max_subarray = max(max_subarray, dp[j])
            prev_dp = dp
        return max_subarray

