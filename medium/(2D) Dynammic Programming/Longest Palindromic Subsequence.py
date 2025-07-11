"""
Solution 1 (Recursion with memorization)
Insight:
---------
This problem allows us to use a two-pointer DP approach (from both ends of the string)
because it deals with **subsequences**, not substrings. Subsequence problems allow
characters to be skipped, which fundamentally changes how mismatches are handled
compared to substring problems.

Key Difference from Substring Palindrome Problems (e.g., Leetcode 5, 647):
-------------------------------------------------------------------------
1. Palindromic Subsequence:
   - Characters do **not** have to be contiguous.
   - On mismatch, we can **skip characters**: try both (l+1, r) and (l, r-1).
   - We don’t rely on a valid center. A larger palindrome can wrap around any
     "best possible middle", even if that middle isn’t a palindrome.
   - We reduce the problem to smaller ranges and use memoization to avoid recomputation.
   - The DP transition is:
       if s[l] == s[r]:
           dp[l][r] = 2 + dp[l+1][r-1]
       else:
           dp[l][r] = max(dp[l+1][r], dp[l][r-1])

2. Palindromic Substring:
   - Characters **must** be contiguous.
   - On mismatch, the current expansion is **abandoned** — you must start a new attempt.
   - The palindrome must be built from a **valid center**, expanding outward symmetrically.
   - You cannot skip any characters; mismatch = invalid.
   - That's why expansion from center is better approach in Palindromic Substring, but not here.

Why Two-Pointer DP from both edges Works for This Problem:
------------------------------------------
- Because we're allowed to skip characters, we never need to restart the process.
- We simply recurse inward:
    - If ends match → wrap them around a smaller subsequence.
    - If they don’t match → skip one character and try both options.
- Each subproblem (l, r) is solved only once with memoization → O(n^2) time.
- This structure reflects the true nature of palindromic subsequences.

Conclusion:
-----------
The larger palindromic subsequence is **not built from a smaller palindromic center**.
Instead, we form it by matching characters at both ends and recursively wrapping around
whatever inner subsequence gives us the longest result — even if the middle itself
is not a palindrome.

This distinction is what makes dynamic programming with two pointers from both ends
not only valid, but optimal in this case.

Time Complexity: O(n^2)
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        M = len(s)
        cache = {}
        def dfs(l,r):
            if l >= M or r < 0 or l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            if l == r:
                return 1
            if s[l] == s[r]:
                cache[(l,r)] = 2 + dfs(l + 1, r - 1)
            else:
                cache[(l,r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            return cache[(l,r)]
        return dfs(0, M - 1)
                

"""
Solution 2.
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
