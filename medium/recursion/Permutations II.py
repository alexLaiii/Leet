"""
The main challenge in this problem is how to avoid generating duplicate permutations.

Example:
Input: [1, 1, 2]

If we use standard backtracking by index (treating each number as distinct by position), we get:
[1, 1, 2] → first 1 → second 1 → 2  
[1, 1, 2] → second 1 → first 1 → 2  
[1, 2, 1] → first 1 → 2 → second 1  
[1, 2, 1] → second 1 → 2 → first 1  
[2, 1, 1] → 2 → first 1 → second 1  
[2, 1, 1] → 2 → second 1 → first 1

That gives 6 permutations due to index differences, but in reality, the correct unique results are:
[1, 1, 2], [1, 2, 1], [2, 1, 1]

This shows that standard index-based backtracking doesn't work when duplicates exist,
because it treats identical values at different indices as different choices.

### Solution 1: Count-based backtracking

**Idea:**
We eliminate duplicates by combining all identical values into a single "slot" using a frequency counter.

That is:
- Count how many times each number appears (e.g., [1,1,2] → {1:2, 2:1})
- At each step in the DFS, loop through the keys in the counter
- For any number with a remaining count > 0:
    - Choose it, decrement the count, recurse
    - Backtrack and restore the count

This approach removes the "which copy of 1 are we picking?" issue. 
It only cares about how many copies are left.

Example run (from [1,1,2]):
Start with count = {1:2, 2:1}

1 → 1 → 2  
↑ pick 1, recurse pick 1, recurse pick 2 (1s exhausted)

1 → 2 → 1  
↑ pick 1, recurse pick 2, recurse pick 1

2 → 1 → 1  
↑ pick 2, recurse pick 1, recurse pick 1

Total: 3 unique paths, no duplicates generated.

This works because we’ve "collapsed" all duplicate values into a count-based structure,
so the program can no longer distinguish between “first 1” or “second 1”.
It only asks: “Is there any 1 left to pick?”

This cleanly and efficiently avoids duplicates.

Implementation:
- We transform the given nums into a count-based hash map:
        hash_nums = {}
        for n in nums:
            hash_nums[n] = 1 + hash_nums.get(n, 0)
- We use a DFS backtracking algorithm on this hash map.
    Base case: if len(path) == len(nums), the path is a valid permutation → append to result.
    Loop through the hash map — since we are generating permutations, we always loop from the beginning at every level:
        - If the current number is exhausted → skip it
        - Else:
            - Append the current number to the permutation
            - Decrement the count of that number by 1
            - Recursively call DFS
            - After recursion finishes, backtrack:
                - Pop this number from the permutation
                - Restore the count of that number by incrementing it by 1 since it is no longer in the permutation
"""

# Count base approach
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_nums = {}
        for n in nums:
            hash_nums[n] = 1 + hash_nums.get(n, 0)
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in hash_nums:
                if hash_nums[num] == 0:
                    continue
                path.append(num)
                hash_nums[num] -= 1
                backtrack(path)
                path.pop()
                hash_nums[num] += 1
        backtrack([])
        return res


"""
Solution 2: visited + sort + skip-duplicate approach

This uses a similar approach to Subsets II and Combination Sum II, but with important tweaks.

**Idea:**
To avoid duplicate permutations, we need to ensure that each set of consecutive duplicates is used only once per recursive level.

Example: [1, 1, 2]  
We should only use the sequence [1,1] once — we cannot allow a permutation where the second 1 comes before the first 1,
as that would produce a duplicate [1,1] permutation from a different ordering.

Therefore, we must first **sort the nums**, so that all duplicate values are placed next to each other.
This makes it easier to detect and skip duplicate patterns by comparing adjacent elements.
The rule is: **a duplicate value can only be picked if its previous identical value has already been used** in this recursion branch.

This prevents the scenario where a duplicate number is chosen before its earlier twin, which would lead to the same permutation structure being explored more than once.

**Implementation:**
- First, sort the `nums` array
- Perform DFS backtracking on the sorted list:
    - Base case: if `len(path) == len(nums)`, the path is a valid permutation → append to result
    - Loop through the indices of `nums`:
        - If index `i` is already in `visited` → skip it
        - If `i > 0` and `nums[i] == nums[i - 1]` and `i - 1` is not in `visited`:
            - This means:
                - We're trying to use a duplicate value
                - Its earlier copy exists but **has not been used** in the current recursion branch
                - So using this value now would place it **before its first copy**, which leads to duplicate branches
            - Therefore: **skip it**
        - Else:
            - Append `nums[i]` to the current path
            - Mark `i` as visited
            - Recurse
            - After recursion, backtrack:
                - Pop `nums[i]` from the path
                - Remove `i` from the visited set
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path, visited):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and i - 1 not in visited:
                    continue
                path.append(nums[i])
                visited.add(i)
                backtrack(path, visited)
                path.pop()
                visited.remove(i)
        backtrack([], set())
        return res
                
