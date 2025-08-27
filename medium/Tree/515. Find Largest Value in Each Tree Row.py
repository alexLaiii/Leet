"""
Simple one:
Perform BFS on the binary Tree and keep track of the largest one on each level, then append to the result.
Should Quit If I can't solve this myself later.
"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        dq = deque([root])
        while dq:
            largest = dq[0].val
            for i in range(len(dq)):
                currNode = dq.popleft()
                largest = max(largest, currNode.val)
                if currNode.left:
                    dq.append(currNode.left)
                if currNode.right:
                    dq.append(currNode.right)
            res.append(largest)
        return res


        
