"""
Just brute force and do what it describe
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            num = i
            while num > 0:
                d = num % 10
                if d == 0 or i % d != 0:
                    break
                num = num // 10
            if num == 0:
                res.append(i)
        return res
                
        
