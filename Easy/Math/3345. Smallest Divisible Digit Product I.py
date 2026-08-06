
"""
Find the smallest integer >= n whose digit product is divisible by t.

Starting from n, checks each successive integer's digit product
(the product of all its digits) until one is found that is
divisible by t.

Note: the answer is always within ~10 of n, since any multiple
of 10 has a digit product of 0, which is divisible by any t.

Args:
    n: Lower bound (inclusive) to start searching from.
    t: The divisor the digit product must be divisible by.

Returns:
    The smallest integer >= n whose digit product is divisible by t.

Time complexity: O(1) amortized (bounded by ~10 iterations),
    each doing O(log n) work to extract digits.
Space complexity: O(1).
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            product = 1
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            if product % t == 0:
                return n
            n += 1
                
        
        

        
                
        
