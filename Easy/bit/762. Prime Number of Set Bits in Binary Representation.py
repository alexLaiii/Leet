"""
Counts how many integers in the inclusive range [left, right] have a prime
number of set bits (1s) in their binary representation.

A helper function iteratively extracts each bit using bitwise AND and
right shifts to compute the number of 1s in O(log n) time.

A precomputed set of prime numbers is used for constant-time membership
checks, since the maximum number of set bits for numbers up to 10^6 is small.

Time Complexity:
    O((right - left + 1) * log N), where N is the size of the number.

Space Complexity:
    O(1), using a fixed-size prime set.

Returns:
    The count of numbers whose binary representation contains a prime
    number of 1 bits.
"""

class Solution:
    
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def countOne(n):
            count = 0
            while n != 0:
                count += n & 1
                n = n >> 1
            return count
        

        res = 0
        prime = set([2, 3, 5, 7, 11, 13, 17, 19])

        for i in range(left, right + 1):
            c = countOne(i)
            if c in prime:
                res += 1
        
        
        return res
