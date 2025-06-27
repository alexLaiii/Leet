"""
Easy version for "124. Binary Tree Maximum Path Sum"
Notice that it want the number of edges of the path, not the number of nodes.

        
Calculates the diameter (longest path between any two nodes) of a binary tree.
Uses post-order DFS to compute subtree heights and updates the maximum diameter
as the sum of left and right heights at each node.

Returns the number of edges in the longest path.
        
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(root):
            if not root: 
                return 0
            left_count = dfs(root.left)
            right_count = dfs(root.right)
            self.maxDiameter = max(left_count + right_count, self.maxDiameter)
            return max(left_count, right_count) + 1
        dfs(root)
        return self.maxDiameter
        
