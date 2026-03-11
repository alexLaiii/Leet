"""
Compute the bitwise complement of a non-negative integer n.

The complement is obtained by flipping every bit in the binary
representation of n, considering only the bits up to the most
significant 1 (no leading zeros).

Key idea:
Python integers conceptually have infinite leading zeros, so using
the bitwise NOT operator (~) would flip infinitely many bits.
Instead, we construct a mask consisting entirely of 1s with the same
bit length as n. XORing n with this mask flips exactly those bits.

Steps:
1. Handle the special case n = 0 (binary "0"), whose complement is 1.
2. Determine the number of bits needed to represent n.
3. Construct a mask of the form (2^bits − 1), which is all 1s.
4. XOR n with the mask to flip all bits.

Example:
n = 5
binary: 101
mask:   111
result: 010 → 2

Time Complexity:  O(log n)
    Determined by the loop that finds the number of bits.

Space Complexity: O(1)
    Only constant extra variables are used.
"""
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        i = 0
        while n >= 2 ** i:
            i += 1
        mask = 2 ** i - 1

        return n ^ mask


       
