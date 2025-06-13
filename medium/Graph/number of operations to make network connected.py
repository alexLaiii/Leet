"""
Idea:
Use Union Find (Disjoint Set Union - DSU) to count the number of edges required to connect all nodes through the given `connections` list.  
Any remaining (redundant) edges can then be used to connect the remaining disconnected components.

By graph theory, to connect `n` nodes into one connected component, we need at least `n - 1` edges.  
So the number of additional operations needed to fully connect the network is:

    operations_needed = (n - 1) - used_edges

Where `used_edges` is the number of edges actually used to merge different components.

Step 1 — Initial Check:
First, check if there are enough connections to begin with:

    - Minimum edges required to connect `n` nodes: n - 1  
    - Edges available: len(connections)

If `len(connections) < n - 1`, it is impossible to fully connect the network. Return -1.

Outer Loop Explanation:
We initialize `used_edges = 0` to track how many connections were actually used to merge components.

We then iterate through each connection `[c1, c2]`:
- If `find(c1) != find(c2)` → the two nodes belong to different components:
    - Increment `used_edges`
    - Call `union(c1, c2)` to merge the sets

- If `find(c1) == find(c2)` → the nodes are already connected:
    - This edge is redundant — do nothing

After processing all edges, return:

    return (n - 1) - used_edges

Which represents the number of extra operations (edge reuses) required to fully connect all `n` nodes.

Union Find Implementation:

- `parents`:
    - Stores the representative (root) of each node
    - Initially, every node is its own parent: `parents[i] = i`

- `rank`:
    - Stores the size (number of nodes) in each set
    - Helps decide which set to merge into which (union by size)

find(node):
- Recursively finds the root (representative) of the node's set
- Applies path compression:
    - While tracing up to the root, update all parent pointers directly to the root
    - This flattens the structure and speeds up future calls

union(c1, c2):
- Merges the sets containing `c1` and `c2`
- Steps:
    1. Find representatives of both nodes
    2. Compare their `rank` (size)
    3. Attach the smaller set to the larger one:
        - If `rank[rep1] >= rank[rep2]`:
            - `parents[rep2] = rep1`
            - `rank[rep1] += rank[rep2]`
        - Else:
            - `parents[rep1] = rep2`
            - `rank[rep2] += rank[rep1]`
    - This keeps the tree balanced and ensures efficient performance

Time Complexity:
- `find()` and `union()` run in **amortized O(α(n))**, where α(n) is the inverse Ackermann function (extremely slow-growing).
- Each of the `m` connections is processed once: **O(m · α(n))**
- In practice, this behaves like **O(m)**

Space Complexity:
- O(n) for `parents` array
- O(n) for `rank` array
- Total: **O(n)**
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        parents = [i for i in range(n)]
        rank = [1 for i in range(n)]
       

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        def union(c1,c2):
            p1,p2 = find(c1), find(c2)
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parents[p2] = p1
            else:
                rank[p2] += rank[p1]
                parents[p1] = p2

        # used_edge record the minimum number of edges to connect all the nodes appear in the input list "connections" 
        # If used_edge = k, then the number of nodes in "connections" must be k + 1
        used_edge = 0
        for c1, c2 in connections:
            if find(c1) != find(c2):
                used_edge += 1
                union(c1, c2)
        return n - 1 - used_edge


"""
Cleaner solution
"""
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        N = len(connections)
        pars = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]

        def find(node):
            if pars[node] != node:
                pars[node] = find(pars[node])
            return pars[node]

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                pars[p2] = p1
            else:
                rank[p2] += rank[p1]
                pars[p1] = p2
            return True
        used_edge = 0
        for c1,c2 in connections:
            if union(c1,c2):
                used_edge += 1
        
        return n - 1 - used_edge


        
                
