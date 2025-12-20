  """
  LeetCode 944 — Delete Columns to Make Sorted

  Idea:
  We need to count how many columns are NOT non-decreasing from top to bottom.
  For each column i, scan adjacent rows j-1 and j:
    - If strs[j-1][i] > strs[j][i], this column is "bad" and must be deleted.
    - Count it once and stop scanning that column (break).

  Why it works:
  A column is valid iff for all j in [1..M-1], strs[j-1][i] <= strs[j][i].
  If any inversion exists, keeping that column violates the sorted condition,
  and deleting it fixes that column entirely (columns are independent in 944).

  Complexity:
  - Time: O(M * N), where M = number of strings (rows), N = length of each string (columns)
  - Space: O(1)

  Notes:
  - Early break saves time on columns that fail quickly, but worst-case remains O(M*N).
  """

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M, N = len(strs), len(strs[0])
        res = 0
        for i in range(N):
            for j in range(1, M):
                if strs[j - 1][i] > strs[j][i]:
                    res += 1
                    break
        return res
                
                
                
        
