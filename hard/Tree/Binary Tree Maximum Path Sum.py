"""
Leetcode 124: Binary Tree Maximum Path Sum

Congrats to my first hard problem solved with very little hint!

Idea:
Since we want to find the **maximum path sum**, we apply the same idea as Leetcode 53: Maximum Subarray —
**ignore negative branches** by resetting them to 0, because negative sums would only reduce the total.

Implementation:
- Use DFS to search the binary tree.
- At each node:
    1. Recursively get left and right subtree max path sums.
    2. If any of them are negative, reset them to 0 (don't include in path).
    3. Check if the current path through this node (`left + right + node.val`) is greater than `self.maxs`, and update it.
    4. Return the maximum **one-branch path** (`max(left, right) + node.val`) to the parent.
SideNote:
Since left and right are always >= 0 after pruning, we do NOT need to check:
    (left + root.val) or (right + root.val)
for updating the global max — they will always be <= (left + right + root.val).


Why not return (left + right + node.val) to the parent?
Because we can only choose one branch when passing the value upward — we cannot fork the path above.
Example:
Assume the current root is 20. To its parent (10), we can only return:
    max(20 + 15, 20 + 7)
The full sum 20 + 15 + 7 is valid **as a complete path**, but cannot be extended upward.

Tree structure for reference:
        10
       /  \
      9    20
          /  \
        15    7

Valid paths:
- 15 → 20 → 7 (valid full path)
- 10 → 20 → 15 or 10 → 20 → 7 (valid one-sided paths)
- NOT: 10 → 20 → 15 → 20 → 7 (invalid, revisits/forks)

Time Complexity: O(n), where n = number of nodes (each visited once)
Space Complexity: O(h), where h = height of the tree (recursion stack)

:type root: TreeNode
:rtype: int
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxs = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right =  dfs(root.right)
            
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            # Since left and right is never smaller than 0 by greedy fix, we don't need to check (left + root.val and right + root.val), as it will always smaller or equals to (left + right + root.val)
            # self.maxs = max(self.maxs, left + right + root.val, left + root.val, right + root.val)
            self.maxs = max(self.maxs, left + right + root.val)
            return max(left + root.val, right + root.val)
        dfs(root)
     
        return self.maxs
            

            



        
