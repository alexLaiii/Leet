"""
🔍 Idea:
Use Union-Find (Disjoint Set Union, DSU) to find the redundant connection.

Union-Find groups all connected nodes into disjoint sets.  
Each set has a unique "representative" (a root node) that represents all nodes within that set.  
In this problem, we are given a list of connections (edges), and we use them to construct our Union-Find structure as we go.  

When we encounter a pair of nodes that already share the same representative (i.e., `find(n1) == find(n2)`), that means they are already connected.  
→ Therefore, this new connection is **redundant**, and we return that edge.

---

🛠️ Implementation:

We initialize two lists to represent the Union-Find structure:  
(Note: each index corresponds to a node.)

- `parents`:  
  - Stores the representative (root) for each node.  
  - Initially, each node is its own representative (`parents[i] = i`), since no connections have been made.

- `set_count` (also called "rank" or "size"):  
  - Stores the number of nodes in the set rooted at a given index.  
  - `set_count[i]` gives the number of nodes in the set whose root is node `i`.

---

🔧 `find(node)`:
- A typical `find` function used in DSU.
- Given a node, it returns the **representative** (root) of its set.
- It uses **path compression** to optimize repeated lookups:
  - As we trace up to the root, we directly reassign the parent of each node on the path to its root.
  - This avoids unnecessary future traversals and greatly improves performance.

---

🔧 `union(n1, n2)`:
- Given two nodes, it joins their sets into one.
- Steps:
  1. Find the representatives of both nodes.
  2. Compare the sizes of the two sets (`set_count[rep1]` vs `set_count[rep2]`).
  3. Attach the smaller set under the larger one to minimize tree height.
     - e.g., if `rep1` has more nodes, do:  
         `set_count[rep1] += set_count[rep2]`
     -Set the representative of the smaller set to point to the larger one’s representative — so the smaller set joins the larger.
         `parents[rep2] = rep1`
     - This ensures balanced trees and efficient future operations.

---

🔁 Main loop:
We iterate through each edge in `edges`:

- If `find(node1) == find(node2)` → the two nodes are already connected → this edge would create a cycle → return it as the answer.
- If they are in different sets → we connect them using `union(node1, node2)`.

Since this is an undirected graph, connecting two nodes means connecting all nodes in their respective sets. So the entire set of `node1` becomes connected to the entire set of `node2`.

📌 The problem guarantees there will always be a result, so we do not need to handle edge cases where no redundant connection is found.

---

⏱ Time Complexity:
- **O(n)** — We process each edge once. Each `find` and `union` operation is nearly constant time due to path compression and union by size/rank.

📦 Space Complexity:
- **O(n)** — Two arrays: `parents` and `set_count`, each of size `n + 1`.
"""




class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [x for x in range(n + 1)]
        set_count = [1 for x in range(n + 1)]

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if set_count[p1] >= set_count[p2]:
                set_count[p1] += set_count[p2]
                parents[p2] = p1
            else:
                set_count[p2] += set_count[p1]
                parents[p1] = p2

        for n1,n2 in edges:
            if find(n1) == find(n2):
                return [n1,n2]
            union(n1,n2)
