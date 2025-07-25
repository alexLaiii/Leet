  """
  Leetcode 241 - Different Ways to Add Parentheses

  Idea:
  This is a recursive divide-and-conquer problem. The goal is to evaluate all possible results from computing 
  a given arithmetic expression by adding parentheses in every possible way.

  The expression contains only numbers and the binary operators '+', '-', and '*'.

  Strategy:
  1. For each character in the expression:
     - If it's an operator, we split the expression into two parts: left and right of the operator.
     - We recursively compute all possible results from the left and right parts.
  2. We then combine each result from the left with each result from the right using the current operator.
  3. The base case is when the expression is just a number (i.e., contains only digits). We return a list
     containing just that number.

  We collect all possible results into a list and return it.

  Example:
  Input: "2*3-4*5"
  Breakdown:
    - First split at '*': left="2", op="*", right="3-4*5"
    - Then split "3-4*5" at '-' → left="3", op="-", right="4*5"
    - Further split "4*5" → left="4", op="*", right="5"
  
  Expression trees (all possible parenthesis placements):
      ((2 * 3) - (4 * 5))  = -14
      ((2 * (3 - 4)) * 5)  = -10
      (2 * ((3 - 4) * 5))  = -10
      ((2 * 3 - 4) * 5)    = 10
      (2 * (3 - (4 * 5)))  = -34

  So the output is: [-34, -14, -10, -10, 10]

  Time Complexity:
  - In the worst case, the recursion forms a binary tree with exponential growth.
  - Roughly O(N * 2^N), where N is the number of operators in the string.
  - Adding memoization can greatly improve performance.

  Returns:
      List[int]: All possible results from computing the expression in different ways.
  """

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) == 1:
            return [int(expression[0])]
        res = []


        def dfs(s):
            if s.isdigit():
                return [int(s)]
            ans = []
            for i in range(len(s)):
               
                if s[i] in "+-*":
                    ans_l, ans_r = [], []
                    left = s[:i]
                    operator = s[i]
                    right = s[i + 1:]
                    ans_l = dfs(left)
                    ans_r = dfs(right)
                    for l in range(len(ans_l)):
                        for r in range(len(ans_r)):
                            if operator == "+":
                                ans.append(ans_l[l] + ans_r[r])
                            elif operator == "-":
                                ans.append(ans_l[l] - ans_r[r])
                            else:
                                ans.append(ans_l[l] * ans_r[r])
            return ans
        
        return dfs(expression)
                
