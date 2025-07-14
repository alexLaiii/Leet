"""
Leetcode 745 – Prefix and Suffix Search (Custom Trie Implementation)

This solution builds a custom Trie where each inserted key has the form: suffix + '#' + word. (Very important)
Such that we can search the suffix in before word[:#], search the prefix in word[#:], If both success, then the word is in Trie and can be added to candidate result.

For each word, we insert all suffixes combined with the full word to enable efficient
lookup based on suffix matching.

Key Ideas:
- We store all strings of the form: word[i:] + '#' + word, for i in 0 to len(word).
  This allows us to later locate all words ending with a given suffix.
- During query f(prefix, suffix), we:
    1. Traverse the Trie using the suffix path and preserve the node (pointer).
    2. From that pointer node, we recursively search all words that also match the given prefix.
- The original word is reconstructed by slicing off the prefix (suffix + '#') when needed.

Helper Functions:
- addWord(word): inserts a key into the Trie character by character.
- searchSuffix(suff): traverses the Trie using the suffix and returns the pointer node (if it exists).
- searchPrefix(pointer, prefix): from a given pointer node, collects all words with the given prefix.
- getAll(pointer, res): recursively collects all valid words from a subtree (used inside searchPrefix).

The final answer is the word with the highest index (stored in self.wordsidx) that matches both
prefix and suffix constraints.

Time Complexity:
- Preprocessing (__init__): O(n * k^2), where k = word length
- Query f(prefix, suffix): Worst case O(total matching suffix subtree + prefix matching)

Note:
This solution is correct and manually manages Trie pointer state, but is more complex than
necessary. A flattened Trie or hash map solution is shorter and more efficient in practice.
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
        
    def searchSuffix(self, suff):
        curr = self.root
        for c in suff:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        if "#" in curr.children:
            return curr.children["#"]
        return None
    
    def searchPrefix(pointer, pre):
        curr = pointer
        for c in pre:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        res = []
        root = curr
        if curr.word:
            res.append(curr.word)
        res = Trie.getAll(root, [])
        return res

    def getAll(pointer, res):
        if pointer.word:
            res.append(pointer.word)
        for every in pointer.children:
            res = Trie.getAll(pointer.children[every], res)
        return res

    
class WordFilter:

    def __init__(self, words: List[str]):
        self.wordsidx = {}
        self.root = Trie()
        for i in range(len(words)):
            self.wordsidx[words[i]] = i
            word = words[i]
            for j in range(len(word) + 1):
                suffPre = word[j:] + "#" + word
                self.root.addWord(suffPre)


    def f(self, pref: str, suff: str) -> int:
        pointer = self.root.searchSuffix(suff)
        if pointer:
            ans = Trie.searchPrefix(pointer, pref)
        else:
            return -1
        res = -1
        for word in ans:
            res = self.wordsidx[word[len(suff) + 1:]] if self.wordsidx[word[len(suff) + 1:]] > res else res
        
        return res



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
