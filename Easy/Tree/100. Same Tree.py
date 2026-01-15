"""
Determine whether two binary trees are identical in both structure and node values.

Approach:
- Perform a breadth-first traversal (BFS) on both trees simultaneously using two queues.
- At each step, pop one node from each queue and compare them:
  * If both nodes are None, continue (structure matches at this position).
  * If both nodes exist and have the same value, enqueue their left and right children
    (including None) to ensure structural consistency.
  * If one node is None and the other is not, or their values differ, return False.
- After traversal, ensure both queues are empty to confirm both trees ended together.

This level-by-level comparison guarantees that both the shape and values of the trees match.

Time Complexity:  O(n), where n is the number of nodes in the trees.
Space Complexity: O(w), where w is the maximum width of the trees due to the BFS queues.
    """
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = deque([p])
        t2 = deque([q])
        while len(t1) and len(t2):
            for i in range(len(t1)):
                node1 = t1.popleft()
                node2 = t2.popleft()
                if node1 and node2 and node1.val == node2.val:
                    t1.append(node1.left)
                    t1.append(node1.right)
                    t2.append(node2.left)
                    t2.append(node2.right)
                    continue
                elif not node1 and not node2:
                    continue
                else:
                    return False
        return not t1 and not t2
            
        
