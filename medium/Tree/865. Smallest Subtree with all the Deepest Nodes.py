  """
  Solves LeetCode 865 (Smallest Subtree with all the Deepest Nodes)
  using a single bottom-up DFS with a tuple return.

  Core idea:
  -----------
  Perform one DFS where each recursive call returns a tuple:
      (deepest_depth_in_subtree, subtree_root_covering_all_deepest_nodes)

  DFS invariant:
  --------------
  For any node `node`, dfs(node, depth) returns:
  - the maximum depth reached by any leaf in the subtree rooted at `node`
  - the root of the smallest subtree that contains *all* nodes at that depth

  Transition logic:
  -----------------
  - Recursively compute results for left and right children.
  - If both subtrees reach the same maximum depth, then the current node
    is the lowest common ancestor (LCA) of all deepest nodes.
  - If one subtree is deeper, propagate that subtree's result upward
    unchanged.

  Base case:
  ----------
  - If the node is None, return the current depth and None as the subtree root.

  Why this works:
  ---------------
  - The deepest nodes must lie entirely in one subtree, or in both.
  - When depths are equal, the current node is the smallest subtree
    covering all deepest nodes.
  - When depths differ, the deeper side fully determines the answer.

  Complexity:
  -----------
  - Time: O(n), where n is the number of nodes (single DFS traversal)
  - Space: O(h), where h is the height of the tree (recursion stack)

  This is the standard and optimal one-pass DFS solution for this problem.
  """
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return (depth, None)
            leftdepth, ancesLeft = dfs(node.left, depth + 1)
            rightdepth, ancesRight = dfs(node.right, depth + 1)
            if leftdepth == rightdepth:
                return (max(leftdepth, rightdepth), node)
            return (leftdepth, ancesLeft) if leftdepth > rightdepth else (rightdepth, ancesRight)
        d, res = dfs(root, 0)
        return res
                
        
