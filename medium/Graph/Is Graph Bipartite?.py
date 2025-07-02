"""
Bipartite means:
A graph is bipartite if its nodes can be split into two groups such that no two nodes within the same group are connected.

To check if a graph is bipartite:
Try to color the graph nodes using two colors — if any two connected nodes end up with the same color, then the graph is not bipartite.

Idea:
Our code implements this idea. We can either:
- Create an adjacency list for clarity
- Or just use the given 2D array `graph`, since the index already represents the node

Implementation:
We use a "colors" array to represent the color of each node:
- index = node
- value = color
    -1 → uncolored
     0 → blue
     1 → red

Outer Loop:
Since not every node is guaranteed to be connected (there might be isolated nodes or disconnected components),
we loop through every node to start DFS from any unvisited one.

DFS Function:
def dfs(node, color)
- node: the current node we're trying to color
- color: the color to assign, which is determined by its neighbor (neighbor is red → this is blue, and vice versa)

Steps:
1. Color the current node:  
   `colors[node] = color`

2. Loop through all neighbors of this node:  
   `for neighbor in graph[node]:`

   - If the neighbor is uncolored:
       - Recursively call DFS to color it with the opposite color
       - If that DFS returns False (conflict detected deeper), return False immediately

   - If the neighbor is already colored:
       - Check if it has the same color as the current node → contradiction → return False

3. If all neighbors are valid and no conflicts arise, return True

Time Complexity:
O(V + E)
- Each node is visited once
- Although there is an outer loop over all nodes (O(V)), the DFS is only called on unvisited nodes.
  Each node is visited once and each edge is explored once during all DFS calls combined.
  So the total work done is O(V) for nodes + O(E) for edges = O(V + E).

Space Complexity:
- Without adjacency list: O(1) extra (excluding input and recursion)
- With adjacency list: O(V + E)
"""

## If not build adj_list ##
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)

        # blue = 0, red = 1
        colors = [-1 for i in range(N)]
        def dfs(node, color):
            colors[node] = color
            for neighbour in graph[node]:
                if colors[neighbour] == -1:
                    if not dfs(neighbour, 1 - color):
                        return False
                elif colors[neighbour] == color:
                    return False
            return True
            


        for node in range(N):
            if colors[node] != -1:
                continue
            if not dfs(node, 0):
                return False
        return True


## If build adj_list ##
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        adj_list = defaultdict(list)
        for i in range(len(graph)):
            for node in graph[i]:
                adj_list[i].append(node)
        colors = [-1 for i in range(N)]
        
        # blue == 0, red == 1
        def dfs(node, color):
   
            if colors[node] == -1:
                colors[node] = color
            for neigbhour in adj_list[node]:
                if colors[neigbhour] == -1:
                    next_color = 1 if color == 0 else 0
                    res = dfs(neigbhour, next_color)
                    if not res:
                        return res
                elif colors[neigbhour] == colors[node]:
                    return False
            return True


        for i in range(N):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

