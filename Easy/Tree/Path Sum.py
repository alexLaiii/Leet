"""
A super easy problem, I manage to solved it in 7 mins.
Logic: Use preorder traversal, 
if this is the leaf node just simpli return True if node.val is equals to the targetSum, otherwise false. check both left subtree and right subtree by doing recursive call
if one of the right path and left path, the node to leaf path exist, so it returns True: that's why return left_res or right_res is formed.
  return False if and only if neither right path or left path is valid.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
         
        left_res= self.hasPathSum(root.left, targetSum - root.val)
        right_res = self.hasPathSum(root.right, targetSum - root.val)
        return left_res or right_res
            
        
        
        
