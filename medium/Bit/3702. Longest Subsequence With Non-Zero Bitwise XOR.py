"""
Trick question, key observation is: 
Suppose:

a ^ b ^ c ^ d = 0

Then taking all n elements doesn't work.

But here's the important property of XOR:

a ^ b ^ c ^ d = 0

If you remove any one element, say a, the XOR of the remaining elements becomes:

b ^ c ^ d

We can derive it:

a ^ b ^ c ^ d = 0
a ^ (a ^ b ^ c ^ d) = a ^ 0
b ^ c ^ d = a

Therefore:
b ^ c ^ d = a

And if a > 0, that's non-zero.

So if the total XOR is 0, you can remove any positive number and get:

length = n - 1

Therefore, the reasoning tree is the following: 

            XOR of entire array
            /                \
         != 0                = 0
          |                    |
    take everything       Can we remove
    answer = n            one non-zero?
                              /    \
                            yes     no
                             |       |
                          n - 1      0
"""

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        
        if res > 0:
            return len(nums)
        elif sum(nums) > 0:
            return len(nums) - 1
        else:
            return 0
            
