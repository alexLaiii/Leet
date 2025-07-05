"""
### Idea:

We use BFS to find the shortest alternating-color path from node 0 to every other node `k` (where 0 ≤ k < n).

The twist is: we can only travel along edges of alternating colors. To handle this, we store the **last used edge color** along with the current node in our BFS state. This helps us decide whether the next edge is valid (it must be the opposite color of the previous one).

Now, consider this edge case:
- If we arrive at a node via a **blue** edge, we can only take **red** edges next.
- This means the **blue** edges from this node remain unexplored for now.
- Later, we might reach this same node via a **red** edge, and now we can explore its blue edges.

Therefore, we must **allow revisiting nodes**, but only under specific conditions.

### Visited Rule:

- We **cannot** mark a node as visited like normally do — that would block valid alternate-color paths (where some nodes might only be reached through this redundant path)
- We **cannot** skip visited tracking — that would allow infinite cycles.
- ✅ So we track visited as a **(node, color)** pair:
  - If we've visited `(node, color)`, skip it — we've already explored all paths with that entry point.
  - If `(node, other_color)` is visited later, allow it — we can now explore previously invalid edges.

### Shortest Distance Guarantee:

Since we're using BFS, the **first time** we reach a node (regardless of color), it's guaranteed to be via the **shortest alternating path**.
So we record the distance only the **first time** we reach a node, or use `min(...)` if multiple paths reach it.

---

## Implementation:

1. Build an adjacency list:
   - Each entry is (next_node, edge_color)
   - Use 0 for red, 1 for blue

2. Initialize:
   - res = [-1 for i in range(n)]
     - Stores shortest distance to each node, -1 means unreachable
   - dq = deque([(0, 0, 0), (0, 1, 0)])
     - BFS queue storing (node, color, distance)
     - These are "fake" starting edges from node 0 with both red and blue to ensure both directions are explored, these edges not really existed in the graph, just initialize for smoothless as the first case, hence they have 0 distance.

3. BFS traversal:
   while dq:
       - Pop (node, color, distance)
       - If visited, skip
       - Update res[node]
       - For each neighbor:
           - If next_color == 1 - color:
               - Enqueue (next_node, next_color, distance + 1) # distance + 1 to simulate travelling this edges

4. Return res after BFS finishes.

Time Complexity:
- O(N + E), where N is the number of nodes and E is the total number of red + blue edges.
- Each node is visited at most twice (once per color), and each edge is processed once.

Space Complexity:
- O(N + E)
    - O(N + E) for the adjacency list
    - O(N) for the result array
    - O(N) for the visited set (each node with each color at most once)
    - O(N) for the BFS queue (in the worst case)
"""


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        # 0 is red, 1 is blue
        for n1,n2 in redEdges:
            adj_list[n1].append((n2, 0))
        for n1, n2 in blueEdges:
            adj_list[n1].append((n2,1))
        
        res = [-1 for i in range(n)]
        dq = deque([(0,0,0), (0,1,0)])
        visited = set()

        while dq:
            curr_node, color, distance= dq.popleft()
            if (curr_node, color) in visited:
                continue
          
            res[curr_node] = min(res[curr_node], distance) if res[curr_node] != -1 else distance
        

            visited.add((curr_node, color))
            for node in adj_list[curr_node]:
                next_node, next_color = node
                if next_color == 1 - color:
                    dq.append((next_node, next_color, distance +  1))
        
        return res

        
