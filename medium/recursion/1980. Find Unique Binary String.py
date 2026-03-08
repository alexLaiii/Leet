class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Return a binary string of length n that does not appear in nums.

        This solution uses backtracking to generate all possible binary
        strings of length n, where n is the number of strings in nums.
        Each completed candidate is checked against a set containing all
        given strings, and the first missing one is returned.

        Strategy:
        - Convert nums into a set for O(1) average membership checks.
        - Build candidate strings one character at a time using DFS.
        - Once a candidate reaches length n, check whether it is absent
          from the input set.
        - Stop immediately when a valid missing string is found.

        Time Complexity:
            O(n * 2^n) in the worst case, since there are 2^n possible
            binary strings and joining/checking a finished string costs O(n).

        Space Complexity:
            O(n^2) for storing the input strings in a set, plus O(n)
            recursion depth for backtracking.
        """
        n_set = set(nums)
        N = len(nums)

        def backtrack(path):
            if len(path) == N:
                strs = "".join(path)
                if strs not in n_set:
                    return strs
                return None

            for d in ["0", "1"]:
                path.append(d)
                s = backtrack(path)
                if s:
                    return s
                path.pop()

        return backtrack([])
