

# Brute Force Expand-Around-Center Approach:
# - A palindrome can be either odd-length (like "aba") or even-length (like "aa")
# - Odd-length palindromes have a single character at the center
# - Even-length palindromes have a center between two characters
# - For each character in the string, we:
# - Expand around it to count all odd-length palindromes
# - Expand between it and the previous character to count even-length palindromes

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
        
