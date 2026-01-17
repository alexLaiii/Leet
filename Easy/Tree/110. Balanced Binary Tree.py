"""
Determine whether a binary tree is height-balanced.

A binary tree is balanced if, for every node, the heights of its left and
right subtrees differ by at most 1.

Approach:
- Use a postorder DFS traversal.
- For each node, recursively compute:
    (1) the height of its subtree
    (2) whether the subtree is balanced
- If either subtree is unbalanced or the height difference exceeds 1,
  propagate an unbalanced result upward immediately.
- Otherwise, return the current subtree height and a balanced flag.

This allows each node to be visited once, avoiding repeated height
computations.

Returns:
    bool: True if the tree is height-balanced, False otherwise.

Time Complexity:
    O(n), where n is the number of nodes in the tree.

Space Complexity:
    O(h), where h is the height of the tree due to recursion stack
    (O(log n) for balanced trees, O(n) in the worst case).
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)
            leftHeight, balanceL= dfs(node.left)
            rightHeight, balanceR = dfs(node.right)
            if not balanceL or not balanceR or abs(leftHeight - rightHeight) > 1:
                 return (-1, False)

            return (max(leftHeight, rightHeight) + 1, True)
        
        _h, res = dfs(root)
        return res
        
                
            
