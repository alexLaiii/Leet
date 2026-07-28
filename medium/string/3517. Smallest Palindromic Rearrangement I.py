"""
The input string is guaranteed to be a palindrome, which means every
character (except the middle character in an odd-length string) appears
in symmetric pairs. Therefore, the first half of the string contains all
the information needed to determine the characters that will appear in
the left half of the lexicographically smallest palindromic rearrangement.

We count the frequency of each character in the first half of the string
and reconstruct the left half in alphabetical order. Sorting the left
half in this manner guarantees the resulting palindrome is lexicographically
smallest. The right half is simply the reverse of the left half, while the
middle character (if it exists) remains unchanged.

Time Complexity: O(n)
    - We traverse the first half of the string once and iterate over the
      26 lowercase letters to construct the left half.

Space Complexity: O(n)
    - O(1) auxiliary space is used for the frequency array (size 26), and
      O(n) space is required for constructing the output string.
"""

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        case_freq = [0] * 26
        n = len(s)
        half = n // 2
        for i in range(half):
            val = ord(s[i]) - ord("a")
            case_freq[val] += 1
        
        new_half = []
        for i in range(26):
            for j in range(case_freq[i]):
                new_half.append(chr(i + ord("a")))

        left = "".join(new_half)
        if n % 2 == 1:
            return left + s[half] + left[::-1]
        return  left + left[::-1]
