"""
Computes the sum of GCDs of formed pairs as defined by the problem.

Algorithm:

1. Traverse the input array while maintaining the maximum value seen so far.
2. For each element `nums[i]`, compute `gcd(nums[i], max(nums[0:i+1]))`
   and store the result in `prefixGcd`.
3. Sort `prefixGcd` in non-decreasing order.
4. Form pairs by repeatedly taking the smallest and largest remaining
   elements in `prefixGcd` and add their GCD to the result.
5. If `prefixGcd` contains an odd number of elements, the middle element
   is ignored.

Time Complexity:
O(n log n + n log M)
where n is the length of `nums` and M is the maximum value in `nums`.

Space Complexity:
O(n)
for storing the `prefixGcd` array.
"""

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        curr_max = nums[0]
        prefixGcd = []
        for num in nums:
            curr_max = max(num, curr_max)
            prefixGcd.append(gcd(curr_max, num))
        
        prefixGcd.sort()
        res = 0
        l = 0
        r = len(prefixGcd) - 1
        while l < r:
            res += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return res
            
        
