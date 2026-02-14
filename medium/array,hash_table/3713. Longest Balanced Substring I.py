  """
  Finds the length of the longest substring in which all characters appear
  the same number of times (i.e., a balanced substring).

  The algorithm checks every possible substring starting at each index.
  For each substring, it maintains a frequency map using a defaultdict
  and verifies whether all character counts are equal after each extension.
  If the current substring is balanced, the maximum length is updated.

  A substring is considered balanced if:
      all values in the frequency dictionary are identical.

  Parameters:
  -----------
  s : str
      The input string.

  Returns:
  --------
  int
      The maximum length of a balanced substring.

  Time Complexity:
  ----------------
  O(n^3) in the worst case:
      - O(n^2) substrings
      - O(n) check of frequency values for each substring

  Space Complexity:
  -----------------
  O(n) for the frequency dictionary in the worst case.

  Example:
  --------
  s = "aabbcc"
  Output = 6   # entire string is balanced

  s = "aaabb"
  Output = 4   # "aabb" is balanced
  """

class Solution:
    def longestBalanced(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            count = defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]] += 1
                isBalance = True
                for c in count.values():
                    if c != count[s[j]]:
                        isBalance = False
                        break
                if isBalance:
               
                    res = max(res, j - i + 1)
        return res

        
