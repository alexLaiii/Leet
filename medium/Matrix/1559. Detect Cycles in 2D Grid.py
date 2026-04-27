"""
DFS solution for LeetCode 1559 - Detect Cycles in 2D Grid.

Idea:
Treat the grid as an undirected graph where each cell is a node,
and edges exist only between adjacent cells (up, down, left, right)
that contain the same character.

A cycle exists if during DFS we reach a neighbor that:
1. Has the same character
2. Has already been visited
3. Is NOT the parent (previous cell we came from)

Why parent matters:
Since this is an undirected graph, moving back to the previous cell
is normal and should not be considered a cycle.

Approach:
- Use DFS to explore each connected component of same-character cells.
- Maintain a global visited set so each cell is processed once.
- For every unvisited cell:
    - Start DFS
    - Track the previous node (parent) to avoid false cycle detection
- If DFS finds a visited neighbor that is not the parent, return True.

Time Complexity:
O(M * N)
Each cell is visited at most once.

Space Complexity:
O(M * N)
For the visited set and recursion stack in the worst case.
"""

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        def dfs(currNode, prevNode):
            curr_i, curr_j = currNode
            prev_i, prev_j = prevNode

            visited.add(currNode)
            for dr, dc in directions:
                next_i = curr_i + dr
                next_j = curr_j + dc
                if next_i == prev_i and next_j == prev_j:
                    continue
                if next_i < 0 or next_i >= M or next_j < 0 or next_j >= N or grid[next_i][next_j] != grid[curr_i][curr_j]:
                    continue
                if (next_i, next_j) in visited:
                    return True
                if dfs((next_i, next_j), currNode):
                    return True

            return False
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited:
                    if dfs((i,j), (i,j)):
                        return True
        return False
            
