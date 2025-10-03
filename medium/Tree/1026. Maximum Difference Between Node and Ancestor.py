"""
Return the maximum Difference between ancestor and children node |ancestor.val - node.val| in a binary tree.

Approach:
  Depth-first search while carrying the minimum and maximum values seen
  along the current root→node path. At each node, update (cur_min, cur_max)
  with node.val and recurse into children. When a leaf/null is reached,
  the best possible difference for that path is cur_max - cur_min.

Why it works:
  For any node, the ancestor that maximizes |ancestor - node| must be either
  the path’s minimum or maximum value. Thus tracking only (min, max) per path
  is sufficient; no need to remember all ancestor values.

Complexity:
  Time O(n) — each node visited once.
  Space O(h) — recursion stack (h = tree height). Handles empty tree (0).
"""



class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, largest, smallest):
            if not root:
                return 0
            if root.val > largest:
                largest = root.val
            elif root.val < smallest:
                smallest = root.val
            res = largest - smallest
            left_res = dfs(root.left, largest, smallest)
            right_res = dfs(root.right, largest, smallest)
            return max(res, left_res, right_res)

        return dfs(root, root.val, root.val)
       
        
