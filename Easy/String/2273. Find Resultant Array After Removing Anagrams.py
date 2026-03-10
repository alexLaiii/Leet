"""
Removes consecutive words that are anagrams of the previous kept word.

The algorithm maintains a stack containing the resultant array of words.
For each new word, it compares it with the last word kept in the stack.
Two words are anagrams if their character frequencies are identical.

To check this, a frequency difference map is constructed:
  - increment counts for characters in the last word in the stack
  - decrement counts for characters in the current word
If all counts return to zero, the two words are anagrams and the current
word is skipped. Otherwise, the word is appended to the stack.

Parameters
----------
words : List[str]
  A list of lowercase strings.

Returns
-------
List[str]
  The resultant array after removing words that are anagrams of the
  previous word.

Time Complexity
---------------
O(n * k)
n = number of words
k = average length of each word

Each comparison builds a frequency map of at most k characters.

Space Complexity
----------------
O(k)
for the frequency map used during each comparison.
"""

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
          return []
        stack = [words[0]]
    
        for i in range(1, len(words)):
            countMap = defaultdict(int)
            for ch in stack[-1]:
                countMap[ch] += 1
            for c in words[i]:
                countMap[c] -= 1
            for val in countMap.values():
                if val != 0:
                    stack.append(words[i])
                    break
        return stack
        
