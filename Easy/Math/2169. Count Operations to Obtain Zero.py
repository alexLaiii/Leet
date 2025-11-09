"""
Too easy, the problem description itself is the solution
"""

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        k = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            k += 1
        return k
            
