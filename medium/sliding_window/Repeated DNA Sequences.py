  """
  Problem:
  Given a DNA string `s` composed of characters 'A', 'C', 'G', and 'T',
  return all the 10-letter-long sequences (substrings) that occur more than once in the string.
  
  Approach:
  - Use a sliding window of length 10 to extract all possible 10-character substrings from `s`.
  - Use a set `seen` to record all 10-letter sequences we've already encountered.
  - Use another set `resSet` to store substrings that appear more than once.
    This ensures we avoid duplicate results and only return each repeated sequence once.
  
  Steps:
  1. Early exit: if the string length is <= 10, no 10-letter sequence can repeat → return [].
  2. Initialize two sets: `seen` for tracking all 10-letter sequences, and `resSet` for those that repeat.
  3. Slide a window of size 10 across `s`:
     - For each index window `s[l:r+1]` where `r` starts at 9 (so the substring has length 10):
       - If the substring has already been seen, add it to `resSet`.
       - Otherwise, add it to the `seen` set.
       - Move the window forward by incrementing `l`.
  4. Return a list of all repeated sequences collected in `resSet`.

  Time Complexity:
  - O(n), where n is the length of `s`, because each 10-character substring is checked once.
  
  Space Complexity:
  - O(n), due to storage of substrings in the `seen` and `resSet` sets.

  Example:
  Input: "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  Output: ["AAAAACCCCC", "CCCCCAAAAA"]
  """


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        seen = set()
        resSet = set()

        l = 0
        for r in range(9, len(s)):
            if s[l:r + 1] in seen:
                resSet.add(s[l:r + 1])
            else:
                seen.add(s[l:r + 1])
            l += 1
        return list(resSet)
