"""
Use cyclic placement to put each number in its correct index.

Since the values are in the range 1 to n, number x should be placed
at index x - 1. For each value, keep moving it to its correct position
until that position already contains the same value, which handles
duplicates safely.

After rearranging, scan the array again. If nums[i] is not i + 1,
then i + 1 was never placed there, so it is a missing number.

Time: O(n)
Space: O(1), excluding the result list
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = nums[i]
            while nums[val - 1] != val:
                temp = val
                val = nums[val - 1]
                nums[temp - 1] = temp
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        
        return res
        
