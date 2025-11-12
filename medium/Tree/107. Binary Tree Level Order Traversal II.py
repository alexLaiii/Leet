  """
  LeetCode 107 — Binary Tree Level Order Traversal II (Bottom-Up)

  Idea:
      Do a standard BFS level-order traversal using a queue, collecting
      node values per level from top to bottom. At the end, reverse the
      list of levels to produce bottom-up order.

  Algorithm (BFS):
      1) If root is None, return [].
      2) Initialize a deque with root. While the deque is non-empty:
         - Snapshot the current queue size `k = len(dq)`.
         - Pop exactly `k` nodes to form the current level.
         - Append children to the deque as we go.
         - Append the collected level to `res`.
      3) Reverse `res` and return it.

  Correctness:
      BFS processes nodes level by level. Each iteration extracts all nodes
      at depth d before enqueuing nodes at depth d+1, so `res` is in
      top-down order. Reversing yields bottom-up order as required.

  Complexity:
      - Time:  O(N), each node is enqueued and dequeued once.
      - Space: O(W) for the queue, where W is the tree's maximum width;
               O(L) for storing levels (overall O(N) output size).

  Edge Cases:
      - Empty tree → [].
      - Single node → [[val]].
      - Skewed trees (all left/right) still traverse correctly.

  Alternatives:
      - Build bottom-up directly by inserting each level at the front of
        a result deque (avoids the final reverse, same asymptotics).
      - DFS with depth-tracking and then reverse at the end.
  """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        dq = deque([root])
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level)
        
        res.reverse()
        return res
                
                
