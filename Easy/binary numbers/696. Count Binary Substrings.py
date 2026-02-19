  """
  Count the number of substrings with equal consecutive 0s and 1s, where all 0s and all 1s
  in the substring are grouped consecutively (e.g., "01", "0011", "1100").

  Key idea:
  View the string as consecutive runs of identical characters. For every adjacent pair of runs
  with lengths a and b, we can form exactly min(a, b) valid substrings that transition between
  these two runs. Therefore, the answer is the sum of min(run[i], run[i+1]) over all adjacent
  run pairs.

  This implementation scans once while maintaining the length of the current run and the
  previous run, adding min(prev_run, cur_run) whenever a run boundary is encountered.

  Time Complexity: O(n), where n = len(s)
  Space Complexity: O(1)
  """

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = 0
        count = defaultdict(int)
        res = 0
        for r in range(len(s)):
            if s[l] == s[r] and s[r - 1] != s[l]:
                res += min(count["0"], count["1"])
                count[s[l]] = 0
                l = r - count[s[r-1]]
            count[s[r]] += 1
        return res + min(count["0"], count["1"])
                
                
            
                
                
