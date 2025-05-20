"""
Example input, output: 
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Intuition:
We use preorder traversal (root → left → right) to explore all root-to-leaf paths.
At each step, we:
1. Add node.val to a running path[] list to track the current path.
2. Maintain a prefix_sum (or current_sum) to keep track of the total so far.

If we reach a leaf node and prefix_sum + node.val == targetSum,
we deep copy the path (path[:]) into the result array.
After visiting left and right children, we backtrack by popping the current node from the path — this allows the path to be reused when returning to the parent node.
This process recursively checks every path from the root to each leaf.

Time Complexity: O(n)
We visit every node exactly once.

Space Complexity:
O(log n) for a balanced tree (height of recursion stack)
O(n) in the worst case (e.g. skewed tree)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        def pathSumHelper(root,prefix_sum, path):
            if not root: 
                return
       
            path.append(root.val)
            if prefix_sum + root.val == targetSum and not root.left and not root.right:
                result.append(path[:])
            pathSumHelper(root.right, prefix_sum + root.val, path)
            pathSumHelper(root.left, prefix_sum + root.val, path)
            path.pop()
        
        pathSumHelper(root, 0, [])
        
        return result
        
    
