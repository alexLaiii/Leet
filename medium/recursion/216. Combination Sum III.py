  """
  Return all combinations of k distinct numbers from 1..9 whose sum is n (LeetCode 216).

  Core idea (backtracking over increasing choices):
    Build a combination in strictly increasing order so each number 1..9 is used
    at most once and permutations aren’t duplicated. The state carries:
      - k:    how many picks remain
      - path: numbers chosen so far
      - pathSum: current sum of path
      - start: next candidate to try (enforces increasing order)

  Pruning used here:
    - Early accept: when k == 0, record the path only if pathSum == n.
    - Early stop in loop: if pathSum + num > n, break (later nums are larger).
      This relies on the increasing loop over num in [start..9].

  Why it works:
    Strictly increasing picks avoid repeats and ensure each number is used at most once.
    Exploring num from `start` to 9 enumerates each k-combination exactly once.

  Complexity:
    Upper bound O(C(9, k)) backtracking states; each successful leaf copies a path of length k.
    The early-break prune reduces branching when sums grow past n.

  Optional extra prune (not implemented but useful):
    Let rem = n - pathSum. With k picks left starting at `start`,
    the minimum achievable sum is k*start + k*(k-1)//2, and the maximum is
    k*9 - k*(k-1)//2. If rem falls outside this range, you can return early.
  """

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(k, path, pathSum, start):
            if  k == 0:
                if pathSum == n:
                    res.append(path.copy())
                return
            for num in range(start, 10):
                if pathSum + num > n:
                    break
                path.append(num)
                backtrack(k - 1, path, pathSum + num, num + 1)
                path.pop()
        
        backtrack(k, [], 0, 1)
        return res
                
        
