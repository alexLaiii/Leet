"""
Idea:  
Use Dijkstra’s algorithm to travel all reachable nodes from the starting node — not to find a shortest path to a specific target, but to determine the time it takes for all nodes to receive the signal.

Logic Flow:
1. **Build the Adjacency List**:  
   `graph = {node1: [(neighbor1, weight), (neighbor2, weight)], node2: [...], ...}`

2. **Dijkstra's Algorithm**:
   - Since we are **not targeting a specific destination**, the algorithm only ends when the minHeap is empty — i.e., all reachable nodes have been visited.
   - Dijkstra guarantees the shortest path is always processed first, so:
     - If we revisit a node already in `visited`, we skip it — a cheaper path has already been processed.
     - If a node hasn’t been visited until now, this is the **cheapest possible way** to reach it — we can safely record it as visited and update the time.
   - We can either:
     - Track the max time with `t = max(t, currTime)` every time we visit a new node
     - Or rely on the fact that the **last node visited** in the heap traversal will have the max delay — and use `t` to store its delay
              (This max delay from the last node is guranteen to be the smallest possible to reach all nodes, since this is the **cheapest possible way** to reach this last node)

3. **Check connectivity**:
   - If `len(visited) != n`, it means not all nodes are reachable from the starting node — return `-1`
   - Otherwise, return the tracked `t` as the minimum time required for all nodes to receive the signal
Time Complexity:  
- **O(E log N)**, where:
  - E = number of edges (at most `times.length`)
  - N = number of nodes  
  - Heap operations cost `log N` and we may push each edge into the heap

Space Complexity:  
- **O(N + E)** for the graph and visited set  
- **O(N)** max size of the minHeap in worst case
"""

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # built adjenacy list
        graph = {i + 1:[] for i in range(n)}
        for u,v, w in times:
            graph[u].append((v,w))

        minHeap = [(0, k)]
        visited = set()
        t = 0
        # Dijkstra−algorithm

        while minHeap:
            curr = heapq.heappop(minHeap)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            # t mark the time that needed to travel to curr
            t = curr[0]
            for nn, w in graph[curr[1]]:
                heapq.heappush(minHeap, (w + curr[0], nn))
        

        return t if len(visited) == n else -1
            
            
    
        
        
