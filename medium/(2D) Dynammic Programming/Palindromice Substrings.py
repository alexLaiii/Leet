

# Brute Force Expand-Around-Center Approach:
# - A palindrome can be either odd-length (like "aba") or even-length (like "aa")
# - Odd-length palindromes have a single character at the center
# - Even-length palindromes have a center between two characters
# - For each character in the string, we:
# - Expand around it to count all odd-length palindromes
# - Expand between it and the previous character to count even-length palindromes
"""
Why Expand Around Center Is Optimal for Palindrome Detection:

- A palindrome is defined by symmetry around its center.
  Therefore, it's more natural and efficient to expand outward from each center 
  (either a character or a gap between characters) instead of checking substrings from both ends.

- Expanding from the center allows early termination:
  As soon as s[left] != s[right], expansion stops immediately — no need to scan to the middle.

- In contrast, checking from the outer edges (i.e., brute-force substring validation) 
  requires full traversal toward the center even if the first or second characters already break symmetry.

- There are only 2n - 1 possible centers in a string of length n,
  while the number of substrings is n(n + 1)/2.
  This means center-expansion considers far fewer candidates than edge-based brute-force.

- Overall, expanding from the center is both structure-aware and computationally efficient 
  for finding or counting palindromic substrings.

"""
# Time Complexity: O(n^2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [1 for i in range(len(s))]
        res = 0
        for center in range(len(s)):
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # check even one
            l = center - 1
            r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
    
        return res
        
