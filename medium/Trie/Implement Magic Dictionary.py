"""
MagicDictionary - Trie-based implementation for Leetcode 676

This class supports building a dictionary of words and searching to check whether 
modifying exactly one character in a given word results in a valid word from the dictionary.

Core Idea:
-----------
- We use a Trie (prefix tree) to store all dictionary words. Each TrieNode contains:
    - 'children': a dictionary mapping characters to the next TrieNode
    - 'isEnd': a boolean indicating whether a complete word ends at this node

- To build the dictionary, we insert each word character by character into the Trie.
  When the end of the word is reached, we mark the final node's `isEnd = True`.

- For searching, we perform DFS (depth-first search) through the Trie.
  We allow **exactly one character** to be different between the search word and 
  the dictionary words.

Search Logic:
--------------
- At each index of the search word, we explore:
    1. The **no-replacement path**: If the current character exists in the current node’s children,
       we proceed without using the replacement.
    2. The **replacement path**: If we still have one replacement allowed, we try all other
       characters in the current node’s children that differ from the current character.

- The recursion continues until we reach the end of the word.
  We return True only if:
    - We have used **exactly one** character replacement (i.e., replace == 0),
    - And we are at a Trie node where `isEnd == True`.

- If neither the exact match nor a valid replacement leads to success, we return False.

This method ensures:
- The modified word has the same length as the original.
- Only one character is changed.
- The resulting word exists in the original dictionary.

This Trie + DFS strategy is both efficient and scalable for repeated queries.
"""



class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def buildDict(self, dictionary: List[str]) -> None:
       
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isEnd = True
        

    def search(self, searchWord: str) -> bool:
        def dfs(idx, node, replace):
            if idx == len(searchWord):
                return node.isEnd and replace == 0
           
            if searchWord[idx] in node.children:
                no_replace = dfs(idx + 1, node.children[searchWord[idx]], replace)
                if no_replace:
                    return True
            if replace == 1:
                for next_n in node.children:
                    if next_n != searchWord[idx] and dfs(idx + 1, node.children[next_n], replace - 1):
                        return True
            return False

        return dfs(0, self.root, 1)
            
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
