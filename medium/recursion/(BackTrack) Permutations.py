"""
## Idea

Use backtracking with a `visited` set to generate all permutations of a list.  
At each recursion level, try every number not yet in the current path.

---

### Example: `nums = [1, 2, 3]`

**Level 0:**  
Loop through [1, 2, 3]  
- `n = 1`  
  - `permute = [1]`  
  - `visited = {1}`  
  - Recursive call: `backtrack([1], {1})`

---

**Level 1:**  
Loop through [1, 2, 3]  
- `1 in visited` → skip  
- `2 not in visited` → add  
  - `permute = [1, 2]`  
  - `visited = {1, 2}`  
  - Recursive call: `backtrack([1, 2], {1, 2})`

---

**Level 2:**  
Loop through [1, 2, 3]  
- `1` → skip  
- `2` → skip  
- `3` → add  
  - `permute = [1, 2, 3]`  
  - `visited = {1, 2, 3}`  
  - Reached full length → add `[1, 2, 3]` to result

Backtrack:
- Pop last → `[1, 2]`, `{1, 2}`  
- Loop ends → backtrack to `[1]`, `{1}`

---

**Continue at Level 1:**
- Next: `n = 3`  
  - `permute = [1, 3]`  
  - `visited = {1, 3}`  
  - Recursive call: `backtrack([1, 3], {1, 3})`

**Level 2:**  
Loop through [1, 2, 3]  
- `1` → skip  
- `2` → add → `[1, 3, 2]`  
  - Full length → add to result  
- Backtrack to `[1, 3]`, `{1, 3}`  
- Loop ends → backtrack to `[1]`, `{1}`

---

Repeat similar logic for:
- Starting from `n = 2`
- Then `n = 3`  
Until the top-level loop finishes.

---

### Summary

- Backtracking tries every unused number at each level.
- Once a path is full-length, it's saved.
- On returning, it pops the last number and continues exploring other options.
"""


class Solution(object):
    def permute(self, nums):
        res = []

        def backtrack(permute, visited):
            if len(permute) == len(nums):
                res.append(permute[:])
                return
            for n in nums:
                if n not in visited:
                    permute.append(n)
                    visited.add(n)
                    backtrack(permute, visited)
                    permute.pop()
                    visited.remove(n)
        backtrack([], set())
        return res


        # res = []
        # def backtrack(permute):
        #     if len(permute) == len(nums):
        #         res.append(permute[:])
        #         return
        #     for n in nums: 
        #         if n not in permute:
        #             permute.append(n)
        #             backtrack(permute)
        #             permute.pop()
        # backtrack([])
        # return res

