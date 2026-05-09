"""
### This implementation use the idea of Union find but didn't explicitly code in Union find approach ###
Use graph connected components to group indices that can be swapped with each other.

Each allowed swap creates an undirected edge between two indices. Any indices in
the same connected component can be rearranged freely through a sequence of swaps.

For each connected component:
1. Count the values from source inside this group.
2. Subtract the values needed by target inside this group.
3. Any negative count means target needs more of that value than source can provide
   within this component, so those positions must remain mismatched.

Add up all missing target values across all components to get the minimum Hamming
distance.

Time Complexity:
    O(n + m), where n = len(source) and m = len(allowedSwaps).

Space Complexity:
    O(n + m), for the adjacency list, visited sets, groups, and frequency counts.
"""

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        groups = []
        for u,v in allowedSwaps:
            adj_list[u].append(v)
            adj_list[v].append(u)

        global_visited = set()

        def dfs(curr_node, grp):
            global_visited.add(curr_node)
            grp.add(curr_node)
            for neighbour in adj_list[curr_node]:
                if neighbour not in global_visited:
                    dfs(neighbour, grp)
            
        
        for i in range(len(target)):
            if i not in global_visited:
                new_grp = set()
                dfs(i, new_grp)
                groups.append(new_grp)
        res = 0
        for grp in groups:
            src_count = defaultdict(int)
            for idx in grp:
                src_count[source[idx]] += 1
                src_count[target[idx]] -= 1
            for c in src_count:
                if src_count[c] < 0:
                    res += -src_count[c]
                  
        return res
            
        
        
