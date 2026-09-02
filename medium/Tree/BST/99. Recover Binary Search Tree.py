"""Restore a BST where exactly two nodes were swapped by value.

Performs an inorder traversal, which should yield strictly increasing
values in a valid BST. `prev` plays a dual role: before the first
out-of-order pair is found, it acts as a genuine running predecessor,
updated at every node. Once the first violation (prev.val > node.val)
is detected, `prev` freezes at that node and effectively becomes the
first swapped node, while `swap2` is reassigned on every subsequent
violation so it ends up holding the correct second swapped node.
This relies on the problem's guarantee of exactly one swap; the
frozen `prev` stays greater than every node up to the true second
culprit precisely because no other node value is out of place.

Args:
    root: Root of the BST containing exactly two swapped nodes.
        Modified in place; no value is returned.

Time complexity:
    O(n), where n is the number of nodes -- each node is visited once
    during the inorder traversal.

Space complexity:
    O(h) auxiliary, where h is the tree height, from the recursive
    call stack. Worst case O(n) for a skewed tree, O(log n) for a
    balanced one. No additional data structures are allocated.
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = swap2 = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev
            if prev and prev.val > node.val:
                nonlocal swap2
                swap2 = node
            elif not swap2:
                prev = node
            dfs(node.right) 
        dfs(root)
        prev.val, swap2.val = swap2.val, prev.val
            
        
