"""
Classy Tree traversal problem:
Intuition: 
DFS alogorithm:
1. traverse to the left most node, during the traversel add each node value to nums and pass it to the next node
2. By doing that to both left side and right side, so I can get the return value from both left and right side.
3. add the left Sum and right Sum together, return it to the root, so each sum of the subtree is being track
4. reursively doing this process, so every subtree's sum is returned to the root
5. Therefore, the top root will return the sum of both subtree on the left and subtree on the right
Side Note:
I times 10 to nums here, so 4->9->5 will become 495
Since 4 * 10 + 9 = 49, and 49 * 10 + 5 = 495, which match the problem's requirements 
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def sumNumbersHelper(root, nums):

            if not root:
                return 0
            # I times 10 to nums here, so 4->9->5 will become 495
            # Since 4 * 10 + 9 = 49, and 49 * 10 + 5 = 495, which match the problem requirements 
            nums = nums * 10 + root.val
            if not root.left and not root.right:
                return nums
                
            l_sum= sumNumbersHelper(root.left, nums)
            r_sum = sumNumbersHelper(root.right, nums)
            
            return l_sum + r_sum
            
        return sumNumbersHelper(root, 0)
   


        

        
        
     
            

        
        
