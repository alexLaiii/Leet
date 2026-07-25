"""
Traverse the digits of n once while maintaining the largest and
second-largest digits encountered so far.

For each digit:
- Update secondMax_d if the current digit is larger.
- If secondMax_d becomes larger than max_d, swap them so that
  max_d always stores the largest digit and secondMax_d stores
  the second-largest digit.

This invariant guarantees that after processing all digits,
max_d and secondMax_d are the two largest digits in n, and their
product is the maximum possible product of any two digits.

Time Complexity: O(d), where d is the number of digits in n.
Space Complexity: O(1).
"""

class Solution:
    def maxProduct(self, n: int) -> int:
        max_d, secondMax_d = 0, 0
        
        while n > 0:
            d = n % 10
            n //= 10
            secondMax_d = max(secondMax_d, d)
            if secondMax_d > max_d:
                max_d, secondMax_d = secondMax_d, max_d
        
        return max_d * secondMax_d
        
