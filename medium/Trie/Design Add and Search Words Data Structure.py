"""
Idea:
This data structure is almost identical to LeetCode 208 (Implement Trie).
The difference is in the `search` function — it must handle the wildcard character '.'.

Implementation:

addWord(self, word):
- Standard Trie insertion: for each character in the word,
  we traverse the Trie and create nodes as needed.
- At the end, mark the final node as `isEnd = True`.
(See Problem 208 if a refresher is needed.)

search(self, word):
We use a helper function `dfs(depth, curr)` to perform depth-first traversal through the Trie.

Parameters:
- `depth`: the current index in the search word (i.e., word[depth] is the current character)
- `curr`: the current TrieNode we're examining

Logic:
1. **Base Case**:  
   If `depth == len(word)`, we’ve reached the end of the word.
   - Return `curr.isEnd`. If True, this word exists in the Trie. If False, it's only a prefix.

2. **Wildcard Case (`.`)**:
   - The `.` character means we must try **all possible children** of the current node.
   - For each non-null child in `curr.child`, recursively call `dfs(depth + 1, child)`.
   - If any call returns True, short-circuit and return True.
   - If none work, return False.

3. **Normal Character Case (`'a'`–`'z'`)**:
   - If the current character doesn’t exist in `curr.child`, return False.
   - Otherwise, recursively call `dfs(depth + 1, curr.child[index])` where `index = ord(word[depth]) - ord('a')`.

This approach works efficiently because:
- The DFS only branches at most 2 times (due to the problem constraint).
- The Trie structure guarantees fast traversal.

Overall, the wildcard-enabled search is handled cleanly with recursion, and the rest behaves like a standard Trie.
"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        curr = self.root
        for chr in word:
            if chr not in curr.child:
                curr.child[chr] = TrieNode()
            curr = curr.child[chr]
        curr.isEnd = True
        

    def search(self, word):
        def dfs(depth, curr):
            if depth == len(word):
                return curr.isEnd
            if word[depth] == ".":
                for key in curr.child:
                    if dfs(depth + 1, curr.child[key]):
                        return True
                return False
            elif word[depth] not in curr.child:
                return False
            else:
                return dfs(depth + 1, curr.child[word[depth]])
                
        return dfs(0, self.root)
            
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
Solution 2: fixed array approach
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        curr = self.root
        for chr in word:
            if not curr.child[ord(chr) - ord("a")]:
                curr.child[ord(chr) - ord("a")] = TrieNode()
            curr = curr.child[ord(chr) - ord("a")]
        curr.isEnd = True
        

    def search(self, word):
        def dfs(depth, curr):
            if depth == len(word):
                return curr.isEnd
            if word[depth] == ".":
                for c in curr.child:
                    if c and dfs(depth + 1, c):
                        return True
                return False
            elif not curr.child[ord(word[depth]) - ord("a")]:
                return False
            else:
                return dfs(depth + 1, curr.child[ord(word[depth]) - ord("a")])
        return dfs(0, self.root)
                        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
