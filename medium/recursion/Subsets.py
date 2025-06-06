"""
If forget how to do this problem, revisit "Combination sum", this problem is much easier than "Combination Sum 2".
Idea:
Since order is matter in subset, for exampe [1,2,3], [1,2] is a subset, [1,3] is a subset, but [2,1] is not since the order has changed
And given the constraint that: "All the numbers of nums are unique.", this problem is much easier
The core idea is a decision tree recursion problem, where:

Example: [1,2,3]
At the first level, 
choose 1, [1]:
  choose 2, [1,2]:
    choose 3, [1,2,3]:
  choose 3, [1,3]:
choose 2, [2]:
  choose 3, [2,3]:
choose 3, [3]:

As we can see the base case is whenever the index reach the end of the array, (the beauty of order matters problem)
Thus, we have base case: if start == len(nums): return

Implementation:
append every current path at each level, such we want all the subsets,
when backtracking, pop the last element, because we are going to a new branch but preserve the previous path

Time Complexity:
O(2^n): There are total 2^n subsets(including the empty subsets), so there will be ran through 2^n nodes
Space Complexity:
O(n * 2^n): Since there are 2^n subsets, and each subsets can be grow to n size, so n* 2^n

"""

class Solution(object):
    def subsets(self, nums):
        res = [[]]
        def dfs(start, path):
            if start == len(nums):
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                res.append(path[:])
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
     
        return res
            

