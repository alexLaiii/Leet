"""
Determines if the input string `s` matches the pattern `p`, where:
- `.` matches any single character
- `*` matches zero or more of the **preceding** element

Approach:
This solution uses bottom-up dynamic programming (DP) with a 2D table `dp` where:
    dp[i][j] = True means s[:i] matches p[:j]

DP Table Size:
- (M+1) x (N+1), where M = len(s), N = len(p)
- dp[0][0] = True (empty string matches empty pattern)

Initialization:
- dp[0][j] is specially initialized to handle patterns like "a*", "a*b*", etc.
  If p[j-1] == '*', then dp[0][j] = dp[0][j-2] — meaning we treat "x*" as matching 0 occurrence
- dp[i][0] is always False because any characters can't match to a empty pattern

DP Transition Rules:
1. If p[j-1] == '*':
    - Case 1: Zero occurrence of p[j-2] → dp[i][j] = dp[i][j-2]
    - Case 2: One or more occurrences of p[j-2]:
        - Only valid if p[j-2] matches s[i-1] (or is '.')
        - Then dp[i][j] = dp[i-1][j]

2. If p[j-1] is a normal char or '.':
    - If it matches s[i-1], then dp[i][j] = dp[i-1][j-1]

Key Concept — Why `dp[i][j-1]` and `dp[i-1][j-1]` are not used for '*':
- `'*'` is a **modifier**, not a standalone matcher
- You must always consider it in combination with the preceding character (p[j-2])
- `dp[i][j-2]`: Zero occurrence of the preceding char
- `dp[i-1][j]`: Reuse the `'*'` to match multiple characters
- Using `dp[i][j-1]` would assume '*' can match like a character, which is incorrect

Example:
    s = "aab", p = "c*a*b"
    - 'c*' matches zero c
    - 'a*' matches "aa"
    - 'b' matches 'b'
    → dp[3][5] = True

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        dp = [[False for j in range(N + 1)] for i in range(M + 1)]
        dp[0][0] = True
        for j in range(1, N + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
            
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if p[j-1] == "*":
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif p[j-2] == "." or s[i-1] == p[j-2]:
                        dp[i][j] = dp[i-1][j]

                elif p[j-1] == "." or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[M][N]
                

