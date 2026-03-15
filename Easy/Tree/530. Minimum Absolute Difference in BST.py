"""
Return the minimum absolute difference between values of any two nodes in a BST.

This solution performs an inorder traversal of the binary search tree, which
visits the node values in sorted order. Since the values are sorted, the
minimum absolute difference must occur between two consecutive values in the
inorder sequence.

Steps:
1. Traverse the BST inorder and store node values in a list.
2. Scan the sorted list once and compute the minimum difference between
   adjacent elements.
3. Return the smallest difference found.

Time Complexity:
    O(n), where n is the number of nodes in the tree.

Space Complexity:
    O(n), due to the inorder list storing all node values
    (ignoring recursion stack).
"""
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sortedNum = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            sortedNum.append(node.val)
            dfs(node.right)
        dfs(root)
        res = float("inf")
        for i in range(1, len(sortedNum)):
            res = min(res, sortedNum[i] - sortedNum[i-1])
        return res
