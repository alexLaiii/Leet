"""
Balance a Binary Search Tree.

Key idea:
A BST's inorder traversal visits nodes in sorted order. Therefore, we can first
convert the BST into a sorted array, then rebuild a balanced BST from that array.

To build the balanced tree, repeatedly choose the middle element of the current
subarray as the root. The left half becomes the left subtree, and the right half
becomes the right subtree. Choosing the middle each time keeps the height as
small as possible, giving a height-balanced BST.

Steps:
1. Run inorder traversal on the original BST to collect all values in sorted order.
2. Recursively build a new tree from the sorted array:
   - Pick the middle index as the root.
   - Build the left subtree from the left half.
   - Build the right subtree from the right half.

Why this works:
- Inorder traversal preserves the BST ordering.
- Building from the middle ensures that the number of nodes on the left and right
  sides is as balanced as possible.
- Since every recursive subtree is built the same way, the entire tree becomes
  height-balanced.

Time Complexity:
O(n), where n is the number of nodes.
Each node is visited once during inorder traversal and recreated once during rebuilding.

Space Complexity:
O(n), for the sorted array.
The recursion stack is O(h) for traversal and O(log n) for building the balanced tree,
but the original tree's traversal stack can be O(n) if the tree is completely skewed.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_arr.append(node.val)
            inorder(node.right)
     
        def create_balanced_tree(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            currNode = TreeNode(sorted_arr[mid])
            currNode.left = create_balanced_tree(start, mid - 1)
            currNode.right  = create_balanced_tree(mid + 1, end)
            return currNode
        inorder(root)
        return create_balanced_tree(0, len(sorted_arr) - 1)

