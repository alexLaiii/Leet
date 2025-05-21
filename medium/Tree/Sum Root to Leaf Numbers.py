"""
Classy Tree traversal problem:
Intuition: 
First create an global array to store all the number of all route
1. traverse to the left most sub treee first, if arrived leaf node, append the nnumber to the global array
2. left sub tree, finished, traverse to the right node, same logic
3. call the helper function recursively until all the subtree are traversed
4. loopthrough the global array and add all the numbers to sums
5. return sums
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        nums, sums = [], 0
        
        def sumNumbersHelper(root, nums_str):
            if not root:
                return 0

            # Since string is immutable object in python, the string modification inside this fucntion will not 
            # affect the nums_str outside, so I don't need to do "nums_str = nums_str[:-1]" (aka pop the last 
            # value to backtrack) like an array, since it will not affect the string in the other stack
            nums_str  += str(root.val)
            if not root.left and not root.right:
                return nums.append(nums_str)
                
            sumNumbersHelper(root.left, nums_str)
            sumNumbersHelper(root.right, nums_str)
            
        sumNumbersHelper(root, "")
        for n in nums:
            sums += int(n)
        return sums

        return sumNumbersHelper(root, "", sums)
     
            

        
        
