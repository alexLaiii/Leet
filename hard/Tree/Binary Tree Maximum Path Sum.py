# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        maxs = [float('-inf')]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right =  dfs(root.right)
            
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            maxs[0] = max(maxs[0], left + right + root.val, left + root.val, right + root.val)
            return max(left + root.val, right + root.val)
        dfs(root)
     
        return maxs[0]
            

            



        
