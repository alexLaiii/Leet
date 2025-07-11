"""
Since we want the Longest Palindromic Subsequences, so we find the Longest Subsequence between string "s" and its reversed, which will be the Longest Palindromic Subsequences.
Subsequence means they must be the same after removing some characters, so if the subsequence "s" == reversed "s", then they must be palindrome.
The LCS(s, reversed(s)) guarantees a palindrome because the only strings that appear as subsequences in both the forward and reversed versions of s must be the same forwards and backwards — by definition
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        M = len(s)
        dp = [[0 for j in range(M + 1)] for i in range(M + 1)]
        
        for i in range(1, M + 1):
            for j in range(1, M + 1):
                if s[i - 1] == s[-j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
