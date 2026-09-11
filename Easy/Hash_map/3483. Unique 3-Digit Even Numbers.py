"""
Counts distinct 3-digit even numbers formable from the given digits.

Enumerates every ordered triple of indices (i, j, k), all pairwise
distinct, treating digits[i] as the hundreds digit, digits[j] as the
tens digit, and digits[k] as the units digit. Each array index may be
used at most once per number, so a repeated digit value at two
different indices may still appear twice in a formed number. Leading
zeros are rejected implicitly: if digits[i] == 0, string concatenation
drops the zero and int() produces a value under 100, which the
num >= 100 check filters out. A number qualifies if it has three
digits, is even, and has not been counted before.

Args:
    digits: List of single digits (0-9), possibly with repeats.

Returns:
    The count of distinct three-digit even numbers that can be
    formed under the above rules.

Time Complexity:
    O(n^3), where n = len(digits), from the triple nested loop.

Space Complexity:
    O(min(n^3, 900)), bounded by both the number of index-triples
    and the fact that only 900 three-digit even numbers exist
    (100 to 998).
"""

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        N = len(digits)
        res = 0
        for i in range(N):
                for j in range(N):
                    if i != j:
                        for k in range(N):
                            if j != k and i != k:
                                num = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                                if num >= 100 and num % 2 == 0 and num not in seen:
                                    res += 1
                                    seen.add(num)
                    
        return res              
        
