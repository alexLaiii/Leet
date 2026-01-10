"""
Dynamic Programming (Bottom-Up) solution for
LeetCode 712: Minimum ASCII Delete Sum for Two Strings.

Idea:
Define dp[i][j] as the minimum ASCII delete sum required to make
the suffixes s1[i:] and s2[j:] equal.

DP Table:
- dp has size (len(s1)+1) x (len(s2)+1)
- dp[M-1][N-1] = 0, where both suffixes are empty

Base Cases:
- dp[i][N-1]: s2 is empty, so delete all remaining characters in s1
dp[i][N-1] = ord(s1[i]) + dp[i+1][N-1]
- dp[M-1][j]: s1 is empty, so delete all remaining characters in s2
dp[M-1][j] = ord(s2[j]) + dp[M-1][j+1]

Transition:
- If s1[i] == s2[j]:
  No deletion needed for these characters
  dp[i][j] = dp[i+1][j+1]
- Else:
  Consider all deletion options and take the minimum:
  1) Delete both characters:
     ord(s1[i]) + ord(s2[j]) + dp[i+1][j+1]
  2) Delete s2[j]:
     ord(s2[j]) + dp[i][j+1]
  3) Delete s1[i]:
     ord(s1[i]) + dp[i+1][j]

Iteration Order:
- Fill dp table from bottom-right to top-left so future states
are already computed when needed.

Result:
- dp[0][0] gives the minimum ASCII delete sum for s1 and s2.

Time Complexity:
- O(len(s1) * len(s2))

Space Complexity:
- O(len(s1) * len(s2))
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        M, N = len(s1) + 1, len(s2) + 1
        dp = [[0 for j in range(N)] for i in range(M)]
        dp[M - 1][N - 1] = 0
        for i in range(M - 2, -1, -1):
            dp[i][N - 1] = ord(s1[i]) + dp[i + 1][N - 1]
        for j in range(N - 2,  -1, -1):
            dp[M - 1][j] = ord(s2[j]) + dp[M - 1][j + 1]
        
        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                    continue
                dp[i][j] = min(ord(s1[i]) + ord(s2[j]) + dp[i + 1][j + 1], ord(s2[j]) + dp[i][j + 1], ord(s1[i]) + dp[i + 1][j])
        return dp[0][0]
