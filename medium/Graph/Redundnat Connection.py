"""
Solution 1(DFS approach with parent check)
Idea:
Create an Adjency list to represent the input graph.
And then we remove one edges in every loop to see if edges[0] can still reach edges[1] despite the removal.
  - If it is still reachable, then this edge is redundant, so we can return it
  - If it is not reachable, then this edge is needed, we add it back to the graph and continue searching

In the recursive function canReach, if need to check the parent of the current node (which node the call is coming from).
Because this is a bi-directional graph, therefore, only indirect connection count as a cycle, neigbour will only cause infinite cycle, as this kind of cycle
are not consider in this problem.
Base case: if we traverse back to some node along the path -> cycle still exist -> return False
           if we reach the node n2 after the edge removal, cycle not exist(as problem guranteen that remove one correct edge will destroy the cycle) -> return True.
whenenver canReach() is true, the current edge will be redundant.

Note that since the problem want the last redundant connection in the edges: so we loop backwards in edges:List.

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
