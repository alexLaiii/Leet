
"""
Determine the number of complete connected components in an undirected graph.

Approach:
- Construct an adjacency list from the given edge list.
- Use Breadth-First Search (BFS) to traverse each unvisited connected
  component.
- For each component:
    - Count the number of vertices.
    - Count the total number of edge occurrences while traversing each
      node's adjacency list. Since every undirected edge is encountered
      twice, divide the final count by 2 to obtain the actual number of
      edges.
- A connected component with k vertices is complete if it contains exactly
  k * (k - 1) // 2 edges. Count every component that satisfies this
  condition.

Time Complexity:
- O(n + m), where n is the number of vertices and m is the number of
  edges. Each vertex is visited once, and each edge is processed twice.

Space Complexity:
- O(n + m) for the adjacency list, visited set, and BFS queue.
"""

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(node, visited):
            nodes_count = edge_counts = 0
            dq = deque([node])
            visited.add(node)
            while dq:
                for i in range(len(dq)):
                    curr_node = dq.popleft()
                    nodes_count += 1
                    for neighbour in adj_list[curr_node]:
                        edge_counts += 1
                        if neighbour not in visited:
                            dq.append(neighbour)
                            visited.add(neighbour)
            return (nodes_count, edge_counts // 2)             
        res = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            nodes_c, edge_c = bfs(node, visited)
            if edge_c == (nodes_c * (nodes_c - 1)) // 2:
                res += 1
            
        return res
            
            
    
