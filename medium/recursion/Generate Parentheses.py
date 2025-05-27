"""
Idea:
Use recursive backtracking to explore all valid combinations of parentheses.
At each step:
- Add '(' if open_count < n
- Add ')' only if close_count < open_count (to maintain validity)

Implementation:
Track three variables:
- open_count: number of '(' used so far
- close_count: number of ')' used so far
- brackets: the current string being built

# Important Note:
# '(' (open) is always considered first because a valid parentheses string must start with an open parenthesis.
# For example, "()" is valid, but ")(" is not.
# We can only close a parenthesis after one has been opened — never before.
# Therefore, the number of closing parentheses (close_count) can never exceed the number of opening ones (open_count).
# In other words, we can only add a closing parenthesis if close_count < open_count.


Example: n = 3

Initial call:
generateParenthesisHelper(0, 0, "")

Step-by-step recursion:
(0, 0, "") → add '(' → (1, 0, "(")
  → add '(' → (2, 0, "((")
    → add '(' → (3, 0, "(((")
      → add ')' → (3, 1, "((()")
        → add ')' → (3, 2, "((())")
          → add ')' → (3, 3, "((()))") ✅ append to result
    → backtrack

Backtrack to (2, 0, "((")
  → add ')' → (2, 1, "(()")
    → add '(' → (3, 1, "(()(")
      → add ')' → (3, 2, "(()()")
        → add ')' → (3, 3, "(()())") ✅

Backtrack to (2, 1, "(()")
  → add ')' → (2, 2, "(())")
    → add '(' → (3, 2, "(())(")
      → add ')' → (3, 3, "(())()") ✅

Backtrack to (1, 0, "(")
  → add ')' → (1, 1, "()" )
    → add '(' → (2, 1, "()(")
      → add '(' → (3, 1, "()((")
        → add ')' → (3, 2, "()(()")
          → add ')' → (3, 3, "()(())") ✅
      → backtrack
    → add ')' → (2, 2, "()()")
      → add '(' → (3, 2, "()()(")
        → add ')' → (3, 3, "()()()") ✅

Final result:
["((()))", "(()())", "(())()", "()(())", "()()()"]
"""


class Solution(object):
    def generateParenthesis(self, n):

        res = []
        def generateParenthesisHelper(open_count, closing_count, brackets):
            if open_count == n and closing_count == n:
                res.append(brackets)
                return
            if open_count != n:
                generateParenthesisHelper(open_count + 1, closing_count, brackets + "(")
            if open_count > closing_count:
                generateParenthesisHelper(open_count, closing_count + 1, brackets + ")")
        
        generateParenthesisHelper(0,0,"")
        return res
            
                
            
            
            
        
