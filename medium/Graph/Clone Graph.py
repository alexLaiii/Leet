"""
Idea:
Use backtracking (DFS) to connect each original node to its correct clone. 
The most important (and most difficult) part of this problem is correctly linking each clone's neighbors to the appropriate cloned nodes.

Implementation:
We use a hash map `visited` to store `{Original_Node: Cloned_Node}` pairs. 
This allows us to return the correct clone when a node is revisited (prevents infinite loops in cyclic graphs).

During DFS, for each neighbor of the original node, we recursively clone it, and append the returned clone to the current clone's neighbors.

Example:

Graph structure:
    1 — 2
    |   |
    4 — 3

Original graph (adjacency list):
    [[1, [2, 4]], [2, [1, 3]], [3, [2, 4]], [4, [1, 3]]]

Step-by-step DFS (simplified):
- Start at Node 1
- Clone Node 1 → visited = {1: c1}
- Recurse into neighbor Node 2:
    - Clone Node 2 → visited = {1: c1, 2: c2}
    - Recurse into Node 1 → already visited, return c1
    - Append c1 to c2.neighbors → c2.neighbors = [c1]
    - Recurse into Node 3:
        - Clone Node 3 → visited = {1: c1, 2: c2, 3: c3}
        - Recurse into Node 2 → already visited, return c2
        - Append c2 to c3.neighbors
        - Recurse into Node 4:
            - Clone Node 4 → visited = {1: c1, 2: c2, 3: c3, 4: c4}
            - Recurse into Node 1 → already visited, return c1
            - Append c1 to c4.neighbors
            - Recurse into Node 3 → already visited, return c3
            - Append c3 to c4.neighbors → c4.neighbors = [c1, c3]
        - Append c4 to c3.neighbors → c3.neighbors = [c2, c4]
    - Append c3 to c2.neighbors → c2.neighbors = [c1, c3]
- Append c2 to c1.neighbors → c1.neighbors = [c2]
- Recurse into Node 4 → already visited, return c4
- Append c4 to c1.neighbors → c1.neighbors = [c2, c4]

Final cloned graph:
    [[c1, [c2, c4]], [c2, [c1, c3]], [c3, [c2, c4]], [c4, [c1, c3]]]

Which matches the structure of the original graph:
    [[1,  [2, 4]], [2, [1, 3]], [3, [2, 4]], [4, [1, 3]]]

Time Complexity:
- O(V + E), where V is the number of nodes (vertices) and E is the number of edges.
  Every node and edge is visited once in the DFS.

Space Complexity:
- O(V + E), due to the recursion stack and the `visited` hash map storing all cloned nodes.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return 
        # pair represent like {node : node_cpy}, where the node represent the reference of the original node, so bascially here I am mapping the original node to its cloned counterpart
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            # create new node
            node_cpy = Node(node.val, [])
            visited[node] = node_cpy
            for n in node.neighbors:
                node_cpy.neighbors.append(dfs(n))
            return node_cpy
        return dfs(node)
        
        

        
