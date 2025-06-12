class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union Find approach
        parent = [x for x in range(len(edges) + 1)]
        set_count = [1 for x in range(len(edges) + 1)]

        def union(n1,n2):
            par1 = find(n1)
            par2 = find(n2)
            if set_count[par1] >= set_count[par2]:
                set_count[par1] += set_count[par2]
                # if the parent is the node itself, good, that is equals to parent[n2] = parent[n1]
                # if not, then we change its parent, so that node will still get trace?
                parent[par2] = parent[par1]
                parent[n2] = parent[n1]
            else:
                set_count[par2] += set_count[par1]
                parent[par1] = parent[par2]
                parent[n1] = parent[n2]
                
            
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]


        for n1,n2 in edges:

            if find(n1) == find(n2):
                return [n1,n2]
            union(n1,n2)


