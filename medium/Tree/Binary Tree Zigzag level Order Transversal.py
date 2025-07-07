"""
ideaur:
standard BFS use direction to mark travel from left or right 
 direction = 0 (left) direction = 1 (right)
  level = [0] * len(dq)
because we are doing bfs uhhh dee dee number of nodes in deque is predetermined so we can fix the size of the level array 
                if direction == 0:
                    level[i] = curr_node.val
                else:
                    level[-(i + 1)] = curr_node.val
         from left, just append to the level in the normal way
         from right, append from the back of the array

since we want a correct length of level, only add to deque when what the node is not None.
              direction = 1 - direction
left right zig zag

time complexity: O(n)
space complexity: O(n), deque: O(n)
                  level + res: O(n)
"""
        



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        direction = 0
        res = []
        while dq:
            level = [0] * len(dq)
            for i in range(len(dq)):
                curr_node = dq.popleft()
                if direction == 0:
                    level[i] = curr_node.val
                else:
                    level[-(i + 1)] = curr_node.val
                if curr_node.left:
                    dq.append(curr_node.left)
                if curr_node.right:
                    dq.append(curr_node.right)
            res.append(level)
            direction = 1 - direction
        return res
