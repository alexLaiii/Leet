"""
Traverse the digits of n from right to left while simultaneously building
the concatenated number formed by all non-zero digits and computing the
sum of those digits.

Since the digits are processed from least significant to most significant,
a decimal multiplier is maintained to place each non-zero digit in its
correct position within the reconstructed number. Zero digits are skipped
entirely, so they neither contribute to the concatenated number nor the
digit sum.

Finally, return the product of the concatenated non-zero number and the
sum of its digits.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        mutiplier = 1
        d_sum = 0
        while n > 0:
            d = n % 10
            if d != 0:
                x += d * mutiplier
                d_sum += d
                mutiplier *= 10
            n //= 10
        
        return x * d_sum
            
        
