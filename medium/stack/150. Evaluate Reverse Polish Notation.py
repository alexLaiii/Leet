  """
  Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).

  The input `tokens` is a list of strings, where each element is either:
  - an integer (possibly negative), or
  - one of the operators: "+", "-", "*", "/".

  The expression is evaluated using a stack:
  - When a number is seen, it is pushed onto the stack.
  - When an operator is seen, the top two numbers are popped from the stack,
    the operator is applied as (num1 op num2), and the result is pushed back.

  Division between two integers truncates toward zero, matching the problem's
  requirement (e.g., -3 / 2 → -1).

  Time Complexity:  O(n), where n is the number of tokens, since each token
                    is processed exactly once.
  Space Complexity: O(n) in the worst case for the stack storage.

  :param tokens: List of tokens representing an RPN expression.
  :return: The integer result of evaluating the RPN expression.
  """

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if n == "+":
                    stack.append(num1 + num2)
                elif n == "-":
                    stack.append(num1 - num2)
                elif n == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(n))
     
        return stack[0]
