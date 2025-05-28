"""
PathSum III:

Idea:
Use nested recursion to count how many valid paths (with any start and end point) sum to the target.
For each node in the tree, start a DFS that checks all downward paths from that node.

Implementation:

- The outer recursive function `each_node(root)`:
  Traverses every node in the tree.
  For each node, it calls `dfs()` to count how many valid paths start from that node.
  Then recursively processes the left and right subtrees.
  Returns the total number of valid paths in the entire tree.

- The inner recursive function `dfs(root, target)`:
  Traverses all downward paths starting at the current node.
  If `root.val == target`, increment the count.
  Subtract `root.val` from the target at each step and continue DFS on left and right.
  Returns the total number of valid paths starting from that node.

Note:
- The logic inside `dfs()` is similar to PathSum II: it checks the sum of values along a path going downward from a node.
- However, unlike PathSum II, the path does **not** need to end at a leaf.
- You count a path **as soon as it reaches the target**, and keep exploring further paths below.
- The count starts from the bottom (base case returns 0 because the root is null), and as the recursion backtracks, 
  each layer returns its local count plus the counts from left and right subtrees. 
  This replaces the need for a global counter and guarantees accurate accumulation.
- No global variable is used — all results are returned through recursive calls.

Time Complexity:
- O(n²) in the worst case:
  - For each of the n nodes, `dfs()` may visit up to O(n) nodes.
  - So total = O(n × n)

Space Complexity:
- O(h), where h is the height of the tree (due to recursion stack)
- No extra data structures used → auxiliary space is O(1) if recursion is not counted
"""



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

            
            
