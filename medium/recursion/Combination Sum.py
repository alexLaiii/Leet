"""
Idea:
The solution of this is based on a decision Tree structure
where at each stage with have len(candidates) choice and decided we should include it or not. (Similar to "17. Letter Combinations of a Phone Number")

The constraint here is, combinations is required, that is [2,2,3] and [2,3,2] is consider as the same
So we pass an start index tothe next stage to prevent the revisit route, prevent it from causing permutations

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, start, curr_sums):
            if curr_sums > target:
                return 
            if curr_sums == target:
                res.append(path[:])
                return 
            
            for i in range(start, len(candidates)):
               
                path.append(candidates[i])
                dfs(path, i, curr_sums + candidates[i])
                path.pop()
        
        dfs([],0, 0)
        return res
        
