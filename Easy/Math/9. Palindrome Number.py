"""
Determines whether an integer is a palindrome by reversing its digits
using pure arithmetic (no string conversion).

The algorithm repeatedly extracts the last digit of the number using
modulo 10 and appends it to a reversed value while shrinking the original
number via integer division.

Args:
    x (int): The input integer.

Returns:
    bool: True if x is a palindrome, False otherwise.

Time Complexity:
    O(log10(x)), where log10(x) is the number of digits in x.

Space Complexity:
    O(1), using constant extra space.

Notes:
    - Negative numbers are not palindromes by definition.
    - This method avoids string conversion and works purely with math.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0 
        x_cpy = x
        while x_cpy > 0:
            r = x_cpy % 10
            x_cpy //= 10
            reverse = reverse * 10 + r
        
        if x == reverse:
            return True
        return False
