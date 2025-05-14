"""
Intuition
Two pointer method, one keep track of the unqiue element, one keep track of the looping element, if the unique element is same as the looping element, ignore that element and continue the loop, since we only care about the first j element in the array, so this method works
i is used to keep track of the looping elements
j is used to keep track of the unique element

Time Complexity: O(n)
Space Complexity: O(1)
"""





class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use i to keep track of the arr 
        # use j to keep track of the unique elements
        j = 0
        
        for i in range(1,len(nums)):
            if nums[j] == nums[i]:
                continue
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
        return j + 1
            
            
