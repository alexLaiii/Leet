

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return 
        visited = {}
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            node_cpy = Node(node.val, [])
            visited[node.val] = node_cpy
            for n in node.neighbors:
                visited[node.val].neighbors.append(dfs(n))
            return visited[node.val]
        return dfs(node)
        
        

        
