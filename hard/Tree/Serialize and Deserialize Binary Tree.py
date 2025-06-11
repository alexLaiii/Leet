"""
Idea:
BFS approach
Use **BFS (level-order traversal)** to serialize and deserialize a binary tree.
This matches how LeetCode represents trees as arrays: **layer by layer (top-down)**.
Example for this tree:
        1
       / \
      2   3
         / \
        4   5
The represented list will be 
[1,2,3,null,null,4,5,null,null,null,null]

Serialize:
- Use a deque to perform BFS.
- For each node:
  - If it's not null, append its value to the result and enqueue its left and right children.
  - If it's null, append a special marker (e.g. "N") to represent null.
- Convert the result list to a comma-separated string.

Deserialize:
- Split the serialized string into a list of values.
- Use a deque to rebuild the tree:
  - The first value becomes the root.
  - Use a queue to track nodes whose children are yet to be assigned.
  - Read values one by one, assigning them as left and right children in BFS order.
  - Use "N" to detect and skip null children.

This method ensures that the serialized and deserialized trees maintain the exact structure.

Note:
You must use the **same traversal order** for both serialization and deserialization.
If you serialize with preorder, you must also deserialize using preorder.
The format (string/list order) is traversal-dependent and not interchangeable across strategies (e.g., BFS vs DFS).

Thus, 
if you use BFS on serialize, you must use BFS on deserialize.
if you use DFS on serialize, you must use BFS on deserialize.
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
        res = []
        deq = deque([])
        deq.append(root)
        while deq:
            curr = deq.popleft()
            if not curr:
                res.append("N")
                continue
            res.append(str(curr.val))
            deq.append(curr.left)
            deq.append(curr.right)
        
        return  ",".join(res)
    def deserialize(self, data):
        if data == "N":
            return
        vals = data.split(",")
        deq = deque(vals)
        root = TreeNode(int(deq.popleft()))
        node_q = deque([root])
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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
DFS approach (Preorder Traversal)

We use a recursive preorder traversal to serialize the binary tree. This means:
- Visit the current node
- Recurse into the left subtree
- Recurse into the right subtree

For null nodes, we record a placeholder like "N" to preserve structure.

Example Tree:
        1
       / \
      2   3
         / \
        4   5

Serialized list using preorder DFS:
[1, 2, N, N, 3, 4, N, N, 5, N, N]

Note:
You must use the **same traversal order** for both serialization and deserialization.
If you serialize with preorder, you must also deserialize using preorder.
The format (string/list order) is traversal-dependent and not interchangeable across strategies (e.g., BFS vs DFS).

Thus, 
if you use BFS on serialize, you must use BFS on deserialize
if you use DFS on serialize, you must use BFS on deserialize
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        if data == "N":
            return
        vals = data.split(",")
        def dfs(idx):
            if vals[idx] == "N":
                return None, idx
            root = TreeNode(int(vals[idx]))
            root.left, idx = dfs(idx + 1)
            root.right, idx = dfs(idx + 1)
            return root, idx
        res, i = dfs(0)
        return res

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
