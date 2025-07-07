"""
This problem uses a similar approach as:
→ 105. Construct Binary Tree from Preorder and Inorder Traversal.

Key insights:
- The root is always the **last element** of the postorder traversal.
- By searching for the root in the inorder list, we can determine how many nodes are in the left and right subtrees.
    - We use this to partition both the inorder and postorder lists.
    - Note: inorder and postorder must have the **same values**, otherwise partitioning will be incorrect.

---

Example walkthrough:

inorder:     [9, 3, 15, 20, 7]  
postorder:   [9, 15, 7, 20, 3]

→ root = 3  
  inorder index of 3 = 1

Left subtree:
  inorder[:mid]       = [9]
  postorder[:mid]     = [9]

Right subtree:
  inorder[mid+1:]     = [15, 20, 7]
  postorder[mid:-1]   = [15, 7, 20]

→ recurse left: root = 9
    inorder: [], postorder: [] → base case → return None

→ recurse right: root = 20
    inorder index of 20 = 1

    Left:
      inorder[:mid]     = [15]
      postorder[:mid]   = [15]
    Right:
      inorder[mid+1:]   = [7]
      postorder[mid:-1] = [7]

    → recurse left: root = 15 → base case (empty left/right) → return
    → recurse right: root = 7 → base case (empty left/right) → return

---

Time Complexity: O(n²)
- `inorder.index()` is O(n) in each recursion.
- Total of n nodes = O(n²) in worst case (e.g., skewed tree)

Space Complexity:
- Call stack: O(n) in worst case (unbalanced tree)
- Python slicing creates new arrays → additional O(n) per level
- So total space: **O(n²)** due to slicing, even though the code doesn't explicitly use extra structures.
"""



class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:len(postorder) - 1])
        return root
