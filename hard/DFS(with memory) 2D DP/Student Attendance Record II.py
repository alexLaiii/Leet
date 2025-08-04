"""
Returns the number of valid attendance records of length `n` that are eligible for an award.

A record is considered valid if:
- It contains **at most one 'A'** (Absent).
- It contains **no more than two consecutive 'L's** (Late).

The solution uses top-down recursion (DFS) with memoization to avoid redundant computation.
Each recursive state is uniquely defined by:
    - `days`: the number of characters placed so far
    - `absents`: the number of 'A's used so far (must be < 2)
    - `consective`: the current streak of consecutive 'L's at the end (must be < 3)

Key ideas:
- We iterate through possible next characters: 'A', 'L', and 'P'.
- Adding 'P' resets the consecutive 'L' count to 0.
- Adding 'L' increments the consecutive 'L' count (but only if it's currently less than 2).
- Adding 'A' increments the absence count (only if it's currently 0) and also resets the 'L' streak to 0.
- The same `(days, absents, consective)` state can be reached through different character paths
  (e.g., both "PA" and "AP" may lead to the same state), and memoization allows us to reuse these subresults efficiently.
- The recursive result is modulo 10^9 + 7 to avoid overflow.

The memoization table is a 3D list of dimensions (n+1) x 2 x 3, representing all combinations
of days so far, 'A' count (0–1), and trailing 'L' count (0–2). Each entry stores the number of
valid ways to complete the sequence from that state onward.

Returns:
    int: The number of valid attendance records of length `n`, modulo 10^9 + 7.
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = [[[-1 for j in range(3)] for k in range(2)] for i in range(n + 1)]

      
        def dfs(days, absents, consective):

            if absents >= 2 or consective >= 3:
                return 0
            if days == n:
                return 1
            if memo[days][absents][consective] != -1:
                return memo[days][absents][consective]
            res = 0
            for c in "ALP":
                if c == "A":
                    res = (res + dfs(days + 1, absents + 1, 0)) % MOD
                elif c == "L":
                    res = (res + dfs(days + 1, absents, consective + 1)) % MOD
                elif c == "P":
                    res =  (res + dfs(days + 1, absents, 0)) % MOD 
            memo[days][absents][consective] = res
            return res
        
        return dfs(0,0,0) 


