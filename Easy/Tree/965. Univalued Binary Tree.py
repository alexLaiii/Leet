"""
Determines whether every node in a binary tree holds the same value.

Captures the root's value as the reference and walks the tree
depth-first, comparing each node against that single reference rather
than against its parent. The conjunction short-circuits, so the
traversal stops descending as soon as a mismatch is found.

Args:
    root: Root of the binary tree. Per the problem constraints the tree
        contains between 1 and 100 nodes, so this is never None.

Returns:
    True if all nodes share the same value, False otherwise. An empty
    subtree is vacuously univalued.

Time complexity: O(n), where n is the number of nodes. Every node is
    visited at most once; an early mismatch cuts the walk short but does
    not change the upper bound.
Space complexity: O(h), where h is the height of the tree, from the
    recursion stack. This is O(log n) for a balanced tree and O(n) for a
    degenerate chain.
"""
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        val = root.val

        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
