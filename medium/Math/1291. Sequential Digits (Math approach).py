"""
Generate sequential-digit numbers by starting with the smallest sequential
number of each digit length and repeatedly adding a number consisting of
all 1s.

For each length from 2 to 9 digits, the algorithm begins with the smallest
sequential number (e.g., 1234). Adding a value such as 1111 increments every
digit by one, producing the next sequential number (e.g., 2345). Generation
stops when the last digit becomes 9 or the number exceeds the upper bound.

Time Complexity: O(1)
    There are only 36 possible sequential-digit numbers, so the algorithm
    performs a constant number of operations.

Space Complexity: O(1)
    Excluding the output list, only a few variables are used.
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        max_num = "123456789"
        res = []
        for r in range(1, len(max_num)):
            num = int(max_num[:r + 1])
            adder = 1
            for i in range(r):
                adder = adder * 10 + 1
            while num <= high:
                if num >= low:
                    res.append(num)
                if num % 10 == 9:
                    break
                num += adder
        return res

                
