"""Computes the reverse degree of a lowercase string.

  Each character is assigned its position in the reversed alphabet
  ('a' = 26, 'b' = 25, ..., 'z' = 1). That value is multiplied by the
  character's 1-indexed position in the string, and the products are
  summed.

  Args:
      s: A non-empty string of lowercase English letters,
          with 1 <= len(s) <= 1000.

  Returns:
      The sum over all positions i (1-indexed) of
      (reversed alphabet value of s[i]) * i.

  Examples:
      >>> Solution().reverseDegree("abc")
      148
      >>> Solution().reverseDegree("zaza")
      160

  Complexity:
      Time: O(n), where n = len(s), since each character is processed
          once with constant work.
      Space: O(1) auxiliary space. The generator expression yields
          one term at a time rather than building a list.
  """

class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += -(ord(s[i]) - ord("a") - 26) * (i + 1)
        
        return res
            
            
        
