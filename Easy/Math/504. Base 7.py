"""
Converts an integer from base 10 to base 7.

The conversion is performed by repeatedly dividing the absolute value
of the number by 7. Each remainder represents a digit in the base-7
representation, collected from least significant to most significant.
The digits are reversed at the end to form the correct order.

Negative numbers are handled separately by converting their absolute
value and adding the '-' sign back to the result.

Time Complexity: O(log_7(n)), where n is the absolute value of num.
Space Complexity: O(log_7(n)) for storing the converted digits.
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        new_num = abs(num)
        res = []

        while new_num:
            res.append(str(new_num % 7))
            new_num //= 7

        ans = "".join(res[::-1])
        return "-" + ans if num < 0 else ans
