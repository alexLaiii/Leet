  """
  LeetCode 230 — Kth Smallest Element in a BST

  Return the k-th smallest key (1-indexed) from a Binary Search Tree.

  Approach
  --------
  Perform a recursive *in-order* traversal (Left → Node → Right), which
  visits BST nodes in nondecreasing order. Carry a running counter
  `count` representing how many nodes have been visited so far. When
  `count == k`, record the answer in `self.res`. A guard
  (`self.res != -1`) short-circuits deeper recursion once the result is found.

  How the helper works
  --------------------
  dfs(node, count) -> int
    - Returns the number of nodes visited after fully processing `node`’s
      subtree in in-order.
    - Invariants:
        * On entry, `count` equals nodes visited strictly before `node`’s subtree.
        * After traversing left, `count` equals nodes visited before `node`.
        * We then increment `count` for `node` itself and check `count == k`.
        * Finally, traverse right and return the updated `count`.

  Correctness
  -----------
  For a BST, in-order traversal yields a sorted sequence:
      all(left) < node < all(right).
  Thus, the k-th node encountered during in-order is exactly the k-th smallest.

  Complexity
  ----------
  Time:  O(h + k) on average with early-exit; worst-case O(n) if we must
         walk the whole tree.
  Space: O(h) recursion stack, where h is the tree height.

  Notes
  -----
  - The early-exit guard avoids unnecessary work once `self.res` is set.
  - An equivalent iterative solution uses an explicit stack and stops after
    popping the k-th node.
  - For many queries or frequent updates, an augmented BST with subtree sizes
    can answer select(k) in O(h), but that’s overkill for this problem.
  """
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        def dfs(root, count):
            if not root:
                return count
            if self.res != -1:
                return count
            count = dfs(root.left, count)
            count += 1
            if count == k:
                self.res = root.val
                return count
            count = dfs(root.right, count)
            return count
            
  
        dfs(root, 0)
        return self.res

        
