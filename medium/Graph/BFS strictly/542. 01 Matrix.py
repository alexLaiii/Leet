"""
542. 01 Matrix — Multi-source BFS (distance to nearest 0)

Idea
-----
Treat the grid as an unweighted graph (4-neighbor moves). Put **all cells with 0**
into the BFS queue at distance 0 and expand outward in layers. Because BFS visits
nodes in order of nondecreasing path length, the **first time** a cell is reached,
that layer index is the shortest distance to **some** 0.

Why multi-source?
-----------------
Running a separate BFS from each 1 (or each cell) is O((MN)^2). Seeding the queue
with **every 0 simultaneously** is equivalent to adding a **super-source** connected
to all zeros with 0-cost edges, so **one** BFS computes all answers in O(MN).

Algorithm (this implementation)
-------------------------------
1) Initialize:
   - `memo` (MxN) for distances.
   - Queue `dq` seeded with **all (i,j) where mat[i][j] == 0**.
   - Mark 0-cells visited (here by writing `-1` into `mat`).
2) BFS by layers:
   - For the current `distance`, pop exactly the current layer size from `dq`,
     set `memo[row][col] = distance`, and push any unvisited 4-neighbors,
     marking them visited.
   - Increment `distance` after finishing the layer.
3) Return `memo`.

Correctness
-----------
In an unweighted graph, BFS discovers shortest paths. With all zeros as sources,
any cell’s first discovery occurs via a shortest path to at least one zero; marking
visited ensures we finalize each cell once.

Complexity
----------
Time:  O(M·N), each cell enqueued/dequeued at most once.
Space: O(M·N) for `memo` + queue.
(Variant: use a `dist` grid initialized to -1 and avoid mutating `mat` by setting
`dist[ni][nj] = dist[i][j] + 1` when first discovered.)

Notes
-----
- Two-pass DP (TL→BR then BR→TL) is an alternative that performs the same relaxations
  without a queue, also O(M·N).
- Assumes at least one zero exists (as per problem); otherwise distances remain undefined.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        memo = [[-1 for i in range(N)] for j in range(M)]
        dq = deque([])
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    # -1 mark visited
                    mat[i][j] = -1
                    dq.append((i,j))
        distance = 0
        directions = [[1,0], [-1,0], [0,1],[0, -1]]
        while dq:
            for i in range(len(dq)):
                row,col = dq.popleft()
              
                memo[row][col] = distance
                for dr,dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if new_r >= M or new_c >= N or new_r < 0 or new_c < 0 or mat[new_r][new_c] == -1:
                        continue
                    dq.append((new_r, new_c))
                    mat[new_r][new_c] = -1
            
            distance += 1
        return memo
