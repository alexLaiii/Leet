"""
Easy, just do as the problem describe
"""
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums = 0
        products = 1
        temp = n
        while temp > 0:
            d = temp % 10
            temp = temp // 10
            sums += d
            products *= d
        
        return (n % (sums + products)) == 0
