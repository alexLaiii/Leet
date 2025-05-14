"""
Intuition:
Since the subarray must have the same order as the original array,
we know that we can search the array linearly.
Since any negative prefix_sum will only lower the result/negative contribution to the later sum, we can simply discard all the elements
before we will hit a negative prefix.

Remember to keep track of the largest value, so the discard won't affect the current maximum


Complexity
Time complexity:
O(n)

Space complexity:
O(1)
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## O(n) needed ##
        curr_max = nums[0]
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            curr_max = max(prefix_sum, curr_max)
            if prefix_sum < 0: 
                prefix_sum = 0

        return curr_max



            

        
