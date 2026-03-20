"""
Beginner level stack problem
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "C":
                stack.pop()
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(o))
        return sum(stack)
