"""
Finds the minimum possible score of a path from city 1 to city n.

The graph is traversed using BFS starting from city 1. During traversal,
the minimum road distance encountered in the connected component is tracked.
Since the problem guarantees that cities 1 and n are connected and paths
may revisit cities and roads, the minimum edge weight in this connected
component is the minimum possible path score.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v,d in roads:
            adj_list[u].append((v,d))
            adj_list[v].append((u,d))

        min_weight = float("inf")
        dq = deque([1])
        visited = set()
        while dq:
            for i in range(len(dq)):
                curr = dq.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                for neighbour, distance in adj_list[curr]:
                    min_weight = min(min_weight, distance)
                    if neighbour not in visited:
                        dq.append(neighbour)
        
        return min_weight
            
            
        
