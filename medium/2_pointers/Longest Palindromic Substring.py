"""
This problem uses the exact same approach as "647. Palindromic Substrings".

The only difference is:
- In 647, we count a palindrome each time we find one.
- In this problem, we compare the currently found palindrome to the previous longest one and update the result if it's longer.

Please refer to the 647 documentation if you forget the detailed implementation.

Time Complexity: O(n^2)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for center in range(len(s)):
            l,r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # (r - 1) - (l + 1) + 1 is the largest palindrome when the center is the center character
            res = res if len(res) > (r -1) - (l + 1) + 1 else s[l + 1: r]
            l = center - 1
            r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            res = res if len(res) > (r -1) - (l + 1) + 1 else s[l + 1: r]
        return res
