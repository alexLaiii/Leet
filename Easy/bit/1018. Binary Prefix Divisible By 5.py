"""
Given a list of bits, treats each prefix as a binary number and returns
a list where res[i] is True if the integer formed by nums[0..i] is
divisible by 5. Uses a running prefix value updated as prev*2 + bit.
Time: O(n), Space: O(n) for the result list.
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False] * len(nums)
        prev = 0
        for i in range(len(nums)):
            prev = (prev * 2 + nums[i]) % 5
            res[i] = (prev == 0)
    
        return res

            
        
