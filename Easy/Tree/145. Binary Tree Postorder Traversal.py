"""
A very standard Tree traversal algorithm
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res

        
