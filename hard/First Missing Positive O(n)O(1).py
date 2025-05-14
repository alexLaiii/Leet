"""
Intuition:
Since the first missing postive can only happen between 1 to len(nums) + 1
we can use the input array nums as a inplace storage, so no extra memory needed
We first sort the array, but sorted under special condition, the index i indicates the nums[i] should include what value:
For example: 
if i = 0, nums[i] should = 1
if i = 3, nums[i] should = 4

Example: [3,4,-1,1] will become [1,-1,3,4] after sorting
After the sort, we loop through nums again to check is there any "out of place" element
That is:
[1,-1,3,4] -> 2 is not in nums, since nums[1] != 1 + 1, more generally nums[i] != i + 1
If the sorting is perfect, like 
[1,2,3,4] -> then every number is inplace, then answer = 4, more generally, answer = len(nums) + 1


Note, careful about the edge case:
Example [1,1]
when i = 1 in sorting, we need to ensure we are not swapping the same number again and again, causing infinite loops,
so condition needs to be checked: nums[nums[i]-1] != nums[i]

*** [1,1,2] -> [1,2,1] after sorting ***, 
if the inplace number does exist, this algorithm would eventually bring it inplace, don't worry about it
"""



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # only 1 -> max_nummatters
        # Hint: the answer must between [1 ...... len(nums) + 1]
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i] and nums[i] != i + 1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        
        for j in range(len(nums)):
            if(j + 1 != nums[j]):
                return j + 1
        
        return len(nums) + 1
        
                



            
            




        
