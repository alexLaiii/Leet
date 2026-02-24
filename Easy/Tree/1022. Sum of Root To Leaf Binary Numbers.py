"""
Computes the sum of all root-to-leaf binary numbers in a binary tree.

Each root-to-leaf path represents a binary number formed by concatenating
the node values (0 or 1). This method performs a depth-first search (DFS)
to explore every path, builds the binary string along the way, and converts
each complete path to its decimal value using base-2 conversion.

Approach:
- Use DFS with backtracking.
- Maintain a list `path` storing the binary digits along the current path.
- When a leaf node is reached, convert the joined path into an integer
  using `int(binary_string, 2)`.
- Backtrack by popping the last digit after each recursive call.

Time Complexity:
- O(n * h), where n is the number of nodes and h is the height of the tree.
  (Each leaf conversion may take up to O(h) time to join the string.)

Space Complexity:
- O(h) for recursion stack and path storage.

Args:
    root (TreeNode): Root of the binary tree.

Returns:
    int: Sum of all root-to-leaf binary values.
"""
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(path, node):
            if not node:
                return 0
            path.append(str(node.val))
            if not node.left and not node.right:
                path = "".join(path)
                return int(path, 2)
            
            leftRes = 0
            rightRes = 0
            if node.left:
                leftRes = dfs(path, node.left)
                path.pop()
            if node.right:
                rightRes = dfs(path, node.right)
                path.pop()

            return leftRes +rightRes
        return dfs([], root)
        
            
            
                
                        
