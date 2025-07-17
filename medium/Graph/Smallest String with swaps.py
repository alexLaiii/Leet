"""
Approach: DFS to Find Connected Components

Idea:
We are allowed to perform any number of swaps between character positions, 
but only for the index pairs that are directly or indirectly connected. 

This naturally forms an undirected graph:
- Each index in the string is a node.
- Each swap pair (i, j) is an edge between nodes i and j.
- All indices that are connected via edges form a connected component.

Since we can swap **freely** within any connected component, we can rearrange
the characters at those indices to form the **lexicographically smallest** 
ordering for that group.

Algorithm:
1. Build the adjacency list (graph) from the given pairs.
2. Use DFS to identify all connected components (i.e., sets of indices that can reach each other).
3. For each connected component:
   - Collect all the indices involved.
   - Extract the characters from `s` at those indices.
   - Sort the characters and the indices separately.
   - Assign the smallest characters to the smallest indices.
4. Convert the modified character list back into a string and return it.

This ensures each independently swappable group of characters is minimized
in lexicographical order while preserving the constraints of allowed swaps.

Time Complexity:
- O(N log N), where N is the length of the string:
  - DFS traverses each node/edge once.
  - Sorting characters and indices per component costs O(K log K), summed across all K.

Space Complexity:
- O(N) for graph storage, visited set, and temporary arrays.
"""

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for n1, n2 in pairs:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, indices):
            if node in visited:
                return
            visited.add(node)
            indices.append(node)
            for next_n in graph[node]:
                dfs(next_n, indices)

        s = list(s)
        for i in range(len(s)):
            if i in visited:
                continue
            indices = []
            dfs(i, indices)
            chars = [s[j] for j in indices]
            chars.sort()
            indices.sort()
            for k in range(len(indices)):
                s[indices[k]] = chars[k]

        return "".join(s)

