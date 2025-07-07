"""
This problem use similar approach as "105.Construct Binary Tree from Preorder and Inorder Traversal.

Key thing to notice in this problem.
-> The root always in the last element of postorder traversal
-> By searching the root inorder list, we can get the information on how many children in the left subtree and how many children in the right subtree of the current know.
    - Use that information to partition the Inorder and Postorder list, so we can recursively built the subtree.
    - Note that the value in Inorder and Postorder must be the same, otherwise we must perform wrong partition logic
Example walkthrough:
inorder:  [9,3,15,20,7]
postorder:[9,15,7,20,3]

-> root = 3,  {left: mid = 1, inorder[:mid] = [9], postorder[:mid] = [9]} : {right: mid = 1, inorder[mid+1:] = [15,20,7], postorder[mid:len(postorder) - 1] = [15,7,20]
  -> root = 9, {left: mid = 0, inorder[:mid] = [], postorder[:mid] = []} : {right: mid = 0, inorder[mid+1:] = [], postorder[mid:len(postorder)-1] = []}
  -> root = 20, {left: mid = 1, inorder[:mid] = [15], postorder[:mid] = [15]] : {right: mid = 1, inorder[mid+1] =[7], postpder[mid:len(postorder)-1] = [7]}
    -> base -> return None
    -> root = 15, {left: mid = 0, inorder[:mid] = [], postorder[:mid] = []} : {right: mid = 0, inorder[mid+1:] = [], postorder[mid:len(postorder)-1] = []}
    -> root = 7, {left: mid = 0, inorder[:mid] = [], postorder[:mid] = []} : {right: mid = 0, inorder[mid+1:] = [], postorder[mid:len(postorder)-1] = []}
      -> base -> return None
      -> base -> return None

time complexity: O(n^2) 
space complexity: O(1)
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
