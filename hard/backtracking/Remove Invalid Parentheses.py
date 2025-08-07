  """
  Removes the minimum number of invalid parentheses to make the input string valid, and
  returns all possible results.

  Core Concept:
  ----------------
  This problem is solved using **backtracking with pruning**. The idea is that for each
  parenthesis character in the string (either '(' or ')'), we have two choices:
  - Either **include** it in the result path
  - Or **exclude** (i.e., delete) it, incrementing a deletion count

  The goal is to **explore all combinations of deletions**, but only collect results that:
  - Are **valid** (parentheses are properly balanced)
  - Use the **minimum number of deletions**

  Algorithm Overview:
  --------------------
  1. Use a recursive `backtrack` function to explore all combinations.
  2. At each character:
      - If it's a letter, always include it.
      - If it's '(', try both including and excluding it.
      - If it's ')', do the same, but ensure that the number of ')' never exceeds '(' so far.
  3. Maintain:
      - `opened`: number of open parentheses added so far
      - `closed`: number of close parentheses added so far
      - `delCount`: how many deletions have been made to reach the current path
      - `mins[0]`: global tracker for the **minimum number of deletions** seen so far
  4. Use a `defaultdict(set)` called `hash_map` to store results grouped by their deletion count.
  5. At the end, return the list of results that had the **fewest deletions** (`mins[0]`).

  Why This Works:
  ----------------
  - We are **exhaustively trying all combinations**, but pruning invalid paths early.
  - We ensure we never accept results with more deletions than needed.
  - By using sets, we avoid duplicate results.
  - The use of `mins[0]` ensures that we only collect the most optimal answers.

  Time Complexity:
  -----------------
  - Worst-case exponential: O(2^n), since for each parenthesis we may recurse twice (use or skip).
  - But effective pruning (e.g., early return if `closed > opened`) cuts down many invalid paths.

  Space Complexity:
  ------------------
  - O(N * 2^N) for the recursion tree, though Python handles this well within the constraints.

  Example:
  ----------
  Input: s = "()())()"
  Output: ["(())()", "()()()"]
  These are all the valid ways to remove **only one** parenthesis to make the string valid.
  """


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        hash_map = defaultdict(set)
        mins = [float("inf")]
        def backtrack(i, opened, closed, path, delCount):
            if closed > opened:
                return 
            if i == len(s):
                if opened == closed and mins[0] >= delCount:
                    hash_map[delCount].add(path)
                    mins[0] = delCount
                return
            if s[i] != "(" and s[i] != ")":
                backtrack(i + 1, opened, closed, path + s[i], delCount)
            elif s[i] == "(":
                backtrack(i + 1, opened, closed, path, delCount + 1)
                backtrack(i + 1, opened + 1, closed, path + "(", delCount)
                
            elif s[i] == ")":
                backtrack(i + 1, opened, closed, path, delCount + 1)
                backtrack(i + 1, opened, closed + 1, path + ")", delCount)
                


        backtrack(0, 0, 0, "", 0)
        
        return list(hash_map[mins[0]])

