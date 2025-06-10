"""
Idea:
Use BFS algorithm to serialize and deserialize a binary tree, since the leetcode input array represent binary tree is always layer by layer.
BFS alogrithm:
Create a deque to store the node that left for visit
Create while loop, and do the following
pop the leftmost node in the deque:
  visit that leftmost node, append its left and right child to the deque
if the leftmost node is null, continue the loop
The while loop ends until the deque is empty

BFS allow us to visit binary tree layer by layer    

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    
    def serialize(self, root):

        res = ""
        de = deque([root])
        
        while de:
            curr = de.popleft()
            if curr: 
                res += str(curr.val) + ","
                de.append(curr.left)
                de.append(curr.right)
            else: res += "N,"
          
        return res[0:len(res) - 1]
       
            
    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "N":
            return None
        deq = deque(vals)
        node_q = deque([])
        root = TreeNode(deq.popleft())
        node_q.append(root)
        while deq:
            curr = node_q.popleft()
            if curr:
                left = deq.popleft()
                right = deq.popleft()
                curr.left = TreeNode(int(left)) if left != "N" else None
                curr.right = TreeNode(int(right)) if right != "N" else None
                node_q.append(curr.left)
                node_q.append(curr.right)
            
        return root



"""
DFS Approach (preorder traversal)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # DFS preorder traversal approach
    def serialize(self, root):
        self.strs = ""
        def dfs(root):
            if not root:
                self.strs += "N,"
                return
                 
            self.strs += str(root.val) + ","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        
        return self.strs[0: len(self.strs) - 1]
            
    def deserialize(self, data):
        if data[0] == "N":
            return
        vals = data.split(",")
       
        def dfs(idx):
            if vals[idx] == "N":
                return None, idx
            curr = TreeNode(int(vals[idx]))
            curr.left, idx = dfs(idx + 1)
            curr.right, idx = dfs(idx + 1)
            return curr, idx

        root, i = dfs(0)
        return root

            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
