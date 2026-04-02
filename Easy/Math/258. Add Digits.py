  """
  Compute the digital root of a non-negative integer.

  The digital root is obtained by repeatedly summing the digits of `num`
  until a single-digit number remains.

  Instead of simulating the process, this implementation uses a
  mathematical shortcut based on modulo 9:

  - If num == 0 → return 0
  - If num is divisible by 9 → return 9
  - Otherwise → return num % 9

  This works because any integer is congruent to the sum of its digits modulo 9.

  Examples:
  - 38 → 3 + 8 = 11 → 1 + 1 = 2
    38 % 9 = 2 → result = 2

  - 18 → 1 + 8 = 9
    18 % 9 = 0 → return 9

  Time Complexity: O(1)
  Space Complexity: O(1)
  """

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9  == 0:
            return 9
        
        return num % 9
        
