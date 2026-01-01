  """
  Increment a non-negative integer represented as an array of decimal digits by 1.

  The number is stored most-significant-digit first (e.g., [1, 2, 3] -> 123).
  We simulate grade-school addition from the least significant digit:

  - Walk from right to left.
  - If a digit is 9, it becomes 0 (carry continues).
  - Otherwise, increment that digit and stop (no further carry).
  - If we finished and the first digit is 0, that means the input was all 9s
    (e.g., [9,9,9] -> [0,0,0]), so we need to "grow" the array to [1,0,0,0].

  Args:
      digits: List of digits (each 0..9), representing a non-negative integer.

  Returns:
      The same list object, modified in-place, representing the original integer + 1.

  Time Complexity:
      O(n) in the worst case (when all digits are 9), otherwise stops early.

  Space Complexity:
      O(1) extra space (in-place), aside from the possible append when all digits are 9.

  Examples:
      [1,2,3] -> [1,2,4]
      [1,2,9] -> [1,3,0]
      [9,9,9] -> [1,0,0,0]
  """

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            digits.append(0)
            digits[0] = 1
        return digits




                
            
            
        
