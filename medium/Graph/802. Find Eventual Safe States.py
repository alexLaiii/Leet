  """
  LeetCode 802 — Eventual Safe States
  -----------------------------------
  Idea
  A node is "eventually safe" iff no path starting from it can enter a cycle.
  We run DFS, keeping a 'visited' set that represents the current recursion
  stack (nodes on the path). Hitting a node already in 'visited' means a
  back-edge ⇒ cycle. We cache results in:
    - isSafe: nodes proven acyclic (all neighbors are safe)
    - isCycle: nodes known to be in/reach a cycle

  DFS logic for node u
  - If u ∈ isSafe:      return True (already proved safe)
  - If u ∈ isCycle:     return False (already known unsafe)
  - If u ∈ visited:     mark u in isCycle and return False (found a cycle)
  - Else: push u to visited and DFS all neighbors.
      * If any neighbor returns False → u is unsafe (add to isCycle).
      * If all neighbors return True → u is safe (add to isSafe).
    Pop u from visited before returning.

  Correctness (sketch)
  - Base: terminal nodes (outdegree 0) are safe (loop sees no failing child).
  - Induction: if any child is unsafe, u can reach a cycle → unsafe; if all
    children are safe, no path from u can reach a cycle → safe.

  Complexity
  - Each node/edge is processed at most a constant number of times: O(n+m)
    time and O(n) extra space.
  """

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isCycle, isSafe, visited = set(), set(), set()
        def dfs(node):
            if node in isSafe:
                return True
            if node in isCycle:
                return False
            if node in visited:
                isCycle.add(node)
                return False
            visited.add(node)
            for neighbour_node in graph[node]:
                if not dfs(neighbour_node):
                    isCycle.add(node)
                    visited.remove(node)
                    return False
            isSafe.add(node)
            visited.remove(node)
            return True
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
                
        
