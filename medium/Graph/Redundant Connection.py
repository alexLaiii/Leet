"""
Solution 1: DFS Approach with Parent Check

 Idea:
We use Depth-First Search (DFS) to detect cycles in an undirected graph.

 Step-by-step:
1. Build an adjacency list from the edges.
2. For each edge (starting from the end of the list, since the problem wants the *last* redundant one):
   - Temporarily remove the edge from the graph.
   - Check if its two nodes are still connected using DFS.
     - If yes → a path still exists → cycle remains → this edge is redundant → return it.
     - If no → this edge is necessary → restore the edge and continue.

 Why we check the parent node:
Since the graph is undirected, neighbors can point back to their caller (parent).
So we ignore the immediate parent in DFS to avoid infinite loops.
Only **indirect** paths are considered real cycles here.

 Base Cases for canReach():
- If `curr == target` → a path exists → cycle remains → this edge is redundant.
- If a node is revisited (and it's not the parent) → cycle.
- Otherwise, explore neighbors recursively.

 Edge Scanning Direction:
We scan the edges list **backwards** because the problem asks for the **last** redundant edge.

---

 Time Complexity:
- Let **n** be the number of nodes and **e** be the number of edges.
- In the worst case, for each edge, we do a DFS.
- DFS can visit up to **O(n)** nodes, and there are **e** edges.
- So total worst-case time: **O(n²)**

 Space Complexity:
- Adjacency list: **O(n + e)** → max **O(n²)** for dense graph.
- DFS call stack + visited set: **O(n)**

---
Conclusion:
 Easy to implement  
 Slower than Union Find for large inputs  
 Still accepted on LeetCode within limits
"""



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS approach
        graph = {x + 1:[] for x in range(len(edges))}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        
        def canReach(curr, target, parent):
            if curr in visited:
                return False
            if curr == target:
                return True
            visited.add(curr)
            for n in graph[curr]:
                if n == parent:
                    continue
                if canReach(n, target, curr):
                    return True
            return False
        
        for i in range(len(edges) -1, -1, -1):
            n1,n2 = edges[i][0], edges[i][1]
            
            graph[n1].remove(n2)
            graph[n2].remove(n1)
            visited = set()
            if canReach(n1, n2, -1):
                return [n1,n2]
            graph[n1].append(n2)
            graph[n2].append(n1)
