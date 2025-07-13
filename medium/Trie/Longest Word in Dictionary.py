
"""
Trie-based solution is natural for this problem.

🧠 Idea:
We only add a word to the Trie if its immediate prefix also exists in the Trie.
That is, for the word "leetcode" to be valid, "leetcod" must already exist.

Therefore:
- We sort the words by length first — this guarantees all possible prefixes are processed before longer words.
- If two words are the same length, we sort them lexicographically — since the problem requires the smallest lexicographical result in case of ties.

🛠️ Implementation:
1. Sort the words using: `words.sort(key=lambda w: (len(w), w))`
   - Ensures we process prefixes first
2. Initialize a Trie.
3. For each word:
   - If the word has length 1, we assume its prefix `""` is always valid, so we add it to the Trie.
   - If the word has length > 1:
     - We check whether its prefix `word[:-1]` exists in the Trie using `root.searchPrefix(word, len(word) - 1)`
     - If it exists, we add the word to the Trie.
       - If this word is longer than the current best result, update the result and length.

4. At the end, return the result.

🧮 Time Complexity:
- Sorting: O(n log n)
- Trie building and prefix checking: O(n * k)
  where:
    - n = number of words
    - k = average length of a word

Total: O(n log n + n * k)
"""



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word
    
    def searchPrefix(self, word, longest):
        curr = self.root
        for c in word[:longest]:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

                
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda w: (len(w), w))
        root = Trie()
        longest = 1
        res = words[0] if len(words[0]) == 1 else ""

        for word in words:
            if len(word) == 1:
                root.addWord(word)
            elif root.searchPrefix(word, len(word) - 1):
                root.addWord(word)
                if len(word) > longest:
                    res = word
                    longest = len(word)

        return res
        
