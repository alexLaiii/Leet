"""
Reverses the bits of a 32-bit unsigned integer.

This method iteratively extracts the least significant bit (LSB) of `n`,
shifts the result accumulator left to make space, and appends the extracted
bit to build the reversed binary representation.

Algorithm:
- Initialize result as 0.
- For 32 iterations (fixed-width integer):
    • Extract LSB using `n & 1`
    • Left shift result to create space
    • Append extracted bit using bitwise OR
    • Right shift n to process next bit
- Return the accumulated reversed value.

Time Complexity: O(32) → O(1)
Space Complexity: O(1)

Args:
    n (int): A 32-bit unsigned integer whose bits are to be reversed.

Returns:
    int: The integer formed by reversing the binary bits of `n`.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            b = n & 1
            res = res << 1
            res = res | b
            n = n >> 1

        return res
            
            
