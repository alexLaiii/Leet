"""
Leetcode 90 – Subsets II

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set) without duplicates.

This solution uses backtracking with pruning to avoid generating duplicate subsets.

Approach:
- First, sort the input list so that duplicate values are adjacent.
- Use backtracking to explore all possible subsets starting from a given index.
- At each level, skip choosing a number if it is the same as the previous number and the previous number was not used in this level (`i > start and nums[i] == nums[i-1]`).
  Note: Why "i > start" is essential here:
  If we remove "i > start", it will cause over-pruning and accidentally skip valid subsets.
  The key point is that "start" represents the first index we can choose from in the current recursion level.
  So even if nums[i] == nums[i - 1], we must not skip the first occurrence (i == start),
  because it’s the first time this value is being considered in this level of recursion.
  
  In other words:
  - We must always allow the *first* occurrence of a value in each level
  - We skip only the *subsequent* duplicates to avoid redundant branches
  
Example:
      Input: [1, 2, 2]
      Output:
          [
              [], [1], [1, 2], [1, 2, 2],
              [2], [2, 2]
          ]
  This ensures we only include one subset for each set of duplicate elements at a given level.

Example:
    Input:  [2, 1, 2]
    Sorted: [1, 2, 2]

    Unique subsets:
    [[], [1], [1,2], [1,2,2], [2], [2,2]]

Time complexity: O(2^n) worst case (without duplicates), reduced by pruning
Space complexity: O(n) recursion depth
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        def backtrack(path, start):
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                res.append(path.copy())
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return res
