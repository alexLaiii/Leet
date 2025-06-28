"""
Brain Teasing Problem, I didnt solve it myself.

Main facts to understand this problem:

1. In preorder traversal, the first value is always the current root.
2. In inorder traversal:
   - All values to the left of the root are part of the left subtree.
   - All values to the right of the root are part of the right subtree.
3. Once we find the index of the root in inorder (let's call it 'mid'), we can:
   - Slice inorder into:
     - Left: inorder[:mid]
     - Right: inorder[mid+1:]
   - Use the same 'mid' value to slice preorder accordingly:
     - Left: preorder[1:mid+1]
     - Right: preorder[mid+1:]

This works because:
- Preorder = root → left → right
- Inorder = left → root → right
- So the number of elements in the left inorder slice (i.e. 'mid') is exactly the number of elements in the left subtree.
- Even though preorder and inorder have different orders, the values in their corresponding slices are always paired and consistent.

Idea:
- Recursively take the root from preorder[0]
- Find its index in inorder to determine how to split left/right subtree
- Slice both preorder and inorder using that index
- Build left and right subtrees using the corresponding slices
- The problem recursivly build all the nodes and link all them to the root node, This is DFS-style tree construction guided by preorder (build the root node first and recursively built its child)

Time Complexity: O(n^2)
  - Each recursive call does: inorder.index(preorder[0]) → O(n) worst case
  - The recursion happens for each node, O(n) recursion called
"""


# Most Intuitive approach
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root



# Solution 2
"""
Time Complexity: O(n^2)
    - Each recursion do: mid = inorder.index(rootVal), possibly O(n)
    - The recursion happen for each node, O(n) recursion called
Space complexity: O(n)
    - recursion stack -> O(n)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        def helper(left_b, right_b):
            if left_b > right_b:
                return None
            
            rootVal = preorder[self.pre_idx]
            root = TreeNode(rootVal)
            
            mid = inorder.index(rootVal)
            
            self.pre_idx += 1
            root.left = helper(left_b, mid - 1)
            root.right = helper(mid + 1, right_b)
            
            return root
        
        return helper(0, len(inorder) - 1)
       
