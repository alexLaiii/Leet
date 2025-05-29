"""
Leetcode 236: Lowest Common Ancestor of a Binary Tree

This problem is not intuitive at all — I couldn't solve it on my own the first time.

Assumptions given by the problem:
- All Node.val values are unique
- p != q
- Both p and q exist in the tree

Idea:
Since the tree is **unsorted**, we need to **search the entire tree**.

We perform DFS. Along the way, if the current node is equal to p or q, we return that node.
We don’t care which one it is — as long as it matches, we bubble it up.

As we backtrack:
- If both `found_1` and `found_2` are not None, that means one target node was found in each subtree.
- Therefore, the current `root` is their **lowest common ancestor** — we return it.

From this point onward, the result won’t change because:
- The problem guarantees **only one unique LCA**.
- Any recursive calls above this level will **not trigger the `found_1 and found_2` condition** again.

Time Complexity:
- O(n) → We visit each node once with DFS.

Space Complexity:
- O(h) → due to recursion stack (h = tree height). Worst case O(n), best case O(log n) for balanced trees.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # This is DFS problem
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        found_1 = self.lowestCommonAncestor(root.left, p, q)
        found_2 = self.lowestCommonAncestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            return root
        if found_1 and found_2:
            return root
        return found_1 if found_1 else found_2

