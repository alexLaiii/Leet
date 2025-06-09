"""
This problem is exactly what the title says: implementing a Trie (prefix tree) from scratch.

Idea:
We create a TrieNode class, where:
- `self.child` is a hashmap (dictionary) that maps:
    - keys: characters leading to child nodes
    - values: TrieNode objects representing the next character in the word
- `self.isEnd` indicates whether the current node marks the end of a valid word (True/False)

In the Trie class:
- `self.root` is an empty TrieNode.
- Each level in the tree represents the next character in a word.
- Shared prefixes are stored in the same path until words diverge.

Example:
Consider inserting: "apple", "app", and "appstore"

root.child = { 'a': TrieNode() }
 └── 'p': TrieNode()
     └── 'p': TrieNode() → isEnd = True  (end of "app")
         ├── 'l': TrieNode()
         │    └── 'e': TrieNode() → isEnd = True  (end of "apple")
         └── 's': TrieNode()
              └── 't': TrieNode()
                   └── 'o': TrieNode()
                        └── 'r': TrieNode()
                             └── 'e': TrieNode() → isEnd = True  (end of "appstore")

Notice how all three words share the prefix path `'a' -> 'p' -> 'p'`. New branches are only created when the characters diverge.

This is how a Trie efficiently stores words with shared prefixes.

Function Explanations:

`search(self, word)`:
We traverse the Trie one character at a time.  
- If at any point a character is missing in the current node’s children, return False.
- Once all characters are matched, return `curr.isEnd`.  
  - If `isEnd` is False, it means the word is only a prefix, not a complete word in the Trie.

`startsWith(self, prefix)`:
This works similarly to `search`, but with a key difference:
- After successfully matching all characters in the prefix, we **always return True**, regardless of `isEnd`.
  - Why? Because the prefix is considered valid whether it is the start of a longer word, a full word, or both.
  - Even a complete word is its own prefix.

"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for character in word:
            if character not in curr.child:
                curr.child[character] = TrieNode()
            curr = curr.child[character]
        curr.isEnd = True
        
        

    def search(self, word):
        curr = self.root
        for character in word:
            if character not in curr.child:
                return False
            curr = curr.child[character]
        return curr.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for character in prefix:
            if character not in curr.child:
                return False
            curr = curr.child[character]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



"""
Solution 2: Fixed Array approach
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word):
        curr = self.root
        for chr in word:
            if not curr.child[ord(chr) - ord("a")]:
                curr.child[ord(chr) - ord("a")] = TrieNode()
            curr = curr.child[ord(chr) - ord("a")]
        curr.isEnd = True     

    def search(self, word):
        curr = self.root
        for chr in word:
            if curr.child[ord(chr) - ord("a")] == None:
                return False
            curr = curr.child[ord(chr) - ord("a")]
        return curr.isEnd
        

    def startsWith(self, prefix):
        curr = self.root
        for chr in prefix:
            if curr.child[ord(chr) - ord("a")] == None:
                return False
            curr = curr.child[ord(chr) - ord("a")]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
