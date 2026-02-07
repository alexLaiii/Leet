"""
Return the minimum number of deletions needed to make s "balanced",
meaning no 'b' appears before an 'a' (i.e., the string can be written
as some number of 'a's followed by some number of 'b's).

Approach:
Consider a split index i. We want all characters left of i to be 'a'
(so delete any 'b' on the left), and all characters right of i to be 'b'
(so delete any 'a' on the right). For each i:
  deletions = (# of 'b' in s[0:i]) + (# of 'a' in s[i+1:n])
Precompute:
  - b_before[i]: number of 'b' in prefix s[0:i]
  - a_after[i]: number of 'a' in suffix s[i+1:n]
Then take the minimum over all i.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_before = [0]
        a_after = [-1] * len(s)
        a_after[-1] = 0
        
        for i in range(1, len(s)):
            if s[i - 1] == "b":
                b_before.append(b_before[i - 1] + 1)
            else:
                b_before.append(b_before[i - 1])
        for j in range(len(s) - 2, -1, -1):
            if s[j + 1] == "a":
                a_after[j] = a_after[j + 1] + 1
            else:
                a_after[j] = a_after[j + 1]
        res = float("inf")
        for i in range(len(s)):
            res = min(res, b_before[i] + a_after[i])
        return res
        
