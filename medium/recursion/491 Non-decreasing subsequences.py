
  """
  Generate all unique non-decreasing subsequences of length ≥ 2 using DFS + backtracking.

  How it works:
  - We build `seq` in index order; we only append nums[i] if `seq` is empty or nums[i] ≥ seq[-1]
    to keep it non-decreasing.
  - At each recursion depth (fixed `start`), we create a fresh `used` set. It records which
    values have already been chosen as the next element at this depth. If the same value
    appears again among sibling choices, we skip it to avoid duplicate subsequences.
    Example: in [4, 6, 7, 7], when exploring children of `start` at the first 7,
    `used={7}` prevents generating the same [4,7] (or [4,6,7]) twice. A deeper level gets
    its own `used`, so valid sequences like [7,7] are still produced.

  Returns:
  - List of distinct non-decreasing subsequences (len ≥ 2), order not guaranteed.

  Complexity:
  - Time: O(2^n) in the worst case (with pruning via monotonic check and per-depth de-dup)
  - Space: O(n) recursion/path; each depth maintains its own small `used` set.
  """


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, seq):
            if len(seq) >= 2:
                res.append(seq.copy())
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used or (seq and nums[i] < seq[-1]):
                    continue
                
                used.add(nums[i])
                seq.append(nums[i])
                dfs(i + 1, seq)
                seq.pop()
            
                
        
        dfs(0, [])
        return res
