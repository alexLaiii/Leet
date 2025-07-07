"""
idea:
We perform a standard BFS (level-order traversal) with a twist: at each level, we alternate the traversal direction.
- `direction = 0` means left-to-right
- `direction = 1` means right-to-left

To handle the zigzag pattern efficiently, we preallocate the `level` array:
    level = [0] * len(dq)
This works because in BFS, the number of nodes at the current level is known in advance (i.e., len(dq)).

We then fill in the `level` array during traversal:
    if direction == 0:
        level[i] = curr_node.val  # left to right
    else:
        level[-(i + 1)] = curr_node.val  # right to left

This avoids the need to reverse the array at the end of each level, making it more efficient.

We only add `curr_node.left` and `curr_node.right` to the deque if they are not None,
ensuring we don't insert nulls that would break the level count or processing logic.

After processing each level, we flip the direction:
    direction = 1 - direction
to alternate between left-to-right and right-to-left for the next level.

Time Complexity: O(n)
- Each node is visited once.

Space Complexity: O(n)
- deque: stores up to n nodes in worst case.
- level + res: both contribute O(n) space total.
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
