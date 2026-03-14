"""
Determines whether a path exists between `source` and `destination`
in an undirected graph.

The graph is first converted into an adjacency list where each vertex
maps to its neighboring vertices. A depth-first search (DFS) is then
performed starting from `source`. During the search, a `visited` set
keeps track of explored vertices to prevent revisiting nodes and
getting stuck in cycles.

The DFS recursively explores neighbors of each vertex. If the
`destination` vertex is reached, the search terminates immediately
and returns True. If all reachable vertices are explored without
encountering `destination`, the function returns False.

Args:
  n (int): Number of vertices labeled from 0 to n - 1.
  edges (List[List[int]]): List of undirected edges where each
      element [u, v] represents a connection between vertex u
      and vertex v.
  source (int): Starting vertex.
  destination (int): Target vertex.

Returns:
  bool: True if a path exists from `source` to `destination`,
  otherwise False.

Time Complexity:
  O(V + E), where V is the number of vertices and E is the number
  of edges. Each vertex and edge is explored at most once.

Space Complexity:
  O(V + E) for the adjacency list and visited set, plus up to
  O(V) recursion stack depth in the worst case.
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def havePath(vertices):
            if vertices == destination:
                return True
            visited.add(vertices)
            found = False
            for neighbour in adj_list[vertices]:
                if neighbour in visited:
                    continue
                if havePath(neighbour):
                    found = True
                    break
            return found
        return havePath(source)
            
        
