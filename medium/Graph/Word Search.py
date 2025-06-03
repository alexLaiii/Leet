"""
Idea: 
DFS on graph traversal, check all 4 direction for each cell, the dfs recursion callonly happened iff the character of that cell is same as the current character we want to find, 
otherwise, it will return false immediately and the further traversal will not happened on this route.
If the char in the cell matched the current character we looking for, we do the recursive call, until it wont't match (step route), or the word ends (curr_len >= len(word), which means 
the valid path exists.


"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])


        visited = set()
        def dfs(r,c, curr_len):
            if curr_len >= len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[curr_len]:
                return False

            visited.add((r,c))
        
            south = dfs(r + 1, c, curr_len + 1)
            north = dfs(r - 1, c, curr_len + 1)
            east = dfs(r, c + 1, curr_len + 1)
            west = dfs(r, c - 1, curr_len + 1)
            visited.remove((r,c))
            # 1 true makes all true
            return south or north or east or west
      
    
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                # if board[i][j] == word[0]:
                if dfs(i,j,0):
                    return True
                    
        return False   
