"""
Computes the maximum distance between two consecutive 1-bits
in the binary representation of a positive integer.

The function scans the binary digits of n from right to left
using bitwise operations. Once the first 1 is encountered,
it begins counting the number of positions until the next 1.
Each time another 1 is found, the maximum gap is updated.

Bit operations used:
- n & 1 extracts the least significant bit
- n >>= 1 shifts n right by one bit

Time Complexity: O(log n)   (number of bits in n)
Space Complexity: O(1)

Args:
    n (int): A positive integer

Returns:
    int: The largest distance between two adjacent 1s in binary form
"""
class Solution:
    def binaryGap(self, n: int) -> int:
        distance = 0
        count = 0
        startCount = False
        while n != 0:
            bit = n & 1
            if bit == 1:
                distance = max(count, distance)
                count = 0
                startCount = True
            if startCount:
                count += 1
            n >>= 1
                
        return distance
        
