"""
Very simple Depth-first search tree problem
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return None
            res.append(node.val)
            for each in node.children:
                dfs(each)
        dfs(root)
        return res
