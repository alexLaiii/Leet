"""
This problem is similar to Leetcode 72: Edit Distance. In fact, Edit Distance is an extension
of this problem, so this one might feel a bit easier.

Idea:
We implement a 2D DP table where the rows represent characters from `text1`, and the columns
represent characters from `text2`. Each cell `dp[i][j]` will store the length of the longest
common subsequence (LCS) between `text1[0:i]` and `text2[0:j]`.

Example:
Let text1 = "abcde", text2 = "ace"
Then dp[4][3] represents the LCS of "abcd" and "ace", which is "ac", so dp[4][3] = 2.

Ultimately, dp[M][N] (the bottom-right cell) will contain the answer: the LCS length of 
the full text1 and text2.

Implementation:

1. Initialize the DP grid:
   - `dp[0][j] = 0` for all j: if text1 is empty, LCS is 0 regardless of text2.
   - `dp[i][0] = 0` for all i: if text2 is empty, LCS is 0 regardless of text1.

2. Fill the DP grid:
   - If `text1[i-1] == text2[j-1]`, then this character is part of the LCS:
     dp[i][j] = dp[i-1][j-1] + 1
   - If not equal, take the best between:
     - dp[i-1][j]: LCS if we exclude the current char from text1
     - dp[i][j-1]: LCS if we exclude the current char from text2
     So: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

   (Note: We do *not* consider dp[i-1][j-1] when characters don't match, since removing
    both characters can't improve the result — longer prefixes give longer LCS.)

3. After the loop, dp[M][N] (or dp[-1][-1]) contains the final LCS length.

Time Complexity: O(M * N)
Space Complexity: O(M * N)
---------------------------------------------------------------------------------

Thought Follow Up:
Why Two-Pointer Approach Doesn’t Work for Longest Common Subsequence (LCS)

The Longest Common Subsequence (LCS) problem might seem solvable using a 
two-pointer approach because of its similarity to other problems that involve 
comparing elements in two sequences. However, there are a few reasons why the 
two-pointer method isn't sufficient for the LCS problem:

1. Non-contiguous nature of the subsequence:
   In the LCS problem, the subsequence doesn't have to be contiguous 
   (i.e., next to each other) in the original strings, but they must 
   appear in the same relative order. So, even if you were able to find 
   a common subsequence with two pointers, it might not be the longest one.
   A two-pointer approach might miss out on a longer subsequence that's 
   spread out more widely across the strings.

2. Multiple Choices:
   At each step, you face a choice: 
   - If the current characters in both strings are the same, they might be part 
     of the LCS.
   - If they're not the same, you have to decide whether to move the pointer 
     in the first string or the second string.
   Choosing the optimal path is not obvious in linear time and requires exploring 
   both options.

3. Overlapping Subproblems:
   The LCS problem involves solving overlapping subproblems, i.e., you end up 
   solving the same subproblems multiple times. A two-pointer approach doesn't 
   efficiently handle these overlapping subproblems, which is why a more 
   sophisticated method like dynamic programming is needed.

Conclusion:
That's why for this problem, a dynamic programming approach is more suitable. 
It systematically breaks down the problem into smaller, overlapping subproblems, 
solves each subproblem just once, and uses the results of these smaller 
subproblems to construct an optimal solution to the problem.
"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match, so this character is part of the LCS.
                    # Add 1 to the result of the subproblem that excludes both characters.
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # dp[i-1][j] = the longest subsequence if I take text1[0:i-1] to text2[0:j]
                    # dp[i][j-1] = the longest subsequence if I take text1[0:i] to text2[0:j - 1]
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        
