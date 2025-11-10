"""
Connect each node’s `next` pointer to its immediate neighbor on the right
within the same level of a perfect binary tree using BFS.

Approach
--------
Perform a level-order traversal with a queue. For each level:
- Let `level_size` be the number of nodes currently in the queue.
- Pop nodes one-by-one. For the i-th node in this level (0-indexed),
  set `node.next` to the queue’s front (`dq[0]`) iff `i < level_size - 1`
  (i.e., it has a neighbor on the same level).
- Push children (left then right) into the queue to process the next level.

Correctness
-----------
During a level, the queue initially contains exactly the nodes of that level
in left-to-right order. After popping a node, the front of the queue
remains the next node in the same level until the last node of the level
is popped, because children are only appended to the back. Thus peeking
`dq[0]` yields the correct right neighbor for all non-last nodes.

Complexity
----------
Time:  O(N) — each node is enqueued and dequeued once.
Space: O(W) — W is the maximum width of the tree (queue for level-order).

Returns
-------
The root with all `next` pointers populated.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        dq = deque([root])
        while dq:
            n = len(dq) - 1
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                if n > i:
                    node.next = dq[0]
        return root
    
                
            
        
