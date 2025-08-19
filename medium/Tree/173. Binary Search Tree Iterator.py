
    """
    Inorder (ascending) iterator over a Binary Search Tree using an explicit stack.

    Core idea / invariant
    ---------------------
    Maintain a stack that always contains the current **left spine** of the
    yet-to-be-visited portion of the tree. The **top of the stack** is the next
    node to output in inorder. We only ever "dive left" in two moments:
      1) during initialization, starting from `root`
      2) after popping a node that has a right child (then push that right
         child's entire left spine)

    Why this works
    --------------
    Inorder traversal is `left -> node -> right`. Preloading the left spine
    means the smallest (next) node is at the top. When we visit (pop) a node,
    its left subtree is already consumed; to continue inorder we must explore
    its right subtree, but even there we must visit the **leftmost** node first,
    so we push that right subtree's left spine. We never re-dive into a left
    that's already processed, because the stack only records paths whose left
    subtrees are done.

    Complexity
    ----------
    - Space:  O(h), where h is the tree height (the stack holds at most one
              root-to-leaf path at a time).
    - Time:   `next()` is amortized O(1): each node is pushed once and popped
              once across the entire iteration.

    Notes on BST vs BT
    ------------------
    The mechanism works for any binary tree, but the problem is meaningful for
    **BSTs** because inorder traversal yields values in **sorted** order.

    Mini dry run
    ------------
      Tree:      7
                / \
               3  15
                 /  \
                9    20

      init stack (bottom->top): [7, 3]
      next -> pop 3  -> output 3        (no right)      stack: [7]
      next -> pop 7  -> output 7        (has right=15)  push left spine of 15: [15, 9]
      next -> pop 9  -> output 9        (no right)      stack: [15]
      next -> pop 15 -> output 15       (has right=20)  push [20]
      next -> pop 20 -> output 20       (done)
    """
class BSTIterator:
  
    def __init__(self, root: Optional[TreeNode]):
        """
        Preload the iterator by pushing the left spine from `root` onto the stack.
        After this, the top of the stack is the smallest element (the first inorder node).
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        """
        Return the next smallest value and advance the iterator.

        Steps:
        1) Pop the top node `ans` (this is the next inorder node).
        2) If `ans` has a right child, push that right child's **left spine**
           (walk `right`, then repeatedly `left`) onto the stack to restore
           the invariant that the stack top is the next inorder node.
        3) Return `ans.val`.

        Amortized O(1): each node is pushed once (when discovered) and popped once (when visited).
        """
        ans = self.stack.pop()
        curr = ans
        if curr.right:
            curr = curr.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return ans.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
