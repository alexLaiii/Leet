"""
Count how many English letters appear in both lowercase and uppercase form.

Idea:
- In ASCII/Unicode, the lowercase and uppercase version of the same
  English letter differ by exactly 32.
      ord('a') - ord('A') == 32
- Store the ASCII value of each character we have already seen.
- When we see a new character, check whether its opposite case has
  already appeared:
      ASCII_c + 32  -> possible lowercase version
      ASCII_c - 32  -> possible uppercase version
- If either opposite-case value is already in seen, then this letter
  is special, so increment the result.
- If the exact same character was already seen before, skip it to avoid
  counting the same letter multiple times.

Example:
    word = "aaAbcBC"

    seen 'a'
    skip second 'a'
    see 'A', opposite case 'a' already exists -> res += 1
    see 'b'
    see 'c'
    see 'B', opposite case 'b' already exists -> res += 1
    see 'C', opposite case 'c' already exists -> res += 1

    return 3

Time Complexity:
    O(n), where n is the length of word.

Space Complexity:
    O(1), because seen can contain at most 52 English letters.
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        seen = set()
        res = 0
        for c in word:
            ASCII_c = ord(c)
            if ASCII_c in seen:
                continue
            if ASCII_c + 32 in seen:
                res += 1
            elif ASCII_c - 32 in seen:
                res += 1
            seen.add(ASCII_c)
        return res
        
