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
