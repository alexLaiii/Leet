    """
    Why use a Trie?

    Take a look at this example:

    board = 
    [["o","a","a","n"],
     ["e","t","a","e"],
     ["i","h","k","r"],
     ["i","f","l","v"]]

    words = ["oath", "pea", "eat", "rain"]

    Notice that for each cell in the board, you need to check:
    "Is the character in this cell equal to the first character of any word in 'words'?"
    This is an O(len(words)) operation per cell, so the total time just to decide whether to search
    is O(m * n * len(words)).

    Now consider a worse case:

    board =
    [["a","n","t"],
     ["a","a","n"],
     ["n","t","t"]]

    words = ["anti", "ant", "anta", "ants"]

    Assume you are in the first cell of the grid ('a'):
    - First, you search for "anti" → call DFS → traverse the entire prefix path.
    - Then search for "ant" → call DFS → same path again.
    - Then "anta" → same path again.
    - Then "ants" → again the same prefix path.

    You are redundantly traversing the same path four times.

    But if you use a Trie:
    - You store all words as a prefix tree.
    - From the first cell 'a', you do DFS only once.
    - The DFS follows the prefix "a" → "n" → "t" just once, and from there explores the extensions
      to match "anti", "ant", "anta", and "ants" in one go.
    - You save all the duplicated work by traversing shared prefixes only once.

    In summary:
    - Without a Trie: repeated DFS calls for each word that shares a prefix = redundant work.
    - With a Trie: one DFS explores all words with shared prefixes together = efficient.
    
    ----------------------------------------------------------------------------------------------------------------------------

    IMPLEMENTATION PARTS:
    
    We define our own "TrieNode" class to represent each node in the Trie.
    We don’t need to define a full Trie class — instead,
    we create a single-use Trie using: root = TrieNode()

    Since we use the Trie to represent all the words in the input list 'words',
    we insert all words into the Trie:

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

    In this Trie implementation, we store the entire word in the node that represents
    the last character, using 'TrieNode.word'. This is initialized to None.
    So if 'curr.word' is not None, then that TrieNode represents a complete word.

    (The more common approach is to use 'TrieNode.isEnd = True', but in this problem,
     storing the full word helps avoid reconstructing it manually from path history.)

    dfs(r, c, curr):
        Perform DFS on the grid and simultaneously walk through the Trie.
        If board[r][c] is not in curr.children, this grid path cannot continue —
        that prefix doesn’t exist in the Trie.
        If board[r][c] is in curr.children, then the path is valid, and we continue DFS.
        If curr.children[board[r][c]].word is not None, then a full word is found.
        Append it to the result, and set 'curr.children[board[r][c]].word = None'
        to prevent duplicates. (Later DFS paths may lead to the same word again from a different
        grid path, so we must disable the word once found.)

    Outer for loop:
        We perform DFS starting from every cell in the board.

    Finally, return 'res', which correctly stores all words from the board that exist in the Trie.
    """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
   

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Insert the words to Trie here
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

        
        visited = set()
        M, N = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = []
        def dfs(r,c, curr):
            if r < 0 or c < 0 or r >= M or c >= N or (r,c) in visited or board[r][c] not in curr.children:
                return 
            
            if curr.children[board[r][c]].word:
                res.append(curr.children[board[r][c]].word)
                curr.children[board[r][c]].word = None
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr, c+dc, curr.children[board[r][c]])
            visited.remove((r,c))
         

        for i in range(M):
            for j in range(N):
                if board[i][j] in root.children:
                    dfs(i,j, root)
                if len(res) == len(words):
                    break
          
        return res
 
