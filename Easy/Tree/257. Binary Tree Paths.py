"""
Returns all root-to-leaf paths in a binary tree, formatted as strings
with '->' separating node values.

Approach:
- Use depth-first search (DFS) with backtracking.
- Maintain the current path as a mutable list of strings.
- Append the current node's value when entering a node.
- When a leaf node is reached, convert the path list into the
  required string format using '->'.join(path) and store it.
- Backtrack by popping the last node value before returning
  to the caller.

Key Implementation Details:
- The path is stored as a list to allow efficient append/pop
  operations during recursion.
- The path is only converted to a string at leaf nodes to avoid
  unnecessary string construction.
- Strings appended to the result list are independent of the
  mutable path list, so later backtracking does not affect them.

Time Complexity:
- O(N * H) in the worst case, where N is the number of nodes and
  H is the height of the tree, due to joining the path at each leaf.
  (In a skewed tree, this can degrade toward O(N^2).)

Space Complexity:
- O(H) for the recursion stack and path list, excluding the output.

This solution emphasizes correctness and backtracking discipline
over premature string optimization, making it robust and
interview-friendly.
"""
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return res           
            
                    
                    
