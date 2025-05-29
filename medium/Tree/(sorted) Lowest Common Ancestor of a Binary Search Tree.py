"""
Since This is a Sorted Binary Search Tree, the idea is simply
Consider the following example
# Binary Tree Structure:
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5
Assume p = 2, q = 5, then the LCA is 2
Assume p = 2, q = 8, then the LCA is 6
Assume p = 3, q = 7, then the LCA is 6

Notice that theres 4 cases at each node we travel:
  1. if the current root is larger then both p and q, current root must not be the LCA, moreover, the LCA must be in the left subtree, so we recursively pass it to the left subtree
  2. if the current root is smaller then both p and q, current root must not be the LCA, moreover, the LCA must be in the right subtree, so we recursively pass it to the right subtree
  3. if the current root is larger than one and smaller than the other, then current root is the split point, then current root must be the LCA, return current root as result
  4. if the current root is equal to one of (or both of) p or q, then the current root must be the LCA, since this is the first ancestor we find, return current root as result
          and the other must be somewhere inside the subtree further down, but we dont need to know where since the LCA is confirmed.

Note that in the code I didn't explicilty state case 3 and 4, since they both have the same result, I implicity include both cases as "else"
Time Complexity: O(logn), we only need to go to either left or right subtree each time, so it is logn
Space Complexity: O(1), No extra space required
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root
        
