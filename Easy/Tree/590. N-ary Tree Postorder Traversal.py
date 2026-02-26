"""
Just a variation of Post order Traversel
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            for n in node.children:
                dfs(n)
            res.append(node.val)
        dfs(root)
        return res
        
