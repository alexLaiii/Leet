"""
PathSum III:
Idea: 
Use nested recursion to check how many paths in each subtree, and sum the result of all subtree as result.

Implementation:
In the outer recursive function "each_node(root)": 
it call the dfs() function on the current root, the dfs() will return the number of paths of this subtree, 
and the recursivly call the left node( subtree in node.left)  and right node (subtree in node.right) and sum them up to return the total result

In the inner recursive function "dfs(root, target)":
it uses the Logic similar to pathSum II, but increase the count immediately once we found a route (Since a valid route in this problem does not require a root to leaf route like pathSum II)
then keep going down the tree to check for anymore valid path, remember, this function performs a root to leaf check, so the target would be subtracted by the root.value at each node before passing on
Note that the count return start from the bottom 0, andqwwqwd

"""




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def pathSum(self, root, targetSum):
        def dfs(root, target):
            if not root:
                return 0
            count = 1 if target == root.val else 0
            left = dfs(root.left, target-root.val)
            right = dfs(root.right, target-root.val)
            return count + left + right
        
        def each_node(root):
            if not root:
                return 0
            res = dfs(root, targetSum) + each_node(root.left) + each_node(root.right)
            return res
        sums = each_node(root)
        return sums 

            
            
