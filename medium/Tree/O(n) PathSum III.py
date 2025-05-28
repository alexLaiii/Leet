"""
The Optimal O(n) Solution — Prefix Sum + HashMap

Idea:
We can solve this problem by traversing the tree **only once**, using the same logic as the classic problem "Subarray Sum Equals K".

- Maintain a running sum from the root to the current node — call it `prefix_sum`.
- Use a HashMap (`prefix`) to store how many times each prefix sum has occurred.
- At each node:
    - Compute the prefix from root to this node`
    - The number of valid paths that end at this node and sum to `target` is equal to:
      `prefix[curr_sum - target]`
    - This means: if there was a prefix sum `curr_sum - target` earlier in the path, 
      then the subpath between that previous point and the current node sums to `target`.

- After visiting the current node’s left and right subtrees,
  **backtrack** by decrementing the current prefix sum count in the map,
  so it doesn't interfere with other paths (standard backtracking cleanup).

This algorithm accumulates valid path counts from the bottom of the tree upward via return values,
ensuring that each recursive layer contributes to the final count without relying on a global variable.

Time Complexity: O(n)
    - Each node is visited once

Space Complexity: 
Worst case (completely unbalanced tree): O(n)
Best case (perfectly balanced tree): O(log n)
    - Due to the recursion stack and the prefix map holding at most O(log n) entries at a time
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def pathSum(self, root, targetSum):
        def dfs(root, prefix, path):
            if not root:
                return 0
            prefix += root.val
            count = path[prefix - targetSum] if prefix - targetSum in path else 0
            path[prefix] = 1 + path.get(prefix, 0)
            left = dfs(root.left, prefix, path)
            right = dfs(root.right, prefix, path)
            path[prefix] -= 1
            return count + left + right
        sums = dfs(root, 0, {0:1})
        return sums
        
        


            
            
