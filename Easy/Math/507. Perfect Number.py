"""
Determine whether num is a perfect number.

A perfect number equals the sum of its proper divisors
(all positive divisors excluding itself), e.g. 28 = 1+2+4+7+14.

Approach: trial-divide from 2 up to floor(sqrt(num)). Each divisor
i found contributes both i and num // i to the running sum, since
divisors come in pairs multiplying to num. If num is a perfect
square, i and num // i coincide at the midpoint, so that value is
added only once (guarded by the `num // i != i` check). The
implicit divisor 1 is added at the end via `res + 1`.

Args:
    num: A positive integer to test.

Returns:
    True if num is a perfect number, False otherwise
    (num == 1 is handled explicitly since it has no proper
    divisors and 0 != 1).

Time complexity: O(sqrt(num)) — trial division only up to sqrt(num).
Space complexity: O(1).
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        d = math.sqrt(num)

        res = 0
        for i in range(2, math.floor(d) + 1):  
            if num % i == 0:
                res += i
                if num // i != i: # This guard is necessary to prevent double counting when "num" is a perfect square
                    res += num // i
        
        return res + 1 == num
