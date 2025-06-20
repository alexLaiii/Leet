"""
Rotting Oranges - BFS Strategy

Why DFS doesn't work:
DFS is depth-first, meaning it explores one full branch before others.
That breaks the timing logic in this problem because all rotten oranges should spread in parallel.
The only correct traversal here is BFS, which processes nodes layer by layer — exactly how minutes pass in this simulation.

Idea:
Each layer of BFS represents 1 minute passed.
BFS naturally fits here because it explores nodes level by level. We attach the "layer time" (minute) to each coordinate in the queue to track when that orange gets rotted.
Since BFS pops nodes from the same layer together before appending the next layer, it simulates time passing correctly.

Key point:
Multiple rotten oranges can appear in the grid initially. To simulate simultaneous rotting, we add all of them to the queue before starting BFS.

Implementation:
1. Preprocessing:
   - Traverse the entire grid to find all initially rotten oranges.
   - Add each of their coordinates to the BFS queue with time = 0.
   - Simultaneously, count the number of fresh oranges.

2. BFS traversal:
   - While the queue is not empty:
     - Pop (r, c, time) from the queue.
     - Skip the cell if it's out of bounds, empty, or already visited.
     - If it's a fresh orange:
         - Mark it as rotten.
         - Decrement the fresh count.
         - Update maxTime = time, since BFS guarantees the shortest time to reach this cell.
     - Append all 4-direction neighbors with time + 1 to the queue.

3. Final result:
   - If fresh == 0 after BFS, return maxTime (all fresh oranges rotted).
   - Otherwise, return -1 (some oranges couldn’t be reached).

Time Complexity: O(m × n), since each cell is visited at most once.
Space Complexity: O(m × n), due to the worst-case size of the queue.
"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
              
        q = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1
                    
        visited = set()
        maxTime = 0
        
        while q:
            r, c, time = q.popleft()
            if r < 0 or c < 0 or r >= m or c >= n or (r,c) in visited or grid[r][c] == 0:
                continue
            visited.add((r,c))
            
            if grid[r][c] == 1:
                fresh -= 1
            maxTime = time
            q.append((r+1,c,time + 1))
            q.append((r-1,c,time + 1))
            q.append((r,c + 1,time + 1))
            q.append((r,c - 1,time + 1))
    
        return maxTime if fresh == 0 else -1
  
                    
        
