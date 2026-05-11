"""
Very Easy problem, explanation omitted.
"""
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            remain = n
            stack = []
            while remain != 0:
                stack.append(remain % 10)
                remain = remain // 10
            while stack:
                res.append(stack.pop())

        return res        
