    """
    Flatten a binary tree to a right-leaning linked list in-place
    following preorder (root → left → right).

    Method (iterative preorder with stack + sentinel):
    - Push right child first, then left child, so left is processed first.
    - Pop a node `cur`, detach its children (`cur.left = cur.right = None`)
      to avoid stale pointers, and stitch it after `prev` via `prev.right = cur`.
    - Advance `prev = cur`. Repeat until stack is empty.

    Invariants:
    - `stack` always holds the next preorder nodes (right before left ensures preorder).
    - `prev` is the tail of the already-flattened chain; all nodes in the chain have `left = None`.
    - Each original node is visited and linked exactly once.

    Correctness:
    - Nodes are produced in preorder by the stack discipline, and we link in that same order,
      so the final right-only chain is exactly the preorder sequence.

    Complexity:
    - Time O(n) (each node pushed/popped once); Space O(n) for the stack.

    Notes:
    - The sentinel `prev = TreeNode()` is just a convenience; you could start with `prev = None`
      and handle the first link conditionally.
    - An O(1)-extra-space variant exists (Morris-style): splice the rightmost node of the left
      subtree to the current right, then rotate left to right and advance.
    """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
           
            stack = [root]
            prev = TreeNode()
            while stack:
                currNode = stack.pop()
                if currNode.right:
                    stack.append(currNode.right)
                    currNode.right = None
                if currNode.left:
                    stack.append(currNode.left)
                    currNode.left = None
                prev.right = currNode
                prev = prev.right

# Recursive approach
"""
Flatten a binary tree to a right-leaning linked list **in preorder** (root → left → right),
modifying the tree in-place.

Core idea (preorder stitching with a moving tail):
- Maintain `self.prev` as the tail of the already-flattened prefix.
- On visiting `root`:
  1) Snapshot `rightNode = root.right` **before** recursing left (we'll overwrite pointers).
  2) If `self.prev` exists, link it to `root` via `self.prev.right = root` and nullify
     `self.prev.left = None`. This stitches `root` after the current tail.
  3) Advance the tail: `self.prev = root`.
  4) Recurse into `root.left`, then into the saved `rightNode`.

Why it works:
- Calls happen in preorder, and each call stitches the current node after the previous one.
- We clear `left` pointers by setting `prev.left = None` at the moment we link `prev → root`.
  Every node eventually becomes `prev` for its successor, so **all** left pointers end up `None`.
- Saving `rightNode` is essential: after linking, `root.right` may be repurposed to point to the
  next preorder node (its left child), so we would otherwise lose the original right subtree.

Correctness invariant:
- At any time, the nodes already visited form a single right-only chain in preorder.

Complexity:
- Time O(n): each node is visited once.
- Space O(h): recursion stack height `h` (worst-case `n` for a skewed tree).
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(root):
            if not root:
                return None
            rightNode = root.right
            if self.prev:
                self.prev.right = root
                self.prev.left = None
            self.prev = root
            dfs(root.left)
            dfs(rightNode)
        dfs(root)
