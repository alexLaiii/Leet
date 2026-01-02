  """
  Determine whether an integer is a "happy number".

  A number is happy if repeatedly replacing it with the sum of the squares
  of its digits eventually reaches 1. If the process enters a cycle that
  does not include 1, the number is not happy.

  Approach:
  - Use a `seen` set to detect cycles.
  - While n != 1:
      * If we've seen n before, we're in a loop -> return False.
      * Otherwise record n, compute next n as sum(digit^2).

  Example:
  n = 19 -> 1^2 + 9^2 = 82 -> 68 -> 100 -> 1 (happy)

  Complexity:
  - Time: O(k * d) where d is number of digits and k is number of steps
    before reaching 1 or repeating (k is small in practice).
  - Space: O(k) for the seen set.

  Note:
  - This implementation converts n to a string to iterate digits, which is
    clear and simple; a math-based digit extraction version also works.
  """

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            stringN = str(n)
            n = 0
            for digit in stringN:
                n += int(digit) ** 2
            
        return True
