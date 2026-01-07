# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
    
        self.maxproduct = float("-inf")
        def dfs(node):
            if not node:
                return 0   
            return node.val + dfs(node.left) + dfs(node.right)
        self.treeSum = dfs(root)

        def dfsFindSubTree(node):
            if not node:
                return 0 
            subTreeSum = node.val + dfsFindSubTree(node.right) + dfsFindSubTree(node.left)
            self.maxproduct = max(self.maxproduct, subTreeSum * (self.treeSum - subTreeSum))
            return subTreeSum
        dfsFindSubTree(root)
        return self.maxproduct % MOD
            
"""
Compute the maximum product obtainable by splitting a binary tree into two subtrees
by removing exactly one edge.

Approach:
1) First DFS (`dfs`) computes the total sum of all node values in the tree, `treeSum`.
   - This is needed because any split produces two parts whose sums are:
     (subTreeSum) and (treeSum - subTreeSum).

2) Second DFS (`dfsFindSubTree`) computes the sum of every subtree in a postorder manner.
   - For each node, let `subTreeSum` be the sum of the subtree rooted at that node.
   - If we cut the edge connecting this subtree to its parent, the product of the two
     resulting trees is:
         subTreeSum * (treeSum - subTreeSum)
   - Track the maximum such product over all nodes.

Why this works:
- Every possible split corresponds to cutting the parent-edge of some subtree.
  By evaluating the product for every subtree sum, we consider all valid splits.

Complexity:
- Time: O(n), where n is the number of nodes (two DFS traversals).
- Space: O(h) recursion stack, where h is the tree height (O(n) worst-case, O(log n) balanced).

Notes:
- The maximum product can be large, so the result is returned modulo 1e9+7 as required.
"""
