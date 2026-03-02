"""
Return the minimum number of deci-binary numbers required to sum to `n`.

A deci-binary number is a number consisting only of digits 0 or 1,
with no leading zeros. We must determine the smallest count of such
numbers whose sum equals the given decimal string `n`.

Key Insight:
----------------
Each deci-binary number can contribute at most 1 to any digit position.
Therefore, for any digit d in `n`, we need at least d separate
deci-binary numbers stacked together to produce that digit.

Since this constraint applies independently to each digit position,
the minimum number of deci-binary numbers required is exactly the
maximum digit present in `n`.

Algorithm:
----------------
- Iterate through each character in the string.
- Track the maximum digit encountered.
- Return that maximum value.

Time Complexity:
----------------
O(n), where n is the length of the string.
We perform a single pass through the digits.

Space Complexity:
----------------
O(1), since only a constant amount of extra space is used.

Example:
----------------
n = "32"
Maximum digit is 3 → answer = 3

n = "82734"
Maximum digit is 8 → answer = 8
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        maxNum = 0
        for d in n:
            maxNum = max(maxNum, int(d))
        return maxNum

 
