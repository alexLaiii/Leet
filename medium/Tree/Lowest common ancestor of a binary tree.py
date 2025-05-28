"""

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # This is DFS problem
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        found_1 = self.lowestCommonAncestor(root.left, p, q)
        found_2 = self.lowestCommonAncestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            return root
        if found_1 and found_2:
            return root
        if found_1: return found_1
        elif found_2: return found_2
        else: return 

