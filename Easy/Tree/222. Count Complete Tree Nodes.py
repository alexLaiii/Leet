"""
Count all nodes of a binary tree by full DFS traversal.

This implementation does not use the "complete" property; it simply
visits every node once and returns 1 + count(left) + count(right).

Args:
    root (Optional[TreeNode]): Root of the binary tree.

Returns:
    int: Total number of nodes in the tree.

Complexity:
    Time O(n): visits each node exactly once.
    Space O(h): recursion stack proportional to tree height (O(log n) for
    balanced/complete trees, O(n) in worst-case skew).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            res = 1 + dfs(root.left) + dfs(root.right)
            return res
        
        return dfs(root)
        
