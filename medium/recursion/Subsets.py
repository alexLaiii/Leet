"""
If you forget how to do this problem, revisit "Combination Sum". This problem is actually much easier than "Combination Sum 2".

Idea:
Since order doesn't matter in a subset, for example, in [1,2,3], [1,2] and [2,1] are considered the same subset. 
To avoid generating permutations, we only proceed forward in the array (by increasing index).

Given the constraint: "All the numbers in nums are unique", we can safely avoid duplicate handling logic.

The core idea is a decision tree (backtracking) recursion problem:
Visualization on [1,2,3]:
Start: res = [[]]

Backtrack([], 0)
├── path = [1]         → res = [[], [1]]
│   └── Backtrack([1], 1)
│       ├── path = [1, 2]     → res = [..., [1, 2]]
│       │   └── Backtrack([1, 2], 2)
│       │       ├── path = [1, 2, 3] → res = [..., [1, 2, 3]]
│       │       └── Backtrack back → path = [1, 2]
│       └── path = [1, 3]     → res = [..., [1, 3]]
│           └── Backtrack([1, 3], 3)
│
├── path = [2]         → res = [..., [2]]
│   └── Backtrack([2], 2)
│       ├── path = [2, 3]     → res = [..., [2, 3]]
│       └── Backtrack back → path = [2]
│
└── path = [3]         → res = [..., [3]]
    └── Backtrack([3], 3)

Final `res`:  
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

This explores all combinations (inclusion or exclusion of each element).  
The base case is when `start == len(nums)`, meaning we’ve considered all elements.

Implementation:
- At each recursion,  include the current number, then recurse.
- Then backtrack (pop it), and move to the next number.
- Add the current `path` is the result at every recursion — this ensures all subsets are captured.

Time Complexity:
O(2^n): We generate all possible subsets, which is 2^n for n elements.
Why 2^n?
                        []
                      /    \
                   [1]     []
                  /   \    /  \
              [1,2] [1] [2]   []
              /   \ /  \ /  \ /  \
         [1,2,3][1,2][1,3][1][2,3][2][3][]
  Consider this binary decision tree, where it contains the same result
  Notice that there are total 8 + 4 + 2 + 1 = 15 nodes, which is = 2^n - 1
  Notice that in each level growth *2, 
  level 1 = 1
  level 2 = 2
  level 3 = 4
  level 4 = 8
So the growth rate is 2^n, Therefore, the time complexity is O(2^n)

Space Complexity:
O(n * 2^n): 
- There are 2^n subsets.
- Each subset can be up to length n.
→ So total space used to store them is O(n * 2^n).
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

"""
This is the solution match exactly like this tree:
                        []
                      /    \
                   [1]     []
                  /   \    /  \
              [1,2] [1] [2]   []
              /   \ /  \ /  \ /  \
         [1,2,3][1,2][1,3][1][2,3][2][3][]
"""
class Solution(object):
    def subsets(self, nums):
        res = []
        subset = []
        def backtrack(start):
            if start >= len(nums):
                res.append(subset[:])
                return
            # Include the curr element
            subset.append(nums[start])
            backtrack(start + 1)

            # Not include the curr element
            subset.pop()
            backtrack(start + 1)
        backtrack(0)
        return res
            

