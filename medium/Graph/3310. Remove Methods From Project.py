"""
Determine which methods can be safely removed without breaking any
suspicious (obfuscated) method calls.

A method is "suspicious" if it is method k, or reachable from method k
via the call graph (invocations). All suspicious methods must be kept,
along with anything they call.

A non-suspicious method can only be safely removed if NONE of the
remaining (non-suspicious) methods call directly into the suspicious
set — otherwise removing it would break that caller. In that case,
no methods can be removed at all, and every method (0..n-1) must stay.

Args:
    n: total number of methods, labeled 0 to n-1.
    k: the method whose calls are considered suspicious/obfuscated.
    invocations: list of [u, v] pairs meaning method u calls method v.

Returns:
    List of method ids that can be safely removed (i.e. not
    suspicious, and not called by any non-suspicious method that
    reaches into the suspicious set). If no method can be removed
    without breaking a call into the suspicious set, returns
    list(range(n)) — meaning all methods must remain.

Approach:
    1. DFS from k to compute `sus`, the full set of methods reachable
       from k (including k itself). These must all be retained.
    2. For every method not in `sus`, check its direct outgoing calls.
       If any such call lands in `sus`, removal is unsafe entirely
       (return all methods). Otherwise, that method is removable.

Time:  O(V + E) - each node's adjacency list is visited once in the
       DFS and once in the removal-check loop.
Space: O(V + E) - adjacency list plus the `sus` set and recursion
       stack (up to O(n) deep in the worst case, e.g. a long chain).
"""

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u,v in invocations:
            adj_list[u].append(v)
        sus = {k}
      
        def dfs_k(node):
            sus.add(node)
            for neighbour in adj_list[node]:
                if neighbour in sus:
                    continue
                dfs_k(neighbour)
        dfs_k(k)
        res = []
        for node in range(n):
            if node in sus:
                continue
            for neigbour in adj_list[node]:
                if neigbour in sus:
                    return list(range(n))
            res.append(node)
        return res
        
   
        
