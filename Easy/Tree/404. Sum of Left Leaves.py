"""
Computes the sum of all left leaf nodes in a binary tree.

A left leaf is defined as a node that:
- is a leaf (has no left or right children), and
- is the left child of its parent.

Approach:
- Use DFS with an extra boolean flag `take` indicating whether the current node
  is a left child.
- When a leaf node is reached and `take` is True, add its value to the sum.
- Recursively traverse:
  - left child with take=True
  - right child with take=False

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree due to recursion stack.
"""
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, take):
            if not node:
                return 0
            if not node.left and not node.right and take:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
