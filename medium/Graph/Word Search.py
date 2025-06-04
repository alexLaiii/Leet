"""
Idea:
We perform DFS-based graph traversal on a 2D grid. From each cell, we attempt to match the current character of the target word.
- If the character at the cell matches the current character (`word[curr_len]`), we recursively explore all four directions (up, down, left, right).
- If it doesn’t match, or if the cell is out of bounds or already visited, we return False immediately — pruning that path.

The recursion continues until either:
- We reach `curr_len == len(word)`, which means we've successfully matched the entire word and found a valid path.
- All recursive paths return False (no valid match), so we backtrack.

The backtracking step (`visited.remove((r, c))`) is crucial. After checking all directions from a given cell, we must unmark it as visited to allow other paths to reuse it during separate DFS branches.

Key Insight:
- `curr_len == len(word)` is **only reachable** if a valid path matching all characters has been found.
- If any character along the path fails to match, recursion terminates before reaching that point.

Time Complexity:
O(n * m * 4^t)  
- We initiate DFS from each cell in the grid → O(n * m)
- Each DFS call explores up to 4 directions at most `t` levels deep (where `t = len(word)`), leading to a branching factor of up to 4 per level.

Space Complexity:
O(t)  
- The recursion stack and visited set both grow up to the length of the word (in the worst case where each letter is on a separate cell).
"""


class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r,c, curr_len):
            if curr_len == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[curr_len]:
                return False

            visited.add((r,c))
        
            south = dfs(r + 1, c, curr_len + 1)
            north = dfs(r - 1, c, curr_len + 1)
            east = dfs(r, c + 1, curr_len + 1)
            west = dfs(r, c - 1, curr_len + 1)
            # backtracking
            visited.remove((r,c))
            # 1 true makes all true
            return south or north or east or west
      
        if not word:
            return False
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
                    
        return False   
