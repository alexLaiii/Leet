"""
# Recursion Approach
Core Idea:
The main challenge of this problem is handling the '*' wildcard.

In the recursive approach, whenever we encounter '*' in the pattern `p`, we explore two possibilities:
1. Use '*' to match the current character in `s` (i.e., consume a character from `s` and stay on the same '*' in `p`)
2. Skip the '*' (i.e., move to the next character in `p` without consuming any character from `s`)

We recursively try both options. If either path leads to a successful match of the remaining string and pattern,
then a valid match exists between `p` and `s`.

This approach tries all valid paths, and with memoization, avoids recomputation of overlapping subproblems.

Time Complexity: O(m * n), where m = len(s), n = len(p)
Space Complexity: O(m * n), due to memoization cache

Returns:
    bool: True if `s` matches `p`, considering wildcard rules; otherwise False.

    
2D DP (Bottom-Up Approach) for Leetcode 44: Wildcard Matching.

In this approach, we use a bottom-up 2D DP table.
Each cell dp[i][j] stores whether the pattern p[0:i] can match the string s[0:j].
For example, s = "adceb", p = "*a*b"
Then dp[3][3] represents whether "adc" matches "*a*".
In this case, it is True:
  - The first "*" takes nothing
  - The "a" matches "a"
  - The second "*" takes "dc"

Like many 2D DP string problems, to determine dp[i][j], there exist relationships with the previous cells.

Example:
  s = "adceb", p = "*a*b"
  To compute dp[3][3] (i.e., "adc" vs. "*a*"):
  The current pattern character is "*", which can take:
    - Nothing: the question becomes "Can 'adc' match '*a'" → check dp[i-1][j]
    - One character: the question becomes "Can 'ad' match '*a*'" → check dp[i][j-1]
  So: 
    - dp[i-1][j] means the "*" takes nothing
    - dp[i][j-1] means the "*" takes one character
    - If either is True, then dp[i][j] = True

What if the current character is not "*"?
Assume we're computing dp[5][4] for:
  s = "adceb", p = "*a*b"
  We're checking if "adceb" matches "*a*b"
  The current pattern character is "b", which must match exactly:
    - If s[j-1] != p[i-1], then dp[i][j] = False
    - If s[j-1] == p[i-1], then we check dp[i-1][j-1]:
          → If dp[i-1][j-1] is True, dp[i][j] = True

Why not use dp[i-1][j] or dp[i][j-1] in this case?
  Because "b" must take exactly one character:
    - dp[i-1][j] implies "b" takes nothing → invalid
    - dp[i][j-1] implies "b" takes multiple → invalid
  So only dp[i-1][j-1] is meaningful.

Summary:
  - If p[i-1] == '*': dp[i][j] = dp[i-1][j] or dp[i][j-1]
  - If p[i-1] == '?' or p[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1]
  - Else: dp[i][j] = False

Initialization:
  - dp[0][0] = True → empty pattern matches empty string
  - dp[0][j] = False → empty pattern can't match non-empty string
  - dp[i][0] = True only if all previous pattern chars are '*'

Time Complexity: O(m * n) — filling the entire grid
Space Complexity: O(m * n) — 2D DP grid

Implementation below:
"""

# 2D DP (Bottom up approach)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(p), len(s)
        dp = [[False for i in range(N + 1)] for j in range(M+1)]
        dp[0][0] = True
        
        for i in range(1, M + 1):
            if dp[i-1][0] and p[i-1] == "*":
                dp[i][0] = True
            for j in range(1, N + 1):
                if p[i - 1] == "*":
                    if dp[i][j-1] or dp[i-1][j]:
                        dp[i][j] = True
                elif p[i-1] == "?" or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
       
        return dp[-1][-1]
        

# Backtracking (Top-down recursion with memorization approach)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def backtrack(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if p[j] == "*":
                # Try take nothing from s
                not_take = backtrack(i, j + 1)
                # Try take the character from s
                if i == len(s):
                    take = False
                else:
                    take = backtrack(i + 1, j)
                cache[(i,j)] = take or not_take
            elif i < len(s) and (p[j] == "?" or p[j] == s[i]):
                cache[(i,j)] = backtrack(i + 1, j + 1)
            else:
                cache[(i,j)] = False
            return cache[(i,j)]
        return backtrack(0,0)
