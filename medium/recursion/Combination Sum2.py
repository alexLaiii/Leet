"""
Idea:
Each candidate can only be used once. So, after choosing a candidate at index `i`, we must start the next recursion from `i + 1`.

The core challenge is to avoid generating duplicate combinations, since the array may contain duplicate values.

Core Idea:
The first occurrence of a number already explores all valid paths using that value, so we should skip any future duplicates at the same recursion level.

To do this:
- First, **sort the array** so that duplicates are adjacent.
- Then, in the DFS loop, skip over any duplicate candidates:
    if i > start and candidates[i] == candidates[i - 1]:
        continue

Why sorting is necessary — counterexample:
Example: [1, 3, 1, 2], target = 3
- Without sorting, the two 1s are separated.
- After checking all paths from the first 1, we move on to 3.
- Later we encounter the second 1, and since its previous value (3) != 1, we can't detect it's a duplicate.
- This leads to repeated combinations like [1, 2] appearing more than once.

Fixes:
1. Sort the array to ensure duplicates are grouped together.
2. Alternatively, use a hash set to track used elements per recursion level (less efficient).
3. Or loop back to check for prior occurrences manually (slower).

Implementation:
- Use DFS (backtracking) to build paths.
- Use `i + 1` as the new start index to enforce single-use of each candidate.
- If `curr_sum == target`, store the path.
- If `curr_sum > target`, prune that path.

Duplicate prevention condition:
    if i > start and candidates[i] == candidates[i - 1]:
        continue
This ensures we only process the **first** instance of each duplicate value at each level.

Time Complexity:
- O(2^n + n log n): n log n for sorting, 2^n for subset generation in the worst case

Space Complexity:
- O(k): total space used by all valid combinations in result
- O(n): recursion stack depth
"""


# Solution 1
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(start, path, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return 
            elif curr_sum > target:
                return
            for i in range(start, len(candidates)):
                if i  > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, curr_sum + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return res


Solution 2
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(start, path, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            elif curr_sum > target:
                return
            i = start
            while i < len(candidates):
                
                path.append(candidates[i])
                dfs(i + 1, path, curr_sum + candidates[i])
                path.pop()
                i += 1
                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i += 1
                        
        dfs(0, [], 0)
        return res



                
     
                


        
        

        
        
