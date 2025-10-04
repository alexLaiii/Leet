    """
    Return the smallest set of starting vertices that can reach all nodes
    in a directed graph.

    Idea:
        A node must be chosen if and only if its indegree is 0 (no edges
        point into it). Every other node (indegree ≥ 1) is reachable from
        some predecessor and does not need to be a starting point.

    How it works:
        - Count indegrees only for destination nodes seen in `edges`.
        - Collect all nodes i in [0..n-1] that never appear as a destination
          (i.e., i not in `indegrees`). These are exactly the sources.

    Complexity:
        Time  : O(n + m), where m = len(edges)
        Space : O(n) for the indegree map and result

    Args:
        n (int): Number of nodes labeled 0..n-1.
        edges (List[List[int]]): Directed edges [u, v] with u -> v.

    Returns:
        List[int]: All nodes with indegree 0 (order not specified).
    """

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        for n1,n2 in edges:
            indegrees[n2] += 1
        res = []
        for i in range(n):
            if i not in indegrees:
                res.append(i)
        
        return res
