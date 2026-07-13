"""
Sliding window solution

Generate sequential-digit numbers by sliding a window over the fixed string
"123456789".

The outer loop determines the window size (from 2 to 9 digits), while the
inner loop slides the window one position at a time to produce every possible
sequential-digit number of that length. Since the generated numbers are in
strictly increasing order, the algorithm can terminate early once a number
exceeds the upper bound.

Time Complexity: O(1)
    At most 36 sequential-digit numbers are generated (8 + 7 + ... + 1),
    so the number of iterations is constant.

Space Complexity: O(1)
    Excluding the output list, only a few variables are used.
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        max_num = "123456789"
        
        res = []
        for r in range(1, len(max_num)):
            l = 0
            while r < 9:
                num = int(max_num[l:r + 1])
                if num > high:
                    return res
                if num >= low:
                    res.append(num)
                l += 1
                r += 1
        return res
