"""
Reverse only the vowels in a string, leaving all other characters
in their original positions.

Uses a two-pointer approach: `head` scans from the start, `tail`
scans from the end. A pointer only stops advancing once it lands
on a vowel, at which point it waits for the other pointer to also
find a vowel so they can be swapped.

Args:
    s: Input string (may contain letters, digits, symbols, etc.)

Returns:
    A new string with vowel positions reversed.

Time:  O(n) - each pointer traverses the string at most once
Space: O(n) - due to converting the immutable string into a list

Example:
    >>> Solution().reverseVowels("hello")
    'holle'
    >>> Solution().reverseVowels("leetcode")
    'leotcede'
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        head, tail = 0, len(s) - 1
        s = list(s)
        while head < tail:
            head_char = s[head]
            tail_char = s[tail]
            if head_char in vowels and tail_char in vowels:
                s[head], s[tail] = s[tail], s[head]
                head += 1
                tail -= 1
            elif head_char in vowels:
                tail -= 1
            elif tail_char in vowels:
                head += 1
            else:
                head += 1
                tail -= 1
        return "".join(s)
        
