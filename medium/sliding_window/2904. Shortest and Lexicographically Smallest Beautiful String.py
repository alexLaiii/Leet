"""
Find the lexicographically smallest substring of s with the minimum
possible length that contains exactly k '1's ("beautiful").

Approach: sliding window with two pointers.
- Expand r, incrementing count when s[r] == '1'.
- Once count == k, the window [l, r] is valid (beautiful). Record it,
  then shrink from the left (l += 1) to search for a shorter valid
  window, decrementing count when a '1' leaves the window.
- After the window breaks (count < k), skip any leading '0's at l
  since they can never start a shorter valid window.
- Among all valid windows, keep the one with minimum length; break
  ties by standard lexicographic comparison (Python's < on equal-
  length strings matches the problem's tie-break rule exactly).

Time:  O(n), l and r each advance at most n steps total.
Space: O(n) auxiliary, due to substring slicing (temp/res/min all
       allocate copies); not O(1) despite only using two pointers
       and a counter for bookkeeping.

:param s: binary string to search.
:param k: required count of '1's in the beautiful substring.
:return: shortest, lexicographically smallest beautiful substring,
         or "" if no beautiful substring exists.
"""
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = count = 0
        res = s
        has_res = False
        for r in range(len(s)):
            if s[r] == "1":
                count += 1
            while count == k:
                has_res = True
                temp = s[l:r + 1]
                if len(temp) < len(res):
                    res = temp
                elif len(temp) == len(res):
                    res = min(res, temp)
                if s[l] == "1":
                    count -= 1
                l += 1
            while l < r and s[l] == "0":
                l += 1
        return res if has_res else ""
