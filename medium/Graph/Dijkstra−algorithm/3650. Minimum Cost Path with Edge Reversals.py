"""
Compute the minimum total cost to travel from node 0 to node n-1 in a directed graph
where you may "reverse" an edge by paying an additional cost.

Idea
----
Build a weighted graph suitable for Dijkstra:
- For each directed edge u -> v with base cost w:
    - Traveling in the given direction (u -> v) costs w.
    - Traveling "against" the direction (v -> u) is treated as using a reversed edge,
      and is assigned a higher cost (here: 2*w).
Then run Dijkstra (min-heap) from node 0 until reaching node n-1.

Data Structures
---------------
- adj_list: defaultdict(list) where adj_list[x] contains (neighbor, weight) edges
- minHeap: priority queue of (cost_so_far, node)
- visited: nodes whose shortest distance is finalized (standard Dijkstra optimization)

Returns
-------
- The minimum cost to reach node n-1 from node 0, or -1 if unreachable.

Complexity
----------
Let m = number of input edges.
- Building adjacency: O(m)
- Dijkstra: O((n + m) log n) using a binary heap

Notes / Caveats
---------------
- This approach is correct only if all edge weights are nonnegative (true here).
- The correctness depends on the problem's exact reversal-cost rule.
  Many "edge reversal" problems use costs like:
    forward cost = 0, reverse cost = 1
  or
    forward cost = w, reverse cost = w + reversal_penalty
  If the problem's rule is different from "reverse costs 2*w", the transformation
  must be adjusted accordingly.
"""

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v,w in edges:
            adj_list[u].append([v, w])
            adj_list[v].append([u, w * 2])
        
        minHeap = [(0,0)]
        visited = set()
    
        while minHeap:
            currCost, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            if currNode == n - 1:
                return currCost
            visited.add(currNode)
            for neigbour, weight in adj_list[currNode]:
                heapq.heappush(minHeap, (currCost + weight, neigbour))
                
        return -1
            
        
        
