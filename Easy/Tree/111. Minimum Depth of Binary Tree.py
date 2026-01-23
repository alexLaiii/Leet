"""
Computes the minimum depth of a binary tree.

The minimum depth is defined as the number of nodes along the shortest
path from the root node down to the nearest leaf node. A leaf is a node
with no children.

This solution uses depth-first search (DFS). For each node:
- If the node is null, its depth is 0.
- If both children are null, the node is a leaf and contributes depth 1.
- If one child is null, the minimum depth must come from the non-null child.
- If both children exist, take the minimum of the two depths.

This correctly avoids counting paths that end prematurely at null nodes.

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree due to recursion stack.
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            leftMin = dfs(node.left)
            rightMin = dfs(node.right)
            if not leftMin and not rightMin:
                return 1
            elif not rightMin:
                return leftMin + 1
            elif not leftMin:
                return rightMin + 1
            else:
                return min(leftMin + 1, rightMin + 1)
        
        return dfs(root)
        
