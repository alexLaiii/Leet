  """
  Return True if the binary representation of n has alternating bits
  (no two adjacent bits are the same), otherwise return False.

  Approach:
  1) Find the highest power of two needed to represent n (most significant bit index).
  2) Reconstruct the full binary representation from that bit down to 0 by repeatedly
     checking whether 2^i fits into the remaining value, appending 1 or 0 accordingly.
  3) Scan the constructed bit list and ensure every adjacent pair differs.

  Example:
  - n = 5 (101) -> alternating -> True
  - n = 7 (111) -> not alternating -> False

  Time Complexity:
  O(k), where k is the number of bits in n (≈ floor(log2(n)) + 1).

  Space Complexity:
  O(k) for storing the binary digits in the list.
  """

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        i = 0
        bit = []

        while n >= 2 ** (i + 1):
            i += 1

        while i >= 0:
            if n >= 2 ** i:
                n -= 2 ** i
                bit.append(1)
            else:
                bit.append(0)
            i -= 1

        for i in range(1, len(bit)):
            if bit[i] == bit[i - 1]:
                return False
        return True

            
