  """
  Return the length of the last word in the string s.
  A word is defined as a maximal substring consisting of non-space characters.
  The algorithm scans from the end: first skips trailing spaces,
  then counts the characters of the last word.

  Time: O(n)
  Space: O(1)
  """

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        res = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            res += 1
        return res
            
