"""
Number theory problem
"""
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        Since         
        odd = n ** 2
        even = n * (n + 1)
        and:
        gcd(n ** 2, n * (n + 1)) = n * gcd(n, n + 1)
        and:
        gcd(n,n + 1) = 1
        -> gcd(n ** 2, n * (n + 1)) = n * 1 = n
        """
        return n

        
