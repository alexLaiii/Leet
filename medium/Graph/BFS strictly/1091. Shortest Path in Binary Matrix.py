  """
  BFS on an 8-direction grid to find the shortest path of 0s
  from (0,0) to (n-1,n-1).

 Why it works: 
  BFS guarantees shortest paths in an unweighted graph (all edges cost 1). 
  This grid is unweighted—each move has cost 1—so the first time we dequeue (n-1,n-1) 
  we've found the shortest path. Dijkstra’s algorithm is the weighted generalization 
  for non-negative edge costs.

  Idea
  - Use layer-by-layer BFS: each BFS "layer" corresponds to paths
    of equal length. The first time we hit the goal, we have the shortest path.
  - We can step to any of 8 neighbors if it's inside bounds and equals 0.

  Steps
  1) If start or end is blocked (1), return -1.
  2) Push (0,0) with distance=1, and mark it visited.
  3) Pop a layer, try all 8 moves; enqueue unseen 0-cells and mark visited on enqueue.
  4) When we pop (n-1,n-1), return the current distance (layer count).

  Complexity
  - Time: O(n^2), Space: O(n^2) for the visited set.
  """


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[M - 1][N - 1] == 1:
            return -1

        # 8 Directions
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    
        dq = deque([(0,0)])
        visited = set()
        pathLength = 1
        while dq:
            for i in range(len(dq)):
                r,c = dq.popleft()
                if r == M - 1 and c == N - 1:
                    return pathLength
                for dr,dc in direction:
                    nr,nc = r + dr, c + dc
                    if nr >= M or nr < 0 or nc >= N or nc < 0 or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    dq.append((nr,nc))
                    visited.add((nr,nc))
            pathLength += 1
        return -1
         
                


            




        
            
            
            
        
