"""
Intuitive version O(nlogn)

Returns the decimal value of the binary string formed by concatenating
the binary representations of all integers from 1 to n (inclusive),
modulo 10^9 + 7.

Approach:
----------
Instead of actually building a binary string (which would be too large),
we construct the result numerically using bit manipulation.

For each integer i from 2 to n:
    1. Compute the number of bits needed to represent i in binary.
       This is done by right-shifting a copy of i until it becomes 0,
       counting the number of shifts. The count equals the bit-length.
    2. Left-shift the current result by `length` bits to make room
       for i’s binary digits.
    3. Add i to append its binary representation.
    4. Apply modulo (10^9 + 7) to prevent overflow.

Key Idea:
----------
Concatenating binary numbers is equivalent to:
    res = (res << bit_length_of_i) + i

Since left-shifting by k bits is equivalent to multiplying by 2^k,
this efficiently appends the binary representation of i to the result.

Time Complexity:
-----------------
O(n log n)
Each number requires O(log i) time to compute its bit-length
via repeated right shifts.

Space Complexity:
------------------
O(1)
Only a few integer variables are used.

Parameters:
-----------
n : int
    Upper bound of consecutive integers to concatenate.

Returns:
--------
int
    The concatenated binary result modulo 10^9 + 7.
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = 10**9 + 7
        res = 1
        for i in range(2, n + 1):
            length = 0
            j = i
            while j != 0:
                j = j >> 1
                length += 1

            res = ((res << length) + i) % MODULO

        return res

"""
Trick version O(n)
          
Returns the decimal value of the binary string formed by concatenating
the binary representations of all integers from 1 to n (inclusive),
modulo 10^9 + 7.

Optimized Approach (Power-of-Two Trick):
----------------------------------------
Instead of recomputing the bit-length of each number using a loop,
we observe an important structural property:

    The binary length increases by 1 *only* when the number becomes
    a power of two (1, 2, 4, 8, 16, ...).

This allows us to track the current bit-length incrementally.

Key Insight:
------------
A number i is a power of two if and only if:

    (i & (i - 1)) == 0

This works because powers of two contain exactly one set bit in binary.
Subtracting 1 flips all trailing zeros to ones, and performing AND
clears the only set bit, producing zero.

Algorithm Steps:
----------------
1. Initialize:
       res = 1       (binary of 1)
       length = 1    (bit-length of 1)
2. For each i from 2 to n:
       - If i is a power of two, increment length.
       - Left shift `res` by `length` bits to make room for i.
       - Add i.
       - Apply modulo to avoid overflow.
3. Return final result.

Concatenation Formula:
----------------------
    res = (res << length) + i

Since left-shifting by k bits is equivalent to multiplying by 2^k,
this efficiently appends i’s binary representation.

Time Complexity:
----------------
O(n)
Each iteration performs constant-time operations.

Space Complexity:
------------------
O(1)
Only a few integer variables are used.

Parameters:
-----------
n : int
    Upper bound of consecutive integers to concatenate.

Returns:
--------
int
    The concatenated binary result modulo 10^9 + 7.
        
"""

  class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = 10**9 + 7
        res = 1
        length = 1
        for i in range(2, n + 1):
            if (i & i - 1) == 0:
                length += 1
            res = ((res << length) + i) % MODULO

        return res
