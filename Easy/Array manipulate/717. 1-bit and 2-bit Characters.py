  """
  Determine whether the last bit represents a 1-bit character.

  We scan from left to right, treating:
  - '0' as a 1-bit character (move i by 1)
  - '10' or '11' as a 2-bit character (move i by 2)

  The loop stops before the last bit. If we land exactly on the last index,
  that last '0' is a separate 1-bit character; if we jump past it, then it
  was part of a 2-bit character.

  Time: O(n), Space: O(1).
  """

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i == len(bits) or bits[i] != 0:
            return False
        return True
        
