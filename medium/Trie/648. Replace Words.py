"""
LeetCode 648 — Replace Words (Trie)

Build a trie of all dictionary words. For each word in the sentence, walk the trie
character by character and stop as soon as:
  (1) the next character path doesn’t exist, or
  (2) we hit a terminal node that stores a root (curr.isWord).
If (2) happens, replace the word with that stored root (guaranteed shortest
prefix); otherwise leave the word unchanged.

Time Complexity:
  Build:  O(sum of lengths of dictionary)
  Replace: O(sum of lengths of sentence words)
Space Complexity: O(sum of lengths of dictionary)
"""

class TrieNode:
    def __init__(self):
        self.node = {}
        self.isWord = None
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for w in dictionary:
            curr = root
            for c in w:
                if c not in curr.node:
                    curr.node[c] = TrieNode()
                curr = curr.node[c]
            curr.isWord = w

        sentence = sentence.split()

        res = []
        for w in sentence:

            curr = root
            for c in w:
                if c not in curr.node or curr.isWord:
                    break
                curr = curr.node[c]

            if curr.isWord:
                res.append(curr.isWord)
            else:
                res.append(w)
              

        return " ".join(res)
