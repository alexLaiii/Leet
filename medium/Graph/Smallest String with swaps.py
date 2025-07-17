"""
Idea:
Since we can swap all the pairs that are connected as we want.
Therefore, we can represent it as a graph and then "sort each connected component alone to get the lexicographically minimum string."
Then, retrieved the character from "s" that related to the represented connected index, and then sort the characters, and then map them back to the index from small to large.

"""


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for n1,n2 in pairs:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited =set()
       
        def dfs(node, indicies):
            if node in visited:
                return
            visited.add(node)
            indicies.append(node)
            for next_n in graph[node]:
                dfs(next_n, indicies)
        s = list(s)
        for i in range(len(s)):
            indices = []
            dfs(i, indices)
            chars = [s[j] for j in indices]
            chars.sort()
            indices.sort()
            for k in range(len(indices)):
                s[indices[k]] = chars[k]
        
        return "".join(s)
            
