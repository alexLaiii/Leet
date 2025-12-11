  """
  Count the number of valid permutations to unlock all computers.

  A room has n computers labeled 0 to n - 1. Computer 0's password is
  already decrypted and acts as the root. For any computer i > 0 to be
  unlocked, there must exist some j < i such that:
      - computer j has already been unlocked, and
      - complexity[j] < complexity[i].

  This function returns the number of permutations of [0, 1, ..., n-1]
  that represent a valid order in which all computers can be unlocked,
  starting with computer 0 as the only initially unlocked one. The answer
  is taken modulo 10^9 + 7.

  Key observations:
  - If any complexity[i] (for i >= 1) is less than or equal to
    complexity[0], then computer i can never be unlocked, because there is
    no j < i with strictly smaller complexity that can serve as its
    unlocker. In this case, the result is 0.
  - Otherwise, if all complexity[i] > complexity[0] for i >= 1, then
    computer 0 can unlock every other computer regardless of their order.
    Since 0 must appear first in the permutation, the remaining n - 1
    computers can be arranged arbitrarily, giving (n - 1)! valid orders.

  Algorithm:
  - Let root = complexity[0].
  - Scan complexity[1:] and if any value is <= root, return 0.
  - Otherwise compute (n - 1)! modulo 10^9 + 7 by multiplying i for
    i from 1 to n - 1.

  Time Complexity:
      O(n), where n is len(complexity), due to a single linear scan.

  Space Complexity:
      O(1) extra space, using only a few scalar variables.
  """


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        root = complexity[0]
        factorial = 1
        res = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= root:
                return 0
            res = (res * i) % (10 ** 9 + 7)
                

        return res
