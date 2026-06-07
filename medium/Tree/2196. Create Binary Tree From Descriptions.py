"""
Builds a binary tree directly from the given parent-child descriptions.

A hashmap is used to store and reuse TreeNode objects by their values.
For each description, the parent and child nodes are created if they do
not already exist, then the child is connected to either the left or
right side of the parent.

A set is used to track all values that appear as children. After all
connections are built, the root is the only node value in the hashmap
that never appears in the child set.

Time Complexity: O(n), where n is the number of descriptions.
Space Complexity: O(n), for the hashmap of nodes and the child set.
"""
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        nodeMap = {}

        for parent, child, isLeft in descriptions:
            children.add(child)
            parent_node = None
            if parent in nodeMap:
                parent_node = nodeMap[parent]
            else:
                parent_node = TreeNode(parent)
                nodeMap[parent] = parent_node
            child_node = None
            if child in nodeMap:
                child_node = nodeMap[child]
            else:
                child_node = TreeNode(child)
                nodeMap[child] = child_node
            if isLeft == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        for key in nodeMap:
            if key not in children:
                return nodeMap[key]
              

"""
# Solution 2
Builds a binary tree from parent-child descriptions.

Each description contains [parent, child, isLeft], where isLeft indicates
whether the child should be attached as the left or right child of the parent.

The root is found by taking the node that appears as a parent but never
appears as a child. After finding the root, BFS is used to construct the
tree level by level using the stored parent-to-child relationships.

Time Complexity: O(n), where n is the number of descriptions.
Space Complexity: O(n), for storing relationships, parent/child sets,
and the BFS queue.
"""
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        des_set = defaultdict(list)
        parent_set = set()
        child_set = set()
        for par, chi, isLeft in descriptions:
            des_set[par].append((chi, isLeft))
            parent_set.add(par)
            child_set.add(chi)
            
        root = TreeNode(next(iter(parent_set - child_set)))
        dq = deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                for chi, isLeft in des_set[node.val]:
                    child = TreeNode(chi)
                    if isLeft == 1:
                        node.left = child
                    else:
                        node.right = child
                    dq.append(child)
        return root
                        
        

        
        
