"""
Merges two binary trees by summing overlapping nodes using depth-first search.

At each corresponding position in the trees:
- If both nodes exist, their values are added and merged recursively.
- If only one node exists, that node (and its subtree) is returned directly.
- If neither node exists, None is returned.

The merge is performed in-place on root1 to avoid creating new nodes.

Args:
    root1 (Optional[TreeNode]): Root of the first binary tree.
    root2 (Optional[TreeNode]): Root of the second binary tree.

Returns:
    Optional[TreeNode]: The root of the merged binary tree.

Time Complexity:
    O(n), where n is the total number of nodes visited across both trees.

Space Complexity:
    O(h), where h is the height of the merged tree due to recursion stack.
"""
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            
            node1.val += node2.val
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right, node2.right)
            return node1
            
        return dfs(root1, root2)
        

        
