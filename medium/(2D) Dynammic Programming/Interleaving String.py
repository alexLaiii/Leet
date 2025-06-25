"""
Idea:
An Interleaving String checks whether a string `s3` can be formed by interleaving **all characters** from `s1` and `s2` while preserving their original character orders.

Why the 3-pointer approach doesn’t work:
At first, I tried using three pointers on `s1`, `s2`, and `s3`. But problems arise quickly.  
Consider this example:
    s1 = "aabc"  
    s2 = "abad"  
    s3 = "aabadabc"

At various decision points, you may have multiple valid-looking choices (e.g., pick from `s1` or `s2`),  
but only one **specific interleaving path** will work to fully reach the end of `s3`.

So how do we decide which path is correct at each step?

That's why we use **Dynamic Programming** — to cache the results of previous decisions  
and only continue building if the previous subpath was valid.

---

DP Definition:
Each `dp[i][j]` means:
> Can we form the prefix `s3[:i + j]` using the first `i` characters of `s2` and first `j` characters of `s1`?

The current state depends on:
1. Taking from `s1`:  
   If `dp[i][j - 1]` is True and `s1[j - 1] == s3[i + j - 1]`, then `dp[i][j] = True`
2. Taking from `s2`:  
   If `dp[i - 1][j]` is True and `s2[i - 1] == s3[i + j - 1]`, then `dp[i][j] = True`

If neither option is valid, this path is **invalid**, and no further build is possible from here — the path is **closed**.

---

Time Complexity: O(m * n), where m = len(s2), n = len(s1) — full DP grid traversal  
Space Complexity(2D): O(m * n) — DP grid of size (m+1) × (n+1)
Space Complexity(1D): O(n) - 1D DP with n = len(s2)
"""
# 2D solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1, lenS2 = len(s1),len(s2)
        if lenS1 + lenS2 != len(s3):
            return False
        dp= [[False for j in range(lenS1 + 1)] for i in range(lenS2 + 1)]
        dp[0][0] = True
        for i in range(lenS2 + 1):
            for j in range(lenS1 + 1):
                # Take from s1
                if j > 0 and dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                # Take from s2
                if i > 0 and dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        return dp[lenS2][lenS1]


# Optimize 1D solution (Same Idea, optimize to only keep track of the previous row)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        M, N = len(s1), len(s2)
        dp = [False for i in range(N + 1)]
        dp[0] = True

        # Base case: fill in first row, only using s2
        for j in range(1, N + 1):
            if s2[j-1] == s3[j-1] and dp[j-1]:
                dp[j] = True
        
        for i in range(1, M + 1):
            new_row = [False for k in range(N + 1)]
            # First column: only using s1
            if s1[i - 1] == s3[i - 1] and dp[0]:
                new_row[0] = True
            for j in range(1, N + 1):
                if s1[i - 1] == s3[i + j -1] and dp[j]:
                    new_row[j] = True
                if s2[j - 1] == s3[i + j -1] and new_row[j-1]:
                    new_row[j] = True
            dp = new_row
        return dp[-1]
        
        



                
            

                    
        
        
        
