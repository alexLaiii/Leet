        """
        Solves the Combination Sum problem using DFS + backtracking.

        At each recursive step, we explore combinations that add up to the target.
        Each candidate can be reused unlimited times.

        To avoid duplicate combinations (e.g., [2,2,3] vs [2,3,2]), we use a `start` index
        to ensure we only consider candidates at or after the current position,
        effectively avoiding permutations and ensuring uniqueness.

        Time Complexity:
            O(2^t) — where t is the target value.
            Each number can be either included or not at each level, forming a binary decision tree.
            Worst-case occurs when target is built from many small values (e.g., lots of 1s).

        Space Complexity:
            O(t) — maximum recursion depth in the worst case (e.g., all 1s to reach target).
            Output space depends on number of valid combinations.

        Approach:
            - Backtrack only when current sum ≤ target
            - Append valid paths when current sum == target
            - Use `start` index to avoid revisiting earlier candidates (preventing duplicates)
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
        
