  """
  Compute the bitwise complement of a positive integer.

  This method constructs a mask of all 1s that matches the bit-length of `num`,
  then applies bitwise NOT and masks out irrelevant leading bits.

  Approach:
  - Build a mask of the form (2^k - 1), where k is the number of bits in `num`.
    Example: num = 5 (101) → mask = 7 (111)
  - Compute ~num to flip all bits.
  - Use bitwise AND with the mask to keep only the lowest k bits.

  Example:
      num = 5 (101)
      mask = 7 (111)
      ~num = ...11111010
      result = (~num) & mask = 010 = 2

  Time Complexity:
      O(log n) — number of bits in `num`

  Space Complexity:
      O(1)
  """

"""
Compute the bitwise complement of a positive integer by reconstructing it bit by bit.

This method first computes the full bitwise complement (~num), then extracts
only the relevant lower bits corresponding to the bit-length of `num`, and
rebuilds the result manually.

Approach:
- Compute cNum = ~num (infinite bit complement).
- Iterate over each bit position i while 2^i <= num.
- At each step:
    - Check if the least significant bit of cNum is 1.
    - If so, add 2^i to the result.
    - Shift cNum right to process the next bit.
- This effectively reconstructs the complement using only the meaningful bits.

Example:
    num = 5 (101)
    ~num = ...11111010
    Extract lowest 3 bits → 010 → result = 2

Time Complexity:
    O(log n) — number of bits in `num`

Space Complexity:
    O(1)
"""

class Solution:
    def findComplement(self, num: int) -> int:
        # mask = 0
        # i = 0
        # while num >= 2 ** i:
        #     mask <<= 1
        #     mask += 1
        #     i += 1
        # return ~num & mask

        i = 0
        res = 0
        cNum = ~num
        while num >= 2 ** i:
            if (cNum & 1) == 1:
                res += 2**i
    
            cNum >>= 1
            i += 1
        return res
