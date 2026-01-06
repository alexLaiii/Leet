"""
Return the 1-indexed level of a binary tree that has the maximum sum of node values.

Approach (BFS / level-order traversal):
- Use a queue (deque) initialized with the root.
- Process the tree level by level:
    * For each level, iterate exactly `len(queue)` times to consume all nodes in that level.
    * Accumulate `levelSum` from those nodes' values.
    * Push each node's non-null children into the queue for the next level.
- Track the best (level, sum) seen so far; update only when a strictly larger sum is found.
  (This preserves the smallest level index in case of ties, as required by the problem.)

Time Complexity:
- O(n), where n is the number of nodes, since each node is enqueued and dequeued once.

Space Complexity:
- O(w), where w is the maximum width of the tree (size of the largest level),
  due to the queue.

Notes:
- Assumes `root` is not None (the LeetCode constraints guarantee a non-empty tree).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        maxlevel = [1, root.val]
        level = 1
        while dq:
            levelSum = 0
            for i in range(len(dq)):
                node = dq.popleft()
                levelSum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if levelSum > maxlevel[1]:
                maxlevel = [level, levelSum]
            level += 1
        return maxlevel[0]
                
                
            
        
