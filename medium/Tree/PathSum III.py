# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  
    def pathSum(self, root, targetSum):

        def dfs(root, target, count):
            if not root:
                return count
            
            if root.val - target == 0:
                count += 1

            return dfs(root.left, target - root.val, count) +  dfs(root.right, target - root.val, 0)
           
            
        def outer_pass(root, sums):
            if not root:
                return sums
            sums += dfs(root, targetSum, 0)
            
            return outer_pass(root.left,  sums) + outer_pass(root.right, 0)
  
        count = outer_pass(root, 0)
        return count
