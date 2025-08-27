"""
Easy one:
Perform level-order traversal (BFS) on an N-ary tree.

Idea:
-----
We use a queue (deque) to process nodes level by level:
- At each iteration, take all nodes currently in the queue as the current level.
- Record their values in a list.
- Enqueue all their children for the next level.

Why it works:
-------------
- By iterating `for i in range(len(dq))`, we ensure we only process
  the nodes that belong to the current level, even though the queue
  grows as children are added.
- This naturally separates the tree into levels without needing extra markers.

Complexity:
-----------
- Time: O(N), where N = number of nodes (each node visited once).
- Space: O(N), for the queue which in the worst case may hold one full level.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        dq = deque([root])
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                for child in node.children:
                    dq.append(child)
            res.append(level.copy())

        return res
                
        
