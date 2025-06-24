"""
This problem uses the same concept as "1143. Longest Common Subsequence" and "72. Edit Distance", with tweaks on how we compute the DP grid.

**Idea:**  
We use each DP cell to store the number of **distinct subsequences** of the substring of "s" that can form the substring of "t".  
The row represents "s", and the column represents "t".  
Example:  
s = "babgbag", t = "bag"  
dp[6][2] = 4, since s[0:7] has 4 subsequences that match t[0:3] ("bag").

**Base cases:**  
Since we are counting how many ways `s` can form `t`:
- If `s` and `t` are both empty (""), there is 1 valid subsequence — the empty subsequence.
- If `s` is empty and `t` is not, there are 0 subsequences — an empty string can't form any non-empty target.
- If `t` is empty and `s` is not, there is always 1 valid subsequence — delete everything from `s`.

So we initialize our DP grid:
- `dp[0][0] = 1`  — both strings are empty
- `dp[i][0] = 1`  — `t` is empty
- `dp[0][j] = 0`  — `s` is empty

**Logic to fill the DP grid:**  
Let’s look at an example to make the recurrence logic clearer.

---

**Case 1: characters match (`s[i-1] == t[j-1]`)**

Suppose we're filling `dp[i][j]`, which represents `s[0:i]` and `t[0:j]`.  
Example:  
s = "babgbag", t = "bag"

If the last characters match (i.e., `s[i-1] == t[j-1]`), two things happen:
1. Any way of forming `t[0:j-1]` from `s[0:i-1]` can be extended with this matching character → contributes `dp[i-1][j-1]`.
2. All previous subsequences that already formed `t[0:j]` without using the new character in `s` → contributes `dp[i-1][j]`.

So:
```dp[i][j] = dp[i-1][j-1] + dp[i-1][j]```

---

**Case 2: characters do not match (`s[i-1] != t[j-1]`)**

The newly added character in `s` doesn't help us match `t`. So we just skip it:
```dp[i][j] = dp[i-1][j]```

This means the count of subsequences stays the same as it was before adding the new character.

---

**Final Result:**  
After filling the entire grid, the value at `dp[M][N]` (where `M = len(s)` and `N = len(t)`) gives the number of distinct subsequences of `s` that equal `t`.

**Time Complexity:** `O(m * n)` — for filling the entire grid  
**Space Complexity:** `O(m * n)` — due to the 2D grid  
(Can be optimized to `O(n)` using a rolling 1D array.)
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [[0 for j in range(N + 1)] for i in range(M+1)]
        for i in range(M + 1):
            dp[i][0] = 1

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]    

# 1D optimization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [0 for j in range(N + 1)]
        dp[0] = 1

        for i in range(1, M + 1):
            new_row = [0 for j in range(N + 1)]
            new_row[0] = 1
            for j in range(1, N + 1):
                if s[i - 1] == t[j - 1]:
                    new_row[j] = dp[j-1] + dp[j]
                else:
                    new_row[j] = dp[j]
            dp = new_row
        return dp[-1]  
